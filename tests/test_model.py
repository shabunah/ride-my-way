from flask import Flask
from flask_testing import TestCase
from run import app
import json
from app.model import Driver, Offer,Passenger,Request

class DriverModelTest(TestCase):

    def create_app(self):
        app = Flask(__name__)
        app.config['TESTING'] = True

        return app


    def test_create_offer(self):
        create = Offer("1", "Joan Nakito","Vitiz","UBC 160N","0779684513","Natete","200")      
        self.assertEqual(create.driver_name,"Joan Nakito")
        self.assertEqual(create.car_type,"Vitiz")
        self.assertEqual(create.licence_number,"UBC 160N")
        self.assertEqual(create.contact,"0779684513")
        self.assertEqual(create.location,"Natete")
        self.assertEqual(create.cost_per_km,"200")






class PassengerModelTest(TestCase):

    def request_app(self):
        return app

    def test_request_ride(self):
        request= Request("1","Passenger_name","pickup","Contact" )      
        self.assertEqual(request.Passenger_name,"Joan Arinanye ")
        self.assertEqual(request.pickup,"kyanja")
        self.assertEqual(create.contact,"0779686513")
        



