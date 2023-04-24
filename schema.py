start_part = """
<html>

<head>

</head>

<body>
<table>

    <tr>

        <td>Изображение</td>
        <td>Номер</td>
        <td>Название</td>
        <td>Описание</td>
        <td>Набор</td>
        <td>Редкость</td>
        <td>Стихия</td>
        <td>Стоимость</td>
        <td>Статы</td>

    </tr>
"""

end_part = """
</table>
</body>

</html>

<style>

table {

    width: 100%;
    text-align: center;

}
td {

    border: 1px solid #000;
    padding: 5px;
    max-width: 20%;

}
.card_image {

    max-width: 120px;
    max-height: 220px;

}

</style>
"""

middle_part = ""

parts = []

def combinate(part):
    global middle_part

    middle_part += "<tr> \n"
     
    for el in part:
        if el == part[0]: 
            middle_part += f"<td><img class='card_image' src={el}></td>"
            continue

        middle_part += f"<td>{el}</td>"

    middle_part += "</tr> \n"

def preparing(data):
    for vals in data:
        tmp_part = []
        
        tmp_part.append(vals["image"])
        tmp_part.append(vals["id"])
        tmp_part.append(vals["name"])
        tmp_part.append(vals["description"])
        tmp_part.append(vals["set"])
        tmp_part.append(vals["rarity"])
        tmp_part.append(vals["fraction"])
        tmp_part.append(f'{vals["cost"]["count"]} ({vals["cost"]["quality"]})')
        tmp_part.append(f'{vals["health"]}:{vals["stamina"]}:{vals["damage"]}')
        

        parts.append(tmp_part)

def clear():
    global middle_part

    parts.clear()
    middle_part = ""

# parts.append(["https://berserk.ru/image/data/%D0%91%D0%B5%D1%80%D1%81%D0%B5%D1%80%D0%BA/%D0%92%D0%BE%D0%B9%D0%BD%D0%B0%20%D0%A1%D1%82%D0%B8%D1%85%D0%B8%D0%B9/%D0%B8%D0%B7%D0%BE%D0%B1%D1%80%D0%B0%D0%B6%D0%B5%D0%BD%D0%B8%D0%B5_2023-03-31_181612114.png",
#             "Кочевник",
#             "Неисчислимы их армии, что вечно кочуют с места на место, превращая в ничто деревни и города пограничья.",
#             "Война стихий",
#             "Частая",
#             "Степи",
#             "3 (Серебро)",
#             "8:2:1-2-3"])
def crete_index(data):
    preparing(data)

    for part in parts: combinate(part)

    valsult = start_part + middle_part + end_part
    open("index_test.html", "w").write(valsult)

    clear()
