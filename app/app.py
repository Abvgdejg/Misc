from flask import Flask, render_template, send_from_directory
import lib.card_base as cards


templates_dir = "./templates"

card_base = cards.copy_base()

app = Flask(__name__, template_folder=templates_dir)

@app.route("/")
def index():
    return render_template("index.html", cards=card_base)

@app.route("/card/<card_id>")
def card_page(card_id):
    returned_card = None
    for card in card_base:
        if str(card.id) == card_id: 
            returned_card = card
            break

    return render_template("card_index.html", card=returned_card)

@app.route('/images/<path:path>')
def send_image(path):
    return send_from_directory('static/images', path)

app.run(port="5555", debug=True)