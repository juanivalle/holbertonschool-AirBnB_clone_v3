#!/usr/bin/python3
"""comments"""

from api.v1.views import app_views
from flask import jsonify
from models import storage


@app_views.route('/status', methods=['GET'])
def status():
    """Returns status: OK"""
    return jsonify({'status': 'OK'})


classes = {"amenities": "Amenity",
           "cities": "City",
           "places": "Place",
           "reviews": "Review",
           "states": "State",
           "users": "User"}

def get_stats():
    """comments"""
    stats = {}
    for name, cls in classes.items():
        count = storage.count(cls)
        stats[name] = count
    return jsonify(stats)
