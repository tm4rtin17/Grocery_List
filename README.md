# Grocery List

This Python program allows users to create and manage a grocery list interactively. Users can add items, view the list, delete items, and exit the program through a simple menu-driven interface.

---

## Features

1. **Add Items to Grocery List**
   - Users can input any item to add it to the grocery list.

2. **View Grocery List**
   - Displays all the items currently in the grocery list in a formatted list.

3. **Delete Items from Grocery List**
   - Users can remove specific items from the list by entering their names.

4. **Exit Program**
   - Users can exit the program gracefully with a farewell message.

---

## Requirements

- Python 3.13.1 or higher
- `pyinputplus` module for input validation

You can install the required module using pip:
```bash
pip install pyinputplus
```

---

## How to Use

1. Run the program in your Python environment.

2. Follow the on-screen prompts to interact with the menu:
   - Enter `1` to add an item to your grocery list.
   - Enter `2` to view your current grocery list.
   - Enter `3` to remove an item from the grocery list.
   - Enter `4` to exit the program.

3. The program will continue running in a loop until you choose to exit.

---

## Example Usage

```plaintext
What would you like to add to your grocery list? Milk
Enter '1' to add more groceries; Enter '2' to view your list; Enter '3' to delete an item from the list; Enter '4' to exit the program: 2
- Milk
Enter '1' to add more groceries; Enter '2' to view your list; Enter '3' to delete an item from the list; Enter '4' to exit the program: 1
What would you like to add to your grocery list? Bread
Enter '1' to add more groceries; Enter '2' to view your list; Enter '3' to delete an item from the list; Enter '4' to exit the program: 2
- Milk
- Bread
Enter '1' to add more groceries; Enter '2' to view your list; Enter '3' to delete an item from the list; Enter '4' to exit the program: 3
What grocery would you like to delete from your list? Milk
Enter '1' to add more groceries; Enter '2' to view your list; Enter '3' to delete an item from the list; Enter '4' to exit the program: 4
Goodbye!
```

---

## Potential Enhancements

1. **Error Handling:**
   - Handle cases where users try to delete an item not in the list.
   - Notify users when viewing or deleting items from an empty list.

2. **Save and Load Functionality:**
   - Allow saving the grocery list to a file and loading it upon restarting the program.

3. **Improved Input Options:**
   - Enable users to add or delete multiple items in a single input.

---

## License

This program is open-source and available for personal or educational use.

