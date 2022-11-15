import math
from PIL import Image

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


def cinza(imagem):
    w, h = imagem.size # pegando o tamanho da imagem
    img = Image.new('RGB', (w, h)) # gerando uma nova imagem copia para manter a original

    # perccorendo pelos pixels da imagem
    for x in range(w):
        for y in range(h):
            pixel = imagem.getpixel((x,y))
            # pegando a media entre as cores para a escala de cinza
            luminancia = (pixel[0] + pixel[1] + pixel[2]) // 3 # pega o resultado da divisão inteira, pois o RGB não aceita decimais
            # para uma cor cinza todos as cores do pixel devem ser iguais
            img.putpixel((x,y), (luminancia, luminancia, luminancia)) # alterando as cores do pixels para transforma em cinza
            
    return img


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


# Transform image in grayscale
img = cinza(Image.open("./img/formas geometricas.jpg"))
img_width = img.width
img_height = img.height

# Output image
output_img = Image.new("L", (img_width, img_height))

for x in range(img_width):
    for y in range(img_height):
        # Horizontal edges
        gx = get_modified_pixel(x, y, HORIZONTAL_KERNEL)
        # Vertical edges
        gy = get_modified_pixel(x, y, VERTICAL_KERNEL)

        g = int(math.sqrt(gx ** 2 + gy ** 2))

        output_img.putpixel((x, y), g)

output_img.save("./img/formas geometricas output.jpg")