# bmi_calc.py


def interface():
    while True:
        print("BMI Calculator")
        print("Options:")
        print("  1 - Metric (kg/m)")
        print("  2 - Imperial (lb/in)")
        print("  9 - Quit")
        choice = input("Enter your option: ")
        if choice == '1':
            metric_analysis()
        elif choice == '2':
            imperial_analysis()
        elif choice == '9':
            return


def data_input():
        weight_input = input("Enter weight: ")
        weight_input = weight_input.split(" ")
        weight_num = float(weight_input[0])
        height_input = input("Enter height: ")
        height_input = height_input.split(" ")
        height_num = float(height_input[0])
        check_input(weight_num, height_num)


def check_input(w, h):
    # check if entered weight and height correct
    print("Your weight and height were input as {} lbs/kg and {} in/m.".format(w, h))
    print("Is this correct?")
    check_choice = input("  1 - Yes, 2 - No\n")
    if check_choice == '1':
        print("On to your BMI calculation!")
        return w, h
    elif check_choice == '2':
        print("Please re-enter weight and height")
        data_input()
    else:
        print("Please pick 1 or 2!")
        check_input(w, h)


def metric_analysis():
    data_input()
    n = 1
    bmi_calc(w, h, n)


def imperial_analysis():
    data_input()
    n = 2
    bmi_calc(w, h, n)


def bmi_calc(w, h, n):
    if n == 1:  # metric
        bmi = w/(h**2)
    elif n == 2:  # imperial
        bmi = 703*w/(h**2)
    return bmi


if __name__ == "__main__":
    interface()
