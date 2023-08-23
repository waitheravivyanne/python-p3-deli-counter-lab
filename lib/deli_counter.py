def take_a_number(line, name):
    line.append(name)
    position = len(line)
    print(f"Welcome, {name}. You are number {position} in line.")

def now_serving(line):
    if len(line) == 0:
        print("There is nobody waiting to be served!")
    else:
        serving_person = line.pop(0)
        print(f"Currently serving {serving_person}.")

def line(line):
    if len(line) == 0:
        print("The line is currently empty.")
    else:
        line_str = ", ".join([f"{i+1}. {person}" for i, person in enumerate(line)])
        print(f"The line is currently: {line_str}")
