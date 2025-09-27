# Hello, How are you?
from flask import Flask, render_template, redirect, url_for, request, jsonify
from config.database import fetchRaw, insertRaw, updateRaw, fetchOneRaw
from hashids import Hashids
app = Flask(__name__, template_folder='views')


@app.route("/<table_name>", methods=['POST'])
def create_item(table_name):
    url = request.form.get('url')
    id = insertRaw(f"INSERT INTO {table_name} (url) values ('{url}')")
    hashids = Hashids(salt='sdfhj298 u2134b132b  23y4i23h4', min_length=10)
    hashid = hashids.encode(id)
    updateRaw(f"UPDATE urls SET short_url = '{hashid}' where id = {id}")
    short_url = 'https://bit.ly/'+hashid
    return jsonify({'success': True, 'short_url': short_url})


@app.route("/<table_name>", methods=['GET'])
def get_list(table_name):
    data = fetchRaw(f"select * from {table_name}")
    return jsonify({'success': True, 'data': data})


@app.route("/<table_name>/<id>", methods=['GET'])
def get_detail(table_name, id):
    data = fetchOneRaw(f"select * from {table_name} where id = {id}")
    return jsonify({'success': True, 'data': data})
