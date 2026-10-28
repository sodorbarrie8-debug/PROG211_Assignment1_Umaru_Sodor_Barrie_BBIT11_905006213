# Crop Yield Monitoring System

**Module:** PROG211 Object-Oriented Programming 1
**Assignment:** Real-World Solutions under DPG Standards
**Domain:** Agriculture
**Student ID:** 905006074

## 1. Introduction

Many small farmers in Sierra Leone do not keep written records of their harvests. Because of this, it is hard to know if a crop did well or badly in a season. This project is a simple Python program that helps a farmer record the crops in a field, enter the expected and actual harvest, and see how well each crop performed.

## 2. How to Run

1. Install Python 3 on your computer.
2. Download the file `crop_yield_system.py`.
3. Open a terminal in the same folder and type: `python crop_yield_system.py`
4. Follow the menu on the screen.

No extra libraries are needed.

## 3. Features (Menu Options)

1. Add a crop
2. Display all crops
3. Search for a crop by ID
4. Update the actual harvest
5. Delete a crop
6. Show field summary (total harvest and best crop)
7. Exit

## 4. How the Program Meets the Task Requirements

**Task 1 - Classes and Objects.** The program has two classes:
- `Crop` has attributes `crop_id`, `name`, `area_hectares`, `expected_yield` and `actual_yield`, and methods such as `update_harvest()` and `display_info()`.
- `FarmField` has attributes `field_name`, `size` and `crops`, and methods such as `add_crop()` and `display_field_info()`.

A `FarmField` object holds many `Crop` objects, which shows interaction between objects.

**Task 2 - Data Structure.** A **dictionary** is used inside `FarmField`. Each `Crop` object is stored with its unique `crop_id` as the key. The functions `add_crop_record()` and `display_all_crops()` add and display the records.

**Bonus - Tuple.** The size of the field is stored as a **tuple** `(length, width)`. It is unpacked in `get_area_hectares()` to calculate the area in hectares.

**Task 3 - Methods.**
- *Instance methods:* `update_harvest()`, `get_performance()`, `get_status()`, `add_crop()`, and others.
- *Class method:* `get_total_fields()` uses `@classmethod` and the class variable `total_fields` to show how many fields were created.

## 5. Digital Public Goods (DPG) Alignment

**Open-source.** The full source code is uploaded to GitHub so anyone can read it, copy it, and improve it. Other students, teachers, or farming groups can use it for free.

**Inclusive and accessible design.** The program uses a simple numbered menu and plain English messages. It runs in any computer with Python, and it needs no internet, no payment and no special hardware. The program also checks the user input, so if someone types a wrong value (like letters instead of a number), it shows a clear message and asks again instead of crashing.

**Privacy-respecting.** The program does **not** store any sensitive personal data. It does not ask for the farmer's name, phone number, address or ID number. It only stores the field name, the field size and crop information such as crop name, area and harvest amounts. Nothing is sent over the internet.

**Modular and reusable.** The code is divided into two classes and small functions, and each one does one job. The `Crop` and `FarmField` classes can be reused in other programs, for example a livestock tracker or a school farm project. New features can be added without rewriting the whole program.

## 6. Example Usage

```
Enter the name of your field: North Field
Enter field length (metres): 100
Enter field width (metres): 50

Choose an option (1-7): 1
Enter crop ID (e.g. C1): C1
Enter crop name: Rice
Enter area used (hectares): 0.3
Enter expected yield (kg): 600
Crop added successfully!

Choose an option (1-7): 4
Enter crop ID to update: C1
Enter actual harvest (kg): 540
Harvest updated!

Choose an option (1-7): 3
Enter crop ID to search: C1
Crop ID        : C1
Crop Name      : Rice
Area (hectares): 0.3
Expected Yield : 600.0 kg
Actual Yield   : 540.0 kg
Performance    : 90.0%
Status         : Good
```

## 7. Limitations and Future Improvements

- The data is lost when the program closes, because it is not saved to a file. In the future, I can save the records to a text file.
- It works with only one field at a time. Later, it can manage many fields.
- It could be improved with a mobile or web interface.

## 8. Conclusion

This project shows how Object-Oriented Programming can be used to solve a real problem in agriculture. It uses classes, objects, a dictionary, a tuple, an instance method and a class method, while following the Digital Public Goods standards.
