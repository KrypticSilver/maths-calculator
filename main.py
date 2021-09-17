class Matricies:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns


    def get_values(self):
        for i in range(self.rows):
            for j in range(self.columns):
                try:
                    value = int(input(f"What would you like the value of the matrix at [{self.rows},{self.columns}] "
                                      f"to be?: "))
                except:
                    None

                if type(value) is not int:
                    print("Invalid input detected. Input must be an integer.")
                    continue





def solve_matricies():
    while True:
        try:
            rows = int(input("How many rows are in your matrix?: "))
        except:
            None

        if type(rows) is not int:
            print("Invalid input detected. Input must be an integer.")
            continue

        try:
            columns = int(input("How many columns are in your matrix?: "))
        except:
            None

        if type(columns) is not int:
            print("Invalid input detected. Input must be an integer.")
            continue

        matrix = Matricies(rows, columns)



while True:
    keep_solving = input("Do you want to solve an equation or quit? (S/C): ").upper()

    if keep_solving == "S":
        computation_type = input("What type of problem do you want so solve(e.g. matricies)?:\n")

        if computation_type == "matricies":
            solve_matricies()

    elif keep_solving == "Q":
        break

    else:
        print("Your input was not detected, please try again.")
