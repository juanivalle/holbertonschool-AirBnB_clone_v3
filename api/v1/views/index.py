#!/usr/bin/python3
"""comments"""

from api.v1.views import app_views
from flask import jsonify
from models import storage


@app_views.route('/status', methods=['GET'])
def status():
    """Returns status: OK"""
    return jsonify({'status': 'OK'})


@app_views.route('/api/v1/stats', methods=['GET'], strict_slashes=False)
def count_objects():
    """comments"""
    classes = ["Amenity", "City", "Place", "Review", "State", "User"]
    counts = {}
    for cls in classes:
        count = storage.count(cls)
        counts[cls] = count
    return jsonify(counts)
