from flask import Blueprint, request, jsonify
from drone_inventory.helpers import token_required
from drone_inventory.models import User, Drone, drone_schema, drones_schema, db

api = Blueprint('api', __name__, url_prefix='/api')

@api.route('/getdata')
def getdata():
    return{'some': 'vlaue'}


# CREATE DRONE ENDPOINT
@api.route('/drones', methods = ['POST'])
@token_required
def create_drone(current_user_token):
    name = request.json['name']
    description = request.json['description']
    price = request.json['price']
    cam_quality = request.json['cam_quality']
    flight_time = request.json['flight_time']
    max_speed = request.json['max_speed']
    dimensions = request.json['dimensions']
    weight = request.json['weight']
    cost_of_prod = request.json['cost_of_prod']
    series = request.json['series']
    user_token = current_user_token
    drone = Drone(name,description,price, cam_quality,flight_time,max_speed,dimensions, weight,cost_of_prod,series,user_token = user_token )

    db.session.add(drone)
    db.session.commit()

    response = drone_schema.dump(drone)
    return jsonify(response)



# RETRIEVAL OF ALL DRONES ENDPOINT
@api.route('/drones', methods = ['GET'])
@token_required
def get_drones(current_user_token):
    owner = current_user_token.token
    drones = Drone.query.filter_by(user_token = owner).all()
    response = drones_schemas.dump(drones)
    return jsonify(response)

@api.route('/drones/<id>', methods = ['GET'])
@token_required
def get_drone(current_user_token, id):
    drone = Drone.query.get(id)
    response = drone_schema.dump(drone)
    return jsonify(response)


@api.route('/drones/<id>', methods = ['POST', 'PUT'])
@token_required
def update_drone(current_user_token, id):
    drone = Drone.query.get(id)
    drone.name = request.json['name']
    drone.description = request.json['description']
    drone.price = request.json['price']
    drone.cam_quality = request.json['cam_quality']
    drone.flight_time = request.json['flight_time']
    drone.max_speed = request.json['max_speed']
    drone.dimensions = request.json['dimensions']
    drone.weight = request.json['weight']
    drone.cost_of_prod = request.json['cost_of_prod']
    drone.series = request.json['series']
    drone.user_token = current_user_token.token

    db.session.commit()
    response = drone_schema.dump(drone)
    return jsonify(response)


@api.route('/drones/<id>', methods = ['DELETE'])
@token_required
def delete_drone(current_user_token, id):
    drone = Drone.query.get(id)
    db.session.delete(drone)
    db.session.commit()
    response = drone_schema.dump(drone)
    return jsonify(response)