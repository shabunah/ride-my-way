from flask import jsonify, request
from app import app
from app.model import Offer

All_offers = []

@app.route("/api/v1/driver/addoffer", methods=["POST"])
def add_offer():
    """End point to create an offer"""
    data = request.get_json()
    driver_name = data.get("driver_name")
    car_type = data.get("car_type")
    licence_plate = data.get("licence_plate")
    contact = data.get("contact")
    cost_per_km = data.get("cost_per_km")
    location = data.get("location")

    if not driver_name:
        return jsonify({"message": "incorrect driver_name parameter"}), 400
    if not car_type:
        return jsonify({"message": "incorrect car_type parameter"}), 400
    if not licence_plate:
        return jsonify({"message": "incorrect licence_plate parameter"}), 400
    if not contact:
        return jsonify({"message": "incorrect contact parameter"}), 400   
    if not cost_per_km:
        return jsonify({"message": "incorrect cost_per_km parameter"}), 400
    if not location:
        return jsonify({"message": "incorrect location parameter"}), 400 
   
    id = len(All_offers) + 1
    new_offer = Offer(id, driver_name,car_type, licence_plate, contact, location, cost_per_km)
    All_offers.append(new_offer)
    return jsonify({'message':'successfully added'}), 201


@app.route("/api/v1/passenger/offers", methods=["GET"])
def fetch_offers():
    """ Endpoint to fetch all available ride offers """
    
    #if there is any offer
    if len(All_offers) < 1:
        return jsonify({"message":"No avaiable offer"})
    
    #if there is more than one offer
    if len(All_offers) > 0:
        return jsonify({
            "message":"Available offers",
            "offers":[
            an_offer for an_offer in All_offers
            ]
        })
    return jsonify({"message":"No available offers"})