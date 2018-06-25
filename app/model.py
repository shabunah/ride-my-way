import json

class Passenger:
    """Class to represent the Passenger model"""
    def __init__(self,first_name, surname,Contact,Email,password,City):
        self.first_name = first_name
        self.surname = surname
        self.Email = Email
        self.password = password
        self.Contact = Contact
        self.City = City


class Driver:
    " Class to represent the Driver model"
    def __init__ (self,first_name, surname,Contact,Email,password,City,Licence_Number,Car_Type,National_ID):
        self.first_name = first_name
        self.surname = surname
        self.Email = Email
        self.password = password
        self.Contact = Contact
        self.City = City
        self.Licence_Number = Licence_Number
        self.Car_Type = Car_Type
        self.National_ID = National_ID


class Offer:
    """ Class to represent the Offer model"""
    def __init__ (self, id, driver_name,car_type,licence_number,contact,location,cost_per_km):
        self.id = id
        self.driver_name = driver_name
        self.car_type = car_type
        self.licence_number= licence_number
        self.contact = contact
        self.location = location
        self.cost_per_km = cost_per_km

    def json(self):
        """json representation of the Offer model"""
        return json.dumps({
            'id': self.id,
        'driver_name':self.driver_name,
        'car_Type':self.car_type,
        'licence_Number':self.licence_number,
        'contact':self.contact,
        'location': self.location,
        'cost_per_km':self.cost_per_km,
        })


class Request:
    """Class to represent the Request model"""
    def __init__(self,Passenger_name,Location,pickup,Contact):
        self.id = id
        self.Passenger_name = Passenger_name
        self.Location = Location
        self.pickup = pickup
        self.Contact = Contact

    def json(self):
        " json representation of the Offer model"
        return json.dumps({ 
        'Passenger_name':self.Passenger_name,
        'Location':self.Location,
        'pickup':self.pickup,
        'Contact':self.Contact,
        })




