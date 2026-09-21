with open('station-history.html','r',encoding='utf-8') as f:
    c = f.read()
# 纠正四张文化卡片的错误对应
c = c.replace('<img src="report-0921/assets/hist-5.jpg" alt="柳子街青石板路">',
              '<img src="report-0921/assets/hist-11.jpg" alt="柳子街青石板路">')
c = c.replace('<img src="report-0921/assets/hist-3.jpg" alt="萍岛航拍">',
              '<img src="report-0921/assets/hist-17.jpg" alt="萍岛航拍">')
c = c.replace('<img src="report-0921/assets/hist-6.jpg" alt="冷水滩文昌阁航拍">',
              '<img src="report-0921/assets/hist-18.jpg" alt="冷水滩文昌阁航拍">')
# 湘江码头用hist-3 老码头
c = c.replace('<img src="report-0921/assets/hist-2.jpg" alt="潇湘二水交汇处萍岛">',
              '<img src="report-0921/assets/hist-3.jpg" alt="冷水滩湘江老码头">')
with open('station-history.html','w',encoding='utf-8',newline='') as f:
    f.write(c)
print('fixed')
