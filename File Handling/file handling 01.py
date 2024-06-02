file = open("data.txt")

# while True:
#     content = file.readline()

#     if not content:
#         break

#     print("Line-->", content)

for i, line in enumerate(file):
    print("line-->", i, line)
