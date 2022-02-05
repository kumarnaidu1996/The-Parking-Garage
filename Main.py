# Import the required libraries
import os
import pandas as pd
import numpy as np

from MangoDB import Mangodb
from Vehicle_Class import Vehicle
from Parking_Garage import Parking


def check_in_for_main():
    vehicle_type = input("Enter your vehicle type: ")
    vehicle_number = input("Enter your vehicle number: ")
    print()

    car = Vehicle(vehicle_type, vehicle_number)
    garage.check_in(car)

    print('Thank you!')


def check_out_for_main():
    vehicle_num = input("Vehicle number: ")
    bill = garage.check_out(vehicle_num)

    if bill is None:
        pass
    else:
        for i, j in bill.items():
            print(f'{i}:\t\t{j}')

        bill['parking_duration_in_hr'] = bill['parking_duration'].seconds / 3600
        bill.pop('parking_duration')
        db = Mangodb()
        db.data_upload_to_mangodb(bill)

# Run garage.create_parking_lot_table() only once to create a parking table


garage = Parking()
garage.create_parking_lot_table()


def main():
    empty, filled = garage.display_parking_lot_capacity()
    print(f'\tAvailable: \t{empty}\n \tfilled: \t{filled}')

    user_input = input('check_in or check_out ?: ')

    if user_input == 'check_in':
        check_in_for_main()

    elif user_input == 'check_out':
        check_out_for_main()

    else:
        print('Error! Wrong input.')
