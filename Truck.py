from datetime import timedelta

# Contains the variables and methods of the Truck class.
class Truck:

    # Constructor that creates a Truck object
    def __init__(self, time, location=0, mileage=0):

        self.package_list = []
        self.time = time
        self.location = location
        self.mileage = mileage

    # O(1)
    # Adds a package to a truck's package list and sets the package's delivery status to "En Route"
    def add_package(self, package):

        package.status = "En Route"
        package.time_loaded = self.time
        self.package_list.append(package)

    # O(n^2)
    # This is the implementation of the nearest neighbor argument that's used to deliver all the packages
    # in the truck's package list. It cycles through the all the packages in the truck's package list and
    # selects the package with the closest address to the truck's current location and then removes the package
    # from the truck's package list once the package is delivered. After all the packages are delivered the
    # truck returns to the hub.
    def deliver_packages(self, address_dict, distance_matrix):

        while(len(self.package_list) > 0):

            nearest_neighbor = "empty"
            lowest_dist = float('inf')

            for package in self.package_list:

                address_index = address_dict.get(package.address)
                distance = distance_matrix[self.location][address_index]
                if distance < lowest_dist:
                    lowest_dist = distance
                    nearest_neighbor = package

            self.mileage += lowest_dist
            self.location = address_dict[nearest_neighbor.address]
            nearest_neighbor.status = "Delivered"
            time_diff = self._find_time(lowest_dist)
            self.time = self.time + timedelta(minutes=time_diff)
            nearest_neighbor.time_delivered = self.time
            self.package_list.remove(nearest_neighbor)

        dist_to_hub = distance_matrix[self.location][0]
        time_diff = self._find_time(dist_to_hub)
        self.time = self.time + timedelta(minutes=time_diff)
        self.mileage += dist_to_hub
        self.location = 0

    def __str__(self):
        return f"Time returned to hub: {self.time} || total miles: {self.mileage}"

    # O(1)
    # Finds the time driven for the distance passed as an argument.
    def _find_time(self, dist):
        return (dist/18) * 60

    # O(n)
    # For each number in the number_list argument each package in the hash table with
    # the matching package id is added to the truck's package list.
    def load_packages(self, number_list, hashtable):
        for number in number_list:
            if number == 9:
                package = hashtable.search(9)
                package.address = "410 S State St"
                package.zipcode = "84111"
            self.add_package(hashtable.search(number))




