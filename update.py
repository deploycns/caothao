import re

with open('d:/PORTFOLIO_THREAD/caothao/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Replace the tea cup with the avatar image
html = html.replace('<div class="ha">🍵</div>', '<div class="ha"><img src="z8014892428359_b7e587fd2d25d7aff680fdc5d28dc07b.jpg" alt="Avatar" style="width:100%;height:100%;border-radius:50%;object-fit:cover;"></div>')

# 2. Update Class code at line 266
html = html.replace('<p class="hm"><strong>MSV: 25040244</strong> &nbsp;·&nbsp; </p>', '<p class="hm"><strong>MSV: 25040244</strong> &nbsp;·&nbsp; Lớp: VNU1001_E252054</p>')

# 3. Update Class code at line 302
html = html.replace('<li><strong>Lớp:</strong> VNU1001_E252062</li>', '<li><strong>Lớp:</strong> VNU1001_E252054</li>')

# 4. Update Class code in footer
html = html.replace('MSV: 25040244 · <br>', 'MSV: 25040244 · Lớp VNU1001_E252054<br>')

with open('d:/PORTFOLIO_THREAD/caothao/index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print('Done!')
