import re
from pathlib import Path

root = Path('.')
readme = ["A collection of mini utiliy tools, collected in [fabge/tools](https://github.com/fabge/tools).\n\n"]
for file in sorted(root.glob('*.html')):
    content = file.read_text()
    title = re.search('<h1>(.*?)</h1>', content).group(1)
    description = re.search(r'<p id="description">\s*(.*?)\s*</p>', content).group(1)
    readme.append(f'* [{title}]({file}) - {description}\n')

Path('README.md').write_text(''.join(readme), encoding='utf-8')
