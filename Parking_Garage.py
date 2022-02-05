# Import the required libraries
import os
import pandas as pd
import numpy as np


# Parking-lot class
class Parking:

    def __init__(self):
        pass

    def create_parking_lot_table(self):

        self.df = pd.DataFrame(index=np.arange(1, 376),
                               columns=['Vehicle_Type', 'Vehicle_Number', 'Check_In', 'Check_Out'])

    def check_in(self, car_details):

        # Checking if there is any empty space in the parking lot
        if not self.df['Vehicle_Number'].isna().any():
            print("Sorry! The parking lot is full")

        else:
            # Get vehicle_type and number from Vehicle class
            vehicle_type, vehicle_number = str(car_details).split(',')

            # Get the last available parking space
            empty = self.df[self.df.Vehicle_Type.isna()].index
            available = empty.max()

            # Allocate the vehicle to the last parking space
            self.df.loc[available, 'Vehicle_Type'] = vehicle_type

            # Assign the vehicle number into parking number
            self.df.loc[available, 'Vehicle_Number'] = vehicle_number

            # Store the check_in date and time
            self.df.loc[available, 'Check_In'] = pd.Timestamp.now()

            print(f'Please park your {vehicle_type} in parking number {available}')

    def display_parking_lot_capacity(self):

        empty_space = self.df.Vehicle_Number.isna().sum()
        filled_space = self.df.Vehicle_Number.notnull().sum()

        return empty_space, filled_space

    def return_parking_lot_table(self):
        return self.df

    @staticmethod
    def parking_price_calculator(duration, vehicle_type):

        # parking price in euro per hour (can be adjustable)
        car = 1
        truck = 1.5
        motor_cycle = 0.7

        # Calculate the parking duration in hours
        parking_time = duration.seconds / 3600

        # parking cost calculation
        cost = [parking_time * car if vehicle_type == 'car'
                else parking_time * truck if vehicle_type == 'truck' else parking_time * motor_cycle]

        return cost

    def parking_duration_calculator(self, parking_lot_number):

        # Get the check_in and check_out timings
        park_in = self.df.loc[parking_lot_number[0], 'Check_In']
        park_out = self.df.loc[parking_lot_number[0], 'Check_Out']

        # Calculate the parking duration
        duration = (park_out - park_in)

        return duration

    def backup(self):

        import os
        t = pd.datetime.now()
        cwd = os.getcwd()
        path = cwd + "/" f'{t.year}.{t.month}.{t.day}.{t.hour}.{t.minute}.{t.second}.{t.microsecond}.csv'
        self.df.to_csv(path)
        print('Took Backup!')

    def check_out(self, vehicle_number):

        # Search for the vehicle number in the parking_lot
        if self.df.Vehicle_Number.isin([vehicle_number]).any():

            # Get the parking_lot number of the vehicle
            exit_lot = self.df[self.df.Vehicle_Number == vehicle_number].index

            # Display parking_lot number
            print(f"Your vehicle is in parking_lot: {exit_lot[0]}")

            print("")
            # Confirm if driver wants to check_out
            exit_type = input('Do you want to exit [y/n]: ')

            if exit_type == 'n':

                # If the driver doesn't want to check-out
                print("Your vehicle is safe!")

            elif exit_type == 'y':

                # Record the check_out date and time
                self.df.loc[exit_lot[0], 'Check_Out'] = pd.Timestamp.now()

                # Vehicle type to decide the parking price
                vehicle_typ = self.df.loc[exit_lot[0], 'Vehicle_Type']
                duration = self.parking_duration_calculator(exit_lot)

                # Parking price calculation
                parking_cost = self.parking_price_calculator(duration, vehicle_typ)

                # Extract vehicle details as dictionary
                record = self.df.loc[exit_lot[0], :].to_dict()
                record['parking_duration'] = duration
                record['parking_cost_in_euro'] = round(parking_cost[0], 2)

                # Erase the data from parking space as the vehicle check_out
                self.df.loc[exit_lot[0], :] = np.NaN

                print('Thank you! Please visit us again.')
                return record

            else:
                print("Error! Wrong input")

        else:
            print()
            print('No vehicle found')  # If driver enters wrong number
            print("Please check your vehicle number")  # When the vehicle is not parked in the parking_lot
