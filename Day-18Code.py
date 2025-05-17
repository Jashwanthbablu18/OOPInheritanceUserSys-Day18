# Day 18 - OOP Inheritance: User System

# This is an user class / base class which represents a general user with name and email as a params.
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    # This method displays the user name along with user's email.
    def show_info(self):
        print(f"👤 Name: {self.name}, 📧 Email: {self.email}")

# This is the inherited class / Child class of user (which has access to user's properties and methods) and it also have an additional
# attribute privileges which is a list of powers that an admin can hold.
class Admin(User):
    def __init__(self, name, email, privileges):

        # The super() is used to access / call properties and methods from a parent class within child class
        super().__init__(name, email)

        # This is the list of powers that the admin holds
        self.privileges = privileges

    # This method displays the privileges that admin have
    def show_privileges(self):
        print(f"🛡️ Admin Privileges for {self.name}:")
        for p in self.privileges:
            print(f"   - {p}")

# This is the inherited class / Child class of user (which has access to user's properties and methods) and additionally it has a balance 
# attribute which represents the balance in the customer account
class Customer(User):
    def __init__(self, name, email, balance):

        # The super() is used to access / call properties and methods from a parent class within child class
        super().__init__(name, email)

        # Customers account balance
        self.balance = balance

        # Storing items added to the cart
        self.cart = []

    # This method adds item to the customers cart and displays msg
    def add_to_cart(self, item):
        self.cart.append(item)
        print(f"🛒 {self.name} added {item} to cart.")

    # This method displays the items in the cart
    def show_cart(self):
        print(f"🧺 {self.name}'s Cart: {self.cart}")

    # This method is used to checkout by customer's name and how many items did customer brought and customers balance.
    def checkout(self):
        print(f"💳 {self.name} checked out with {len(self.cart)} items. Balance: ₹{self.balance}")


# This is an additional class which represents the loyalty of the customer towards the company by giving rating and an encourage repeat 
# purchases, This involves offering rewards, discounts... who make repeated purchases. 
class LoyaltyProgram:

    # It gets loyalty status based upon the points 
    def get_loyalty_status(self, points):
        if points > 1000:
            return "Platinum"
        elif points > 500:
            return "Gold"
        else:
            return "Silver"


# This is an additional class which inherits the properties and methods from Customer and LoyaltyProgram classes (representing multiple inheritance).
# This adds a points attribute to track loyalty points 
class PremiumCustomer(Customer, LoyaltyProgram):
    def __init__(self, name, email, balance, points):
        super().__init__(name, email, balance)
        self.points = points

    # This method uses the get_loyalty_status() from LoyaltyProgram class to determine loyalty status of customer. 
    def show_status(self):
        status = self.get_loyalty_status(self.points)
        print(f"🌟 {self.name} is a {status} member with {self.points} points.")

# main
def main():
    print("👨‍👩‍👧‍👦 Day 18 - User System with Inheritance\n")

    # Admin demo: Here we created an object / instance of Admin class and Passed admin's name and email with the privileges that 
    # admin can hold. And calls show_info() and show_privileges() methods with object name to show the information abour admin and privileges of admin.
    admin = Admin("MaheshBabu", "maheshAdmin@Croma.com", ["add_user", "delete_user", "ban_user"])
    admin.show_info()
    admin.show_privileges()

    print("\n---\n")

    # Customer demo: Here we created an object for Customer class with name, email and balance and used all of the methods that are in
    # customer class i.e show_info(), add_to_cart(), show_cart() and checkout().
    cust = Customer("Tarak", "tarak9999@gmail.com", 3000)
    cust.show_info()
    cust.add_to_cart("Laptop")
    cust.add_to_cart("Mouse")
    cust.show_cart()
    cust.checkout()

    print("\n---\n")

    # PremiumCustomer with multiple inheritance. And creates a object for PremiumCustomer class and calls the show_info() from User class, 
    # show-cart() from Customer class and show_status() from PremiumCustomer class.
    prem = PremiumCustomer("Prabhas", "PrabhasRaju@gmail.com", 5000, 850)
    prem.show_info()
    prem.show_cart()
    prem.show_status()


# calling main() to starting execution of program
if __name__ == "__main__":
    main()
