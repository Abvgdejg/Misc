import requests

ids = [98264 + el for el in range(20)]

results = []

base_url = "https://berserk.ru/?route=card/card&card_id="

def formating(form_text):

    tmp = r.text.split(form_text)[-1].split("</p>")[0]
    tmp = tmp.replace("\n", "").replace(" ", "")
    
    return tmp

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

    stats = {

        "id": id,
        "cost": {

                    "count": formating("Стоимость:").split("(")[0],
                    "quality":formating("Стоимость:").split("(")[-1].split(")")[0]

                },
        "health": health,
        "stamina": stamina,
        "damage": damage,
        "fraction": fraction,

    }

    results.append(stats)



print(results)