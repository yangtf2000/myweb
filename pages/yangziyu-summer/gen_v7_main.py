# -*- coding: utf-8 -*-
"""v7 main generator"""
import sys
sys.path.insert(0,r'C:\Users\ytf20\Desktop\杨子禺暑假')
from gen_v7_data import *

DAYS=[
(7,11,'六','休息·练字','cal',[B('09:00','12:00','上午休息','rs','7.11上午休息'),L,N]+cal_pm()+EVs(B('19:30','21:30','语文U1背诵+默写','cn','2h·必背必默')),'练字课+作业≤1h、语文U1背诵+默写','下午练字课，晚上语文U1','作文'),
(7,12,'日','练字·周末','cal',[B('09:00','10:00','语文U2背诵+默写','cn','1h·必背必默'),B('10:00','11:00','英语U1单词+朗读','en','1h·必完成'),B('11:00','12:00','篮球训练','bb','弹性')]+[L,N]+cal_pm()+EVf(),'语文U2背诵+默写、英语U1单词+朗读、练字课+作业≤1h','上午语文U2+英语U1+篮球，下午练字','作文'),
(7,13,'一','豆神+练字','ds',ds_am(bb=False,en_u='U2')+[L,N]+cal_pm()+EVs(B('19:30','21:30','语文U3背诵+默写','cn','2h·必背必默')),'豆神课+作业1h、英语U2单词+朗读、练字课+作业≤1h、语文U3背诵+默写','上午豆神+英语U2，下午练字，晚上语文U3','作文'),
(7,14,'二','豆神+练字','ds',ds_am(bb=True)+[L,N]+cal_pm()+EVs(B('19:30','20:30','英语U3单词+朗读','en','1h·必完成'),B('20:30','21:30','语文U4背诵+默写','cn','1h·必背必默')),'豆神课+作业、练字课+作业≤1h、英语U3单词+朗读、语文U4背诵+默写','上午豆神+篮球，下午练字，晚上英语U3+语文U4','作文'),
(7,15,'三','豆神+练字','ds',ds_am(bb=False,en_u='U4')+[L,N]+cal_pm()+EVs(B('19:30','21:30','语文U5背诵+默写','cn','2h·必背必默')),'豆神课+作业1h、英语U4单词+朗读、练字课+作业≤1h、语文U5背诵+默写','上午豆神+英语U4，下午练字，晚上语文U5','作文'),
(7,16,'四','豆神+练字','ds',ds_am(bb=True)+[L,N]+cal_pm()+EVs(B('19:30','20:30','英语U5单词+朗读','en','1h·必完成'),B('20:30','21:30','语文U6背诵+默写','cn','1h·必背必默')),'豆神课+作业、练字课+作业≤1h、英语U5单词+朗读、语文U6背诵+默写','上午豆神+篮球，下午练字，晚上英语U5+语文U6','作文'),
(7,17,'五','豆神+练字','ds',ds_am(bb=False,en_u='U6')+[L,N]+cal_pm(last=True)+EVs(B('19:30','21:30','语文U7背诵+默写','cn','2h·必背必默')),'豆神课+作业1h、英语U6单词+朗读、练字最后一课+作业≤1h、语文U7背诵+默写','上午豆神+英语U6，下午练字最后一课，晚上语文U7','作文·英语预习完成'),
(7,18,'六','豆神·周末','ds',ds_am(bb=True)+[L,N]+[B('14:00','18:00','自由活动','fr','周六下午休息')]+EVs(B('19:30','21:30','语文U8背诵+默写','cn','2h·必背必默')),'豆神课+作业1h、语文U8背诵+默写','上午豆神+篮球，下午自由，晚上语文U8','作文·语文预习完成'),
(7,19,'日','数学预习','ma',[B('09:00','11:00','数学U1预习','ma','2h·含练习·必完成'),B('11:00','12:00','语文+英语阅读训练','rv','1h·各30min')]+[L,N]+[B('14:00','16:00','数学U2预习','ma','2h·含练习·必完成'),B('16:00','18:00','自由活动','fr')]+EVf(),'数学U1+U2预习、阅读训练1h','上午数学U1+阅读训练，下午数学U2，晚上自由','作文'),
(7,20,'一','豆神+篮球','ds',ds_new(bb=True)+[L,N]+new_pm(True)+new_ev(),'豆神课、篮球、数学预习(网课+实验班)、练字1h、阅读理解4篇','上午豆神+篮球，下午练字+阅读理解+数学预习，晚上复习+锻炼','作文'),
(7,21,'二','豆神日','ds',ds_new(bb=False)+[L,N]+new_pm(True)+new_ev(),'豆神课、数学预习(网课+实验班)、练字1h、阅读理解4篇','上午豆神+语文复习，下午练字+阅读理解+数学预习，晚上复习+锻炼','作文'),
(7,22,'三','豆神+篮球','ds',ds_new(bb=True)+[L,N]+new_pm(True)+new_ev(),'豆神课、篮球、数学预习(网课+实验班)、练字1h、阅读理解4篇','上午豆神+篮球，下午练字+阅读理解+数学预习，晚上复习+锻炼','作文'),
(7,23,'四','豆神日','ds',ds_new(bb=False)+[L,N]+new_pm(True)+new_ev(),'豆神课、数学预习(网课+实验班)、练字1h、阅读理解4篇','上午豆神+语文复习，下午练字+阅读理解+数学预习，晚上复习+锻炼','作文'),
(7,24,'五','豆神+篮球','ds',ds_new(bb=True)+[L,N]+new_pm(True)+new_ev(),'豆神课、篮球、数学预习(网课+实验班)、练字1h、阅读理解4篇','上午豆神+篮球，下午练字+阅读理解+数学预习，晚上复习+锻炼','作文'),
(7,25,'六','豆神最后','ds',ds_new(bb=False,last=True)+[L,N]+new_pm(True)+new_ev(),'豆神最后一课、数学预习(网课+实验班)、练字1h、阅读理解4篇','上午豆神最后一课+语文复习，下午练字+阅读理解+数学预习，晚上复习+锻炼','作文·数学预习完成'),
(7,26,'日','可旅行','tv',am_cn()+[L,N]+new_pm()+new_ev(),'练字1h、阅读理解4篇、数学实验班习题2.5h','上午语文复习，下午练字+阅读理解+实验班习题，晚上复习+锻炼','旅行调整·作文'),
(7,27,'一','可旅行','tv',am_cn()+[L,N]+new_pm()+new_ev(),'练字1h、阅读理解4篇、数学实验班习题2.5h','上午语文复习，下午练字+阅读理解+实验班习题，晚上复习+锻炼','旅行调整'),
(7,28,'二','可旅行','tv',am_cn()+[L,N]+new_pm()+new_ev(),'练字1h、阅读理解4篇、数学实验班习题2.5h','上午语文复习，下午练字+阅读理解+实验班习题，晚上复习+锻炼','旅行调整'),
(7,29,'三','可旅行','tv',am_cn()+[L,N]+new_pm()+new_ev(),'练字1h、阅读理解4篇、数学实验班习题2.5h','上午语文复习，下午练字+阅读理解+实验班习题，晚上复习+锻炼','旅行调整'),
(7,30,'四','可旅行','tv',am_cn()+[L,N]+new_pm()+new_ev(),'练字1h、阅读理解4篇、数学实验班习题2.5h','上午语文复习，下午练字+阅读理解+实验班习题，晚上复习+锻炼','旅行调整'),
(7,31,'五','旅行出发','tr',travel(31),'—','旅行出发','—'),
(8,1,'六','旅行','tr',travel(1),'—','旅行','—'),
(8,2,'日','旅行','tr',travel(2),'—','旅行','—'),
(8,3,'一','旅行','tr',travel(3),'—','旅行','—'),
(8,4,'二','旅行','tr',travel(4),'—','旅行','—'),
(8,5,'三','旅行','tr',travel(5),'—','旅行','—'),
(8,6,'四','旅行返回','tr',travel(6),'—','旅行返回','—'),
(8,7,'五','可旅行','tv',pre_travel(),'语文阅读理解1篇、英语阅读理解1篇、数学实验班1h','阅读理解+准备英语课','旅行调整'),
(8,8,'六','英语课日','en',en_only(we=True),'英语课+作业3h','上午英语课，下午作业，晚上自由','阅读理解'),
(8,9,'日','英语课日','en',en_only(we=True),'英语课+作业3h','上午英语课，下午作业，晚上自由','阅读理解'),
(8,10,'一','英语课日','en',en_only(),'英语课+作业3h','上午英语课，下午作业，晚上阅读理解','阅读理解'),
(8,11,'二','英语课日','en',en_only(),'英语课+作业3h','上午英语课，下午作业，晚上阅读理解','阅读理解'),
(8,12,'三','英语课日','en',en_only(),'英语课+作业3h','上午英语课，下午作业，晚上阅读理解','阅读理解'),
(8,13,'四','英语休息','rv',en_rest(bb=True),'篮球·语文阅读理解','上午语文阅读理解+篮球，下午自由复习','阅读理解'),
(8,14,'五','英语课日','en',en_only(),'英语课+作业3h','上午英语课，下午作业，晚上阅读理解','阅读理解'),
(8,15,'六','英数双课','bb',en_math(we=True),'英语课+作业、数学课+作业','上午英语，下午数学+作业，晚上英语作业','仅阅读'),
(8,16,'日','英数双课','bb',en_math(we=True),'英语课+作业、数学课+作业','上午英语，下午数学+作业，晚上英语作业','仅阅读'),
(8,17,'一','英数双课','bb',en_math(),'英语课+作业、数学课+作业','上午英语，下午数学+作业，晚上英语作业','仅阅读'),
(8,18,'二','英数双课','bb',en_math(),'英语课+作业、数学课+作业','上午英语，下午数学+作业，晚上英语作业','仅阅读'),
(8,19,'三','英语休息·数课','ma',en_rest(mc=True,bb=True),'数学课+作业2h','上午语文+篮球，下午数学课+作业','仅阅读'),
(8,20,'四','英数双课','bb',en_math(),'英语课+作业、数学课+作业','上午英语，下午数学+作业，晚上英语作业','仅阅读'),
(8,21,'五','双休息','rv',en_rest(),'复习·阅读理解','上午语文+英语阅读理解，下午数学实验班','仅阅读'),
(8,22,'六','英数双课','bb',en_math(we=True),'英语课+作业、数学课+作业','上午英语，下午数学+作业，晚上英语作业','仅阅读'),
(8,23,'日','英数双课','bb',en_math(we=True),'英语课+作业、数学课+作业','上午英语，下午数学+作业，晚上英语作业','仅阅读'),
(8,24,'一','英数双课','bb',en_math(),'英语课+作业、数学课+作业','上午英语，下午数学+作业，晚上英语作业','仅阅读'),
(8,25,'二','英语休息·数课','ma',en_rest(mc=True,bb=True),'数学课+作业2h','上午语文+篮球，下午数学课+作业','仅阅读'),
(8,26,'三','英数双课','bb',en_math(),'英语课+作业、数学课+作业','上午英语，下午数学+作业，晚上英语作业','仅阅读'),
(8,27,'四','数学最后','bb',en_math(last=True),'英语课+作业、数学最后一课+作业','上午英语，下午数学最后一课+作业，晚上英语作业','仅阅读'),
(8,28,'五','英语课日','en',en_only(),'英语课+作业3h','上午英语课，下午作业，晚上阅读理解','阅读理解'),
(8,29,'六','英语最后','en',en_only(we=True,last=True),'英语最后一课+作业','上午英语最后一课，下午作业，晚上自由','庆祝'),
(8,30,'日','收尾','rd',end_day(water=True),'暑假作业检查','水上乐园/查漏补缺','水上乐园'),
(8,31,'一','开学准备','rs',end_day(),'调整作息·准备开学','查漏补缺·收心','—'),
]
CSS="""
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:'PingFang SC','Microsoft YaHei',sans-serif;background:#0d1117;color:#e6edf3;line-height:1.5;font-size:13px;padding:16px}
.wrap{max-width:1500px;margin:0 auto}
.hdr{background:linear-gradient(135deg,#1a1f35 0%,#1c2842 50%,#0d2137 100%);border:1px solid #30363d;border-radius:12px;padding:24px 30px;margin-bottom:16px}
.hdr h1{font-size:24px;color:#58a6ff;margin-bottom:4px}
.hdr .sub{font-size:13px;color:#8b949e}
.hdr .lg{display:flex;gap:6px;flex-wrap:wrap;margin-top:10px}
.hdr .lg span{background:rgba(88,166,255,0.1);border:1px solid #30363d;padding:3px 10px;border-radius:12px;font-size:11px;color:#8b949e}
.sec{background:#161b22;border:1px solid #30363d;border-radius:10px;padding:18px 22px;margin-bottom:16px}
.sec-t{font-size:18px;font-weight:bold;color:#58a6ff;margin-bottom:12px;padding-bottom:8px;border-bottom:1px solid #21262d}
.sec-sub{color:#8b949e;font-size:12px;margin-bottom:12px}
.rt{width:100%;border-collapse:collapse;font-size:12px}
.rt th{background:#21262d;color:#58a6ff;padding:7px 10px;text-align:left;border:1px solid #30363d}
.rt td{padding:6px 10px;border:1px solid #21262d}
.rt td:first-child{color:#8b949e;white-space:nowrap;font-weight:bold}
.rt .am td:first-child{color:#3fb950}.rt .pm td:first-child{color:#bc8cff}.rt .ev td:first-child{color:#58a6ff}
.tl{display:grid;grid-template-columns:1fr 1fr 1fr;gap:12px}
.tl-c{background:#0d1117;border:1px solid #30363d;border-radius:8px;padding:14px}
.tl-c h3{font-size:14px;margin-bottom:8px;padding-bottom:6px;border-bottom:1px solid #21262d}
.tl-c h3.a{color:#f85149}.tl-c h3.b{color:#58a6ff}.tl-c h3.c{color:#f778ba}
.tl-c table{width:100%;font-size:11px;border-collapse:collapse}
.tl-c th{color:#8b949e;text-align:left;padding:3px 4px;border-bottom:1px solid #21262d;font-weight:normal}
.tl-c td{padding:3px 4px;border-bottom:1px solid #0d1117}
.tl-l{font-size:12px;line-height:2.1}
.tl-l li{list-style:none;padding-left:18px;position:relative}
.tl-l li:before{content:'☐';position:absolute;left:0;color:#30363d}
.ov{display:grid;grid-template-columns:repeat(7,1fr);gap:3px;background:#21262d;padding:3px;border-radius:6px}
.ov-h{text-align:center;padding:5px;font-weight:bold;font-size:11px;background:#21262d;color:#8b949e;border-radius:3px}
.ov-d{background:#0d1117;border-radius:3px;padding:5px 6px;min-height:68px;font-size:10px;border-left:3px solid #30363d}
.ov-d.we{background:#1a1500;border-left-color:#f5a623}
.ov-d.tr{background:#0a1f0a;border-left-color:#3fb950}
.ov-d.tv{background:#0d1f1a;border-left-color:#2d8c6e}
.ov-d.fr{background:#0d1117;border-left-color:#7d8590;opacity:0.6}
.ov-d .dt{font-weight:bold;color:#e6edf3;font-size:11px}
.ov-d .dl{font-size:9px;color:#8b949e;margin-top:2px}
.ov-d .cls{font-size:9px;color:#58a6ff;margin-top:1px;line-height:1.3}
.ov-d .dot{display:inline-block;width:6px;height:6px;border-radius:50%;margin-right:2px}
.dc{background:#161b22;border:1px solid #30363d;border-radius:8px;margin-bottom:8px;overflow:hidden}
.dch{display:flex;align-items:center;gap:8px;padding:8px 12px;background:#0d1117;border-bottom:1px solid #21262d}
.dch .dn{font-size:15px;font-weight:bold;color:#e6edf3}
.dch .dw{font-size:11px;color:#8b949e}
.dch .dt{font-size:10px;padding:2px 8px;border-radius:10px;color:white;font-weight:bold}
.dch .dp{margin-left:auto;font-size:11px;color:#8b949e}
.sum{display:flex;gap:8px;padding:6px 12px;background:#0d1117;border-bottom:1px solid #21262d;font-size:11px;flex-wrap:wrap}
.sum>div{flex:1;min-width:200px}
.sum .mu{color:#f85149}.sum .mu b{color:#f85149}
.sum .fl{color:#79c0ff}.sum .fl b{color:#79c0ff}
.sum .op{color:#8b949e}.sum .op b{color:#8b949e}
.cols{display:grid;grid-template-columns:1fr 1fr 1fr;gap:1px;background:#21262d}
.col{padding:8px 10px}
.col.cam{background:rgba(63,185,80,0.04)}
.col.cpm{background:rgba(163,113,247,0.04)}
.col.cev{background:rgba(88,166,255,0.04)}
.col h4{font-size:12px;color:#8b949e;margin-bottom:6px;text-transform:uppercase;letter-spacing:1px}
.tr{display:flex;align-items:flex-start;gap:6px;padding:3px 0;border-bottom:1px solid #0d1117;font-size:11px}
.tr:last-child{border-bottom:none}
.tr .tm{color:#8b949e;white-space:nowrap;min-width:80px;font-size:10px}
.tr .bar{width:3px;align-self:stretch;border-radius:2px;min-height:16px;flex-shrink:0}
.tr .tt{flex:1;color:#e6edf3}
.tr .nt{color:#8b949e;font-size:10px}
.cl{display:grid;grid-template-columns:1fr 1fr;gap:12px}
.cl-c{background:#0d1117;border:1px solid #30363d;border-radius:8px;padding:14px}
.cl-c h3{font-size:14px;color:#58a6ff;margin-bottom:10px}
.cl-i{display:flex;align-items:center;gap:8px;padding:4px 0;font-size:12px;border-bottom:1px solid #21262d}
.cl-i:last-child{border-bottom:none}
.cl-i input{width:16px;height:16px;accent-color:#3fb950}
.cl-i .st{margin-left:auto;font-size:10px;color:#8b949e}
.note{background:#1a1f35;border-left:3px solid #58a6ff;padding:8px 12px;margin:8px 0;font-size:12px;border-radius:4px}
.note.danger{background:#2a1515;border-left-color:#f85149}
.note.good{background:#0a1f0a;border-left-color:#3fb950}
.note.tv-note{background:#0d1f1a;border-left-color:#2d8c6e}
@media(max-width:900px){.cols{grid-template-columns:1fr}.tl{grid-template-columns:1fr}.cl{grid-template-columns:1fr}}
"""
def period_of(s):
 h=int(s.split(':')[0])
 if h<12 or(h==12 and int(s.split(':')[1])<=30):return 'am'
 if h<18 or(h==18 and int(s.split(':')[1])<30):return 'pm'
 return 'ev'
def gblock(b):
 s,e,t,c,n=b
 col=C.get(c,'#7d8590')
 nh='<span class="nt">'+n+'</span>' if n else ''
 return '<div class="tr"><span class="tm">'+s+'-'+e+'</span><div class="bar" style="background:'+col+'"></div><span class="tt">'+t+'</span>'+nh+'</div>'
def get_cls(blocks):
 cls=[]
 for s,e,t,c,n in blocks:
  if '豆神语文课' in t:cls.append('豆神'+s)
  elif '练字课' in t:cls.append('练字'+s)
  elif '课外英语课' in t:cls.append('英语'+s)
  elif '课外数学课' in t:cls.append('数学'+s)
 return ' '.join(cls)
def gday(m,d,wd,lb,ck,blocks,must,tasks,opt):
 cc=C.get(ck,'#7d8590')
 am=''.join(gblock(b) for b in blocks if period_of(b[0])=='am')
 pm=''.join(gblock(b) for b in blocks if period_of(b[0])=='pm')
 ev=''.join(gblock(b) for b in blocks if period_of(b[0])=='ev')
 return f'<div class="dc"><div class="dch"><span class="dn">{m}.{d}</span><span class="dw">周{wd}</span><span class="dt" style="background:{cc}">{lb}</span><span class="dp">{len(blocks)}个时段</span></div><div class="sum"><div class="mu"><b>必须完成：</b>{must}</div><div class="fl"><b>今日任务：</b>{tasks}</div><div class="op"><b>可机动：</b>{opt}</div></div><div class="cols"><div class="col cam"><h4>☀ 上午</h4>{am}</div><div class="col cpm"><h4>☁ 下午</h4>{pm}</div><div class="col cev"><h4>🌙 晚上</h4>{ev}</div></div></div>'
def goverview():
 from datetime import date,timedelta
 wds=['一','二','三','四','五','六','日']
 dm={}
 for row in DAYS:
  m,d,wd,lb,ck,blocks=row[0],row[1],row[2],row[3],row[4],row[5]
  dm[(m,d)]=(wd,lb,ck,blocks)
 h='<div class="ov">'
 for w in wds:h+='<div class="ov-h">周'+w+'</div>'
 cur=date(2026,7,6);end=date(2026,8,31)
 while cur<=end:
  m,d=cur.month,cur.day;k=(m,d)
  if k in dm:
   wd,lb,ck,blocks=dm[k]
   col=C.get(ck,'#7d8590')
   we=wd in['六','日']
   cls='ov-d'
   if we:cls+=' we'
   if ck=='tr':cls+=' tr'
   if ck=='tv':cls+=' tv'
   if ck=='fr':cls+=' fr'
   ci=get_cls(blocks)
   ci_html='<div class="cls">'+ci+'</div>' if ci else ''
   h+='<div class="'+cls+'"><div class="dt">'+str(m)+'/'+str(d)+'</div><div class="dl"><span class="dot" style="background:'+col+'"></span>'+lb+'</div>'+ci_html+'</div>'
  else:
   h+='<div class="ov-d" style="opacity:0.3"><div class="dt">'+str(m)+'/'+str(d)+'</div></div>'
  cur+=timedelta(days=1)
 h+='</div>'
 return h
def main():
 routine="""<table class="rt">
<tr><th>时段</th><th>时间</th><th>内容</th></tr>
<tr class="am"><td>起床</td><td>08:00-09:00</td><td>起床·洗漱·早餐（英语课时07:30起）</td></tr>
<tr class="am"><td>上午</td><td>09:00-12:00</td><td>豆神语文课(网课)+语文复习/篮球（隔天）</td></tr>
<tr><td>午餐</td><td>12:30-13:00</td><td>午餐</td></tr>
<tr><td>午休</td><td>13:00-14:00</td><td>午休</td></tr>
<tr class="pm"><td>下午</td><td>14:00-18:30</td><td>练字1h + 阅读理解1h(语文2篇+英语2篇) + 数学预习2.5h(网课+实验班习题)</td></tr>
<tr><td>晚餐</td><td>18:30-19:00</td><td>晚餐</td></tr>
<tr class="ev"><td>复习</td><td>19:00-20:00</td><td>语文背诵+英语单词复习（1h）</td></tr>
<tr class="ev"><td>锻炼</td><td>20:00-21:30</td><td>锻炼·自由活动（1.5h）</td></tr>
<tr class="ev"><td>阅读</td><td>21:30-22:00</td><td>课外阅读（30min）</td></tr>
<tr><td>就寝</td><td>22:00</td><td>就寝</td></tr>
</table>"""
 task_a="""<table>
<tr><th>课程</th><th>日期</th><th>上课时间</th><th>作业</th><th>休息日</th></tr>
<tr><td>练字</td><td>7.6-7.17</td><td>14:30-16:00</td><td>≤1h</td><td>无</td></tr>
<tr><td>豆神语文(网课)</td><td>7.13-7.25</td><td>9:00-10:30</td><td>1h</td><td>7/19</td></tr>
<tr><td>课外英语</td><td>8.8-8.29</td><td>8:30-11:30</td><td>3h</td><td>8/13·8/19·8/25</td></tr>
<tr><td>课外数学</td><td>8.15-8.27</td><td>13:30-15:30</td><td>2h</td><td>8/21</td></tr>
</table>
<div class="note">以上为<b>固定安排不可变更</b>。豆神为网课无需通勤，其他课程通勤已纳入前后任务时间，不单独列出。课后作业<b>紧接课程完成</b>。</div>"""
 task_b="""<table>
<tr><th>科目</th><th>任务</th><th>每单元</th><th>完成期限</th></tr>
<tr><td>语文</td><td>8单元必背课文+默写</td><td>1-2h</td><td>7/18前</td></tr>
<tr><td>英语</td><td>6单元单词+朗读</td><td>1h</td><td>7/17前</td></tr>
<tr><td>数学</td><td>8单元预习(网课+实验班习题)</td><td>2.5h</td><td>7/25前</td></tr>
<tr><td>阅读理解</td><td>语文2篇+英语2篇/天</td><td>1h</td><td>7/20起每天</td></tr>
</table>
<div class="note good">语文+英语预习<b>7/18前完成</b>，数学预习(网课+实验班习题)<b>7/25前完成</b>。7/20起每天下午：练字1h+阅读理解1h+数学预习2.5h。7/26起数学预习完成后改为实验班习题。</div>"""
 task_c="""<ul class="tl-l">
<li>作文 2-4 篇（见缝插针，不给定时间）</li>
<li>非遗实践活动 1 次</li>
<li>旅行 7/31-8/6（7/26-8/7为可旅行窗口，可前后调整）</li>
<li>水上乐园 1-2 次（周末机动）</li>
<li>篮球训练 10 次（隔天·弹性·可取消）</li>
<li>每日课外阅读 30min（22:00-22:30）</li>
<li>预习完成后：语文/英语阅读理解、数学实验班习题</li>
</ul>
<div class="note tv-note">7/26-8/7为<b>可旅行窗口</b>（绿色标注）。7/31-8/6旅行期间每天3×30min：语文阅读训练+英语阅读训练+课外阅读。前后日期可调整。</div>"""
 cards=''.join(gday(*row) for row in DAYS)
 checklist="""<div class="cl"><div class="cl-c"><h3>📚 课内预习任务</h3>
<div class="cl-i"><input type="checkbox"><span>语文 U1 背诵+默写</span><span class="st">7/11</span></div>
<div class="cl-i"><input type="checkbox"><span>语文 U2 背诵+默写</span><span class="st">7/12</span></div>
<div class="cl-i"><input type="checkbox"><span>语文 U3 背诵+默写</span><span class="st">7/13</span></div>
<div class="cl-i"><input type="checkbox"><span>语文 U4 背诵+默写</span><span class="st">7/14</span></div>
<div class="cl-i"><input type="checkbox"><span>语文 U5 背诵+默写</span><span class="st">7/15</span></div>
<div class="cl-i"><input type="checkbox"><span>语文 U6 背诵+默写</span><span class="st">7/16</span></div>
<div class="cl-i"><input type="checkbox"><span>语文 U7 背诵+默写</span><span class="st">7/17</span></div>
<div class="cl-i"><input type="checkbox"><span>语文 U8 背诵+默写</span><span class="st">7/18</span></div>
<div class="cl-i"><input type="checkbox"><span>英语 U1 单词+朗读</span><span class="st">7/12</span></div>
<div class="cl-i"><input type="checkbox"><span>英语 U2 单词+朗读</span><span class="st">7/13</span></div>
<div class="cl-i"><input type="checkbox"><span>英语 U3 单词+朗读</span><span class="st">7/14</span></div>
<div class="cl-i"><input type="checkbox"><span>英语 U4 单词+朗读</span><span class="st">7/15</span></div>
<div class="cl-i"><input type="checkbox"><span>英语 U5 单词+朗读</span><span class="st">7/16</span></div>
<div class="cl-i"><input type="checkbox"><span>英语 U6 单词+朗读</span><span class="st">7/17</span></div>
<div class="cl-i"><input type="checkbox"><span>数学 U1+U2 预习</span><span class="st">7/19</span></div>
<div class="cl-i"><input type="checkbox"><span>数学预习(网课+实验班)</span><span class="st">7/20-7/25</span></div>
<div class="cl-i"><input type="checkbox"><span>每日阅读理解(语文2篇+英语2篇)</span><span class="st">7/20起</span></div>
</div><div class="cl-c"><h3>🎯 课外课程完成</h3>
<div class="cl-i"><input type="checkbox"><span>练字课 12 天全勤</span><span class="st">7/6-7/17</span></div>
<div class="cl-i"><input type="checkbox"><span>豆神语文 12 天全勤</span><span class="st">7/13-7/25</span></div>
<div class="cl-i"><input type="checkbox"><span>课外英语 18 天全勤</span><span class="st">8/8-8/29</span></div>
<div class="cl-i"><input type="checkbox"><span>课外数学 12 天全勤</span><span class="st">8/15-8/27</span></div>
<h3 style="margin-top:14px">📝 机动任务</h3>
<div class="cl-i"><input type="checkbox"><span>作文 2-4 篇</span><span class="st">见缝插针</span></div>
<div class="cl-i"><input type="checkbox"><span>非遗实践活动</span><span class="st">机动</span></div>
<div class="cl-i"><input type="checkbox"><span>旅行（7/31-8/6）</span><span class="st">可调整</span></div>
<div class="cl-i"><input type="checkbox"><span>水上乐园</span><span class="st">周末机动</span></div>
<div class="cl-i"><input type="checkbox"><span>篮球训练 10 次</span><span class="st">隔天·弹性</span></div>
<div class="cl-i"><input type="checkbox"><span>每日阅读 30min</span><span class="st">全程</span></div>
<div class="cl-i"><input type="checkbox"><span>每日阅读理解+实验班习题</span><span class="st">7/20起</span></div>
</div></div>"""
 notes="""
<div class="note good">✅ <b>7月是主战场</b>：语文8单元(7/18前) + 英语6单元(7/17前) + 数学8单元(网课+实验班,7/25前)。7/20起每天下午固定：练字1h+阅读理解1h+数学预习2.5h。</div>
<div class="note tv-note">🟢 <b>可旅行窗口 7/26-8/7</b>（绿色标注）：7/26-7/30练字+阅读理解+实验班习题，7/31-8/6旅行，8/7准备英语课。可前后调整。</div>
<div class="note danger">⚠️ <b>8.15-8.27 双课期</b>：每天英语3h+作业2h+数学2h+作业2h≈9h。仅保证阅读，不安排其他任务。所有预习务必7/25前完成。</div>
<div class="note">📋 <b>每日下午三段</b>：① 练字1h(14:00-15:00) ② 阅读理解1h(15:00-16:00·语文2篇+英语2篇) ③ 数学预习2.5h(16:00-18:30·网课+实验班习题·一课一习题)</div>
<div class="note">🕐 <b>晚上安排</b>：18:30晚餐→19:00语文背诵+英语单词复习(1h)→20:00锻炼+自由(1.5h)→21:30阅读(30min)→22:00就寝</div>
<div class="note">🏀 <b>篮球隔天1次</b>：7/20·7/22·7/24(7月) + 8/13·8/19·8/25(8月) = 剩余5次。弹性可取消。</div>
<div class="note">📖 <b>数学预习方式</b>：网课视频学习+实验班习题，一课一习题，加快进度。7/26起预习完成后改为实验班习题专项练习。</div>
<div class="note">🚌 <b>通勤</b>：已纳入前后任务时间，不单独列出。豆神为网课无需通勤。</div>"""
 ov=goverview()
 html=f"""<!DOCTYPE html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>暑假详细月历表 v7</title><style>{CSS}</style></head><body><div class="wrap">
<div class="hdr"><h1>📅 杨子禺 2026 暑假详细月历表</h1><div class="sub">7月11日 — 8月31日 · 共52天 · 7/21起上午只有语文课+篮球 · 下午练字1h+阅读理解1h+数学预习2.5h · 晚上19:00复习·20:00锻炼 · 数学预习7/25前完成 · 可旅行窗口7.26-8.7</div><div class="lg">
<span style="border-left:3px solid #f0883e;padding-left:6px">语文</span><span style="border-left:3px solid #3fb950;padding-left:6px">英语</span><span style="border-left:3px solid #a371f7;padding-left:6px">数学</span><span style="border-left:3px solid #f85149;padding-left:6px">练字</span><span style="border-left:3px solid #ff7b72;padding-left:6px">豆神</span><span style="border-left:3px solid #ff6b6b;padding-left:6px">篮球</span><span style="border-left:3px solid #2d8c6e;padding-left:6px">可旅行</span><span style="border-left:3px solid #3fb950;padding-left:6px">旅行</span><span style="border-left:3px solid #58a6ff;padding-left:6px">阅读</span><span style="border-left:3px solid #7d8590;padding-left:6px">机动</span></div></div>
<div class="sec"><div class="sec-t">一、每日作息时间表</div><div class="sec-sub">7/21起：上午豆神+语文/篮球 · 下午练字1h+阅读理解1h+数学2.5h · 晚上19:00复习·20:00锻炼 · 22:00就寝</div>{routine}</div>
<div class="sec"><div class="sec-t">二、任务清单</div><div class="tl"><div class="tl-c"><h3 class="a">A. 课外固定课程</h3>{task_a}</div><div class="tl-c"><h3 class="b">B. 课内学习任务</h3>{task_b}</div><div class="tl-c"><h3 class="c">C. 机动任务</h3>{task_c}</div></div></div>
<div class="sec"><div class="sec-t">三、月历总览</div><div class="sec-sub">7月11日 — 8月31日 · 周末标黄 · 可旅行窗口标绿 · 旅行标亮绿 · 每格显示课程时间</div>{ov}</div>
<div class="sec"><div class="sec-t">四、每日详细安排</div><div class="sec-sub">7/21起：上午只有语文课+篮球 · 下午练字+阅读理解+数学预习(不指定单元) · 晚上19:00复习·20:00锻炼 · 必须完成+今日任务+可机动</div>{cards}</div>
<div class="sec"><div class="sec-t">五、关键提醒</div>{notes}</div>
<div class="sec"><div class="sec-t">六、完成清单检查</div><div class="sec-sub">打印后逐项勾选 · 语文英语预习7/18前 · 数学预习(网课+实验班)7/25前 · 每日阅读理解7/20起 · 课外课程全勤</div>{checklist}</div>
</div></body></html>"""
 with open(OUT,'w',encoding='utf-8') as f:f.write(html)
 print(f'OK: {OUT}')
 print(f'Size: {len(html)} bytes, Days: {len(DAYS)}')

if __name__=='__main__':
 main()
