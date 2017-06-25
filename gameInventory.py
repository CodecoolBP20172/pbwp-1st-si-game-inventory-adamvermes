# This is the file where you must work. Write code in the functions, create new functions, 
# so they work according to the specification

# Displays the inventory.
def display_inventory(inventory):
    print('Inventory:')
    for k, v in inventory.items(): #items() displays a list of the inventory's (key, value) tuple pair
        print(v, k) #print the values and keys
    print('Total number of items', sum(inventory.values())) #print the sum of items in the inventory
    pass

# Adds to the inventory dictionary a list of items from added_items.
def add_to_inventory(inventory, added_items):
    from collections import Counter #import Counter: a dict subclass to count hashable objects(keys)
    updated_dict = {} #create an empty dictionary
    for items in range(len(added_items)): #for loop items in the range in length of add_items (0->add item length)
        updated_dict[added_items[items]] = added_items.count(added_items[items]) #updated_dict keys&values added from add_items
    update_inv = Counter(inventory) + Counter(updated_dict) #add inventory and updated_dict
    inventory.update(update_inv) #update inventory keys&values with update_inv keys&values
    pass


# Takes your inventory and displays it in a well-organized table with 
# each column right-justified. The input argument is an order parameter (string)
# which works as the following:
# - None (by default) means the table is unordered
# - "count,desc" means the table is ordered by count (of items in the inventory) 
#   in descending order
# - "count,asc" means the table is ordered by count in ascending order
def print_table(inventory, order=None):
    print('Inventory:')
    from tabulate import tabulate #import tabulate to create table from dictionary
    headers = ['count', 'item name'] #create table headers
    if order == 'count,asc': #if user input is this
        inv_data = sorted([(v, k) for k, v in inventory.items()], reverse=False) #flip key&value and sort asc or desc with True/False
        print(tabulate(inv_data, headers = headers, stralign="right")) #print out inventory in a table with headers, aligned right
    elif order == 'count,desc': #if user input is this
        inv_data = sorted([(v, k) for k, v in inventory.items()], reverse=True) #flip key&value and sort asc or desc with True/False
        print(tabulate(inv_data, headers = headers, stralign="right")) #print out inventory in a table with headers, aligned right
    elif order == None: #if user input is None
        inv_data = [(v, k) for k, v in inventory.items()] #flip key&value without sorting
        print(tabulate(inv_data, headers = headers, stralign="right")) #print out inventory in a table with headers, aligned right
    else: #otherwise do this
        print("order value must either be: None, count,desc, or count,asc") #if order input is different to the ones above, print message
    inv_data_normal = sorted(inventory.items()) #create a temporary dictionary without flipped keys&values
    inventory.update(inv_data_normal) #update inventory with inv_data_normal items
    print('----------------------------')
    print('Total number of items', sum(inventory.values())) #sum and print inventory values
    pass


# Imports new inventory items from a file
# The filename comes as an argument, but by default it's 
# "import_inventory.csv". The import automatically merges items by name.
# The file format is plain text with comma separated values (CSV).
def import_inventory(inventory, filename="import_inventory.csv"):
    import csv #read csv data from file and use it with import csv module
    with open(filename, 'r') as imported_inv: #open filename in read mode
        imported_inv_reader = csv.reader(imported_inv) #return a reader object which iterates over lines, and then assign it to a variable
        updated_inv = [] #create an empty list
        for item in imported_inv_reader:
            updated_inv += item #add each item of the imported list to the empty list
    add_to_inventory(inventory, updated_inv) #sum the inventory and the updated list from the imported file
    pass


# Exports the inventory into a .csv file.
# if the filename argument is None it creates and overwrites a file
# called "export_inventory.csv". The file format is the same plain text 
# with comma separated values (CSV).
def export_inventory(inventory, filename="export_inventory.csv"):
    import csv #read csv data from file and use it with import csv module
    with open(filename, 'w') as exported_inv: #open filename in write mode
        csvwriter = csv.writer(exported_inv) #return a writer object responsible for converting the imported data into strings on the file-like object.
        updated_export_inv =[] #create empty list
        final_list = [] #create another empty list
        for k, v in inventory.items(): #for every iteration of the keys and values in the inventory
            updated_export_inv += [k] * v #add the keys multiplied by the values into the first empyt list
        final_list = updated_export_inv #insert the last line of the above list into the second empty list
        csvwriter.writerow(final_list) #write the final list paramenters to the writer's file object
    pass