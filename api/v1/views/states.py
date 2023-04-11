#!/usr/bin/python3
"""comments"""

from api.v1.views import app_views
from flask import jsonify, abort, request
from models import storage
from models.state import State


@app_views.route('/states', methods=['GET'], strict_slashes=False)
def get_all_states():
    """ Retrieves the list of all State objects"""
    states = storage.all(State).values()
    list_states = []
    for state in states:
        list_states.append(state.to_dict())
    return jsonify(list_states)


@app_views.route('/states/<state_id>', methods=['GET'], strict_slashes=False)
def get_state_by_id(state_id):
    """ Retrieves a State object """
    state = storage.get(State, state_id)
    if state:
        return jsonify(state.to_dict())
    abort(404)


@app_views.route('/states/<state_id>', methods=['DELETE'],
                 strict_slashes=False)
def delete_state_by_id(state_id):
    """ Deletes a State object """
    state = storage.get(State, state_id)
    if state:
        storage.delete(state)
        storage.save()
        return jsonify({}), 200
    abort(404)


@app_views.route('/states', methods=['POST'], strict_slashes=False)
def create_state():
    """ Creates a State object """
    req_data = request.get_json()
    if not req_data:
        return jsonify({'error': 'Not a JSON'}), 400
    if 'name' not in req_data:
        return jsonify({'error': 'Missing name'}), 400
    state = State(**req_data)
    state.save()
    return jsonify(state.to_dict()), 201


@app_views.route('/states/<state_id>', methods=['PUT'], strict_slashes=False)
def update_state(state_id):
    """ Updates a State object """
    state = storage.get(State, state_id)
    if state:
        req_data = request.get_json()
        if not req_data:
            return jsonify({'error': 'Not a JSON'}), 400
        ignore_keys = ['id', 'created_at', 'updated_at']
        for key, value in req_data.items():
            if key not in ignore_keys:
                setattr(state, key, value)
        state.save()
        return jsonify(state.to_dict()), 200
    abort(404)
