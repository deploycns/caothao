import re

with open('d:/PORTFOLIO_THREAD/caothao/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace footer name
html = html.replace('<div class="fl">Lại Minh <span>Ngọc</span></div>', '<div class="fl">Cao Phương <span>Thảo</span></div>')

with open('d:/PORTFOLIO_THREAD/caothao/index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print('Done!')
