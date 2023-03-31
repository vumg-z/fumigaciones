from bs4 import BeautifulSoup
import json
import re
from unidecode import unidecode

def replace_accents(text):
    replacements = {
        'á': 'a',
        'é': 'e',
        'í': 'i',
        'ó': 'o',
        'ú': 'u',
        'ü': 'u',
        'Á': 'A',
        'É': 'E',
        'Í': 'I',
        'Ó': 'O',
        'Ú': 'U',
        'Ü': 'U',
        'ñ': 'n',
        'Ñ': 'N'
    }
    for char, replacement in replacements.items():
        text = text.replace(char, replacement)
    return text

def clean_text(text):
    text = text.strip()
    text = replace_accents(text)
    text = re.sub(r"[^a-zA-Z0-9\s]+", "", text)
    text = re.sub(r"\s+", " ", text)
    return text

def clean_extra_spaces(text):
    text = text.strip()
    text = re.sub(r"\s+", " ", text)
    return text

with open('blog.html', 'r', encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')

data = []

divs = soup.find_all('div', {'id': 'article'})

for div in divs:
    div_data = {
        'id': clean_text(div.get('id')),
        'ps': [],
        'h5s': [],
        'h5s_original': [],
        'imgs': []
    }

    ps = div.find_all('p')
    for p in ps:
        div_data['ps'].append(clean_text(p.text))

    h5s = div.find_all('h5')
    for h5 in h5s:
        div_data['h5s'].append(clean_text(h5.text))
        div_data['h5s_original'].append(clean_extra_spaces(h5.text))

    imgs = div.find_all('img')
    for img in imgs:
        div_data['imgs'].append(img.get('src'))

    data.append(div_data)

with open('articulos/articulos.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print('Datos guardados en articulos.json')