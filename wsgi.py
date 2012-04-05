import os
from io import BytesIO
from random import randint

from PIL import Image, ImageOps
from flask import render_template, request, Flask, send_file

application = app = Flask(__name__)
themes = [t for t in os.listdir("./images")]
themes.sort()
default_theme = themes[-1]
GREY = 'G'
COLOR = 'RGB'


def get_cropped_image(theme, x, y, grey=False):
    '''crops a random image from a given theme.'''
    im_list = os.listdir('./images/%s' % theme)
    im_src = im_list[randint(1, len(im_list)) - 1]
    im = Image.open("images/%s/%s" % (theme, im_src))
    out = BytesIO()
    max_x, max_y = im.size
    if x < max_x or y < max_y:
        im = ImageOps.fit(im, (x, y), Image.ANTIALIAS, 0, (.5, .5))
    if grey:
        im = ImageOps.grayscale(im)
    im.save(out, 'JPEG', quality=70)
    out.seek(0)
    return out


def make_response(x, y, color_mode=COLOR, theme=default_theme):
    im = get_cropped_image(theme, x, y, color_mode == GREY)
    return send_file(im, mimetype='image/jpeg')


@app.route("/")
def hello():
    u = request.host
    return render_template("index.html", url=u)


@app.route("/<theme>")
def themed_hello(theme):
    u = request.host
    return render_template("index.html", url=u, theme=theme)


@app.route("/bookmarklet")
def bookmarklet():
    u = request.host
    return render_template("bookmarklet.html", url=u, themes=themes, default=default_theme)


@app.route("/<int:x>/<int:y>")
def generate(x, y):
    return make_response(x, y, COLOR)


@app.route("/<int:x>/<int:y>/<theme>")
def generate_custom(x, y, theme):
    return make_response(x, y, COLOR, theme)


@app.route("/g/<int:x>/<int:y>")
def generate_grey(x, y):
    return make_response(x, y, GREY)


@app.route("/g/<int:x>/<int:y>/<theme>")
def generate_grey_custom(x, y, theme):
    return make_response(x, y, GREY, theme)


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5001))
    app.run(host='0.0.0.0', port=port)
