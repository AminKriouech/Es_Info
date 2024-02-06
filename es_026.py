from math import sqrt

def ask_data_to_user() -> list[int]:
    a = int(input("a: "))
    b = int(input("b: "))
    c = int(input("c: "))
    return [a, b, c]


def calculate_solutions(a: int, b: int, c: int) -> list[float] | None:
    delta = b * b - 4 * a * c
    if delta < 0:
        return None
    elif delta == 0:
        solution1 = -b / (2 * a)
        solution2 = solution1
    else:
        solution1 = (-b + sqrt(delta)) / (2 * a)
        solution2 = (-b - sqrt(delta)) / (2 * a)
    return [solution1, solution2]


def print_results(solutions: list[float] | None) -> None:
    if solutions is not None:
        x1, x2 = solutions
        print(f"x1 = {x1}")
        print(f"x2 = {x2}")
    else:
        print("No real solutions.")


a, b, c = ask_data_to_user()  
solutions = calculate_solutions(a, b, c)  
print_results(solutions)