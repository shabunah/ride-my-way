import unittest
from run import app
import json
from app.model import Driver, Offer,Passenger,Request

class DriverModelTest(unittest.TestCase):

    def setUp(self):
        self.app=app.test_client()


    def test_create_offer(self):
        response = self.app.post("api/v1/driver/addoffer",
            data=json.dumps(dict(driver_name="shab",car_type= "Benz",licence_plate="UAB 221Q",contact= "079435337",cost_per_km= "200",location="kulambiro")),
            content_type="application/json"
            
            )
        response_data=json.loads(response.data)  
        self.assertEqual(response.status_code,201)
        self.assertEqual(response_data["message"],"successfully added")

    def test_create_missing_parameter(self):
        response = self.app.post("api/v1/driver/addoffer",
            data=json.dumps(dict(driver_name="shab",licence_plate="UAB 221Q",contact= "079435337",cost_per_km= "200",location="kulambiro")),
            content_type="application/json"
            
            )
        response_data=json.loads(response.data)  
        self.assertEqual(response.status_code,400)
        self.assertEqual(response_data["message"],"incorrect car_type parameter")







# class PassengerModelTest(TestCase):

#     def request_app(self):
#         return app

#     def test_request_ride(self):
#         request= Request("1","Passenger_name","pickup","Contact" )      
#         self.assertEqual(request.Passenger_name,"Joan Arinanye ")
#         self.assertEqual(request.pickup,"kyanja")
#         self.assertEqual(create.contact,"0779686513")
        



