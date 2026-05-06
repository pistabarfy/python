gg = []
roll = []

while (student := input("Enter the name of the student: ")) != "q" and student != "quit":
    roll_rank = int(input("Enter the roll number:"))
    duplicate_status = False
    for r in roll:
        if roll_rank== r:
            print("Dont enter duplicate numbers")
            duplicate_status = True
    
    if duplicate_status == False:
        gg.append(student)
        roll.append(roll_rank)
        for position,value in enumerate(gg):
            print(f"position is {position} and the name is {value}")

        for name,call in zip(gg,roll):
            print(f"the name is {name} and its roll number is {call}")
print("Sahil")
print("Bye!")