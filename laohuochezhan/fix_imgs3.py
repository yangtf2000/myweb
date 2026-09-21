import re
with open('station-history.html','r',encoding='utf-8') as f:
    c = f.read()
replace_map = {
    '荒草漫过铁轨': 'report-0921/assets/hist-16.jpg',
    '蹲铁轨等绿皮': 'report-0921/assets/old-community-1.jpg',
    '活龙井街坊日常': 'report-0921/assets/community-1.jpg',
    '黄泥井老街巷': 'report-0921/assets/old-community-2.jpg',
    '铁路大院家属院': 'report-0921/assets/community-2.jpg',
    '文创休闲街区火车市集': 'report-0921/assets/new-street-1.jpg',
    '沿铁轨慢行步道': 'report-0921/assets/new-street-2.jpg',
    '文创艺术街区': 'report-0921/assets/new-street-3.jpg',
    '不到潇湘岂有诗': 'report-0921/assets/hist-4.jpg',
    '摩崖石刻女书文化遗存': 'report-0921/assets/hist-8.jpg',
    '冷水滩河西老码头': 'report-0921/assets/hist-3.jpg',
    '文昌阁凌崖耸立': 'report-0921/assets/hist-7.jpg',
}
for alt, new_src in replace_map.items():
    c = re.sub(r'<img src="[^"]+" alt="' + re.escape(alt) + r'">', f'<img src="{new_src}" alt="{alt}">', c)
with open('station-history.html','w',encoding='utf-8',newline='') as f:
    f.write(c)
print('done')
