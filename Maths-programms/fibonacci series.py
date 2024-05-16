while True:
    input_number = int(
        input("\nEnter your number to calculate \nfibonacci number series: "))

    previous_number = 0
    current_number = 1

    if input_number < 0:
        print("\nThis sereis can't be get fibonacci series!")

    else:
        print("\nThe sereis is ")
        for i in range(1, input_number):
            next_number = previous_number + current_number
            print(i,".",previous_number, "+", current_number, "=", next_number)
            previous_number = current_number
            current_number = next_number

    choice = input("\nCalculate another fibonacci sereis (yes/no): ")
    x = choice[0].lower()
    if x != "y":
        break
print("\nThank you!!")
