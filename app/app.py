from flask import Flask, render_template, send_from_directory, request
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

@app.route('/css/<path:path>')
def send_css(path):
    return send_from_directory('static/css', path)

@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('static/js', path)

@app.route('/fonts/<path:path>')
def send_font(path):
    return send_from_directory('static/fonts', path)

@app.route('/test')
def test():
    return render_template("test.html")

@app.route('/test/post', methods=["GET", "POST"])
def test_post():
    

    return request.args.get('text') * 2

app.run(port="5555", debug=True)