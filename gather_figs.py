import os
import re
import shutil

with open('PW13Paper.log') as fin:
    for l in fin:
        searchst = r'\<use (.+?)\>'
        name = re.search(searchst,l)
        if name:
            print(name.group(1))
            try:
                shutil.copy(name.group(1), './figs')
            except:
                pass

try:
    shutil.copy('/Users/jklymak/texmf/bibtex/bib/main.bib', './main.bib')
except:
    pass