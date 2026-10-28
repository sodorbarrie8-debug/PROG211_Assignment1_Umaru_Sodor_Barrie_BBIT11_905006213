# Crop Yield Monitoring System
# PROG211 Object-Oriented Programming 1 - Assignment 1
# Domain: Agriculture
#
# This program helps a farmer keep track of the crops planted in a field
# and compare the expected harvest with the actual harvest.
# No personal data is stored (only field and crop information).


# ---------------------------------------------------------
# CLASS 1: Crop
# ---------------------------------------------------------
class Crop:
    def __init__(self, crop_id, name, area_hectares, expected_yield, actual_yield=0):
        # Attributes of a crop
        self.crop_id = crop_id                  # unique ID, e.g. "C1"
        self.name = name                        # e.g. "Rice"
        self.area_hectares = area_hectares      # land used by this crop
        self.expected_yield = expected_yield    # expected harvest in kg
        self.actual_yield = actual_yield        # real harvest in kg

    # Instance method: update the real harvest amount
    def update_harvest(self, new_amount):
        self.actual_yield = new_amount

    # Instance method: how much of the expected yield was reached (in %)
    def get_performance(self):
        if self.expected_yield == 0:
            return 0
        percent = (self.actual_yield / self.expected_yield) * 100
        return percent

    # Instance method: turn the percentage into a simple status word
    def get_status(self):
        percent = self.get_performance()
        if self.actual_yield == 0:
            return "Not harvested yet"
        elif percent >= 100:
            return "Excellent"
        elif percent >= 70:
            return "Good"
        else:
            return "Low"

    # Instance method: show all the crop information
    def display_info(self):
        print("Crop ID        :", self.crop_id)
        print("Crop Name      :", self.name)
        print("Area (hectares):", self.area_hectares)
        print("Expected Yield :", self.expected_yield, "kg")
        print("Actual Yield   :", self.actual_yield, "kg")
        print("Performance    : " + str(round(self.get_performance(), 1)) + "%")
        print("Status         :", self.get_status())
        print("-" * 35)


# ---------------------------------------------------------
# CLASS 2: FarmField
# ---------------------------------------------------------
class FarmField:
    # Class variable: shared by every FarmField object
    total_fields = 0

    def __init__(self, field_name, size):
        self.field_name = field_name
        self.size = size        # TUPLE: (length, width) in metres
        self.crops = {}         # DICTIONARY: crop_id -> Crop object
        FarmField.total_fields = FarmField.total_fields + 1

    # Instance method: add a crop to the dictionary
    def add_crop(self, crop):
        if crop.crop_id in self.crops:
            return False        # this ID is already used
        else:
            self.crops[crop.crop_id] = crop
            return True

    # Instance method: remove a crop using its ID
    def remove_crop(self, crop_id):
        if crop_id in self.crops:
            del self.crops[crop_id]
            return True
        else:
            return False

    # Instance method: field area in hectares (1 hectare = 10,000 square metres)
    def get_area_hectares(self):
        length, width = self.size       # unpacking the tuple
        return (length * width) / 10000

    # Instance method: total harvest of all crops in the field
    def get_total_yield(self):
        total = 0
        for crop in self.crops.values():
            total = total + crop.actual_yield
        return total

    # Instance method: show the field details
    def display_field_info(self):
        length, width = self.size
        print("Field Name :", self.field_name)
        print("Field Size :", length, "m x", width, "m")
        print("Area       :", round(self.get_area_hectares(), 2), "hectares")
        print("Crops      :", len(self.crops))
        print("-" * 35)

    # Class method: tells us how many fields have been created
    @classmethod
    def get_total_fields(cls):
        return cls.total_fields


# ---------------------------------------------------------
# SIMPLE FUNCTIONS (for Task 2: add and display records)
# ---------------------------------------------------------
def add_crop_record(field):
    print("\n--- Add a New Crop ---")
    crop_id = input("Enter crop ID (e.g. C1): ").strip().upper()
    if crop_id == "":
        print("Crop ID cannot be empty.")
        return
    if crop_id in field.crops:
        print("That crop ID already exists. Use a different ID.")
        return

    name = input("Enter crop name: ").strip()
    area = get_number("Enter area used (hectares): ")
    expected = get_number("Enter expected yield (kg): ")

    new_crop = Crop(crop_id, name, area, expected)
    field.add_crop(new_crop)
    print("Crop added successfully!")


def display_all_crops(field):
    print("\n--- All Crops in", field.field_name, "---")
    if len(field.crops) == 0:
        print("No crops recorded yet.")
    else:
        for crop_id in field.crops:
            field.crops[crop_id].display_info()


# Keeps asking until the user types a valid number
def get_number(message):
    while True:
        value = input(message)
        try:
            number = float(value)
            if number < 0:
                print("Please enter a positive number.")
            else:
                return number
        except ValueError:
            print("Invalid input. Please enter a number.")


def search_crop(field):
    crop_id = input("\nEnter crop ID to search: ").strip().upper()
    if crop_id in field.crops:
        print()
        field.crops[crop_id].display_info()
    else:
        print("Crop not found.")


def update_crop_harvest(field):
    crop_id = input("\nEnter crop ID to update: ").strip().upper()
    if crop_id in field.crops:
        amount = get_number("Enter actual harvest (kg): ")
        field.crops[crop_id].update_harvest(amount)
        print("Harvest updated!")
    else:
        print("Crop not found.")


def delete_crop(field):
    crop_id = input("\nEnter crop ID to delete: ").strip().upper()
    if field.remove_crop(crop_id):
        print("Crop deleted.")
    else:
        print("Crop not found.")


def show_summary(field):
    print("\n--- Field Summary ---")
    field.display_field_info()
    print("Total fields created:", FarmField.get_total_fields())
    print("Total harvest       :", field.get_total_yield(), "kg")

    # Find the best performing crop using a loop
    best_crop = None
    best_percent = -1
    for crop in field.crops.values():
        if crop.actual_yield > 0 and crop.get_performance() > best_percent:
            best_percent = crop.get_performance()
            best_crop = crop

    if best_crop is None:
        print("Best crop           : No harvest data yet")
    else:
        print("Best crop           :", best_crop.name,
              "(" + str(round(best_percent, 1)) + "%)")


# ---------------------------------------------------------
# MAIN PROGRAM
# ---------------------------------------------------------
def main():
    print("=" * 40)
    print("   CROP YIELD MONITORING SYSTEM")
    print("=" * 40)

    # Create the field first
    field_name = input("Enter the name of your field: ").strip()
    length = get_number("Enter field length (metres): ")
    width = get_number("Enter field width (metres): ")
    my_field = FarmField(field_name, (length, width))   # tuple passed in
    print("\nField created!\n")
    my_field.display_field_info()

    # Menu loop
    while True:
        print("\n========== MENU ==========")
        print("1. Add a crop")
        print("2. Display all crops")
        print("3. Search for a crop")
        print("4. Update actual harvest")
        print("5. Delete a crop")
        print("6. Show field summary")
        print("7. Exit")
        choice = input("Choose an option (1-7): ").strip()

        if choice == "1":
            add_crop_record(my_field)
        elif choice == "2":
            display_all_crops(my_field)
        elif choice == "3":
            search_crop(my_field)
        elif choice == "4":
            update_crop_harvest(my_field)
        elif choice == "5":
            delete_crop(my_field)
        elif choice == "6":
            show_summary(my_field)
        elif choice == "7":
            print("\nThank you for using the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 7.")


main()
