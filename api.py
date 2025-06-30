from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from datetime import datetime
import pandas as pd
from pricing_model import rental_price, total_price
from Inventory import inventory, Car
from typing import Optional, Union

app = FastAPI()


class PricingResponse(BaseModel):
    rental_price: float
    total_price: float

# This is a root check, basically is a way to check that the API is running

@app.get("/")
def read_root():
    return {"message": "Car Pricing API is running!"}

# this get allows us to get the car details by the VIN number

@app.get("/cars/{vin}", response_model=Car)
def get_car(vin: str): 
    if vin not in inventory:
        raise HTTPException(status_code=404, detail="Car not found")
    return inventory[vin]

# this get allows us to get the pricing details by vin
@app.get("/pricing/{vin}", response_model=PricingResponse)
def get_pricing(vin: str):
    if vin not in inventory:
        raise HTTPException(status_code=404, detail="Car not found") 
    
    car = inventory[vin]
    total = total_price(car)
    num_days = (car.end_date - car.start_date).days + 1
    daily = total / num_days

    return {"rental_price": round(daily, 2), "total_price": total}