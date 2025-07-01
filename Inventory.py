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
    num_seats: int
    drive_train: str 
    transmission: str


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
    "mileage" : 15000,
    "owner" : "Premium Motors San Diego",
    "vin" : "TSLA123456789",
    "start_date" : "8/6/2025",
    "end_date" : "8/11/2025",
    "fuel_type" : "electric",
    "mpg" : None,
    "range" : 300,
    "num_seats": 5,
    "drive_train": "RWD",
    "transmission": "Automatic"},

    {"make" : "BMW",
    "model" : "X5",
    "year" : 2022,
    "zip_code" : 92101,
    "address" : "1234 Harbor Dr, San Diego, CA 92101",
    "mileage" : 25000,
    "owner" : "Premium Motors San Diego",
    "vin" : "BMW123456789",
    "start_date" : "8/6/2025",
    "end_date" : "8/11/2025",
    "fuel_type" : "gas",
    "mpg" : 28,
    "range" : None,
    "num_seats": 7,
    "drive_train": "AWD",
    "transmission": "Automatic"},

    {"make" : "Jeep",
    "model" : "Wrangler",
    "year" : 2022,
    "zip_code" : 92101,
    "address" : "1234 Harbor Dr, San Diego, CA 92101",
    "mileage" : 30000,
    "owner" : "Premium Motors San Diego",
    "vin" : "JEEP123456789",
    "start_date" : "8/6/2025",
    "end_date" : "8/11/2025",
    "fuel_type" : "gas",
    "mpg" : 19,
    "range" : None,
    "num_seats": 7,
    "drive_train": "4WD",
    "transmission": "Manual"},

    {"make" : "Honda",
    "model" : "Civic",
    "year" : 2023,
    "zip_code" : 92101,
    "address" : "1234 Harbor Dr, San Diego, CA 92101",
    "mileage" : 12000,
    "owner" : "Premium Motors San Diego",
    "vin" : "HONDA123456789",
    "start_date" : "8/6/2025",
    "end_date" : "8/11/2025",
    "fuel_type" : "gas",
    "mpg" : 35,
    "range" : None,
    "num_seats": 5,
    "drive_train": "FWD",
    "transmission": "CVT"},

    {"make" : "Audi",
    "model" : "A4",
    "year" : 2023,
    "zip_code" : 92108,
    "address" : "5678 Mission Valley Rd, San Diego, CA 92108",
    "mileage" : 18000,
    "owner" : "Premium Motors San Diego",
    "vin" : "AUDI123456789",
    "start_date" : "8/6/2025",
    "end_date" : "8/11/2025",
    "fuel_type" : "gas",
    "mpg" : 32,
    "range" : None,
    "num_seats": 5,
    "drive_train": "AWD",
    "transmission": "Automatic"},

    {"make" : "Mercedes-Benz",
    "model" : "C-Class",
    "year" : 2022,
    "zip_code" : 92108,
    "address" : "5678 Mission Valley Rd, San Diego, CA 92108",
    "mileage" : 22000,
    "owner" : "Elite Auto Group",
    "vin" : "MERC123456789",
    "start_date" : "8/6/2025",
    "end_date" : "8/11/2025",
    "fuel_type" : "gas",
    "mpg" : 30,
    "range" : None,
    "num_seats": 5,
    "drive_train": "RWD",
    "transmission": "Automatic"},

    {"make" : "Toyota",
    "model" : "RAV4",
    "year" : 2023,
    "zip_code" : 92108,
    "address" : "5678 Mission Valley Rd, San Diego, CA 92108",
    "mileage" : 16000,
    "owner" : "Elite Auto Group",
    "vin" : "TOYO123456789",
    "start_date" : "8/6/2025",
    "end_date" : "8/11/2025",
    "fuel_type" : "gas",
    "mpg" : 33,
    "range" : None,
    "num_seats": 5,
    "drive_train": "AWD",
    "transmission": "CVT"},

    {"make" : "Nissan",
    "model" : "Altima",
    "year" : 2023,
    "zip_code" : 92108,
    "address" : "5678 Mission Valley Rd, San Diego, CA 92108",
    "mileage" : 14000,
    "owner" : "Elite Auto Group",
    "vin" : "NISS123456789",
    "start_date" : "8/6/2025",
    "end_date" : "8/11/2025",
    "fuel_type" : "gas",
    "mpg" : 34,
    "range" : None,
    "num_seats": 5,
    "drive_train": "FWD",
    "transmission": "CVT"},

    {"make" : "Porsche",
    "model" : "Macan",
    "year" : 2023,
    "zip_code" : 92037,
    "address" : "9012 La Jolla Village Dr, La Jolla, CA 92037",
    "mileage" : 8000,
    "owner" : "Coastal Car Collection",
    "vin" : "PORS123456789",
    "start_date" : "8/6/2025",
    "end_date" : "8/11/2025",
    "fuel_type" : "gas",
    "mpg" : 26,
    "range" : None,
    "num_seats": 5,
    "drive_train": "AWD",
    "transmission": "Automatic"},

    {"make" : "Lexus",
    "model" : "RX",
    "year" : 2022,
    "zip_code" : 92037,
    "address" : "9012 La Jolla Village Dr, La Jolla, CA 92037",
    "mileage" : 19000,
    "owner" : "Coastal Car Collection",
    "vin" : "LEXU123456789",
    "start_date" : "8/6/2025",
    "end_date" : "8/11/2025",
    "fuel_type" : "hybrid",
    "mpg" : 30,
    "range" : None,
    "num_seats": 5,
    "drive_train": "AWD",
    "transmission": "CVT"},

    {"make" : "Volkswagen",
    "model" : "Atlas",
    "year" : 2023,
    "zip_code" : 92037,
    "address" : "9012 La Jolla Village Dr, La Jolla, CA 92037",
    "mileage" : 17000,
    "owner" : "Coastal Car Collection",
    "vin" : "VOLK123456789",
    "start_date" : "8/6/2025",
    "end_date" : "8/11/2025",
    "fuel_type" : "gas",
    "mpg" : 27,
    "range" : None,
    "num_seats": 7,
    "drive_train": "AWD",
    "transmission": "Automatic"},

    {"make" : "Subaru",
    "model" : "Outback",
    "year" : 2023,
    "zip_code" : 92037,
    "address" : "9012 La Jolla Village Dr, La Jolla, CA 92037",
    "mileage" : 13000,
    "owner" : "Coastal Car Collection",
    "vin" : "SUBA123456789",
    "start_date" : "8/6/2025",
    "end_date" : "8/11/2025",
    "fuel_type" : "gas",
    "mpg" : 29,
    "range" : None,
    "num_seats": 7,
    "drive_train": "AWD",
    "transmission": "CVT"},

    {"make" : "Ford",
    "model" : "Mustang",
    "year" : 2023,
    "zip_code" : 92104,
    "address" : "2345 University Ave, San Diego, CA 92104",
    "mileage" : 9000,
    "owner" : "Hillcrest Motors",
    "vin" : "FORD123456789",
    "start_date" : "8/6/2025",
    "end_date" : "8/11/2025",
    "fuel_type" : "gas",
    "mpg" : 25,
    "range" : None,
    "num_seats": 4,
    "drive_train": "RWD",
    "transmission": "Manual"},

    {"make" : "Chevrolet",
    "model" : "Tahoe",
    "year" : 2022,
    "zip_code" : 92104,
    "address" : "2345 University Ave, San Diego, CA 92104",
    "mileage" : 35000,
    "owner" : "Hillcrest Motors",
    "vin" : "CHEV123456789",
    "start_date" : "8/6/2025",
    "end_date" : "8/11/2025",
    "fuel_type" : "gas",
    "mpg" : 21,
    "range" : None,
    "num_seats": 8,
    "drive_train": "4WD",
    "transmission": "Automatic"},
    
    {"make" : "Hyundai",
    "model" : "Tucson",
    "year" : 2023,
    "zip_code" : 92104,
    "address" : "2345 University Ave, San Diego, CA 92104",
    "mileage" : 11000,
    "owner" : "Hillcrest Motors",
    "vin" : "HYUN123456789",
    "start_date" : "8/6/2025",
    "end_date" : "8/11/2025",
    "fuel_type" : "gas",
    "mpg" : 29,
    "range" : None,
    "num_seats": 5,
    "drive_train": "AWD",
    "transmission": "Automatic"},

    {"make" : "Mazda",
    "model" : "CX-5",
    "year" : 2023,
    "zip_code" : 92104,
    "address" : "2345 University Ave, San Diego, CA 92104",
    "mileage" : 10000,
    "owner" : "Hillcrest Motors",
    "vin" : "MAZD123456789",
    "start_date" : "8/6/2025",
    "end_date" : "8/11/2025",
    "fuel_type" : "gas",
    "mpg" : 31,
    "range" : None,
    "num_seats": 5,
    "drive_train": "AWD",
    "transmission": "Automatic"},

    {"make" : "Acura",
    "model" : "MDX",
    "year" : 2023,
    "zip_code" : 92109,
    "address" : "3456 Mission Blvd, San Diego, CA 92109",
    "mileage" : 7000,
    "owner" : "Pacific Beach Auto",
    "vin" : "ACUR123456789",
    "start_date" : "8/6/2025",
    "end_date" : "8/11/2025",
    "fuel_type" : "gas",
    "mpg" : 26,
    "range" : None,
    "num_seats": 7,
    "drive_train": "AWD",
    "transmission": "Automatic"},

    {"make" : "Infiniti",
    "model" : "QX50",
    "year" : 2022,
    "zip_code" : 92109,
    "address" : "3456 Mission Blvd, San Diego, CA 92109",
    "mileage" : 20000,
    "owner" : "Pacific Beach Auto",
    "vin" : "INFI123456789",
    "start_date" : "8/6/2025",
    "end_date" : "8/11/2025",
    "fuel_type" : "gas",
    "mpg" : 28,
    "range" : None,
    "num_seats": 5,
    "drive_train": "AWD",
    "transmission": "CVT"},

    {"make" : "Genesis",
    "model" : "G90",
    "year" : 2023,
    "zip_code" : 92109,
    "address" : "3456 Mission Blvd, San Diego, CA 92109",
    "mileage" : 5000,
    "owner" : "Pacific Beach Auto",
    "vin" : "GENE123456789",
    "start_date" : "8/6/2025",
    "end_date" : "8/11/2025",
    "fuel_type" : "gas",
    "mpg" : 25,
    "range" : None,
    "num_seats": 5,
    "drive_train": "RWD",
    "transmission": "Automatic"},

    {"make" : "Cadillac",
    "model" : "XT6",
    "year" : 2022,
    "zip_code" : 92109,
    "address" : "3456 Mission Blvd, San Diego, CA 92109",
    "mileage" : 26000,
    "owner" : "Pacific Beach Auto",
    "vin" : "CADI123456789",
    "start_date" : "8/6/2025",
    "end_date" : "8/11/2025",
    "fuel_type" : "gas",
    "mpg" : 24,
    "range" : None,
    "num_seats": 7,
    "drive_train": "AWD",
    "transmission": "Automatic"},

    {"make" : "Volvo",
    "model" : "XC90",
    "year" : 2023,
    "zip_code" : 91910,
    "address" : "4567 Broadway, Chula Vista, CA 91910",
    "mileage" : 6000,
    "owner" : "Chula Vista Premium Cars",
    "vin" : "VOLV123456789",
    "start_date" : "8/6/2025",
    "end_date" : "8/11/2025",
    "fuel_type" : "hybrid",
    "mpg" : 27,
    "range" : 33,
    "num_seats": 7,
    "drive_train": "AWD",
    "transmission": "Automatic"},

    {"make" : "Lincoln",
    "model" : "Aviator",
    "year" : 2023,
    "zip_code" : 91910,
    "address" : "4567 Broadway, Chula Vista, CA 91910",
    "mileage" : 4000,
    "owner" : "Chula Vista Premium Cars",
    "vin" : "LINC123456789",
    "start_date" : "8/6/2025",
    "end_date" : "8/11/2025",
    "fuel_type" : "hybrid",
    "mpg" : 23,
    "range" : 21,
    "num_seats": 7,
    "drive_train": "AWD",
    "transmission": "Automatic"},

    {"make" : "Jaguar",
    "model" : "F-PACE",
    "year" : 2023,
    "zip_code" : 91910,
    "address" : "4567 Broadway, Chula Vista, CA 91910",
    "mileage" : 8500,
    "owner" : "Chula Vista Premium Cars",
    "vin" : "JAGU123456789",
    "start_date" : "8/6/2025",
    "end_date" : "8/11/2025",
    "fuel_type" : "gas",
    "mpg" : 23,
    "range" : None,
    "num_seats": 5,
    "drive_train": "AWD",
    "transmission": "Automatic"},

    {"make" : "Land Rover",
    "model" : "Range Rover Evoque",
    "year" : 2022,
    "zip_code" : 91910,
    "address" : "4567 Broadway, Chula Vista, CA 91910",
    "mileage" : 23000,
    "owner" : "Chula Vista Premium Cars",
    "vin" : "LAND123456789",
    "start_date" : "8/6/2025",
    "end_date" : "8/11/2025",
    "fuel_type" : "gas",
    "mpg" : 26,
    "range" : None,
    "num_seats": 5,
    "drive_train": "AWD",
    "transmission": "Automatic"}

]

for car_data in raw_inventory:
    car = build_car(car_data)
    inventory[car.vin] = car
         

