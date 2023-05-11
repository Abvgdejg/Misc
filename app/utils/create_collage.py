from PIL import Image, ImageEnhance
import os

files = os.listdir("images")
files_count = len(files)

schema = Image.new("RGBA", (24 * files_count,48))

for f in range(files_count):

    image = Image.open(f"images/{files[f]}")
    print(image.size)
    image = image.crop((100,100, 550, 550)).resize((24,24))
    

    schema.paste(image, (24*f,24))

    darker = ImageEnhance.Brightness(image).enhance(0.5)

    schema.paste(darker, (24*f,0))

schema.save("result.png")

schema.show()