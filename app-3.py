def operation_for_color(color):
    match color.lower():
        case "red":
            print("This is red color!")
        case "green":
            print("This is green color!")
        case "blue":
            print("This is blue color!")
        case _:
            print("Cannot match any color!")


def operation_for_option(option):
    match option:
        case 1:
            print("Option 1!")
        case 2:
            print("Option 2!")
        case 3:
            print("Option 3!")
        case _:
            print("Wrong option number!")


if __name__ == '__main__':
    operation_for_color('RED')
    operation_for_color('GREEN')
    operation_for_color('BLUE')
    operation_for_color('ORANGE')

    operation_for_option(1)
    operation_for_option(2)
    operation_for_option(3)
    operation_for_option(4)