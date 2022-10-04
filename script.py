from rdkit import Chem
from rdkit.Chem import Draw
import sys


def smiletoimage(sm):
    my_mol = Chem.MolFromSmiles(sm)
    Draw.MolToFile(my_mol, 'static/molecule.png')


# smile = sys.argv[1]
# smile = 'OC[C@@H](O1)[C@@H](O)[C@H](O)[C@@H](O)[C@H](O)1'
# smiletoimage(smile)
