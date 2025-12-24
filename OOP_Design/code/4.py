# ==================== MENU ITEM ==================== #

class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Item name must be a string")
        self.__name = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if not isinstance(value, (int, float)) or value <= 0:
            raise ValueError("Price must be positive")
        self.__price = value

    def discounted_price(self, discount):
        return self.__price * (1 - discount / 100)


# ==================== COURSE CATEGORY ==================== #

class CourseCategory:
    def __init__(self, name):
        self.name = name
        self.__items = []     # PRIVATE list

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Category name must be string")
        self.__name = value

    def add_item(self, item):
        if not isinstance(item, MenuItem):
            raise TypeError("Only MenuItem allowed")
        self.__items.append(item)

    @property
    def items(self):
        return tuple(self.__items)   # READ-ONLY access


# ==================== MENU ==================== #

class Menu:
    def __init__(self, name):
        self.name = name
        self.__categories = []   # PRIVATE list

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Menu name must be string")
        self.__name = value

    def add_category(self, category):
        if not isinstance(category, CourseCategory):
            raise TypeError("Only CourseCategory allowed")
        self.__categories.append(category)

    @property
    def categories(self):
        return tuple(self.__categories)   # READ-ONLY

    def display_items(self):
        for category in self.__categories:
            print("Category:", category.name)
            for item in category.items:
                print(f"  {item.name} - ₹{item.price}")


# ==================== SPECIAL MENU ==================== #

class SpecialMenu(Menu):
    def __init__(self, name, discount=30):
        super().__init__(name)
        self.discount = discount

    @property
    def discount(self):
        return self.__discount

    @discount.setter
    def discount(self, value):
        if not isinstance(value, (int, float)) or not (0 < value < 100):
            raise ValueError("Discount must be between 0 and 100")
        self.__discount = value

    def display_items(self):
        for category in self.categories:
            print("Category:", category.name)
            for item in category.items:
                print(
                    f"  {item.name} - ₹{item.price} -> "
                    f"₹{item.discounted_price(self.discount):.2f} "
                    f"({self.discount}% off)"
                )


# ==================== BRANCH ==================== #

class Branch:
    def __init__(self, location):
        self.location = location
        self.__menus = []    # PRIVATE list

    @property
    def location(self):
        return self.__location

    @location.setter
    def location(self, value):
        if not isinstance(value, str):
            raise TypeError("Location must be string")
        self.__location = value

    def add_menu(self, menu):
        if not isinstance(menu, Menu):
            raise TypeError("Only Menu or SpecialMenu allowed")
        self.__menus.append(menu)

    @property
    def menus(self):
        return tuple(self.__menus)   # READ-ONLY


# ==================== RESTAURANT ==================== #

class Restaurant:
    def __init__(self, name):
        self.name = name
        self.__branches = []   # PRIVATE list

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Restaurant name must be string")
        self.__name = value

    def add_branch(self, branch):
        if not isinstance(branch, Branch):
            raise TypeError("Only Branch allowed")
        self.__branches.append(branch)

    # 1. Total menu items
    def total_menu_items(self):
        count = 0
        for branch in self.__branches:
            for menu in branch.menus:
                for category in menu.categories:
                    count += len(category.items)
        return count

    # 2. Items by category
    def items_by_category(self, category_name):
        result = []
        for branch in self.__branches:
            for menu in branch.menus:
                for category in menu.categories:
                    if category.name == category_name:
                        result.extend(category.items)
        return result

    # 3. Special discount menus
    def list_special_menus(self):
        for branch in self.__branches:
            for menu in branch.menus:
                if isinstance(menu, SpecialMenu):
                    print("\nSpecial Menu:", menu.name)
                    menu.display_items()


# ==================== MAIN ==================== #

if __name__ == "__main__":

    starter = CourseCategory("Starter")
    main = CourseCategory("Main Course")
    dessert = CourseCategory("Dessert")

    starter.add_item(MenuItem("Soup", 120))
    main.add_item(MenuItem("Paneer Curry", 250))
    dessert.add_item(MenuItem("Ice Cream", 100))

    regular_menu = Menu("Regular Menu")
    regular_menu.add_category(starter)
    regular_menu.add_category(main)
    regular_menu.add_category(dessert)

    sweet = CourseCategory("Sweet")
    drinks = CourseCategory("Drinks")
    dips = CourseCategory("Dips")

    sweet.add_item(MenuItem("Chocolate Cake", 150))
    drinks.add_item(MenuItem("Cold Coffee", 120))
    dips.add_item(MenuItem("Brownie", 180))

    special_menu = SpecialMenu("Offer Menu", 30)
    special_menu.add_category(sweet)
    special_menu.add_category(drinks)
    special_menu.add_category(dips)

    branch = Branch("Hyderabad")
    branch.add_menu(regular_menu)
    branch.add_menu(special_menu)

    restaurant = Restaurant("Food Palace")
    restaurant.add_branch(branch)

    print("Total Menu Items:", restaurant.total_menu_items())

    print("\nItems in Sweet Category:")
    for item in restaurant.items_by_category("Sweet"):
        print("-", item.name)

    restaurant.list_special_menus()
