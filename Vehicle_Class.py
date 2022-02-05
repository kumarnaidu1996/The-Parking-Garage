# Import the required libraries
import os
import pandas as pd
import numpy as np


# vehicle class
class Vehicle:

    def __init__(self, vehicle_type, vehicle_number):
        self.vehicle_type = vehicle_type
        self.vehicle_number = vehicle_number

    def __repr__(self):
        return f'{self.vehicle_type},{self.vehicle_number}'
