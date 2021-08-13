def get_number_of_quadratic_solutions(a, b, c):
    number_of_solutions = ""
    quadratic_discriminant = (b ** 2) - (4 * a * c)

    if quadratic_discriminant > 0:
        number_of_solutions = "two solutions"
    elif quadratic_discriminant == 0:
        number_of_solutions = "one solution"
    else:
        number_of_solutions = "no real solutions"

    return number_of_solutions


if __name__ == '__main__':
    print("*********  Quadratic Equation Formula ==>> (a)x^2 + (b)x + (c) = 0  *********")

    a = int(input("Please enter 'a' value:"))
    if a == 0:
        print("Invalid input values! Please try again.")
    else:
        b = int(input("Please enter 'b' value:"))
        c = int(input("Please enter 'c' value:"))
        answer = get_number_of_quadratic_solutions(a, b, c)
        print("({})x^2 + ({})x + ({}) = 0 has {}.".format(a, b, c, answer))