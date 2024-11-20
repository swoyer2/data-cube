from PIL import Image
from cube import *
import math

def image_to_binary(file_path):
    try:
        # Open the image file
        with Image.open(file_path) as img:
            # Convert image to RGB
            img = img.convert('RGB')
            # Get image data
            pixels = list(img.getdata())
            # Convert each pixel to binary
            binary_data = ''.join('{:08b}{:08b}{:08b}'.format(r, g, b) for r, g, b in pixels)
            print(len(binary_data))
            return binary_data
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def binary_to_image(binary_data, output_file_path, size):
    try:
        # Convert binary data back to pixel data
        pixels = [(int(binary_data[i:i+8], 2), int(binary_data[i+8:i+16], 2), int(binary_data[i+16:i+24], 2)) for i in range(0, len(binary_data), 24)]
        # Create a new image with the given size
        img = Image.new('RGB', size)
        # Put pixel data into the image
        img.putdata(pixels)
        # Save the image to the specified file path
        img.save(output_file_path)
    except Exception as e:
        print(f"An error occurred: {e}")

def binary_to_cube(binary_data, output_file_path):
    print("Encoding binary data to cube data:")
    cube_information = ''
    number_of_cubes = 0
    while len(binary_data) > 0:
        number_of_cubes += 1
        cube = RubiksCube()
        if len(binary_data) % 1000 == 0:
            print(f'Bytes left: {len(binary_data)}')
        while cube.get_amount_of_pieces() < 16:
            if len(binary_data) < 1:
                break
            binary_move = {}
            all_moves = cube.get_possible_moves() 
            for i, move in enumerate(all_moves):
                binary_move[bin(i)[2:]] = move
            
            options = sorted(binary_move.keys(), key=len, reverse=True) #Binary choices from largest to smallest string length
            
            #print(binary_data[0:10])
            for option in options:
                if option == binary_data[0:len(option)]:
                    move = binary_move[option]
                    cube.add_piece(move[0], move[1])
                    binary_data = binary_data[len(option):]
                    break
        cube_information += cube.get_information()

    with open(output_file_path, 'w') as file:
        print(f"{output_file_path} Complete! \n File length: {len(cube_information)} Number of cubes: {number_of_cubes}")
        file.write(cube_information)

def cube_to_binary(cube_data_file, output_file_path):
    print("Decoding cube data into binary data:")
    with open(cube_data_file, 'r') as file:
        cube_data = file.read()
    binary_information = ''
    while len(cube_data) > 0:
        if len(cube_data) % 1000 == 0:
            print(f'Bytes left: {len(cube_data)}')
        cube = RubiksCube()
        while cube.get_amount_of_pieces() < 16:
            if len(cube_data) < 1:
                break
            move_binary = {}
            all_moves = cube.get_possible_moves() 
            for i, move in enumerate(all_moves):
                move_binary[move] = bin(i)[2:]
            
            options = sorted(move_binary.keys(), key=len, reverse=True) #Binary choices from largest to smallest string length
            
            # print(cube_data[0:10])
            for option in options:
                colors = tuple(int(c) for c in cube_data[0:len(option[0])])
                rotation = cube_data[len(option[0])+1:2+len(option[0])]
                move = (colors, int(rotation))
                if option == move:
                    binary = move_binary[option]
                    cube.add_piece(move[0], move[1])
                    cube_data = cube_data[len(option[0])+3:]
                    break
            binary_information += binary

    with open(output_file_path, 'w') as file:
        print(f"{output_file_path} Complete! \n File length: {len(binary_information)}")
        file.write(binary_information)
    

# Example usage
file_path = 'cube.jpg'
binary_data = image_to_binary(file_path)

binary_to_cube(binary_data,'cube_data.txt')
cube_to_binary('cube_data.txt','binary_data_2.txt')

# if binary_data:
#     with open('binary_data.txt', 'w') as file:
#         for binary_pixel in binary_data:
#             file.write(binary_pixel)

# To undo the conversion, specify the size of the original image
original_size = (256, 256)
with open('binary_data_2.txt', 'r') as file:
    binary_data_2 = file.read()
binary_to_image(binary_data_2, 'reconstructed_cube.jpg', original_size)
