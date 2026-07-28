#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Main generator for calendar v4 - dark theme"""
import sys
sys.path.insert(0, r'C:\Users\ytf20\Desktop\杨子禺暑假')
from gen_cal_v4_data import *

def cc(cat):
    return COL.get(cat, COL['rest'])

def cn(cat):
    return CATS.get(cat, cat)

# ============ CSS ============
def gen_css():
    c = COL
    return f"""*{{box-sizing:border-box;margin:0;padding:0}}
body{{font-family:'PingFang SC','Microsoft YaHei',sans-serif;background:{c['bg']};color:{c['text']};line-height:1.6;font-size:14px}}
.container{{max-width:1500px;margin:0 auto;padding:20px}}
.hdr{{background:linear-gradient(135deg,#1a3a5c,#2d5a87,#1a3a5c);border:1px solid {c['border']};border-radius:12px;padding:24px 32px;margin-bottom:20px}}
.hdr h1{{font-size:24px;margin-bottom:6px}}
.hdr .sub{{color:{c['text2']};font-size:14px}}
.legend{{display:flex;flex-wrap:wrap;gap:8px;margin-top:12px}}
.legend span{{display:flex;align-items:center;gap:4px;font-size:12px;color:{c['text2']}}}
.legend i{{width:10px;height:10px;border-radius:3px;display:inline-block}}
.sec{{background:{c['card']};border:1px solid {c['border']};border-radius:10px;padding:20px 24px;margin-bottom:20px}}
.sec-t{{font-size:18px;font-weight:700;margin-bottom:14px;padding-bottom:10px;border-bottom:1px solid {c['border']};display:flex;align-items:center;gap:8px}}
.sec-t .n{{background:#2d5a87;width:26px;height:26px;border-radius:6px;display:flex;align-items:center;justify-content:center;font-size:14px}}
.sub-t{{font-size:15px;font-weight:600;color:{c['reading']};margin:16px 0 10px;padding-left:8px;border-left:3px solid {c['reading']}}}
/* routine */
.rt{{width:100%;border-collapse:collapse}}
.rt th{{background:{c['card2']};color:{c['text2']};padding:8px;text-align:left;font-size:12px;border:1px solid {c['border']}}}
.rt td{{padding:8px;border:1px solid {c['border2']};font-size:13px}}
.rt .tm{{color:{c['reading']};font-weight:600;white-space:nowrap}}
.rt .pd{{color:{c['text2']};font-weight:600}}
/* task cards */
.tg{{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin:10px 0}}
.tc{{background:{c['card2']};border:1px solid {c['border']};border-radius:8px;padding:14px;border-left:4px solid {c['border']}}}
.tc.ch{{border-left-color:{c['chinese']}}}
.tc.en{{border-left-color:{c['english']}}}
.tc.ma{{border-left-color:{c['math']}}}
.tc.ca{{border-left-color:{c['calligraphy']}}}
.tc.do{{border-left-color:{c['doushen']}}}
.tc.ot{{border-left-color:{c['heritage']}}}
.tc h4{{font-size:15px;margin-bottom:6px}}
.tc .mt{{color:{c['text2']};font-size:12px;margin-bottom:6px}}
.tc ul{{list-style:none}}
.tc li{{padding:3px 0;font-size:12px}}
.tc li b{{color:{c['text2']};font-weight:400}}
/* calendar */
.cg{{display:grid;grid-template-columns:repeat(7,1fr);gap:3px;background:{c['border2']};padding:3px;border-radius:8px;margin:10px 0}}
.ch{{background:{c['card2']};color:{c['text2']};text-align:center;padding:6px;font-size:12px;font-weight:600;border-radius:4px}}
.ch.we{{color:{c['calligraphy']}}}
.cc{{background:{c['card']};border-radius:4px;padding:5px;min-height:55px;font-size:10px}}
.cc.ep{{background:transparent}}
.cc.we{{background:{c['card2']}}}
.cc .dn{{font-size:13px;font-weight:700}}
.cc .e{{display:block;font-size:9px;padding:1px 3px;border-radius:2px;margin:1px 0}}
/* phase */
.ph{{background:{c['card2']};border:1px solid {c['border']};border-radius:8px;padding:12px 18px;margin:20px 0 12px;display:flex;align-items:center;gap:12px}}
.ph .pn{{background:#2d5a87;width:32px;height:32px;border-radius:8px;display:flex;align-items:center;justify-content:center;font-weight:700;font-size:15px}}
.ph .pt{{font-size:16px;font-weight:600}}
.ph .pd{{color:{c['text2']};font-size:13px;margin-left:auto}}
/* day card */
.dc{{background:{c['card']};border:1px solid {c['border']};border-radius:10px;margin-bottom:10px;overflow:hidden}}
.dch{{display:flex;align-items:center;padding:10px 16px;background:{c['card2']};border-bottom:1px solid {c['border']};gap:10px}}
.dch .dd{{font-size:15px;font-weight:700}}
.dch .dw{{font-size:12px;color:{c['text2']};padding:2px 8px;background:{c['border']};border-radius:4px}}
.dch .dw.we{{color:{c['calligraphy']};background:rgba(248,81,73,0.15)}}
.dch .dt{{font-size:12px;color:{c['text2']};margin-left:auto}}
.dcb{{padding:8px 16px}}
.tr{{display:flex;align-items:stretch;padding:4px 0;border-bottom:1px solid {c['border2']};gap:0}}
.tr:last-child{{border-bottom:none}}
.tr .tt{{width:90px;color:{c['reading']};font-size:12px;font-weight:600;flex-shrink:0;padding-top:2px}}
.tr .tb{{width:4px;border-radius:2px;flex-shrink:0;margin-right:10px}}
.tr .tc2{{flex:1;font-size:13px}}
.tr .tc2 .tn{{color:{c['text2']};font-size:11px;margin-left:6px}}
.tr .tc2 .tg2{{display:inline-block;padding:1px 6px;border-radius:3px;font-size:10px;margin-right:6px;font-weight:600}}
.pd2{{padding:4px 0;font-size:11px;color:{c['text3']};font-weight:600;letter-spacing:1px;border-top:1px dashed {c['border']};margin-top:4px}}
/* progress */
.pg{{display:grid;grid-template-columns:1fr 1fr;gap:16px;margin:10px 0}}
.pc{{background:{c['card2']};border:1px solid {c['border']};border-radius:8px;padding:14px}}
.pc h4{{font-size:14px;margin-bottom:8px}}
.pi{{display:flex;align-items:center;gap:6px;padding:3px 0;font-size:12px}}
.pi .ck{{width:16px;height:16px;border:1px solid {c['border']};border-radius:3px;flex-shrink:0}}
/* note */
.nt{{background:rgba(210,153,34,0.1);border:1px solid rgba(210,153,34,0.3);border-radius:6px;padding:10px 14px;margin:10px 0;font-size:12px}}
.nt.dg{{background:rgba(248,81,73,0.1);border-color:rgba(248,81,73,0.3)}}
.nt.gd{{background:rgba(63,185,80,0.1);border-color:rgba(63,185,80,0.3)}}
.nt b{{color:{c['essay']}}}
.nt.dg b{{color:{c['calligraphy']}}}
.nt.gd b{{color:{c['english']}}}"""

# ============ SECTIONS ============

def gen_legend():
    items = []
    for cat, name in CATS.items():
        items.append(f'<span><i style="background:{cc(cat)}"></i>{name}</span>')
    return f'<div class="legend">{"".join(items)}</div>'

def gen_routine():
    rows = [
        ('08:00','09:00','起床·洗漱·早餐','—','生活','准备一天'),
        ('09:00','12:30','上午学习时段','3.5h','学习','语文背诵+英语单词朗读 / 数学预习'),
        ('12:30','13:00','午餐','0.5h','生活','可利用时间听英语音频'),
        ('13:00','14:00','午休','1h','休息','保证充足午睡'),
        ('14:00','18:00','下午学习时段','4h','学习','数学预习+练习 / 其他任务'),
        ('16:00','16:30','休息·娱乐(可选)','30min','娱乐','观看游戏/视频·利用碎片时间'),
        ('18:00','19:30','晚餐·休息','1.5h','生活','可利用时间听英语音频'),
        ('19:30','22:00','晚上学习时段','2.5h','学习','作业+复习 / 自由(周六)'),
        ('22:00','22:30','课外阅读','30min','阅读','固定不变·每日必做'),
        ('22:30','—','就寝','—','休息','保证充足睡眠'),
    ]
    html = '<table class="rt"><tr><th>时间</th><th>时段</th><th>活动</th><th>时长</th><th>类型</th><th>说明</th></tr>'
    for tm, tm2, act, dur, typ, note in rows:
        cls = 'pd' if typ in ('生活','休息','娱乐','阅读') else ''
        html += f'<tr><td class="tm">{tm}</td><td class="tm">{tm2}</td><td>{act}</td><td>{dur}</td><td class="{cls}">{typ}</td><td style="color:{COL["text2"]};font-size:12px">{note}</td></tr>'
    html += '</table>'
    html += '<div class="nt"><b>核心原则：</b>上午记忆型（语文背诵+英语单词朗读），下午理解型（数学预习+练习），晚上巩固型（作业+复习）。每个学习块≥1h，同一项目连续几天集中完成，避免频繁切换。</div>'
    return html

def gen_tasks_fixed():
    c = COL
    cards = [
        ('ca','练字课','7.11-7.17','12天（已过4天）','14:30-16:00','2h/天','42h',[
            '日期：7.6(一)-7.17(五)，从7.11起剩余7天',
            '时间：下午14:30-16:00（1.5h课）',
            '课后作业：2h（当天完成）',
            '7.11-7.12为周末，7.13-7.17为工作日',
        ]),
        ('do','豆神语文','7.13-7.25','12天','9:00-10:30','1h/天','30h',[
            '日期：7.13(一)-7.25(六)，7.19(日)休息',
            '时间：上午9:00-10:30（1.5h课）',
            '课后作业：1h（当天完成，有篮球日移至晚上）',
            '7.25为最后一课',
        ]),
        ('en','课外英语','8.1-8.29','26天','8:30-11:30','3h/天','156h',[
            '日期：8.1(六)-8.29(六)',
            '时间：上午8:30-11:30（3h课）',
            '课后作业：3h（当天完成）',
            '休息日：8.13(四)、8.19(三)、8.25(一)',
            '学习内容：6个单元朗读+背诵+单词记忆',
        ]),
        ('ma','课外数学','8.15-8.27','12天','13:30-15:30','2h/天','48h',[
            '日期：8.15(六)-8.27(四)',
            '时间：下午13:30-15:30（2h课）',
            '课后作业：2h（当天完成）',
            '休息日：8.21(五)',
            '与英语课重叠期（8.15-8.27）为地狱期',
        ]),
    ]
    html = '<div class="tg">'
    for cls, name, dates, days, time, hw, total, items in cards:
        html += f'<div class="tc {cls}"><h4 style="color:{cc(cls.replace("ca","calligraphy").replace("do","doushen").replace("en","english").replace("ma","math"))}">{name}</h4>'
        html += f'<div class="mt">📅 {dates} · {days} · ⏰ {time} · 📝 作业{hw} · 总耗时{total}</div><ul>'
        for it in items:
            html += f'<li>• {it}</li>'
        html += '</ul></div>'
    html += '</div>'
    html += '<div class="nt dg"><b>不可变更：</b>以上4门课外课程时间固定，不可调整。所有其他任务必须围绕这些时间安排。8.15-8.27英语+数学同时上课期间（地狱期），每天10h被占满，仅保证22:00-22:30阅读，不安排其他学习任务。</div>'
    return html

def gen_tasks_school():
    c = COL
    cards = [
        ('ch','语文背诵','8个单元','每单元2h','16h',[
            '<b>U1</b> 古人谈读书 + 观书有感（7.11完成）',
            '<b>U2</b> 语文园地二·日积月累（7.12完成）',
            '<b>U3</b> 语文园地三·日积月累（7.13完成）',
            '<b>U4</b> 古诗三首：示儿/题临安邸/己亥杂诗（7.14完成）',
            '<b>U5</b> 少年中国说节选（7.15完成）',
            '<b>U6</b> 语文园地四·日积月累（7.16完成）',
            '<b>U7</b> 古诗三首：山居秋暝/枫桥夜泊/早春呈水部张十八员外（7.17完成）',
            '<b>U8</b> 白鹭 + 语文园地六/七/八（7.19完成）',
            '<b>复习</b> 7.21-7.22 综合复习+背诵检查',
        ]),
        ('ma','数学预习','8个单元','每单元3h+','24h+',[
            '<b>U1</b> 第一单元（7.11完成）',
            '<b>U2-U3</b> 集中3h完成（7.12完成）',
            '<b>U4</b> 7.18完成（豆神日·10:30-12:00+14:00-15:30）',
            '<b>U5-U6</b> 集中完成（7.19·豆神休息日）',
            '<b>U7</b> 7.20完成（豆神日·10:30-12:00+14:00-15:30）',
            '<b>U8</b> 7.20-7.21完成',
            '<b>复习</b> 7.22 综合复习U1-U8',
            '原则：每单元预习2h+练习1h，集中连续完成',
        ]),
        ('en','英语预习','6个单元','每单元2h','12h',[
            '<b>U1</b> 单词+朗读（7.11-7.12）',
            '<b>U2</b> 单词+朗读（7.13-7.14）',
            '<b>U3</b> 单词+朗读（7.15-7.16）',
            '<b>U4</b> 单词+朗读（7.19）',
            '<b>U5</b> 单词+朗读（7.20-7.21）',
            '<b>U6</b> 单词+朗读+总复习（7.21-7.22）',
            '原则：每天1-1.5h，单词+朗读合并进行',
            '利用午餐/晚餐时间听英语音频',
        ]),
    ]
    html = '<div class="tg">'
    for cls, name, units, per, total, items in cards:
        color = cc({'ch':'chinese','ma':'math','en':'english'}[cls])
        html += f'<div class="tc {cls}"><h4 style="color:{color}">{name}</h4>'
        html += f'<div class="mt">📚 {units} · ⏱ {per}/单元 · 总耗时{total}</div><ul>'
        for it in items:
            html += f'<li>{it}</li>'
        html += '</ul></div>'
    html += '</div>'
    html += '<div class="nt gd"><b>7月25日前全部完成：</b>语文8单元+数学8单元+英语6单元的所有预习任务在7.25前完成。7.26-7.31旅行无忧，8月专注课外课程。</div>'
    return html

def gen_tasks_other():
    c = COL
    cards = [
        ('ot','作文','2-4篇','每篇1.5-2h','6-8h',[
            '<b>作文1</b> 7.22(三) 10:30-12:00',
            '<b>作文2</b> 7.23(四) 14:00-15:30',
            '<b>作文3</b> 7.24(五) 14:00-16:00',
            '<b>作文4</b> 8.10(一) 19:30-21:00（可选）',
        ]),
        ('ot','非遗实践','1次','半天','3h',[
            '<b>准备</b> 7.23(四) 16:00-18:00 选题+材料',
            '<b>实践</b> 7.24(五) 10:30-12:00',
            '主题待定（可结合旅行中的文化体验）',
        ]),
        ('ot','旅行','1次','约6天','—',[
            '<b>时间</b> 7.26(日)-7.31(五)',
            '所有预习已完成，无忧旅行',
            '保持每天22:00-22:30阅读习惯',
            '可结合非遗实践体验',
        ]),
        ('ot','水上乐园','1-2次','每次半天','—',[
            '<b>第1次</b> 8.8(六) 16:00-18:00（英语课后）',
            '<b>第2次</b> 8.30(日) 09:00-18:00（全天）',
            '安排在周末，不冲突课程',
        ]),
        ('ot','篮球训练','10次（弹性）','每次1.5h','15h',[
            '<b>7月</b> 7.11/7.13/7.15/7.17/7.19/7.23/7.25',
            '<b>8月</b> 8.13/8.19/8.25（英语休息日）',
            '弹性安排，时间紧张可取消',
            '时间：10:30-12:00（豆神课后直接去）',
        ]),
        ('ot','每日娱乐','每天','30min','—',[
            '下午16:00-16:30 观看游戏/视频',
            '利用碎片时间，不占用学习时段',
            '地狱期(8.15-8.27)可取消',
            '周六晚上自由时间可适当延长',
        ]),
    ]
    html = '<div class="tg">'
    for cls, name, qty, per, total, items in cards:
        html += f'<div class="tc {cls}"><h4 style="color:{c["heritage"]}">{name}</h4>'
        html += f'<div class="mt">📋 {qty} · ⏱ {per} · 总耗时{total}</div><ul>'
        for it in items:
            html += f'<li>{it}</li>'
        html += '</ul></div>'
    html += '</div>'
    return html

def gen_calendar():
    """Generate monthly calendar overview"""
    html = ''
    for month, start_d, end_d, label in [(7,11,31,'7月'),(8,1,31,'8月')]:
        html += f'<div class="sub-t">{label}（{month}.{start_d}-{month}.{end_d}）</div>'
        html += '<div class="cg">'
        for i, wn in enumerate(WD_NAMES):
            cls = 'we' if i >= 5 else ''
            html += f'<div class="ch {cls}">周{wn}</div>'
        # Calculate offset for first day
        first_wd = wd(month, 1)
        for i in range(first_wd):
            html += '<div class="cc ep"></div>'
        for d in range(1, end_d+1):
            if month == 7 and d < 11:
                html += '<div class="cc ep"></div>'
                continue
            w = wd(month, d)
            we_cls = 'we' if w >= 5 else ''
            # Find this day's events
            day_data = None
            for dm, dd, dp, dt, blocks in DAYS:
                if dm == month and dd == d:
                    day_data = (dp, dt, blocks)
                    break
            if day_data:
                dp, dt, blocks = day_data
                # Collect unique categories
                cats_seen = set()
                evts = []
                for s, e, title, cat, note in blocks:
                    if cat in ('rest','meal','free') and cat not in cats_seen:
                        continue
                    if cat not in cats_seen:
                        cats_seen.add(cat)
                        short = cn(cat)
                        evts.append(f'<span class="e" style="background:{cc(cat)};color:#0d1117">{short}</span>')
                evts_html = ''.join(evts[:4])
                html += f'<div class="cc {we_cls}"><div class="dn">{d}</div><div style="font-size:9px;color:{COL["text2"]}">{dt[:8]}</div><div class="evts">{evts_html}</div></div>'
            else:
                html += f'<div class="cc {we_cls}"><div class="dn">{d}</div></div>'
        html += '</div>'
    return html

def gen_phase_header(phase_num):
    dates, title, desc = PHASES[phase_num]
    return f'<div class="ph"><div class="pn">{phase_num}</div><div class="pt">{title}</div><div class="pd">{dates} · {desc}</div></div>'

def is_period_boundary(prev_time, curr_time):
    """Check if we crossed a period boundary"""
    if not prev_time:
        return True
    # Morning: before 12:30
    # Afternoon: 14:00-18:00
    # Evening: after 19:30
    def get_period(t):
        if not t or t == '—':
            return None
        h = int(t.split(':')[0])
        if h < 12:
            return '上午'
        elif h < 14:
            return '午间'
        elif h < 18:
            return '下午'
        else:
            return '晚上'
    return get_period(prev_time) != get_period(curr_time) and get_period(curr_time) is not None

def gen_day_card(m, d, phase, dtype, blocks):
    w = wd(m, d)
    wn = WD_NAMES[w]
    we_cls = 'we' if w >= 5 else ''
    html = f'<div class="dc"><div class="dch"><span class="dd">{m}月{d}日</span><span class="dw {we_cls}">周{wn}</span><span class="dt">{dtype}</span></div><div class="dcb">'
    
    prev_period = None
    for start, end, title, cat, note in blocks:
        # Determine period
        if start and start != '—':
            h = int(start.split(':')[0])
            if h < 12:
                period = '上午'
            elif h < 14:
                period = '午间'
            elif h < 18:
                period = '下午'
            else:
                period = '晚上'
        else:
            period = None
        
        if period and period != prev_period and period in ('上午','下午','晚上'):
            html += f'<div class="pd2">━━ {period} ━━</div>'
            prev_period = period
        
        color = cc(cat)
        time_str = f'{start}-{end}' if end and end != '—' else start
        note_html = f'<span class="tn">{note}</span>' if note else ''
        html += f'<div class="tr"><div class="tt">{time_str}</div><div class="tb" style="background:{color}"></div><div class="tc2"><span class="tg2" style="background:{color};color:#0d1117">{cn(cat)}</span>{title}{note_html}</div></div>'
    
    html += '</div></div>'
    return html

def gen_progress():
    c = COL
    html = '<div class="pg">'
    
    # Chinese
    html += f'<div class="pc"><h4 style="color:{c["chinese"]}">语文背诵进度（8单元）</h4>'
    for i in range(1,9):
        html += f'<div class="pi"><div class="ck"></div>第{i}单元</div>'
    html += '</div>'
    
    # Math
    html += f'<div class="pc"><h4 style="color:{c["math"]}">数学预习进度（8单元）</h4>'
    for i in range(1,9):
        html += f'<div class="pi"><div class="ck"></div>第{i}单元</div>'
    html += '</div>'
    
    # English
    html += f'<div class="pc"><h4 style="color:{c["english"]}">英语预习进度（6单元）</h4>'
    for i in range(1,7):
        html += f'<div class="pi"><div class="ck"></div>第{i}单元</div>'
    html += '</div>'
    
    # Other
    html += f'<div class="pc"><h4 style="color:{c["heritage"]}">其他任务进度</h4>'
    others = ['作文1','作文2','作文3','作文4(可选)','非遗实践','旅行','水上乐园1','水上乐园2','篮球10次','每日阅读']
    for o in others:
        html += f'<div class="pi"><div class="ck"></div>{o}</div>'
    html += '</div>'
    
    html += '</div>'
    return html

# ============ ASSEMBLE ============

def main():
    html = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>暑假详细月历表 2026</title>
<style>{gen_css()}</style>
</head>
<body>
<div class="container">

<div class="hdr">
  <h1>📅 杨子禺 2026暑假详细月历表</h1>
  <div class="sub">7月11日 — 8月31日 · 共52天 · 深色版 v4 · 集中型学习方案</div>
  {gen_legend()}
</div>

<!-- ===== 一、每日作息时间表 ===== -->
<div class="sec">
  <div class="sec-t"><span class="n">1</span>每日作息时间表</div>
  {gen_routine()}
</div>

<!-- ===== 二、任务清单 ===== -->
<div class="sec">
  <div class="sec-t"><span class="n">2</span>任务清单</div>
  <div class="sub-t">A. 课外固定课程（不可变更）</div>
  {gen_tasks_fixed()}
  <div class="sub-t">B. 课内学习任务（7月完成）</div>
  {gen_tasks_school()}
  <div class="sub-t">C. 其他活动任务</div>
  {gen_tasks_other()}
</div>

<!-- ===== 三、月历总览 ===== -->
<div class="sec">
  <div class="sec-t"><span class="n">3</span>月历总览</div>
  {gen_calendar()}
</div>

<!-- ===== 四、每日详细安排 ===== -->
<div class="sec">
  <div class="sec-t"><span class="n">4</span>每日详细安排</div>
"""
    
    # Group days by phase
    current_phase = None
    for m, d, phase, dtype, blocks in DAYS:
        if phase != current_phase:
            html += gen_phase_header(phase)
            current_phase = phase
        html += gen_day_card(m, d, phase, dtype, blocks)
    
    # Progress tracking
    html += f"""
</div>

<!-- ===== 五、进度追踪 ===== -->
<div class="sec">
  <div class="sec-t"><span class="n">5</span>进度追踪</div>
  {gen_progress()}
</div>

<!-- ===== 六、关键提醒 ===== -->
<div class="sec">
  <div class="sec-t"><span class="n">6</span>关键提醒</div>
  <div class="nt gd"><b>✅ 最低保证清单：</b>①每天22:00-22:30阅读30min ②每天英语单词+朗读≥1h（8月地狱期除外）③7.25前完成所有预习</div>
  <div class="nt dg"><b>⚠️ 地狱期 8.15-8.27：</b>每天英语3h+作业3h+数学2h+作业2h=10h被占满。仅保证阅读，不安排其他学习任务。英语休息日(8.19/8.25)和数学休息日(8.21)可喘息。</div>
  <div class="nt"><b>📌 篮球弹性：</b>共安排10次，时间紧张可取消。豆神日先上课(9:00-10:30)再篮球(10:30-12:00)，豆神作业移至晚上。8月篮球仅在英语休息日安排。</div>
  <div class="nt"><b>📌 集中学习原则：</b>同一项目连续几天完成（如数学U2+U3集中7.12一天完成），避免每天频繁切换科目。上午记忆型，下午理解型，晚上巩固型。</div>
  <div class="nt"><b>📌 周末策略：</b>周六下午+晚上留出自由时间，周日下午可安排复习。旅行安排在7.26-7.31（全暑假唯一无课窗口期）。</div>
</div>

</div>
</body>
</html>"""
    
    out_path = r'C:\Users\ytf20\Desktop\杨子禺暑假\暑假详细月历表.html'
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f'Generated: {out_path}')
    print(f'Total days: {len(DAYS)}')
    print(f'File size: {len(html)} bytes')

if __name__ == '__main__':
    main()
