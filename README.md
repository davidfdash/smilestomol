# smilestomol

This app will accept SMILES formatted strings as a url parameter, convert them to a png, and then serve that image as a web page.
/////////////////////////////////////////////
  Prereqs
install python 3.10
pip install update
pip install rdkit
pip install flask
flask --app flask_site.py run
/////////////////////////////////////////////

Test SMILES
/?smile=CN1CCC[C@H]1c2cccnc2

/////////////////////////////////////////////

https://192.168.209.1:5000
flask --app flask_site.py run --host=192.168.209.1 --cert='client.pem' --key='client_key.pem'

http://192.168.209.1:5000
flask --app flask_site.py run --host=192.168.209.1
