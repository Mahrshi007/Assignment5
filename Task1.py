students={
    'Alice':80,
    'Bob':70,
    'Oggy':65,
    'Jack':55
}
name=input("Enter student name: ")
if name in students:
    print(f"{name}'s marks: {students[name]}")
else:
    print("Student not found")