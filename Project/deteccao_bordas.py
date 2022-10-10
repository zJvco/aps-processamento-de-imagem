import math
from PIL import Image

from cinza import cinza

VERTICAL_KERNEL = [
    [1, 2, 1],
    [0, 0, 0],
    [-1, -2, -1]
]
HORIZONTAL_KERNEL = [
    [-1, 0, 1],
    [-2, 0, 2],
    [-1, 0, 1]
]

# Transform image in grayscale
img = cinza(Image.open("./img/baloes.jpg"))
img_width = img.width
img_height = img.height

# Output image
output_img = Image.new("L", (img_width, img_height))


def get_modified_pixel(x, y, dir_kernel, offset=0):
    acc = 0

    # Getting window pixels
    for i, k in enumerate(range(x - 1, x + 2)):
        for j, m in enumerate(range(y - 1, y + 2)):
            if k < 0 or m < 0 or k >= img_width or m >= img_height:
                continue

            # Getting kernel value in current position
            cur_kernel_value = dir_kernel[i][j]
            
            if cur_kernel_value == 0:
                continue

            pixel = img.getpixel((k, m))[0]

            result = pixel * cur_kernel_value

            acc += result

    return acc


for x in range(img_width):
    for y in range(img_height):
        # Horizontal edges
        gx = get_modified_pixel(x, y, HORIZONTAL_KERNEL)
        # Vertical edges
        gy = get_modified_pixel(x, y, VERTICAL_KERNEL)

        g = int(math.sqrt(gx ** 2 + gy ** 2))

        output_img.putpixel((x, y), g)

output_img.save("./img/resultado.jpg")

# x - 1, y - 1 || x - 1, y || x - 1, y + 1
# x, y - 1 || x, y || x, y + 1
# x + 1, y - 1 || x + 1, y || x + 1, y + 1