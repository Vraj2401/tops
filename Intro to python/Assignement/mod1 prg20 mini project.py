class User:
    def __init__(self, user_id, name, password):
        self.details = (user_id, name, password)

    def display(self):
        print("\n User Created Successfully!")
        print("User ID:", self.details[0])
        print("Name:", self.details[1])
        print("Password:", self.details[2])


# Main Program
try:
    user_id = input("Enter User ID: ")
    name = input("Enter your name: ")

    while True:
        password = input("Create your password (must be more than 8 characters): ")
        if len(password) > 8:
            break
        else:
            print(" Password too short. Please try again.\n")

    new_user = User(user_id, name, password)
    new_user.display()

except Exception as e:
    print("Unexpected error:", e)