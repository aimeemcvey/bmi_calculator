# bmi_calc.py


def interface():
    print("BMI Calculator")
    k = 0
    while k == 0:
        print("Options:")
        print("  1 - Metric (kg/m)")
        print("  2 - Imperial (lb/in)")
        print("  9 - Quit")
        choice = input("Enter your option: ")
        if choice == '1':
            k = 1
            analysis(1)
        elif choice == '2':
            k = 2
            analysis(2)
        elif choice == '9':
            k = 1
            return
        else:  # other number
            k = 0
            print("That's not an option. Select a different number.")


def data_input():
    weight_input = input("Enter weight: ")
    weight_input = weight_input.split(" ")
    data_input.weight = float(weight_input[0])
    height_input = input("Enter height: ")
    height_input = height_input.split(" ")
    data_input.height = float(height_input[0])
    check_input(data_input.weight, data_input.height)


def check_input(w, h):
    # check if entered weight and height correct
    print("Your weight and height were input as {} lbs/kg and {} in/m.".format(w, h))
    print("Is this correct?")
    check_choice = input("  1 - Yes, 2 - No\n")
    if check_choice == '1':
        print("On to your BMI calculation!")
    elif check_choice == '2':
        print("Please re-enter weight and height")
        data_input()
    else:
        print("Please pick 1 or 2!")
        check_input(w, h)


def analysis(n):
    data_input()
    analysis.bmi = bmi_calc(data_input.weight, data_input.height, n)
    bmi_output(analysis.bmi)


def bmi_calc(w, h, n):
    if n == 1:  # metric
        bmi = w/(h**2)
    elif n == 2:  # imperial
        bmi = 703*w/(h**2)
    print("Your BMI is {:0.2f}." .format(bmi))
    return bmi


def bmi_output(bmi):
    if bmi < 18.50:
        result = "underweight"
    elif 18.50 <= bmi < 24.99:
        result = "normal"
    elif 25 <= bmi < 29.99:
        result = "overweight"
    else:  # bmi >30
        result = "obese"
    print("Your BMI indicates that you are {}." .format(result))


if __name__ == "__main__":
    interface()
