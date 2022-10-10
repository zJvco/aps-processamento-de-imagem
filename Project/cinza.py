from PIL import Image


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


imagem = Image.open('./img/baloes.jpg')

imagem_cinza = cinza(imagem)
imagem_cinza.save('./img/baloes cinza.jpg')