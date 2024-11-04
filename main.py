from PIL import Image

def to_base6(n):
    """Convert an integer to a base-6 string with at least 4 digits."""
    base6 = []
    for _ in range(4):
        n, remainder = divmod(n, 6)
        base6.append(str(remainder))
    return ''.join(reversed(base6))


def image_to_senary(file_path):
    try:
        # Open the image file
        with Image.open(file_path) as img:
            # Convert image to RGB
            img = img.convert('RGB')
            # Get image data
            pixels = list(img.getdata())
            # Convert each pixel to base 6
            senary_data = ['{}{}{}'.format(to_base6(r), to_base6(g), to_base6(b)) for r, g, b in pixels]
            return senary_data
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def senary_to_image(senary_data, output_file_path, size):
    try:
        # Convert base 6 data back to pixel data
        pixels = [(int(s[:4], 6), int(s[4:8], 6), int(s[8:], 6)) for s in senary_data]
        # Create a new image with the given size
        img = Image.new('RGB', size)
        # Put pixel data into the image
        img.putdata(pixels)
        # Save the image to the specified file path
        img.save(output_file_path)
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
file_path = 'cube.jpg'
senary_data = image_to_senary(file_path)
if senary_data:
    with open('senary_data.txt', 'w') as file:
        file.write("Senary data for the image:\n")
        for senary_pixel in senary_data:
            file.write(senary_pixel + '\n')

# To undo the conversion, specify the size of the original image
original_size = (256, 256)
senary_to_image(senary_data, 'reconstructed_cube.jpg', original_size)
