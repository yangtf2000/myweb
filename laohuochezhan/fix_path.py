import re
with open('station-history.html','r',encoding='utf-8') as f:
    c = f.read()
# 把所有../report-0921/assets/ 改成 report-0921/assets/
c = c.replace('../report-0921/assets/', 'report-0921/assets/')
with open('station-history.html','w',encoding='utf-8',newline='') as f:
    f.write(c)
print('fixed path')
