import cv2

# Read the image
image = cv2.imread("C:/Users/Asus/Documents/Thea/SMT3/TubesAlgeo2/Algeo02-22012/dataset/1.jpg")

# Get the dimensions of the image
height, width, _ = image.shape

# Calculate the size of each grid cell
cell_height = height // 3
cell_width = width // 3

# Create a list to store RGB values of each section
sections_rgb = []

# Iterate through the image in a 3x3 grid and extract RGB values
for y in range(0, height, cell_height):
    for x in range(0, width, cell_width):
        section = image[y:y+cell_height, x:x+cell_width]
        if section.shape[0] == cell_height and section.shape[1] == cell_width:  # Check for exact section size
            rgb_values = [section[:, :, i].mean() for i in range(3)]  # Get average RGB values
            sections_rgb.append(rgb_values)

# Display or print RGB values of each section
for i, rgb in enumerate(sections_rgb, 1):
    print(f"Section {i}: RGB values - {rgb}")
