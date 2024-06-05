# file = open("data.txt", "w")

# while True:
#     content = file.readline()

#     if not content:
#         break

#     print("Line-->", content)

# for i, line in enumerate(file):
#     i+=1
#     print("line-->", i, line)

# for i in range(0, 100):
#     i += 1
#     file.write(str(i)+"\n")
# file.close()
i = 0
while True:
    i += 1
    with open("data.txt", "a") as file:

        name = input("Enter Your name here: ")
        age = int(input("Enter your age here: "))

        age = str(age)

        file.write(str(i)+"\n"+"Name is: "+name+"\n"+"Age is: "+age+"\n")

    x = input("Retry or Exit (r/e): ")
    x = x[0].lower()
    if x != "r":
        break

print("Thank You!")
