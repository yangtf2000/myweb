with open('station-history.html','r',encoding='utf-8') as f:
    c = f.read()
c = c.replace('<img src="report-0921/assets/station-1.jpg" alt="废弃站台荒草">',
              '<img src="report-0921/assets/hist-16.jpg" alt="荒草漫过铁轨">')
with open('station-history.html','w',encoding='utf-8',newline='') as f:
    f.write(c)
print('fixed')
