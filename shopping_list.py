# shopping_list.py
"""shopping_list.py
User enters items for shopping list
type 'SHOW' to show current items in list
type 'HELP' for help information
type 'DONE' when list is complete and
the shopping list prints to the screen."""

shopping_list = []

def show_help():
    print("What should we pick up at the store?")
    print("Enter DONE to stop. Enter HELP to stop. Enter SHOW to see current list.")


def add_to_list(item):
    shopping_list.append(item)
    print("Added: List has {} items.".format(len(shopping_list)))

def show_list():
    print("Here's your shopping list.")
    for item in shopping_list:
        print(item)

show_help()

while True:
    new_item = input("> ").upper()
    if new_item == 'DONE':
        break
    elif new_item == 'HELP':
        show_help()
        continue
    elif new_item == 'SHOW':
        show_list()
        continue
    
    add_to_list(new_item)
    continue

show_list()

