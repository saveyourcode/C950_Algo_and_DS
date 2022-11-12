# Kyle Jack
# Student Id: 009204163

import csv
import datetime

from HashTable import LinearProbingHashTable
from Package import Package
from Truck import Truck

# O(n)
# Creates a dictionary with the address string as the key and the integer value of the corresponding
# index in the distance matrix.
def get_address_dict(filename):
    dict = {}
    with open(filename) as address_file:
        address_data = csv.reader(address_file, delimiter=',')
        for row in address_data:
            dict[row[1]] = int(row[0])

    return dict

# O(n^2)
# Returns a two dimensional array of float values containing the distance from each address to
# every other address.
def get_distance_matrix(filename):

    dist_matrix = []
    with open(filename) as distance_file:
        distance_data = csv.reader(distance_file, delimiter=",")
        for row in distance_data:
            dist_matrix.append(row)
    for row in range(len(dist_matrix)):
        for col in range(len(dist_matrix[row])):
            dist_matrix[row][col] = float(dist_matrix[row][col])

    return dist_matrix

# O(n)
# Returns a hash table that contains objects containing each package's information.
def get_hashtable(filename):

    hashmap = LinearProbingHashTable()

    with open(filename) as package_file:
        package_date = csv.reader(package_file, delimiter=",")
        for row in package_date:
            package_id = int(row[0])
            address = row[1]
            city = row[2]
            state = row[3]
            zipcode = row[4]
            deadline = row[5]
            weight = int(row[6])
            special_instruct = row[7]

            package = Package(package_id, address, city, state, zipcode, deadline, weight, special_instruct)

            hashmap.insert(package_id, package)

    return hashmap
# O(1)
# Prints the header that contains the labels for each field of the package output.
def print_header():
    id = "Id"
    address = "Address"
    city = "City"
    zipcode = "Zipcode"
    weight = "KG"
    deadline = "Deadline"
    status = "Status"
    delivered = "Delivered at"
    print(f"{id:2} || {address:^38} || {city:^16} || {zipcode} || {weight:^2} || {deadline:^9} || {status:^9} || {delivered}")
    print("-" * 123)

# Creates variables that hold the address dictionary, distance matrix, and hash table.
address_dictionary = get_address_dict("Addresses.csv")
distance_matrix = get_distance_matrix("DistanceData.csv")
hashtable = get_hashtable("PackageData.csv")

# Truck1 has the packages 13, 14, 15, 16, 19, and 20 that need to be delivered on the same truck.
truck1_load = [1, 4, 8, 13, 14, 15, 16, 19, 20, 21, 29, 30, 31, 34, 39, 40]

# Truck 2 has packages 3, 18, 36, 38 that need to be on truck 2.
truck2_load = [3, 5, 6, 18, 25, 26, 36, 37, 38]

truck3_load = [2, 7, 9, 10, 11, 12, 17, 22, 23, 24, 27, 28, 32, 33, 35]

datetime_now = datetime.datetime.now()

# Truck1's departure time is set to 8:00 am, the earliest time a truck can leave the hub.
truck1 = Truck(datetime_now.replace(hour=8, minute=0, second=0))

# Truck2's departure time is set to 9:10 am, this accommodates the delayed packages.
truck2 = Truck(datetime_now.replace(hour=9, minute=10, second=0))

# Truck3's departure time is set to 10:30 am, this is for package 9 that changes address and is after
# Truck1 returns from its first round of deliveries.
truck3 = Truck(datetime_now.replace(hour=10, minute=30, second=0))

# Truck 1, 2, and 3 are loaded with truck1_load, truck2_load, and truck3_load respectively.
truck1.load_packages(truck1_load, hashtable)
truck2.load_packages(truck2_load, hashtable)
truck3.load_packages(truck3_load, hashtable)

# The deliver_packages class method is called for truck1, truck2, and truck3 to deliver the packages.
truck1.deliver_packages(address_dictionary, distance_matrix)
truck2.deliver_packages(address_dictionary, distance_matrix)
truck3.deliver_packages(address_dictionary, distance_matrix)

# This while loops shows the menu of user choices and will continue to reprint it until the user chooses
# option 4 which will exit the while loop and end the program.
while True:
    print("1 - Total miles driven by all trucks")
    print("2 - Status of all packages at specific time")
    print("3 - Status of a specific package at a specific time")
    print("4 - Close the program")
    user_choice = int(input("Enter selection number here: "))

    if user_choice == 1:
        print(f"Total miles driven by all trucks: {truck1.mileage + truck2.mileage + truck3.mileage} miles\n")

    # The user's time is used to set the status of each package at the chosen time and then each package is
    # printed in order of package id.
    if user_choice == 2:
        chosen_time = input("Enter the time (HH:MM):  ")
        (h, m) = chosen_time.split(":")
        chosen_datetime = datetime.datetime.now()
        chosen_datetime = chosen_datetime.replace(hour=int(h), minute=int(m), second=0)
        print_header()
        for i in range(len(hashtable.table)):
            package = hashtable.search(i + 1)
            package.change_status(chosen_datetime)
            package.print_package()

    # The user's choice of time is used to set the status of the package with the id that matches the user's
    # choice and then that package is printed.
    if user_choice == 3:
        chosen_time = input("Enter the time (HH:MM:SS):  ")
        chosen_id = int(input("Enter the package id: "))
        (h, m) = chosen_time.split(":")
        chosen_datetime = datetime.datetime.now()
        chosen_datetime = chosen_datetime.replace(hour=int(h), minute=int(m), second=0)
        package = hashtable.search(chosen_id)
        package.change_status(chosen_datetime)
        print_header()
        package.print_package()

    # The program ends.
    if user_choice == 4:
        break











