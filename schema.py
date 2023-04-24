start_part = """
<html>

<head>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-KK94CHFLLe+nY2dmCWGMq91rCGa5gtU4mk92HdvYe+M/SXH301p5ILy+dN9+nJOZ" crossorigin="anonymous">
</head>

<body>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ENjdO4Dr2bkBIFxQpeoTz1HIcje39Wm4jDKdf19U8gI4ddQ3GYNS7NTKfAdVQSZe" crossorigin="anonymous"></script>

    <div class="container mt-1">
"""

end_part = """
</div>
</body>

</html>

<style>
:root {
  --border-color: #fff;
}
body {

    background-color: #000;

}
.info_title {

    border-bottom: 1px solid var(--border-color);

}
.card_image {

    max-width: 100%;

}
.card_image_col {

max-width: 20%;
border: 1px solid var(--border-color);
border-radius: 5px;
padding: 5px;

}
.card_info_row {

    margin: 0;

}
.card_data_col {

color: #fff;

}
.card_title_row {

    border: 1px solid var(--border-color);
    border-radius: 5px;
    margin: 0;
    padding: 5px;

}
.card_info {

    border: 1px solid var(--border-color);
    border-radius: 5px;
    margin-top: 5px;
    padding: 5px;
    text-align: center;
    display: inline-block;

}

</style>
"""

middle_part = ""

def combinate(part):
    global middle_part

    middle_part += f"""
    <div class="row mt-2" style="border: 1px solid #fff; padding: 5px;">     

        <div class="col card_image_col">
            <div class="card_image"><img class="card_image" src="{part["image"]}"></div>
        </div>

        <table class="col card_data_col m-2"><tbody><td>
            <div class="row card_title_row mb-2">
                <div class="text-center">{part["name"]}</div>
                <div class="text-center" style="font-size: 12px;"><i>{part["description"]}</i></div>
            </div>
            <div class="row card_info_row"> 
                <div class="col card_info me-1">
                    <div class="info_title">№</div>
                    <div>{part["number"]}</div>
                </div>
                
                <div class="col card_info me-1">
                    <div class="info_title">Набор</div>
                    <div>{part["set"]}</div>
                </div>
                
                <div class="col card_info me-1">
                    <div class="info_title">Стихия</div>
                    <div>{part["fraction"]}</div>
                </div>
                
                <div class="col card_info me-1">
                    <div class="info_title">Редкость</div>
                    <div>{part["rarity"]}</div>
                </div>
                
                <div class="col card_info me-1">
                    <div class="info_title">Стоимость</div>
                    <div>{part["cost"]["count"]} ({part["cost"]["quality"]})</div>
                </div>
                
                <div class="col card_info me-1">
                    <div class="info_title">Здоровье</div>
                    <div>{part["health"]}</div>
                </div>
                
                <div class="col card_info me-1">
                    <div class="info_title">Движение</div>
                    <div>{part["stamina"]}</div>
                </div>
                
                <div class="col card_info">
                    <div class="info_title">Удар</div>
                    <div>{part["damage"]}</div>
                </div>
            </div>
        </td></tbody></table>
    </div>
    """
    
def clear():
    global middle_part
    middle_part = ""

def crete_index(data):

    for part in data: combinate(part)

    valsult = start_part + middle_part + end_part
    open("index_test.html", "w").write(valsult)

    clear()
