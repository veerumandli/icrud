from flask import request, jsonify


def create_item(Model):
    data = request.json
    if Model:
        obj = Model.create(**data)
        return jsonify({'success': True, 'id': obj.id})
    else:
        return jsonify({'success': False, 'error': 'Model not provided'}), 400


def fetch_list(Model):
    if Model:
        page = request.args.get('page', 1)
        limit = request.args.get('limit', 20)
        filter = request.args.get('filter', '')
        data = Model.all(page=int(page), limit=int(limit), filter=filter)
        return jsonify({'success': True, 'data': data})
    else:
        return jsonify({'success': False, 'error': 'Model not provided'}), 400


def fetch_detail(Model, id):
    if Model:
        obj = Model.find(id)
        data = obj if obj else None
        return jsonify({'success': True, 'data': data})
    else:
        return jsonify({'success': False, 'error': 'Model not provided'}), 400


def update_item(Model, id):
    data = request.json
    if Model:
        obj = Model.find(id)
        if not obj:
            return jsonify({'success': False, 'error': 'Item not found'}), 404
        for key, value in data.items():
            setattr(obj, key, value)
        obj.save()
        return jsonify({'success': True, 'id': id})
    else:
        return jsonify({'success': False, 'error': 'Model not provided'}), 400


def delete_item(Model, id):
    if Model:
        obj = Model.find(id)
        if not obj:
            return jsonify({'success': False, 'error': 'Item not found'}), 404
        obj.delete()
        return jsonify({'success': True, 'id': id})
    else:
        return jsonify({'success': False, 'error': 'Model not provided'}), 400


# -------------------------
def create_item(Model):
    data = request.get_json()  # expects JSON body
    try:
        result = Model.create(**data)
        return jsonify({"message": "Item created successfully", "data": result}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400