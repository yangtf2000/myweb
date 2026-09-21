with open('station-history.html','r',encoding='utf-8') as f:
    c = f.read()
replace_map = {
    # 荒草漫轨大配图：用废弃站台荒草铁轨实拍
    '荒草漫过铁轨': 'report-0921/assets/station-5.jpg',
    # 柳宗元文传千年：柳子庙
    '柳子庙': 'report-0921/assets/hist-4.jpg',
    # 周敦颐理学开宗：濂溪文化
    '理学开宗真理求索': 'report-0921/assets/hist-8.jpg',
    # 冷水滩湘江码头：湘江老码头
    '潇湘之源千年文脉': 'report-0921/assets/hist-3.jpg',
    # 文昌阁凌崖耸立：文昌阁实景
    '文昌阁凌崖耸立': 'report-0921/assets/hist-7.jpg',
}
for alt, new_src in replace_map.items():
    # 匹配任意src，alt对应就换
    import re
    c = re.sub(r'<img src="[^"]+" alt="' + re.escape(alt) + r'">', f'<img src="{new_src}" alt="{alt}">', c)
with open('station-history.html','w',encoding='utf-8',newline='') as f:
    f.write(c)
print('done')
