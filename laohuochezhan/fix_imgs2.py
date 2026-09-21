import re
with open('station-history.html','r',encoding='utf-8') as f:
    c = f.read()
# 完全1:1对应，和初步报告里alt完全一致
replace_map = {
    '修筑湘桂铁路逢山开路': '../report-0921/assets/hist-1.jpg',
    '湘桂铁路南镇段民工开工': '../report-0921/assets/hist-2.jpg',
    '冷水滩河西老码头': '../report-0921/assets/hist-3.jpg',
    '老站台绿皮火车': '../report-0921/assets/hist-13.jpg',
    '1937年难民火车逃难': '../report-0921/assets/hist-5.jpg',
    '运输生命线': '../report-0921/assets/hist-6.jpg',
    '毁路阻敌': '../report-0921/assets/war-1.jpg',
    '抗日武装破坏敌人铁路线': '../report-0921/assets/war-2.jpg',
    '冷水滩老站房高清': '../report-0921/assets/hist-9.jpg',
    '2000年代冷水滩火车站广场': '../report-0921/assets/hist-10.jpg',
    '老火车站现状1': '../report-0921/assets/station-1.jpg',
    '老火车站现状2': '../report-0921/assets/station-2.jpg',
    '老火车站现状3': '../report-0921/assets/station-3.jpg',
    '老火车站现状4': '../report-0921/assets/station-4.jpg',
    '老火车站现状5': '../report-0921/assets/station-5.jpg',
    '老火车站现状6': '../report-0921/assets/station-6.jpg',
}
for alt, new_src in replace_map.items():
    c = re.sub(r'<img src="[^"]+" alt="' + re.escape(alt) + r'">', f'<img src="{new_src}" alt="{alt}">', c)
with open('station-history.html','w',encoding='utf-8',newline='') as f:
    f.write(c)
print('done, replaced', len(replace_map), 'exact matches')
