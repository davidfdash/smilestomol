from flask import Flask
from flask import request
from flask import render_template
import script

app = Flask(__name__)


@app.route('/')
def my_molecule():
    param = request.args.get('smile')
    script.smiletoimage(param)
    return render_template("imagepage.html")
