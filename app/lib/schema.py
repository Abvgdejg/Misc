middle_part = ""

def combinate(part):
    global middle_part

    # middle_part += {part.name}{part.number}
               
                
    #             {part.set}
                
                
    #           {part.fraction}
                
    #             {part.rarity}
    #             {part.cost["count"]} ({part.cost["quality"]}
    #             {part.health}
                
    #             {part.stamina}
                
    #             {part.damage}
    
def clear():
    global middle_part
    middle_part = ""

def crete_index(data):

    for part in data: combinate(part)

    valsult = middle_part
    open("index_test.html", "w").write(valsult)

    clear()

def create_cards_html(data):
    tmp = ""

    for part in data:
        # tmp += f"""
        # <div class="card-search-item col-lg-3 col-sm-4 col-xs-6 add-card-main element-relative">
        #     <div class="card-search-cardview-image">
        #         <a href="/card/{ part.id }"><img class="b-lazy lazyload img-responsive" src={ part.image } alt="" height="660" width="416"></a>
        #     </div>
        # </div>
        
        # """
        tmp += f"""
            <div class="card_image_col">
                <div class="card_image"><a href="/card/{ part.id }"><img class="card_image" src={ part.image }></a></div>
            </div>
        """

    return tmp

def error_filter():
    tmp = """
    
    <div> Not found </div>
    
    """
    return tmp

def apply_filters(filters, data):
    result_data = []
    if filters == {} : return create_cards_html(data)
    
    if "PowerCosts" in filters:
        current_filters = filters["PowerCosts"]
        for f in current_filters:
            for card in data:
                if card.cost["count"] == f: result_data.append(card)

    if result_data == []: return error_filter()

    return create_cards_html(result_data)