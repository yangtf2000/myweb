# -*- coding: utf-8 -*-
"""暑假月历表 v5 生成器 - 深色主题三列布局"""
import sys, os
sys.path.insert(0, r'C:\Users\ytf20\Desktop\杨子禺暑假')
from gen_v5_final import *

CSS = """
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
.tl-c tr:hover td{background:#161b22}
.tl-l{font-size:12px;line-height:2.1}
.tl-l li{list-style:none;padding-left:18px;position:relative}
.tl-l li:before{content:'☐';position:absolute;left:0;color:#30363d}
.ov{display:grid;grid-template-columns:repeat(7,1fr);gap:3px;background:#21262d;padding:3px;border-radius:6px}
.ov-h{text-align:center;padding:5px;font-weight:bold;font-size:11px;background:#21262d;color:#8b949e;border-radius:3px}
.ov-d{background:#0d1117;border-radius:3px;padding:4px 5px;min-height:50px;font-size:10px;border-left:2px solid #30363d}
.ov-d.we{background:#1a1500;border-left-color:#f5a623}
.ov-d.tr{background:#0a1f0a;border-left-color:#3fb950}
.ov-d .dt{font-weight:bold;color:#e6edf3}
.ov-d .dl{font-size:9px;color:#8b949e;margin-top:2px}
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
.sum .fl{color:#e3b341}.sum .fl b{color:#e3b341}
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
@media(max-width:900px){.cols{grid-template-columns:1fr}.tl{grid-template-columns:1fr}.cl{grid-template-columns:1fr}}
"""

def period_of(start):
    """Determine if a time block is morning/afternoon/evening"""
    h = int(start.split(':')[0])
    if h < 12 or (h == 12 and int(start.split(':')[1]) <= 30):
        return 'am'
    elif h < 18 or (h == 18 and int(start.split(':')[1]) < 30):
        return 'pm'
    else:
        return 'ev'

def gen_block_html(blk):
    s, e, title, cat, note = blk
    color = COL.get(cat, '#7d8590')
    note_html = '<span class="nt">' + note + '</span>' if note else ''
    return '<div class="tr"><span class="tm">' + s + '-' + e + '</span><div class="bar" style="background:' + color + '"></div><span class="tt">' + title + '</span>' + note_html + '</div>'

def gen_day_card(m, d, wd, label, ck, blocks, must, flex, opt):
    ck_color = COL.get(ck, '#7d8590')
    # Split blocks into periods
    am_blocks = [b for b in blocks if period_of(b[0]) == 'am']
    pm_blocks = [b for b in blocks if period_of(b[0]) == 'pm']
    ev_blocks = [b for b in blocks if period_of(b[0]) == 'ev']

    am_html = ''.join(gen_block_html(b) for b in am_blocks)
    pm_html = ''.join(gen_block_html(b) for b in pm_blocks)
    ev_html = ''.join(gen_block_html(b) for b in ev_blocks)

    return f"""
<div class="dc">
  <div class="dch">
    <span class="dn">{m}.{d}</span>
    <span class="dw">周{wd}</span>
    <span class="dt" style="background:{ck_color}">{label}</span>
    <span class="dp">{len(blocks)}个时段</span>
  </div>
  <div class="sum">
    <div class="mu"><b>必完成：</b>{must}</div>
    <div class="fl"><b>可灵活：</b>{flex}</div>
    <div class="op"><b>可机动：</b>{opt}</div>
  </div>
  <div class="cols">
    <div class="col cam"><h4>☀ 上午 (09:00-12:30)</h4>{am_html}</div>
    <div class="col cpm"><h4>☁ 下午 (14:00-18:00)</h4>{pm_html}</div>
    <div class="col cev"><h4>🌙 晚上 (19:30-22:30)</h4>{ev_html}</div>
  </div>
</div>"""

def gen_overview():
    """Generate calendar overview grid"""
    from datetime import date, timedelta
    weekdays = ['一','二','三','四','五','六','日']
    days_map = {}
    for m, d, wd, label, ck, blocks, must, flex, opt in DAYS:
        days_map[(m, d)] = (wd, label, ck)

    html = '<div class="ov">'
    for w in weekdays:
        html += '<div class="ov-h">周' + w + '</div>'

    start = date(2026, 7, 6)  # Monday before 7/11
    end = date(2026, 8, 31)
    cur = start
    while cur <= end:
        m, d = cur.month, cur.day
        key = (m, d)
        if key in days_map:
            wd, label, ck = days_map[key]
            color = COL.get(ck, '#7d8590')
            we = wd in ['六','日']
            tr = ck == 'tr'
            cls = 'ov-d'
            if we: cls += ' we'
            if tr: cls += ' tr'
            html += '<div class="' + cls + '"><div class="dt">' + str(m) + '/' + str(d) + '</div><div class="dl"><span class="dot" style="background:' + color + '"></span>' + label + '</div></div>'
        else:
            html += '<div class="ov-d" style="opacity:0.3"><div class="dt">' + str(m) + '/' + str(d) + '</div></div>'
        cur += timedelta(days=1)

    html += '</div>'
    return html

def main():
    # Daily routine table
    routine = """
<table class="rt">
<tr><th>时段</th><th>时间</th><th>内容</th></tr>
<tr class="am"><td>起床</td><td>08:00-09:00</td><td>起床·洗漱·早餐（有课时按课表提前）</td></tr>
<tr class="am"><td>上午①</td><td>09:00-10:30</td><td>语文背诵 / 豆神课（1.5h）</td></tr>
<tr class="am"><td>上午②</td><td>10:30-12:00</td><td>英语单词+朗读（1.5h，合并进行）</td></tr>
<tr class="am"><td>缓冲</td><td>12:00-12:30</td><td>休息·准备午餐</td></tr>
<tr><td>午餐</td><td>12:30-13:00</td><td>午餐</td></tr>
<tr><td>午休</td><td>13:00-14:00</td><td>午休</td></tr>
<tr class="pm"><td>下午①</td><td>14:00-16:00</td><td>数学预习 / 英语作业（2h）</td></tr>
<tr class="pm"><td>下午②</td><td>16:00-17:00</td><td>数学练习 / 练字作业（1h）</td></tr>
<tr class="pm"><td>机动</td><td>17:00-18:00</td><td>机动时间</td></tr>
<tr><td>晚餐</td><td>18:30-19:30</td><td>晚餐·休息</td></tr>
<tr class="ev"><td>晚上①</td><td>19:30-20:30</td><td>豆神作业 / 复习（1h）</td></tr>
<tr class="ev"><td>晚上②</td><td>20:30-22:00</td><td>语文背诵 / 数学练习（1.5h）</td></tr>
<tr class="ev"><td>阅读</td><td>22:00-22:30</td><td>课外阅读（固定·30min）</td></tr>
<tr><td>就寝</td><td>22:30</td><td>就寝</td></tr>
</table>"""

    # Task list A: Fixed courses
    task_a = """
<table>
<tr><th>课程</th><th>日期</th><th>上课时间</th><th>课后作业</th><th>休息日</th></tr>
<tr><td>练字</td><td>7.6-7.17</td><td>14:30-16:00</td><td>1h</td><td>无</td></tr>
<tr><td>豆神语文</td><td>7.13-7.25</td><td>9:00-10:30</td><td>1h</td><td>7/19</td></tr>
<tr><td>课外英语</td><td>8.1-8.29</td><td>8:30-11:30</td><td>3h</td><td>8/13·8/19·8/25</td></tr>
<tr><td>课外数学</td><td>8.15-8.27</td><td>13:30-15:30</td><td>2h</td><td>8/21</td></tr>
</table>
<div class="note">以上课程为<b>固定安排，不可变更</b>。上课前后需预留通勤和休息时间。</div>"""

    # Task list B: School tasks
    task_b = """
<table>
<tr><th>科目</th><th>任务</th><th>目标</th><th>计划完成</th></tr>
<tr><td>语文</td><td>8单元必背课文</td><td>每单元2h</td><td>7.18前</td></tr>
<tr><td>数学</td><td>8单元预习+练习</td><td>每单元≥2h</td><td>7.22前</td></tr>
<tr><td>英语</td><td>6单元单词+朗读背诵</td><td>每天1-1.5h</td><td>7.17前</td></tr>
</table>
<div class="note good">学校暑假作业本已完成，不再计入。所有预习任务<b>7月底前全部完成</b>。</div>"""

    # Task list C: Optional tasks
    task_c = """
<ul class="tl-l">
<li>完成 2-4 篇作文（见缝插针，不给定时间）</li>
<li>完成 1 次非遗实践活动</li>
<li>1 次旅行（7.26-7.31）</li>
<li>水上乐园 1-2 次（周末机动）</li>
<li>篮球训练 10 次（隔天·弹性·可取消）</li>
<li>每日课外阅读 30min（22:00-22:30）</li>
</ul>
<div class="note">以上为<b>机动任务</b>，不给定具体时间，根据每日情况灵活插入。</div>"""

    # Generate day cards
    day_cards = ''
    for m, d, wd, label, ck, blocks, must, flex, opt in DAYS:
        day_cards += gen_day_card(m, d, wd, label, ck, blocks, must, flex, opt)

    # Checklist
    checklist = """
<div class="cl">
  <div class="cl-c">
    <h3>📚 课内学习任务</h3>
    <div class="cl-i"><input type="checkbox"><span>语文 U1 古人谈读书+观书有感</span><span class="st">7/11</span></div>
    <div class="cl-i"><input type="checkbox"><span>语文 U2 园地二·成语</span><span class="st">7/12</span></div>
    <div class="cl-i"><input type="checkbox"><span>语文 U3 园地三·名言</span><span class="st">7/13</span></div>
    <div class="cl-i"><input type="checkbox"><span>语文 U4 古诗三首+少年中国说</span><span class="st">7/14</span></div>
    <div class="cl-i"><input type="checkbox"><span>语文 U5 园地四·成语</span><span class="st">7/15</span></div>
    <div class="cl-i"><input type="checkbox"><span>语文 U6 园地六·乞巧</span><span class="st">7/16</span></div>
    <div class="cl-i"><input type="checkbox"><span>语文 U7 古诗三首+白鹭</span><span class="st">7/17</span></div>
    <div class="cl-i"><input type="checkbox"><span>语文 U8 渔歌子+游子吟</span><span class="st">7/18</span></div>
    <div class="cl-i"><input type="checkbox"><span>数学 U1 预习+练习</span><span class="st">7/11</span></div>
    <div class="cl-i"><input type="checkbox"><span>数学 U2 预习+练习</span><span class="st">7/12</span></div>
    <div class="cl-i"><input type="checkbox"><span>数学 U3 预习+练习</span><span class="st">7/18</span></div>
    <div class="cl-i"><input type="checkbox"><span>数学 U4 预习+练习</span><span class="st">7/19</span></div>
    <div class="cl-i"><input type="checkbox"><span>数学 U5 预习+练习</span><span class="st">7/19</span></div>
    <div class="cl-i"><input type="checkbox"><span>数学 U6 预习+练习</span><span class="st">7/20</span></div>
    <div class="cl-i"><input type="checkbox"><span>数学 U7 预习+练习</span><span class="st">7/21</span></div>
    <div class="cl-i"><input type="checkbox"><span>数学 U8 预习+练习</span><span class="st">7/22</span></div>
    <div class="cl-i"><input type="checkbox"><span>英语 U1-U6 单词+朗读+背诵</span><span class="st">7/11-7/17</span></div>
  </div>
  <div class="cl-c">
    <h3>🎯 课外课程完成</h3>
    <div class="cl-i"><input type="checkbox"><span>练字课 12 天全勤</span><span class="st">7/6-7/17</span></div>
    <div class="cl-i"><input type="checkbox"><span>豆神语文课 12 天全勤</span><span class="st">7/13-7/25</span></div>
    <div class="cl-i"><input type="checkbox"><span>课外英语课 26 天全勤</span><span class="st">8/1-8/29</span></div>
    <div class="cl-i"><input type="checkbox"><span>课外数学课 12 天全勤</span><span class="st">8/15-8/27</span></div>
    <h3 style="margin-top:14px">📝 机动任务</h3>
    <div class="cl-i"><input type="checkbox"><span>作文 1</span><span class="st">见缝插针</span></div>
    <div class="cl-i"><input type="checkbox"><span>作文 2</span><span class="st">见缝插针</span></div>
    <div class="cl-i"><input type="checkbox"><span>作文 3</span><span class="st">见缝插针</span></div>
    <div class="cl-i"><input type="checkbox"><span>作文 4</span><span class="st">见缝插针</span></div>
    <div class="cl-i"><input type="checkbox"><span>非遗实践活动</span><span class="st">机动</span></div>
    <div class="cl-i"><input type="checkbox"><span>旅行 7.26-7.31</span><span class="st">6天</span></div>
    <div class="cl-i"><input type="checkbox"><span>水上乐园 1</span><span class="st">周末机动</span></div>
    <div class="cl-i"><input type="checkbox"><span>水上乐园 2</span><span class="st">周末机动</span></div>
    <div class="cl-i"><input type="checkbox"><span>篮球训练 10 次</span><span class="st">隔天·弹性</span></div>
    <div class="cl-i"><input type="checkbox"><span>每日阅读 30min 坚持</span><span class="st">全程</span></div>
  </div>
</div>"""

    # Key notes
    notes = """
<div class="note danger">⚠️ <b>8.15-8.27 地狱期</b>：每天英语3h+作业2.5h+数学2h+作业2h = 约9.5h被占满。仅保证阅读，不安排其他任务。所有预习务必7月底前完成。</div>
<div class="note good">✅ <b>7月是主战场</b>：语文8单元(7/18前) + 数学8单元(7/22前) + 英语6单元(7/17前) + 旅行(7/26-7/31)</div>
<div class="note">📋 <b>每日最低保证</b>：① 上午语文背诵+英语单词朗读 ② 下午数学预习 ③ 22:00-22:30 阅读</div>
<div class="note">🏀 <b>篮球弹性安排</b>：隔天1次，共10次。与课程冲突时优先课程，篮球可取消。豆神日先上课再打球，作业移至晚上。</div>
<div class="note">📝 <b>作文/非遗/水上乐园</b>为机动任务，不给定时间，利用空闲灵活插入。</div>"""

    # Overview
    overview = gen_overview()

    html = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>暑假详细月历表 v5</title>
<style>{CSS}</style>
</head>
<body>
<div class="wrap">

<div class="hdr">
  <h1>📅 杨子禺 2026 暑假详细月历表</h1>
  <div class="sub">7月11日 — 8月31日 · 共52天 · 深色主题 · 三列布局</div>
  <div class="lg">
    <span style="border-left:3px solid #f0883e;padding-left:6px">语文</span>
    <span style="border-left:3px solid #3fb950;padding-left:6px">英语</span>
    <span style="border-left:3px solid #a371f7;padding-left:6px">数学</span>
    <span style="border-left:3px solid #f85149;padding-left:6px">练字</span>
    <span style="border-left:3px solid #ff7b72;padding-left:6px">豆神</span>
    <span style="border-left:3px solid #ff6b6b;padding-left:6px">篮球</span>
    <span style="border-left:3px solid #3fb950;padding-left:6px">旅行</span>
    <span style="border-left:3px solid #58a6ff;padding-left:6px">阅读</span>
    <span style="border-left:3px solid #7d8590;padding-left:6px">机动</span>
  </div>
</div>

<div class="sec">
  <div class="sec-t">一、每日作息时间表</div>
  <div class="sec-sub">9:00开始学习 · 22:30就寝 · 上午语文+英语 · 下午数学 · 晚上作业+复习 · 22:00-22:30阅读</div>
  {routine}
</div>

<div class="sec">
  <div class="sec-t">二、任务清单</div>
  <div class="tl">
    <div class="tl-c">
      <h3 class="a">A. 课外固定课程（不可变更）</h3>
      {task_a}
    </div>
    <div class="tl-c">
      <h3 class="b">B. 课内学习任务</h3>
      {task_b}
    </div>
    <div class="tl-c">
      <h3 class="c">C. 机动任务清单</h3>
      {task_c}
    </div>
  </div>
</div>

<div class="sec">
  <div class="sec-t">三、月历总览</div>
  <div class="sec-sub">7月11日 — 8月31日 · 周末标黄 · 旅行标绿</div>
  {overview}
</div>

<div class="sec">
  <div class="sec-t">四、每日详细安排</div>
  <div class="sec-sub">每天分上午 / 下午 / 晚上三列 · 每段≥1h · 集中学习 · 语文英语放上午 · 数学放下午</div>
  {day_cards}
</div>

<div class="sec">
  <div class="sec-t">五、关键提醒</div>
  {notes}
</div>

<div class="sec">
  <div class="sec-t">六、完成清单检查</div>
  <div class="sec-sub">打印后逐项勾选 · 课内任务7月底前完成 · 课外课程全勤 · 机动任务灵活完成</div>
  {checklist}
</div>

</div>
</body>
</html>"""

    with open(OUT, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f'OK: {OUT}')
    print(f'Size: {len(html)} bytes')

if __name__ == '__main__':
    main()
