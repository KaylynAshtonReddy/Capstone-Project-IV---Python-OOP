# Amended logic for printing the locid_largest variable
# Uploaded new file to dropbox - did not auto-connect earlier.
# Changed Cost variable to float type

from tabulate import tabulate


class Shoe(object):
    """This class defines the attributes of the stock of a shoe within a specific country

    Attributes:
        country : str
            Describes the country location in which the stock of the shoe is located

        code    : int
            Describes the code of the shoe

        product : str
            Describes the shoe  - the description

        cost    : int
            Describes the price of the shoe

        quantity: int
            Describes the number of that particular shoe

        value   : float
            Describes the total cost for the quantity of shoes available per location
    """

    # Initializing global list
    global shoe_object_list
    shoe_object_list = []

    def __init__(self, country, code, product, cost: int, quantity: int):
        self.country = country
        self.code = code
        self.product = product
        self.cost = int(cost)
        self.quantity = int(quantity)
        self.value = cost * quantity
        shoe_object_list.append(self)

    """ '''Methods''' """

    # Returns the country of an instance
    def get_country(self):
        return self.country

    # Returns the code of an instance
    def get_code(self):
        return self.code

    # Returns the product of an instance
    def get_product(self):
        return self.product

    # Returns the cost of an instance
    def get_cost(self):
        return self.cost

    # Returns the quantity of an instance
    def get_quantity(self):
        return self.quantity

    # Returns the value of an instance in float
    def get_value(self):
        return float(self.value)

    # Updates the quantity of an instance and returns the updated quantity
    def set_quantity(self):
        restock_amount = int(input('Enter in the amount you would like to add: '))
        self.quantity = self.quantity + restock_amount
        return self.quantity

    # Updates the value of an instance and returns the updated value
    def update_value(self):
        self.value = self.quantity * self.cost
        return round(float(self.value), 2)

    # Updates the cost of an instance and returns the updated cost
    def mark_up_cost(self):
        mark_up = int(input('Enter in the percentage you want to mark it up by:'))
        mark_up = mark_up / 100
        self.cost = self.cost + (int(self.cost) * mark_up)
        return round(self.cost, 2)

    def __str__(self):
        return '''{},{},{},{},{},{}'''.format(self.country, self.code, self.product, self.cost, self.quantity,
                                              self.value)


# ===========================================================================================================================


def add_shoe(a, b, c, d, e):
    """
    add_shoe takes in 5 variables and passes it to the Shoe object to create an instance

    Args:
        a (str): country
        b (str): code
        c (str): product
        d (int): cost
        e (int): quantity

    Returns:
        object : Shoe object is returned
    """
    return Shoe(a, b, c, d, e)


# Opens text file, requests user for input
# searches the file for the input
# if found, prints out the line item
def search_product():
    """
    search_product : allows user to insert a product code and will return the item if it matches the code within the text file

    """
    # Requests user to enter in data for a specific code
    product_code = input('Please enter in your product code: ')

    # Create header variables
    country_header = 'Country'
    code_header = 'Code'
    product_header = 'Product'
    cost_header = 'Cost'
    quantity_header_5 = 'Quantity'
    value_header = 'Value'
    line_list = []

    # Open file to search for data
    with open('inventory.txt', 'r') as file:

        found = False

        # Loop through each line in file
        for line in file.readlines():
            idx = +1

            # Split each str by comma and declare each as a separate variable
            country, code, product, cost, quantity, value = line.split(',', maxsplit=6)
            line = country, code, product, cost, quantity, value.strip()
            line_list.append(line)

            # Condition to confirm if user input(product_code)
            # Matches any line in the file
            # If true, the line will be displayed for the user

            if product_code == code:
                found = True
                print(f'\nCode {code} is : ')
                print('{:15s}{:<15}{:<20}{:13s}{:10s} {:10s}'.format(country_header, code_header, product_header,
                                                                     cost_header,
                                                                     quantity_header_5,
                                                                     value_header))
                print('{:15s}{:<15}{:<20}R{:13s}{:10s}R{:10s}\n'.format(country, code, product, cost, quantity, value))
                break
            if product_code not in line:
                found = False

        # If product not found, print message to user
        if (not found):
            print('\nProduct not found, please try again! \n')


def mark_up_high_quantity():
    """
    mark_up_high_quantity : Finds the stocked item with the highest quantity and will mark it up a percentage based
    on user input.
    the object instance will be updated and updated data will be written to a file by calling update_inventory()

    """

    # Initilize a list
    quantity_list = []

    # Read data from file
    with open('inventory.txt', 'r') as file:
        # Strip newlines
        file = [x.strip() for x in file.readlines()]

        # Skip the header in the file
        for data in file[1:]:
            data = data.split(',')
            quantity = int(data[4])

            # Append the number to a list
            quantity_list.append(quantity)

        # Find max from the list
        largest = max(quantity_list)

        # Locate index of the largest number
        locid_largest = quantity_list.index(largest) + 1

        # Display to user
        print('The item with the largest quantity is:')

        print(shoe_object_list[locid_largest - 1])

        # Call the method for the specific index
        # Marks up cost attribute of object instance
        print(Shoe.mark_up_cost(shoe_object_list[locid_largest - 1]))

        # Updates the value of the object instance
        print(Shoe.update_value(shoe_object_list[locid_largest - 1]))

        # Prints the updated object instance to the user
        print(shoe_object_list[locid_largest - 1])
        print('\n Product cost has been marked up!'
              'Please check the inventory\n')

        # Calls function to update the inventory file
        update_inventory()


def re_stock_quantity():
    """
    re_stock_quantity : Finds the stocked item with the lowest quantity and will restock it up based
    on user input.
    the object instance will be updated and updated data will be written to a file by calling update_inventory()

    """

    # Initialize list
    quantity_list = []

    with open('inventory.txt', 'r') as file:

        file = [x.strip() for x in file.readlines()]

        # Loop through each line and split data according to variables
        for data in file[1:]:
            data = data.split(',')
            country = data[0]
            code = data[1]
            product = data[2]
            quantity = int(data[4])

            # Append quantity to list
            quantity_list.append(quantity)

        # Find the lowest number in the list
        lowest = min(quantity_list)

        # Find the index of the lowest number -adding 1
        # Due to not reading the header when reading the file lines
        locid_lowest = quantity_list.index(lowest) + 1

        count = 0

        # Search for the object instance with the same index
        for item in shoe_object_list:
            count += 1

        # Display the current data to the user
        print(shoe_object_list[locid_lowest - 1])

        # Update quantity attribute
        Shoe.set_quantity(shoe_object_list[locid_lowest - 1])

        # Update value attribute
        Shoe.update_value(shoe_object_list[locid_lowest - 1])

        print('\n Product has been re-stocked!'
              'Please check the inventory\n')

        # Update the inventory file
        update_inventory()


# Function to update the data in a file each time
# A change is made to any attribute values (mark up, re stock)
def update_inventory():
    """
    update_inventory : Iterates over object instance list and writes data to inventory file
    """
    with open('inventory.txt', 'w') as file:
        file.write('Country,Code,Product,Cost,Quantity,Value\n')

        for items in shoe_object_list:
            file.write(str(items))
            file.write('\n')


# Function to read data from text file
def read_data():
    """
    read_data : This function will read the data in the text file and send it to the class to creat objects
    """

    # Using a try except to catch any errors when reading the file
    try:
        with open('inventory.txt', 'r') as file:
            file = [x.strip() for x in file.readlines()]
            for data in file[1:]:
                data = data.split(',')
                country = data[0]
                code = data[1]
                product = data[2]
                str_cost = data[3]
                cost = float(str_cost)
                str_quantity = data[4]
                quantity = int(str_quantity)
                add_shoe(country, code, product, int(cost), quantity)

    # Prints an error if the file is not found or name is incorrect
    except OSError as e:
        print(f"{type(e)}: {e}, please check file name or file path")


def table_data(shoe_object_list):
    """
    table_data : This function will iterate through each object instance in the list
    and retrieve the attributes for all paramaters.
    Once all attributes are obtained it will add them to a list and that list will be added to the table list.
    Creating and array

    Args:
        shoe_object_list (list): list of object instances
    """

    # Initializing the header list
    table = [['Country', 'Code', 'Product', 'Cost in (R)', 'Quantity', 'Value in (R)']]

    # loop through each item in the object list
    # Returns each attribute and adds it to a list
    for shoes in shoe_object_list:
        shoe_country = Shoe.get_country(shoes)
        shoe_code = Shoe.get_code(shoes)
        shoe_product = Shoe.get_product(shoes)
        shoe_cost = Shoe.get_cost(shoes)
        shoe_quantity = Shoe.get_quantity(shoes)
        shoe_value = Shoe.get_value(shoes)

        # Add each iteration values to the table list-creating a list of lists
        table.append([shoe_country, shoe_code, shoe_product, shoe_cost, shoe_quantity, shoe_value])

    # Print table list using tabulate
    print(tabulate(table, headers="firstrow", tablefmt="pretty"))


# Main code
def main():
    # Reads data in file
    # Updates inventory.txt with values
    read_data()
    update_inventory()

    # Adding additional objects to the bottom of the list
    shoe_1 = Shoe('South Africa', 'SKU2999', 'Nike Airforce Max', 258, 25)
    shoe_2 = Shoe('Denmark', 'SKU22568', 'Yeezys Mk3', 258, 45)
    shoe_3 = Shoe('Malaysia', 'SKU88223', 'Bellenciaga yk2', 23, 75)
    shoe_4 = Shoe('Canada', 'SKU992284', 'Superga T3', 269, 5)
    shoe_5 = Shoe('Dubai', 'SKU00122', 'UnderArmour Special Edition 2', 23, 99)
    user_choice = ''

    # Loop to present user with options
    while user_choice != 4:
        print('Welcome to the inventory management,'
              'Please Choose from the options below')
        print('''
1. View current stock
2. Search for a product
3. Exit ''')

        # A try except to
        # Cater if a user incorrectly inserts alphabets
        try:
            user_choice = int(input(''))

            if user_choice == 1:
                table_data(shoe_object_list)
                print('Select an option:')
                print('''
                1.Restock items
                2.Mark Up items
                3.Return to main menu''')
                stock_choice = int(input(''))

                if stock_choice == 1:
                    re_stock_quantity()
                elif stock_choice == 2:
                    mark_up_high_quantity()
                else:
                    continue

            elif user_choice == 2:
                search_product()

            elif user_choice == 3:
                print('\nGoodbye!\n')
                exit()

        except ValueError:
            print('You have entered an incorrect character, enter only numbers')


main()
