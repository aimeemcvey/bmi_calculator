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


def metric_analysis():
    data_input()


def imperial_analysis():
    data_input()


if __name__ == "__main__":
    interface()
