import requests
import schema

ids = [98264 + el for el in range(5)]

results = []


base_url = "https://berserk.ru/?route=card/card&card_id="

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

    if r.status_code == 404: continue

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
    image = formating('<div class="image"><img src="', '"></div>', has_limit=False)

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
        "image": image

    }

    results.append(stats)

    # outputs.append(f'| ID: {id}: {name}')
    # outputs.append(f'| Описание: {description}')
    # outputs.append(f'| Набор: {card_set}')
    # outputs.append(f'| Редкость: {rarity}')
    # outputs.append(f'| Стихия: {fraction}')
    # outputs.append(f'| Стоимость: {cost["count"]} ({cost["quality"]})')
    # outputs.append(f'| Статы: {health}:{stamina}:{damage}')
    # outputs.append(f'| Картинка: {image}')


max_len = 0

for res in results:

    outputs = []

    outputs.append(f'| ID: {res["id"]}: {res["name"]}')
    outputs.append(f'| Описание: {res["description"]}')
    outputs.append(f'| Набор: {res["set"]}')
    outputs.append(f'| Редкость: {res["rarity"]}')
    outputs.append(f'| Стихия: {res["fraction"]}')
    outputs.append(f'| Стоимость: {res["cost"]["count"]} ({res["cost"]["quality"]})')
    outputs.append(f'| Статы: {res["health"]}:{res["stamina"]}:{res["damage"]}')
    outputs.append(f'| Картинка: {res["image"]}')

    for out in outputs:
        if len(out) > max_len: max_len = len(out)
    
max_len = max_len + 1

print("="*(max_len+1))
for res in results:

    outputs = []
    
    outputs.append(f'| ID: {res["id"]}: {res["name"]}')
    outputs.append(f'| Описание: {res["description"]}')
    outputs.append(f'| Набор: {res["set"]}')
    outputs.append(f'| Редкость: {res["rarity"]}')
    outputs.append(f'| Стихия: {res["fraction"]}')
    outputs.append(f'| Стоимость: {res["cost"]["count"]} ({res["cost"]["quality"]})')
    outputs.append(f'| Статы: {res["health"]}:{res["stamina"]}:{res["damage"]}')
    outputs.append(f'| Картинка: {res["image"]}')
    
    for out in outputs:
        tmp_len = max_len - len(out)
        print(out + " "*tmp_len + "|")
    print("="*(max_len+1))

schema.crete_index(results)