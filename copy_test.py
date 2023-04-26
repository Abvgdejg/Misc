import requests
import schema
import sys
import os
import json
from Classes import Card, Deck

count = 20

ids = [98264 + el for el in range(count)] #201

results = []

cards = {}

error_count = 0

images_dir = "images/"
os.makedirs(images_dir, exist_ok=True)

cards_dir = f"{images_dir}cards/"
os.makedirs(cards_dir, exist_ok=True)

base_url = "https://berserk.ru/?route=card/card&card_id="

def log(text):
    sys.stdout.write(f'\r{text}')
    sys.stdout.flush()

def save_image(url, id, card_set: str):
    img = requests.get(url)
    card_set_text = card_set.replace(" ", "_").lower()
    save_path = f"{cards_dir}card__{card_set_text}_{id}.png"
    open(save_path, "wb").write(img.content)
    return save_path

def formating(form_text, closing = "</p>", is_spaced = False, has_limit=True):

    tmp = r.text.split(form_text)[-1].split(closing)[0]
    tmp = tmp.replace("\n", " ")
    
    tmp = tmp.split(" ")

    if tmp[0] == "": tmp.remove("")
 
    if is_spaced == False: tmp = "".join(tmp)
    else: tmp = " ".join(tmp)
    
    if has_limit and len(tmp) > 50: return None
    elif len(tmp) < 250: return tmp
    

for id in ids:
    url = base_url + str(id)

    r = requests.get(url=url)

    if r.status_code == 404: 
        error_count += 1
        continue

    health = formating("Здоровье:")

    try: 
        stamina = int(formating("Количество ходов:"))
    except:
        stamina = None
    
    damage = formating("Простой удар:")
    fraction = formating("Стихия:")
    cost = {
            "count": formating("Стоимость:").split("(")[0],
            "quality":formating("Стоимость:").split("(")[-1].split(")")[0]
            }
    card_set = formating("Выпуск:", "</a>", True) 
    rarity = formating("Редкость:", "<img")
    name = formating('<div class="desc-title"><h2>', "</h2>", True)
    description = formating("<div><em>", "</em>", True, False)
    number = formating("Номер:")

    original_image_path = formating('<div class="image"><img src="', '"></div>', True, False).replace(" ", "%20")
    image = save_image(original_image_path, number, card_set)

    card = Card(id, name, description, card_set, number, fraction, rarity, cost, health, stamina, damage, image)

    stats = {

        "id": id,
        "cost": cost,
        "health": health,
        "stamina": stamina,
        "damage": damage,
        "fraction": fraction,
        "set": card_set,
        "rarity": rarity,
        "name": name,
        "description": description,
        "image": image,
        "number": number

    }

    cards[id] = stats
    results.append(card)

    log(f'Complite: {len(results)}/{count} {f"Errors: {error_count}" if error_count != 0 else ""}')


log(f'\nCreate json file')
open("cards.json", "w").write(json.dumps(cards, ensure_ascii=False, indent=4))

log(f'\nCreate index file')
schema.crete_index(results)

log(f'\nComplited \n')
 
deck = Deck([results[1], results[1],results[1],
             results[3],results[3],results[3],
             results[4],results[4],results[4],
             results[7],results[7],results[9],
             results[12],results[15],results[15]], "Best deck")
copyed_deck = Deck.deck_from_code(deck.create_code(), results)
log(f"{deck}\n")
log(f"{copyed_deck}\n")