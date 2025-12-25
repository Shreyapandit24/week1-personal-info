# Personal Information Manager
# Stores and displays your name, age, city, and hobbies

class PersonalInfoManager:
    def __init__(self):
        self.name = ""
        self.age = 0
        self.city = ""
        self.hobbies = []

    def set_info(self, name, age, city, hobbies):
        self.name = name
        self.age = age
        self.city = city
        self.hobbies = hobbies

    def display_info(self):
        print("=" * 60)
        print(" PERSONAL INFORMATION ".center(60, "="))
        print("=" * 60)
        print(f"Name : {self.name}")
        print(f"Age  : {self.age}")
        print(f"City : {self.city}")
        print("-" * 60)
        print("Hobbies:")
        if self.hobbies:
            for i, hobby in enumerate(self.hobbies, start=1):
                print(f"  {i}. {hobby}")
        else:
            print("  (No hobbies listed)")
        print("=" * 60)


# -------- Main Program --------
if __name__ == "__main__":
    # Get user input
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    city = input("Enter your city: ")
    hobbies_input = input("Enter your hobbies (comma-separated): ")

    # Convert string to list
    hobbies = [h.strip() for h in hobbies_input.split(",") if h.strip()]

    # Create Personal Information Manager object
    person = PersonalInfoManager()
    person.set_info(name, age, city, hobbies)

    # Display formatted info
    print("\nYour Stored Information:")
    person.display_info()
