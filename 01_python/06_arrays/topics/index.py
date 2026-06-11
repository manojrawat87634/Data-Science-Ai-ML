arr = [
    {
        "que0" : "Who is the capital of india?",
        "options" : ["Delhi", "mumbai", "patna"],
        "ans" : 0
    },
]

for i in arr:
    print(i.get("que0"))
    print(i.get('options'))
    ch = input("Enter ch")
    if (ch == i.get("options")[i.get("ans")]):
        print("Correct Ans")
    else:
        print("Incorrect")