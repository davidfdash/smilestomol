import time
import os
from flask import Flask
from flask import request
from flask import render_template
from rdkit import Chem
from rdkit.Chem import Draw

app = Flask(__name__)
mol_name = "molecule" + str(time.time()) + ".png"

for filename in os.listdir('static/'):
    if filename.startswith('molecule_'):
        os.remove('static/' + filename)

def smiletoimage(sm):
    my_mol = Chem.MolFromSmiles(sm)
    Draw.MolToFile(my_mol, 'static/' + mol_name)

@app.route('/')
def my_molecule():
    param = request.args.get('smile')
    smiletoimage(param)
    return render_template("imagepage.html", molecule=mol_name)
