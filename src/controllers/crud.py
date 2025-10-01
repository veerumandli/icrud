from flask import request, jsonify
from config.database import fetchRaw, insertRaw, updateRaw, fetchOneRaw
from hashids import Hashids


def create_item(table_name):
    url = request.form.get('url')
    id = insertRaw(f"INSERT INTO {table_name} (url) values ('{url}')")
    hashids = Hashids(salt='sdfhj298 u2134b132b  23y4i23h4', min_length=10)
    hashid = hashids.encode(id)
    updateRaw(f"UPDATE urls SET short_url = '{hashid}' where id = {id}")
    short_url = 'https://bit.ly/'+hashid
    return jsonify({'success': True, 'short_url': short_url})


def fetch_list(table_name):
    data = fetchRaw(f"select * from {table_name}")
    return jsonify({'success': True, 'data': data})


def fetch_detail(table_name, id):
    data = fetchOneRaw(f"select * from {table_name} where id = {id}")
    return jsonify({'success': True, 'data': data})
