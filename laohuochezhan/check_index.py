import re

with open(r'D:\myweb\laohuochezhan\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

print(f'文件大小: {len(content)} 字符')
print()
for m in re.finditer(r'<!--.*?-->|<div class="section|<footer|</body', content):
    pos = m.start()
    snippet = content[pos:pos+70].replace('\n', ' ')
    print(f'[{pos}] {snippet}')
