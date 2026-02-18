# print("Hello World!")

def testGreeting():
    Greeting = "Hello World!" 
    print(Greeting)
    print(len(Greeting))

    print(Greeting[0])
    print(Greeting[-1])
    print(Greeting[0:5])

    stringWithQuotationMark = "He said, \"Hello World\""

    print(stringWithQuotationMark)

def stringDealing():
    firstName = "Hoosun"
    lastName = "Chan"
    fullNameF = f"{firstName} {lastName}"
    fullName = firstName + " " + lastName
    print(fullNameF)
    print(fullNameF.upper())
    print(fullNameF.lower())
    print(fullName)
    print(fullName.strip())
    #print(fullName.lstrip())
    #print(fullName.rstrip())
    print(fullName.find("Hoo"))
    print(fullName.replace("o", "a"))
    print("Hoo" in fullName)
