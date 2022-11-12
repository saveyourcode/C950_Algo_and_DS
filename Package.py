# Contains the variables and methods of the package class
class Package:

    # The constructor that creates a package object
    def __init__(self, package_id, address, city, state, zipcode, deadline, weight, special_note,
                status="At Hub", time_loaded=None, time_delivered=None):

        self.package_Id = package_id
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.deadline = deadline
        self.weight = weight
        self.special_note = special_note
        self.status = status
        self.time_loaded = time_loaded
        self.time_delivered = time_delivered

    # O(1)
    # Changes the delivery status of the package depending on the datetime object passed as an argument.
    def change_status(self, time):

        if time < self.time_loaded:
            self.status = "At Hub"
        elif time > self.time_loaded and time < self.time_delivered:
            self.status = "En Route"
        else:
            self.status = "Delivered"

    def print_package(self):
        time_delivered = "N/A"
        if self.status != "Delivered":

            print(f"{self.package_Id:2} || {self.address:^38} || {self.city:^16} || {self.zipcode:^7} || {self.weight:^2} ||"
               f" {self.deadline:^9} || {self.status:^9} || {time_delivered}")
        else:
            print(self)

    # When a package object is printed the specified variables are printed in this order.
    def __str__(self):
        return f"{self.package_Id:2} || {self.address:^38} || {self.city:^16} || {self.zipcode:^7} || {self.weight:^2} ||" \
               f" {self.deadline:^9} || {self.status:^9} || {self.time_delivered:%H:%M:%S}"




