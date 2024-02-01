import shapes_area, object_area , math

def main():
    print("\n\n\n********AREA CALCULATOR********\n")
    print("What do you whant to find out? \n")
    print("1.Calculate the area of a shape ")
    print("2.Calculate the area of a object ")
    print("3.Calculate the area of combine shape")
    print("4.Calculate the area of combine surface area of object")

    choice = input("\n\nEnter your choice (1 , 2 , 3 or 4): ")

    if choice =='1':
        shape_choice = input("\nSelect a shape: \n 1.Circle \n 2.Rectangle \n 3.Triangle \n 4.Square \n 5.Pentagon \n 6.Hexagon \n 7.Octagon \n 8.Rhombus \n 9.Trapezoid \n 10.Parallelogram\n\n")

        if shape_choice =='1':
            radius = float(input("\nEnter the radius: \n"))
            area =shapes_area.circle(radius)
            print(f"\nThe area of the circle is:{area}\n\n")
        
        elif shape_choice == '2':
            length = float(input("Enter the length:  "))
            width = float(input("Enter the width:  \n"))
            area = shapes_area.rectangle(length, width)
            print(f"\nThe area of the rectangle is: {area}\n\n")
            
        elif shape_choice == '3':
            base = float(input("Enter the base: "))
            height = float(input("Enter the height:  \n"))
            area = shapes_area.triangle(base, height)
            print(f"\nThe area of the triangle is: {area}\n\n")
            
        elif shape_choice == '4':
            side = float(input("Enter the side length: \n"))
            area = shapes_area.square(side)
            print(f"\nThe area of the square is: {area}\n\n")

        elif shape_choice == '5':
            side = float(input("Enter the side length: \n"))
            area = shapes_area.pentagon(side)
            print(f"\nThe area of the pentagon is: {area}\n\n")

        elif shape_choice == '6':
            side = float(input("Enter the side length: \n"))
            area = shapes_area.hexagon(side)
            print(f"\nThe area of the hexagon is: {area}\n\n")

        elif shape_choice == '7':
            side = float(input("Enter the side length: \n"))
            area = shapes_area.octagon(side)
            print(f"\nThe area of the octagon is: {area}\n\n")

        elif shape_choice == '8':
            diagonal1 = float(input("Enter the length of diagonal 1: \n"))
            diagonal2 = float(input("Enter the length of diagonal 2: \n"))
            area = shapes_area.rhombus(diagonal1, diagonal2)
            print(f"\nThe area of the rhombus is: {area}\n\n")

        elif shape_choice == '9':
            base1 = float(input("Enter the length of base 1: \n"))
            base2 = float(input("Enter the length of base 2: \n"))
            height = float(input("Enter the height: \n"))
            area = shapes_area.trapezoid(base1, base2, height)
            print(f"\nThe area of the trapezoid is: {area}\n\n")

        elif shape_choice == '10':
            base = float(input("Enter the base: \n"))
            height = float(input("Enter the height: \n"))
            area = shapes_area.parallelogram(base, height)
            print(f"\nThe area of the parallelogram is: {area}\n\n")

        else:
            print("***Invalid shape choice! Try again***")
        
    elif choice == '2':
        object_choice = input("\nSelect a object: \n 1.Cube \n 2.Sphere \n 3.Cylinder \n 4.Cuboid \n 5.Prism \n 6.Cone\n 7.Pyramid\n\n")

        if object_choice == '1':
            side = float(input("Enter the side length: \n"))
            surface_area = object_area.cube(side)
            print(f"\nThe surface area of the cube is: {surface_area}\n\n")
            
        elif object_choice == '2':
            radius = float(input("Enter the radius: \n"))
            surface_area = object_area.sphere(radius)
            print(f"\nThe surface area of the sphere is: {surface_area}\n\n")
            
        elif object_choice == '3':
            radius = float(input("Enter the radius: \n"))
            height = float(input("Enter the height: \n"))
            surface_area = object_area.cylinder(radius, height)
            print(f"\nThe surface area of the cylinder is: {surface_area} \n\n")
        
        elif object_choice == '4':
            length = float(input("Enter the length: \n"))
            width = float(input("Enter the width: \n"))
            height = float(input("Enter the height: \n"))
            surface_area = object_area.cuboid(length, width, height)
            print(f"\nThe surface area of the cuboid is: {surface_area}\n\n")

        elif object_choice == '5':
            base_shape = input("Enter the base shape (triangle, square, pentagon, hexagon): \n")
            base_length = float(input("Enter the base length: \n"))
            height = float(input("Enter the height: \n"))
            surface_area = object_area.prism(base_shape, base_length, height)
            print(f"\nThe surface area of the prism is: {surface_area}\n\n")

        elif object_choice == '6':
            radius = float(input("Enter the radius: \n"))
            height = float(input("Enter the height: \n"))
            surface_area = object_area.cone(radius, height)
            print(f"\nThe surface area of the cone is: {surface_area}\n\n")

        elif object_choice == '7':
            base_shape = input("Enter the base shape (triangle, square, pentagon, hexagon): \n")
            base_length = float(input("Enter the base length: \n"))
            slant_height = float(input("Enter the slant height: \n"))
            surface_area = object_area.pyramid(base_shape, base_length, slant_height)
            print(f"\nThe surface area of the pyramid is: {surface_area}\n\n")

        else:
            print("INVALID CHOICE")

    elif choice == '3':
        num_shapes = int(input("Enter the number of shapes: "))
        total_area = 0
        for i in range(num_shapes):
            shape_choice = input(f"Select shape {i+1} (circle, rectangle, triangle, square, pentagon, hexagon, octagon, rhombus, trapezoid, parallelogram): ")
            if shape_choice == 'circle':
                radius = float(input("Enter the radius: "))
                area = shapes_area.circle(radius)
                total_area += area
            elif shape_choice == 'rectangle':
                length = float(input("Enter the length: "))
                width = float(input("Enter the width: "))
                area = shapes_area.rectangle(length, width)
                total_area += area
            elif shape_choice == 'triangle':
                base = float(input("Enter the base: "))
                height = float(input("Enter the height: "))
                area = shapes_area.triangle(base, height)
                total_area += area
            elif shape_choice == 'square':
                side = float(input("Enter the side length: "))
                area = shapes_area.square(side)
                total_area += area
            elif shape_choice == 'pentagon':
                side = float(input("Enter the side length: "))
                area = shapes_area.pentagon(side)
                total_area += area
            elif shape_choice == 'hexagon':
                side = float(input("Enter the side length: "))
                area = shapes_area.hexagon(side)
                total_area += area
            elif shape_choice == 'octagon':
                side = float(input("Enter the side length: "))
                area = shapes_area.octagon(side)
                total_area += area
            elif shape_choice == 'rhombus':
                diagonal1 = float(input("Enter the length of diagonal 1: "))
                diagonal2 = float(input("Enter the length of diagonal 2: "))
                area = shapes_area.rhombus(diagonal1, diagonal2)
                total_area += area
            elif shape_choice == 'trapezoid':
                base1 = float(input("Enter the length of base 1: "))
                base2 = float(input("Enter the length of base 2: "))
                height = float(input("Enter the height: "))
                area = shapes_area.trapezoid(base1, base2, height)
                total_area += area
            elif shape_choice == 'parallelogram':
                base = float(input("Enter the base: "))
                height = float(input("Enter the height: "))
                area = shapes_area.parallelogram(base, height)
                total_area += area
            else:
                print("Invalid shape choice!")
        print(f"The combined area of {num_shapes} shapes is: {total_area}")
    elif choice == '4':
        num_objects = int(input("Enter the number of objects: "))
        total_surface_area = 0
        for i in range(num_objects):
            object_choice = input(f"Select object {i+1} (cube, sphere, cylinder, cuboid, cone): ")
            if object_choice == 'cube':
                side = float(input("Enter the side length: "))
                surface_area = object_area.cube(side)
                total_surface_area += surface_area
            elif object_choice == 'sphere':
                radius = float(input("Enter the radius: "))
                surface_area = object_area.sphere(radius)
                total_surface_area += surface_area
            elif object_choice == 'cylinder':
                radius = float(input("Enter the radius: "))
                height = float(input("Enter the height: "))
                surface_area = object_area.cylinder(radius, height)
                total_surface_area += surface_area
            elif object_choice == 'cuboid':
                length = float(input("Enter the length: "))
                width = float(input("Enter the width: "))
                height = float(input("Enter the height: "))
                surface_area = object_area.cuboid(length, width, height)
                total_surface_area += surface_area
            
            elif object_choice == 'cone':
                radius = float(input("Enter the radius: "))
                height = float(input("Enter the height: "))
                surface_area = object_area.cone(radius, height)
                total_surface_area += surface_area
           
            else:
                print("Invalid object choice!")
        print(f"The combined surface area of {num_objects} objects is: {total_surface_area}")

              
    else:
        print("INVALID SELECTION")


main()

