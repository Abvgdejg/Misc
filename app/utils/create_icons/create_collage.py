from PIL import Image, ImageEnhance
import os
print(os.path.abspath("./"))
icons = ["Forests", "Plains", 
        "Swamps", "Mountains", 
        "Darkness", "Neutral", 
        "ManaCost", "Damage", "Health"]
icons_dir = "./icons/"
icons_suf = "_icon.png"

icons_count = len(icons)

schema = Image.new("RGBA", (24 * icons_count,48))

for i in range(icons_count):
    icon_path = icons_dir + icons[i] + icons_suf

    image = Image.open(icon_path)
    
    schema.paste(image, (24*i,24))

    darker = ImageEnhance.Brightness(image).enhance(0.5)

    schema.paste(darker, (24*i,0))

schema.save("result.png")

schema.show()