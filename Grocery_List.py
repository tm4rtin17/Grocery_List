#Import modules
import pyinputplus as pyip

#Define list
grocery_list = []

#Define user input function to enter grocieres
def input_grocery():
    grocery = pyip.inputStr("What would you like to add to your grocery list?")
    grocery_list.append(grocery)

#Function prints groceries in a list format
def read_grocery():
    for grocery in grocery_list:
        print(f"- {grocery}")

#Function allows the user to delete an item from the list
def remove_grocery():
    delete_grocery = pyip.inputStr("What grocery would you like to delete from your list?")
    grocery_list.remove(delete_grocery)

#Initial function call
input_grocery()

#Infinite loop to allow users multiple re-attemps; Enter number 1-4 to choose what to do
while True:
    decision = pyip.inputNum("Enter '1' to add more groceries; Enter '2' to view your list; Enter '3' to delete an item from the list; Enter '4' to exit the program")

    if decision == 1:
        input_grocery()
    elif decision == 2:
        read_grocery()
    elif decision == 3:
        remove_grocery()
    elif decision == 4:
        print("Goodbye!")
        break
