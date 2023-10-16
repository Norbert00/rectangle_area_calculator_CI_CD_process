def calculate_rectangle_area(length, width):
    if float(length) <= 0 or float(width) <= 0:
        raise ValueError("Length and width should be positive numbers.")
    return length * width

def main():
    try:
        length = float(input("Enter the length of the rectangle: "))
        width = float(input("Enter the width of the rectangle: "))
        area = calculate_rectangle_area(length, width)
        print(f"The area of the rectangle is: {area}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()