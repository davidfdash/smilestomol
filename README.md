# smilestomol

This app will accept SMILES formatted strings as a url parameter, convert them to a png, and then serve that image as a web page.

/////////////////////////////////////////////

  Prereqs<br>
install python 3.10<br>
pip install update<br>
pip install rdkit<br>
pip install flask<br>
flask --app flask_site.py run<br>

/////////////////////////////////////////////

Test SMILES<br>
/?smile=CN1CCC[C@H]1c2cccnc2

/////////////////////////////////////////////

https://192.168.209.1:5000
flask --app flask_site.py run --host=192.168.209.1 --cert='client.pem' --key='client_key.pem'

http://192.168.209.1:5000
flask --app flask_site.py run --host=192.168.209.1
