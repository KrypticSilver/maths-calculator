line_break = "/" * 51


class Matricies:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns


def compute_matrix():
    print("\n// Operation types available for matricies include:\n -Addition\n- Subtraction \n- Multiplication")
    print("\n // Also note that only two matricies can be involved in an operation together.")

    operation = input("\nGreat, what type of operation do you want to perform?: ").lower()

    if operation == "addition":
        pass

    elif operation == "subraction":
        pass

    elif operation == "multiplication":
        pass


while True:
    keep_solving = input("Do you want to solve an equation or quit? (S/C): ").lower()

    if keep_solving == "s":
        print("\n// Examples of problems that can be solved include:\n- Matricies")
        computation_type = input("\nWhat type of problem do you want so solve?: ")

        if computation_type == "matricies" or computation_type == "matrix":
            compute_matrix()

        else:
            print(f"The type of computation '{computation_type}' is unavailable, please try again.")

    elif keep_solving == "q":
        break

    else:
        print("Your input was not detected, please try again.")
