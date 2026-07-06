import re

with open('d:/PORTFOLIO_THREAD/caothao/mau.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace personal info
html = html.replace('Lại Minh Ngọc', 'Cao Phương Thảo')
html = html.replace('Minh Ngọc', 'Phương Thảo')
html = html.replace('25040931', '25040244')
html = html.replace('Lớp: VNU1001_E252062', '')
html = html.replace('Lớp VNU1001_E252062', '')

# Replace pdf links
html = html.replace('bai1.pdf', 't1.pdf')
html = html.replace('bai2.pdf', 't2.pdf')
html = html.replace('bai3.pdf', 't3.pdf')
html = html.replace('bai4.pdf', 't4.pdf')
html = html.replace('bai5.pdf', 't5.pdf')
html = html.replace('bai6.pdf', 't6.pdf')

# Replace color palette in :root
root_old = """--c1:#dcecd1;--c2:#a3c995;--c3:#6b9e5e;--c4:#3f6b32;
  --warm1:#eef3d0;--warm2:#c9d46d;--cool1:#d0eae5;--cool2:#72b5a4;
  --olive1:#d8dfbf;--olive2:#8e9b5a;
  --bg:#f7fdf3;--txt:#2e3e26;--txt2:#4e6642;--txt3:#7a9468;
  --gbg:rgba(255,255,255,.55);--gbr:rgba(163,201,149,.35);
  --gbl:blur(20px);
  --sh1:0 2px 16px rgba(80,120,60,.09);
  --sh2:0 8px 40px rgba(80,120,60,.15);
  --sh3:0 20px 72px rgba(80,120,60,.22);
  --glow:0 0 40px rgba(107,158,94,.35);"""

root_new = """--c1:#dbe4ff;--c2:#91a7ff;--c3:#5c7cfa;--c4:#3b5bdb;
  --warm1:#f3d9fa;--warm2:#cc5de8;--cool1:#c5f6fa;--cool2:#22b8cf;
  --olive1:#ffd8a8;--olive2:#fd7e14;
  --bg:#f8f9fa;--txt:#212529;--txt2:#495057;--txt3:#868e96;
  --gbg:rgba(255,255,255,.65);--gbr:rgba(92,124,250,.35);
  --gbl:blur(20px);
  --sh1:0 2px 16px rgba(59,91,219,.09);
  --sh2:0 8px 40px rgba(59,91,219,.15);
  --sh3:0 20px 72px rgba(59,91,219,.22);
  --glow:0 0 40px rgba(92,124,250,.35);"""

html = html.replace(root_old, root_new)

# Replace other colors globally
html = html.replace('rgba(247,253,243', 'rgba(248,249,250') # nav bg
html = html.replace('rgba(163,201,149', 'rgba(92,124,250') # hover backgrounds etc
html = html.replace('rgba(80,120,60', 'rgba(59,91,219') # shadows
html = html.replace('rgba(107,158,94', 'rgba(92,124,250') # glow
html = html.replace('rgba(220,236,209', 'rgba(219,228,255') # c1 transparent
html = html.replace('rgba(238,243,208', 'rgba(243,217,250') # warm1 transparent
html = html.replace('rgba(208,234,229', 'rgba(197,246,250') # cool1 transparent
html = html.replace('rgba(216,223,191', 'rgba(255,216,168') # olive1 transparent
html = html.replace('rgba(103,180,140', 'rgba(34,184,207') # cool2 shadows

# Hex color replacements
html = html.replace('#1e3016', '#18223c')
html = html.replace('#3d5e33', '#364fc7')
html = html.replace('#5a6324', '#862e9c')
html = html.replace('#346b5e', '#0b7285')
html = html.replace('#526135', '#d9480f')
html = html.replace('#1a2e14', '#192038')
html = html.replace('#2a4520', '#25345c')
html = html.replace('#1e3820', '#1f2d4f')

# Canvas particles
html = html.replace("'#a3c995','#c9d46d','#72b5a4','#8e9b5a','#dcecd1','#e8edcc'", "'#91a7ff','#cc5de8','#22b8cf','#fd7e14','#dbe4ff','#f3d9fa'")
html = html.replace("strokeStyle='#a3c995'", "strokeStyle='#91a7ff'")

# Leaves (bubbles/stars instead)
html = html.replace("'#dcecd1','#e8edcc','#d0eae5','#d8dfbf','#c5d8bc'", "'#dbe4ff','#f3d9fa','#c5f6fa','#ffd8a8','#e5dbff'")

# Data colors
html = html.replace("'#b0c44e'", "'#91a7ff'")
html = html.replace("'#7a9a2e'", "'#5c7cfa'")
html = html.replace("'#72b5a4'", "'#22b8cf'")
html = html.replace("'#3d8078'", "'#1098ad'")
html = html.replace("'#a3c995'", "'#cc5de8'")
html = html.replace("'#5e8a48'", "'#ae3ec9'")
html = html.replace("'#c9d46d'", "'#fd7e14'")
html = html.replace("'#8f9e30'", "'#e8590c'")
html = html.replace("'#4a8a3c'", "'#862e9c'")
html = html.replace("'#2a7068'", "'#0b7285'")

html = html.replace('hsl(78,50%,45%)', 'hsl(230,100%,67%)') # c2 ish
html = html.replace('hsl(168,38%,45%)', 'hsl(188,72%,47%)')
html = html.replace('hsl(88,38%,42%)', 'hsl(288,72%,47%)')
html = html.replace('hsl(60,55%,42%)', 'hsl(28,100%,50%)')
html = html.replace('hsl(118,42%,42%)', 'hsl(270,72%,47%)')
html = html.replace('hsl(168,38%,40%)', 'hsl(188,72%,40%)')

html = html.replace('  <p class="hm"><strong>MSV: 25040244</strong> &nbsp;·&nbsp;  </p>', '  <p class="hm"><strong>MSV: 25040244</strong></p>')
html = html.replace('<li><strong>Lớp:</strong> </li>', '')
html = html.replace('<br> · <br>', '<br>')

with open('d:/PORTFOLIO_THREAD/caothao/index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print('Done!')
