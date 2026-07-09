import json
import zipfile
import xml.etree.ElementTree as ET
from pathlib import Path

source = Path(r'c:/Users/Admin/Downloads/portfolio.docx')
out = Path('portfolio_content.json')

with zipfile.ZipFile(source) as z:
    xml = z.read('word/document.xml')

root = ET.fromstring(xml)
ns = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
paragraphs = []
for p in root.findall('.//w:p', ns):
    texts = []
    for t in p.findall('.//w:t', ns):
        texts.append(t.text or '')
    text = ''.join(texts).strip()
    if text:
        paragraphs.append(text)

with out.open('w', encoding='utf-8') as f:
    json.dump(paragraphs, f, ensure_ascii=False, indent=2)

print(f'Wrote {len(paragraphs)} paragraphs to {out}')
print('\n'.join(paragraphs[:40]))
