"""x = input("x: ")
print(type(x))
y = int(x) + 1
print(f"x: {x}, y: {y}")"""
"""
int(x)
float(x)
bool(x)
str(x)
"""

"""
Values that are considered false in Python:
""
0
None
"""
"""
for number in range(3):
    print("Attempt", number + 1)
    if number > 4:
        print("Greater than 4, successful!")
        break
else:
    print("Attempted 3 times and failed!")

for x in range(5):
    for y in range(3):
        print(f"({x + 1}, {y + 1})")
        
for x in "python":
    print(x)
        
# and or not

command = ""
while command.lower() != "quit":
    command = input(">")
    print("ECHO", command)
    
"""
"""
count = 0
for number in range (1,10):
    if number % 2 == 0:
        count += 1
        print(number)
print(f"We have {count} even numbers")
"""

def getGreeting (name) :
    return f"Hello {name}"

