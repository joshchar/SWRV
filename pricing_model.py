import pandas as pd
#from pandasgui import show
from Inventory import Car, classify_make, classify_model, inventory

# we give this model something that looks like 
# {make = , model = , mileage = , start_date = , end_date = }}


#need to update the lists with new car types







def rental_price(car, date):
    base_price = 50 #this is our base price per day
    current_price = 0
    daily_multiplier = 1.0
    

    if date.weekday() in [4,5]:
            daily_multiplier += .2

    if date.month in [6,7,8,12]:
            daily_multiplier += .1

    if car.model_class in ['Sedan', 'Coupe']:
        current_price = base_price
    elif car.model_class in ['SUV', 'Truck']:
        current_price = base_price + 10
    

    if car.make_class == 'Standard':
        current_price = current_price
    elif car.make_class == 'Luxury':
        current_price *=  1.2
    elif car.make_class == 'Premium':
        current_price *=  1.5
    
    if car.mileage > 100000:
        current_price *= 0.8

    current_price *= daily_multiplier

    return round(current_price, 2)

def total_price(car):
    total = 0
    mpg_multiplier = 1.0

    
    rental_days = pd.date_range(start = car.start_date, end = car.end_date)

    for date in rental_days:
        total += rental_price(car, date)


    if car.fuel_type == 'electric':
        if car.range > 240:
            mpg_multiplier = 1.15
    elif car.fuel_type == 'gas':
        if car.model_class == 'SUV' or car.model_class == 'Truck':
            if car.mpg > 28 :
                mpg_multiplier = 1.15
        elif car.model_class == 'Sedan' or car.model_class == 'Coupe':
            if car.mpg > 35:
                mpg_multiplier = 1.15
    elif car.fuel_type == 'hybrid':
        if car.range == "None":
            if car.model_class == 'SUV' or car.model_class == 'Truck':
                if car.mpg > 36:
                    mpg_multiplier = 1.15
            elif car.model_class == 'Sedan' or car.model_class == 'Coupe':
                if car.mpg > 45:
                    mpg_multiplier = 1.15
        elif car.range != "None":
            if car.model_class == 'SUV' or car.model_class == 'Truck':
                if car.mpg > 29:
                    mpg_multiplier = 1.15
            elif car.model_class == 'Sedan' or car.model_class == 'Coupe':
                if car.mpg > 40:
                    mpg_multiplier = 1.15

    total *= mpg_multiplier

    return round(total, 2)


