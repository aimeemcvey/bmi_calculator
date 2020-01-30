# bmi_calc.py


def interface():
    while True:
        print("BMI Calculator")
        print("Options:")
        print("  1 - Metric")
        print("  2 - Imperial")
        print("  9 - Quit")
        choice = input("Enter your option: ")
        if choice == '9':
            return


if __name__ == "__main__":
    interface()
