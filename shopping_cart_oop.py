class Cart():
    def __init__(self, cart):
        self.cart = cart
    def remove_item(self, removing):
        self.cart = removing
        return self.cart
    def add_item(self, adding):
        self.cart = adding
        return self.cart
    def show_cart(self, cart):
        self.cart = cart
        print(self.cart)
    def exit_app(exit):
        print("Thank you for stopping by.")
        quit()
    def shopping_cart(cart_list):
        # Make an empty cart list
        cart_list = []
        # Set valid commands to be accepted
        valid_cart_commands = ['add','remove','see','exit']
        # Set a flag to break out of while loop
        done = False
        while not done:
            # Check for user input against acceptable commands
            user_input = input("Would you like to add items, remove items, see contents, empty cart or exit shopping cart? ").lower()
            if user_input in valid_cart_commands:
                if user_input == 'add':
                    items = input("What would you like to add to the cart? ")
                    adding = cart_list.append(items)
                    cart.add_item(adding)
                    continue
                elif user_input == 'remove':
                    remove_item = input("What would you like to remove from the cart? ")
                    if remove_item in cart_list:
                        removing = cart_list.pop(cart_list.index(remove_item))
                        cart.remove_item(removing)
                        print(f'{remove_item} has been removed from the cart ')
                    else:
                        print(f'{remove_item} is not in the cart.')
                elif user_input == 'see':
                    if len(cart_list) == 0:
                        print("There's nothing in the cart.")
                    else:
                        print(f'Here are the contents of your shopping cart: {cart.show_cart(cart_list)}')
                        continue
                elif user_input == 'exit': 
                    cart.exit_app()
            # Print message if user enters invalid input
            else:
                print("Please enter a valid option!")
                continue
        # Check if there is anything in the cart and display message accordingly
        if len(cart_list) == 0:
            print("We hope you find what you were looking for next time.")
        else:
            print(f'Here are the contents of your shopping cart: {cart_list}')

cart = Cart(list)
cart.shopping_cart()