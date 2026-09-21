with open('station-history.html','r',encoding='utf-8') as f:
    c = f.read()
# 荒草漫铁轨换对图
c = c.replace('<img src="report-0921/assets/hist-16.jpg" alt="荒草漫过铁轨">',
              '<img src="report-0921/assets/station-2.jpg" alt="荒草漫过铁轨">')
# 文创休闲街区那张桥换成文创街实景
c = c.replace('<img src="report-0921/assets/new-street-2.jpg" alt="沿铁轨慢行步道">',
              '<img src="report-0921/assets/new-street-4.jpg" alt="文创休闲街区火车市集">')
c = c.replace('<img src="report-0921/assets/new-street-1.jpg" alt="文创休闲街区火车市集">',
              '<img src="report-0921/assets/new-street-5.jpg" alt="文创休闲街区火车市集">')
with open('station-history.html','w',encoding='utf-8',newline='') as f:
    f.write(c)
print('fixed')
