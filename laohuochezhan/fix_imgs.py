import re
with open('station-history.html','r',encoding='utf-8') as f:
    c = f.read()
replace_map = {
    '纽约高线公园铁轨与绿植融合': '../report-0921/assets/case-1.jpg',
    '杭州白塔公园樱花与复古蒸汽机车': '../report-0921/assets/case-2.jpg',
    '厦门铁路文化公园樱花步道与休憩空间': '../report-0921/assets/case-3.jpg',
    '永州铁路主题文化公园设计图': '../report-0921/assets/case-4.jpg',
    '铁路文化公园景观设计': '../report-0921/assets/case-5.jpg',
    '铁路文创新天地设计': '../report-0921/assets/case-6.jpg',
    '废弃站台荒草': '../report-0921/assets/station-1.jpg',
    '废弃站台高清': '../report-0921/assets/station-2.jpg',
    '老站货运雨棚': '../report-0921/assets/station-platform-1.jpg',
    '夕阳下的永州东站': '../report-0921/assets/station-3.jpg',
    '冷水滩老站房高清': '../report-0921/assets/station-4.jpg',
    '2000年代冷水滩火车站广场': '../report-0921/assets/hist-1.jpg',
    '潇湘二水交汇处萍岛': '../report-0921/assets/hist-2.jpg',
    '萍岛航拍': '../report-0921/assets/hist-3.jpg',
    '柳子庙': '../report-0921/assets/hist-4.jpg',
    '柳子街青石板路': '../report-0921/assets/hist-5.jpg',
    '冷水滩文昌阁航拍': '../report-0921/assets/hist-6.jpg',
    '文昌阁临江': '../report-0921/assets/hist-7.jpg',
}
for alt, new_src in replace_map.items():
    c = re.sub(r'<img src="https://aka.doubaocdn.com/s/[^"]+" alt="' + re.escape(alt) + r'">', f'<img src="{new_src}" alt="{alt}">', c)
with open('station-history.html','w',encoding='utf-8',newline='') as f:
    f.write(c)
print('done, replaced', len(replace_map), 'images')
