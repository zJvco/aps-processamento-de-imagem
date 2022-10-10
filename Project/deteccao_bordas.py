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

img = cinza(Image.open("./img/baloes.jpg"))
img_width = img.width
img_height = img.height

output_img = Image.new("RGB", (img_width, img_height))


def get_modified_pixel(x, y, dir_kernel):
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

            r, g, b = img.getpixel((k, m))

            result = r * cur_kernel_value
            # g += g * cur_kernel_value
            # b += b * cur_kernel_value

            acc += result

    return acc


for x in range(img_width):
    for y in range(img_height):
        pixel = get_modified_pixel(x, y, VERTICAL_KERNEL)

        output_img.putpixel((x, y), pixel)

output_img.save("./img/output.jpg")

# x - 1, y - 1 || x - 1, y || x - 1, y + 1
# x, y - 1 || x, y || x, y + 1
# x + 1, y - 1 || x + 1, y || x + 1, y + 1