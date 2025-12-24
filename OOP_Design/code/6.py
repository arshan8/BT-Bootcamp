# ==================== CUSTOMER ==================== #
from abc import ABC, abstractmethod

class Customer:
    def __init__(self, customer_id, name):
        self.__id = customer_id
        self.name = name

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Customer name must be string")
        self.__name = value


# ==================== BOOKING ==================== #

class Booking:
    def __init__(self, booking_id, customer, amount):
        self.__id = booking_id
        if not isinstance(customer, Customer):
            raise TypeError("Invalid customer")
        if not isinstance(amount, (int, float)) or amount <= 0:
            raise ValueError("Invalid amount")

        self.__customer = customer
        self.__amount = amount

    @property
    def id(self):
        return self.__id

    @property
    def customer(self):
        return self.__customer

    @property
    def amount(self):
        return self.__amount


# ==================== SHIP ==================== #

class Ship(ABC):
    def __init__(self, ship_id, name):
        self.__id = ship_id
        self.name = name
        self.__bookings = []

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Ship name must be string")
        self.__name = value

    def add_booking(self, booking):
        if not isinstance(booking, Booking):
            raise TypeError("Only Booking allowed")
        self.__bookings.append(booking)

    @property
    def bookings(self):
        return tuple(self.__bookings)

    def total_amount(self):
        return sum(b.amount for b in self.__bookings)


class CruiseShip(Ship):
    pass


class CargoShip(Ship):
    pass


# ==================== MARINE COMPANY ==================== #

class MarineCompany:
    def __init__(self, company_id, name):
        self.__id = company_id
        self.name = name
        self.__ships = []

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Company name must be string")
        self.__name = value

    def add_ship(self, ship):
        if not isinstance(ship, Ship):
            raise TypeError("Only Ship allowed")
        self.__ships.append(ship)

    @property
    def ships(self):
        return tuple(self.__ships)

    # 1. Total amount collected
    def total_amount_collected(self):
        return sum(ship.total_amount() for ship in self.__ships)

    # 2. Total amount per ship
    def amount_per_ship(self):
        return {ship.name: ship.total_amount() for ship in self.__ships}

    # 3. Customers for a particular cruise ship
    def customers_for_cruise_ship(self, ship_id):
        for ship in self.__ships:
            if ship.id == ship_id and isinstance(ship, CruiseShip):
                return [b.customer for b in ship.bookings]
        return []



if __name__ == "__main__":

    # Marine Company
    company = MarineCompany(1, "Blue Ocean Ltd")

    # Ships
    cruise_ship = CruiseShip(101, "Ocean Queen")
    cargo_ship = CargoShip(201, "Cargo Titan")

    company.add_ship(cruise_ship)
    company.add_ship(cargo_ship)

    # Customers
    c1 = Customer(1, "Alice")
    c2 = Customer(2, "Bob")
    c3 = Customer(3, "Charlie")

    # Bookings
    cruise_ship.add_booking(Booking(1, c1, 5000))
    cruise_ship.add_booking(Booking(2, c2, 6000))
    cargo_ship.add_booking(Booking(3, c3, 12000))

    # Outputs
    print("Total amount collected:",
          company.total_amount_collected())

    print("\nAmount collected per ship:")
    for ship, amount in company.amount_per_ship().items():
        print(ship, ":", amount)

    print("\nCustomers for Cruise Ship Ocean Queen:")
    for customer in company.customers_for_cruise_ship(101):
        print("-", customer.name)