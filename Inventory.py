import pandas as pd
from typing import List, Optional, Union
from pydantic import BaseModel
from datetime import datetime

#this is our car inventory, ideally AI populates this list

class Car(BaseModel):
    make: str
    model: str
    mileage: int
    start_date: datetime
    end_date: datetime
    year: int
    zip_code: int
    address: str
    owner: str
    vin: str
    fuel_type: str
    mpg: Optional[Union[int, float]] = None
    range: Optional[Union[int, float]] = None
    make_class: str
    model_class: str
    total_price: float


make_standard = ['Toyota', 'Honda', 'Jeep']
make_luxury =  ['BMW', 'Mercedes', 'Audi', 'Tesla']
make_premium = ['Porsche', 'Lamborghini', 'Ferrari']

model_coupe = ['TT', 'GR86', 'Genesis']
model_sedan = ['Civic', 'Model 3', 'Camry']
model_suv = ['X5', 'Rav4', 'Wrangler']
model_truck = ['F150', 'Tacoma', 'Silverado']

def classify_make(make: str) -> str:
    if make in make_standard:
        return 'Standard'
    elif make in make_luxury:
        return 'Luxury'
    elif make in make_premium:
        return 'Premium'
    else:
        return 'Unknown'
    
def classify_model(model: str) -> str:
    if model in model_coupe:
        return 'Coupe'
    elif model in model_sedan:
        return 'Sedan'
    elif model in model_suv:
        return 'SUV'
    elif model in model_truck:
        return 'Truck'
    else:
        return 'Unknown'

inventory: dict[str, Car] = {}

def build_car(data: dict) -> Car:
    data["start_date"] = datetime.strptime(data["start_date"], "%m/%d/%Y")
    data["end_date"] = datetime.strptime(data["end_date"], "%m/%d/%Y")
    data["make_class"] = classify_make(data["make"])
    data["model_class"] = classify_model(data["model"])
    data["total_price"] = 0.0  # Placeholder until pricing function runs

    return Car(**data)

raw_inventory = [
    {"make" : "Tesla",
    "model" : "Model 3",
    "year" : 2023,
    "zip_code" : 92101,
    "address" : "1234 Harbor Dr, San Diego, CA 92101",
    "mileage" : 12500,
    "owner" : "EV Motors Dealership",
    "vin" : "5YJ3E1EA9JF000001",
    "start_date" : "8/6/2025",
    "end_date" : "8/11/2025",
    "fuel_type" : "electric",
    "mpg" : None,
    "range" : 130},

    {"make" : "BMW",
    "model" : "X5",
    "year" : 2022,
    "zip_code" : 92109,
    "address" : "5678 Mission Bay Dr, San Diego, CA 92109",
    "mileage" : 18750,
    "owner" : "Sarah Johnson",
    "vin" : "5UXCR6C0XN9000002",
    "start_date" : "8/6/2025",
    "end_date" : "8/11/2025",
    "fuel_type" : "gas",
    "mpg" : 23,
    "range" : None},

    {"make" : "Jeep",
    "model" : "Wrangler",
    "year" : 2023,
    "zip_code" : 92103,
    "address" : "9012 Balboa Park Dr, San Diego, CA 92103",
    "mileage" : 8900,
    "owner" : "Adventure Rentals Co.",
    "vin" : "1C4HJXDG9NW000003",
    "start_date" : "8/6/2025",
    "end_date" : "8/11/2025",
    "fuel_type" : "gas",
    "mpg" : 19,
    "range" : None},

    {"make" : "Honda",
    "model" : "Civic",
    "year" : 2024,
    "zip_code" : 92104,
    "address" : "3456 University Ave, San Diego, CA 92104",
    "mileage" : 3200,
    "owner" : "Mike Chen",
    "vin" : "19XFC2F59NE000004",
    "start_date" : "8/6/2025",
    "end_date" : "8/11/2025",
    "fuel_type" : "gas",
    "mpg" : 35,
    "range" : None}

]

for car_data in raw_inventory:
    car = build_car(car_data)
    inventory[car.vin] = car
         

