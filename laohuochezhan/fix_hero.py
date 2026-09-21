with open('station-history.html','r',encoding='utf-8') as f:
    c = f.read()
# 找到hero封面部分，把背景图换成老站台绿皮火车
old_hero = '''<section class="hero" style="background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%);">'''
new_hero = '''<section class="hero" style="background: linear-gradient(rgba(13,13,13,0.82), rgba(13,13,13,0.92)), url('report-0921/assets/hist-13.jpg') center/cover no-repeat;">'''
c = c.replace(old_hero, new_hero)
with open('station-history.html','w',encoding='utf-8',newline='') as f:
    f.write(c)
print('hero bg updated')
