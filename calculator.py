import math

if __name__ == '__main__':
    print("==================\n Area Calculator 📐 \n==================\n")
    while True:
        choice = int(input("1.Square\n2.Rectangle\n3.Triangle\n4.Circle\n5.Quit\n\nWhat would you like to do? \n"))
        if choice == 1:
            side = int(input("Enter the side of the square: "))
            area = side * side
            print(f"The area of the square is: {area}\n")
        elif choice == 2:
            length = int(input("Enter the length of the rectangle: "))
            height = int(input("Enter the height of the rectangle: "))
            area = length * height
            print(f"The area of the rectangle is: {area}\n")
        elif choice == 3:
            base = int(input("Enter the base of the triangle: "))
            height = int(input("Enter the height of the triangle: "))
            area = (base * height) / 2
            print(f"The area of the triangle is: {area}\n")
        elif choice == 4:
            radius = int(input("Enter the radius of the circle: "))
            area = math.pi * (radius ** 2)
            print(f"The area of the circle is: {area}\n")
        elif choice == 5:
            print("Exiting the program.\n")
            break
        else:
            print("Invalid choice. Please try again.\n")
