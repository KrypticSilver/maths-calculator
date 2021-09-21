from time import sleep

line_break = "\n" + ("=" * 51) + "\n"


class Matrix:
    def __init__(self):
        self.rows = 0
        self.columns = 0


    def get_rows(self):
        print(line_break)
        while True:
            rows = input("How many rows would you like your matrix to have?: ")
            rows_confirmation = input(f"Are you sure you want {rows} rows in your matrix? (yes/no): ")

            if rows_confirmation == "yes":
                self.rows = rows
                print(line_break)

            elif rows_confirmation == "no":
                continue

            else:
                print("Your input was not recognised, please try again.")
                break

    def get_columns(self):
        while True:
            columns = input("How many columns would you like your matrix to have?: ")
            columns_confirmation = input(f"Are you sure you want {columns} columns in your matrix? (yes/no): ")

            if columns_confirmation == "yes":
                self.columns = columns
                print(line_break)

            elif columns_confirmation == "no":
                continue

            else:
                print("Your input was not recognised, please try again.")
                break

    def get_values(self):


def compute_matrix():
    print(line_break)
    confirm_compute_matrix = input("Are you sure you want to solve a matrix problem? (yes/no): ")

    if confirm_compute_matrix == "yes":
        print("// Operation types available for matricies include:\n -Addition\n- Subtraction \n- Multiplication")
        print("\n // Also note that only two matricies can be involved in an operation together.")

        operation = input("\nGreat, what type of operation do you want to perform?: ").lower()

        if operation == "addition":
            matrix_1 = Matrix()
            matrix_1.get_rows()
            matrix_1.get_columns()

            matrix_2 = Matrix()
            matrix_2.get_rows()
            matrix_2.get_columns()

        elif operation == "subraction":
            pass

        elif operation == "multiplication":
            pass

    elif confirm_compute_matrix == "no":
        pass


while True:
    print(line_break)

    keep_solving = input("Do you want to solve an equation or quit? (solve/quit): ").lower()

    print(line_break)

    if keep_solving == "solve":
        print("// Examples of problems that can be solved include:\n- Matricies")
        computation_type = input("\nWhat type of problem do you want so solve?: ")

        if computation_type == "matricies" or computation_type == "matrix":
            compute_matrix()

        else:
            print(f"The type of computation '{computation_type}' is unavailable, please try again.")

    elif keep_solving == "quit":
        print("[Okay, no worries. Powering off in: ]")

        sleep(1)

        for i in range(3, 0, -1):
            print(f"[{i}]")
            sleep(0.5)

        print("[Powered off]")
        break

    else:
        print("Your input was not detected, please try again.")
