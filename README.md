# The-Parking-Garage
The project is The Parking Garage software system. There are 4 files in total namely: MangoDB.py, Vehicle_Class.py, Parking_Garage.py and Main.py. 
In order to understand the requirements and the capacity of the layout, please go through the "TheParkingGarage" PDF file I have attached in the same repository. 

### MangoDB.py
It is a class to upload the complete details of every vehicle into the MangoDb database when the vehicle exit the parking garage. 

### Vehicle_Classs.py
This file contains the vehicle class which takes vehicle type and vehicle number as an input. 

### Parking_Garage.py
This file has the class named Parking which is responsible only for parking lot details.It contains around 7 functions to perform related to parking lot starting from the veicle check-in to till the vehicle check-out. 
The Parking class includes the following functions, 
1. Create parking lot table 
2. upload the data along with check-in time 
3. display the status 
4. return the parking lot table and details as a DataFrame whenever we call
5. price calculation
6. parking duration calculation
7. backup the parking lot table for security
8. check_out

### Main.py 
This is where all the above mentioned files have been imported to and run the final function main(). 
Since the program is designed having an intention that it would run 24/7 on the server, we need to run (only once) these two lines of code *garage = Parking() & garage.create_parking_lot_table()* before we run main() functio from Main.py. 
I have uploaded ipynb file which includes all lines of code. Incase you are familiar with jupyter notebook, you can run The_Parking_garage_Kumar.ipynb file.

### Further Development
I need to deploy it in the server and make it run over there. Also, I need to connect backup function to take backup of the data everyday at a specific time. 
