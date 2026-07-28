#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate summer calendar HTML"""

chinese_units = {
    1: '古人谈读书 + 观书有感',
    2: '语文园地二（成语积累）',
    3: '语文园地三（名言警句）',
    4: '古诗三首（示儿·题临安邸·己亥杂诗）+ 少年中国说节选',
    5: '语文园地四（成语积累）',
    6: '语文园地六·乞巧',
    7: '古诗三首（山居秋暝·枫桥夜泊·早春呈水部张十八员外）+ 白鹭',
    8: '渔歌子 + 游子吟',
}

math_units = {
    1: '小数乘法', 2: '位置', 3: '小数除法', 4: '可能性',
    5: '简易方程', 6: '多边形的面积', 7: '数学广角—植树问题', 8: '总复习',
}

# (month, day, weekday, type, params)
days = [
    (7,11,'六','A',{'m':1,'c':1}),
    (7,12,'日','B',{'m':2,'c':2}),
    (7,13,'一','C',{}),
    (7,14,'二','D',{'m':3}),
    (7,15,'三','C',{}),
    (7,16,'四','D',{'m':4}),
    (7,17,'五','C',{}),
    (7,18,'六','F',{'m':5,'c':3}),
    (7,19,'日','G',{'m':6,'c':4}),
    (7,20,'一','F',{'m':7,'c':5}),
    (7,21,'二','E',{'c':6}),
    (7,22,'三','F',{'m':8,'c':7}),
    (7,23,'四','E',{'c':8}),
    (7,24,'五','F',{'rev':1}),
    (7,25,'六','E',{'rev':1}),
    (7,26,'日','H',{}),
    (7,27,'一','H',{'bb':1}),
    (7,28,'二','H',{}),
    (7,29,'三','H',{'bb':1}),
    (7,30,'四','H',{}),
    (7,31,'五','H',{}),
    (8,1,'六','I',{}),
    (8,2,'日','I',{}),
    (8,3,'一','I',{}),
    (8,4,'二','I',{}),
    (8,5,'三','I',{}),
    (8,6,'四','I',{}),
    (8,7,'五','I',{}),
    (8,8,'六','I',{}),
    (8,9,'日','I',{}),
    (8,10,'一','I',{}),
    (8,11,'二','I',{}),
    (8,12,'三','I',{}),
    (8,13,'四','JB',{}),
    (8,14,'五','I',{}),
    (8,15,'六','K',{}),
    (8,16,'日','K',{}),
    (8,17,'一','K',{}),
    (8,18,'二','K',{}),
    (8,19,'三','MB',{}),
    (8,20,'四','K',{}),
    (8,21,'五','L',{}),
    (8,22,'六','K',{}),
    (8,23,'日','K',{}),
    (8,24,'一','K',{}),
    (8,25,'二','M',{}),
    (8,26,'三','K',{}),
    (8,27,'四','K',{}),
    (8,28,'五','I',{}),
    (8,29,'六','I',{}),
    (8,30,'日','O',{}),
    (8,31,'一','O',{}),
]

def S(time, act, cat):
    return (time, act, cat)

LIFE = 'life'; REST = 'rest'; MATH = 'math'; CH = 'chinese'; ENG = 'english'
HW = 'hw'; BB = 'basket'; TRAVEL = 'travel'; FREE = 'free'; READ = 'read'

def gen(t, p):
    m = p.get('m'); c = p.get('c'); rev = p.get('rev'); bb = p.get('bb')
    mtxt = f'数学预习 第{m}单元：{math_units[m]}' if m else None
    ctxt = f'语文背诵 第{c}单元：{chinese_units[c]}' if c else None

    if t == 'A':  # 练字+篮球(无豆神)
        return [
            S('8:00-8:30','起床洗漱',LIFE),
            S('8:30-10:30',mtxt or '自由学习(2h)',MATH),
            S('10:30-12:00','篮球训练(1.5h)',BB),
            S('12:00-12:30','休息换衣',REST),
            S('12:30-13:00','午餐',LIFE), S('13:00-14:00','午休',REST),
            S('14:00-14:30','英语单词+朗读(30min)',ENG),
            S('14:30-16:00','练字课',CH), S('16:00-18:00','练字作业(2h)',HW),
            S('18:00-19:30','晚餐+休息',LIFE),
            S('19:30-21:30',ctxt or '语文复习(2h)',CH),
            S('21:30-22:00','自由活动',FREE), S('22:00-22:30','阅读',READ),
            S('22:30','就寝',LIFE),
        ]
    if t == 'B':  # 练字only(周末缓冲)
        return [
            S('8:00-8:30','起床洗漱',LIFE),
            S('8:30-10:30',mtxt or '自由学习(2h)',MATH),
            S('10:30-11:00','英语单词(30min)',ENG),
            S('11:00-11:30','英语朗读(30min)',ENG),
            S('11:30-12:30','自由活动',FREE),
            S('12:30-13:00','午餐',LIFE), S('13:00-14:00','午休',REST),
            S('14:00-14:30','自由休息',FREE),
            S('14:30-16:00','练字课',CH), S('16:00-18:00','练字作业(2h)',HW),
            S('18:00-19:30','晚餐+休息',LIFE),
            S('19:30-21:30',ctxt or '语文复习(2h)',CH),
            S('21:30-22:00','自由活动',FREE), S('22:00-22:30','阅读',READ),
            S('22:30','就寝',LIFE),
        ]
    if t == 'C':  # 豆神+练字+篮球
        return [
            S('8:00-8:30','起床洗漱',LIFE),
            S('8:30-9:00','英语单词(30min)',ENG),
            S('9:00-10:30','豆神语文课',CH),
            S('10:30-12:00','篮球训练(1.5h)',BB),
            S('12:00-12:30','休息换衣',REST),
            S('12:30-13:00','午餐',LIFE), S('13:00-14:00','午休',REST),
            S('14:00-14:30','英语朗读(30min)',ENG),
            S('14:30-16:00','练字课',CH), S('16:00-18:00','练字作业(2h)',HW),
            S('18:00-19:30','晚餐+休息',LIFE),
            S('19:30-20:30','豆神作业(1h)',HW),
            S('20:30-22:00','语文背诵复习/数学练习(1.5h)',CH),
            S('22:00-22:30','阅读',READ), S('22:30','就寝',LIFE),
        ]
    if t == 'D':  # 豆神+练字(无篮球)
        return [
            S('8:00-8:30','起床洗漱',LIFE),
            S('8:30-9:00','英语单词(30min)',ENG),
            S('9:00-10:30','豆神语文课',CH),
            S('10:30-12:30',mtxt or '自由学习(2h)',MATH),
            S('12:30-13:00','午餐',LIFE), S('13:00-14:00','午休',REST),
            S('14:00-14:30','英语朗读(30min)',ENG),
            S('14:30-16:00','练字课',CH), S('16:00-18:00','练字作业(2h)',HW),
            S('18:00-19:30','晚餐+休息',LIFE),
            S('19:30-20:30','豆神作业(1h)',HW),
            S('20:30-22:00','语文背诵复习(1.5h)',CH),
            S('22:00-22:30','阅读',READ), S('22:30','就寝',LIFE),
        ]
    if t == 'E':  # 豆神+篮球(无练字)
        aft = ctxt or ('总复习' if rev else '自由学习(2h)')
        return [
            S('8:00-8:30','起床洗漱',LIFE),
            S('8:30-9:00','英语单词(30min)',ENG),
            S('9:00-10:30','豆神语文课',CH),
            S('10:30-12:00','篮球训练(1.5h)',BB),
            S('12:00-12:30','休息换衣',REST),
            S('12:30-13:00','午餐',LIFE), S('13:00-14:00','午休',REST),
            S('14:00-16:00',aft,CH if c else FREE),
            S('16:00-17:00','英语朗读+复习(1h)',ENG),
            S('17:00-18:00','自由活动',FREE),
            S('18:00-19:30','晚餐+休息',LIFE),
            S('19:30-20:30','豆神作业(1h)',HW),
            S('20:30-22:00','自由/复习(1.5h)',FREE),
            S('22:00-22:30','阅读',READ), S('22:30','就寝',LIFE),
        ]
    if t == 'F':  # 豆神only
        morn = mtxt or ('总复习' if rev else '自由学习(2h)')
        aft = ctxt or ('总复习' if rev else '自由学习(2h)')
        return [
            S('8:00-8:30','起床洗漱',LIFE),
            S('8:30-9:00','英语单词(30min)',ENG),
            S('9:00-10:30','豆神语文课',CH),
            S('10:30-12:30',morn,MATH if m else FREE),
            S('12:30-13:00','午餐',LIFE), S('13:00-14:00','午休',REST),
            S('14:00-16:00',aft,CH if c else FREE),
            S('16:00-17:00','英语朗读(30min)+复习',ENG),
            S('17:00-18:00','自由活动',FREE),
            S('18:00-19:30','晚餐+休息',LIFE),
            S('19:30-20:30','豆神作业(1h)',HW),
            S('20:30-22:00','自由/复习(1.5h)',FREE),
            S('22:00-22:30','阅读',READ), S('22:30','就寝',LIFE),
        ]
    if t == 'G':  # 篮球only(豆神休息日)
        return [
            S('8:00-8:30','起床洗漱',LIFE),
            S('8:30-10:30',mtxt or '自由学习(2h)',MATH),
            S('10:30-12:00','篮球训练(1.5h)',BB),
            S('12:00-12:30','休息换衣',REST),
            S('12:30-13:00','午餐',LIFE), S('13:00-14:00','午休',REST),
            S('14:00-16:00',ctxt or '自由学习(2h)',CH),
            S('16:00-17:00','英语单词+朗读(1h)',ENG),
            S('17:00-18:00','自由活动',FREE),
            S('18:00-19:30','晚餐+休息',LIFE),
            S('19:30-22:00','自由/复习(2.5h)',FREE),
            S('22:00-22:30','阅读',READ), S('22:30','就寝',LIFE),
        ]
    if t == 'H':  # 旅行
        base = [
            S('8:00-8:30','起床洗漱',LIFE),
            S('8:30-9:00','英语单词(30min)',ENG),
            S('9:00-12:30','旅行活动',TRAVEL),
            S('12:30-13:00','午餐',LIFE), S('13:00-14:00','午休',REST),
            S('14:00-14:30','英语朗读(30min)',ENG),
            S('14:30-18:00','旅行活动',TRAVEL),
            S('18:00-19:30','晚餐+休息',LIFE),
            S('19:30-22:00','自由/日记/复习',FREE),
            S('22:00-22:30','阅读',READ), S('22:30','就寝',LIFE),
        ]
        if bb:
            base = [
                S('8:00-8:30','起床洗漱',LIFE),
                S('8:30-10:30','自由/旅行',TRAVEL),
                S('10:30-12:00','篮球训练(视情况)',BB),
                S('12:00-12:30','休息',REST),
                S('12:30-13:00','午餐',LIFE), S('13:00-14:00','午休',REST),
                S('14:00-14:30','英语朗读(30min)',ENG),
                S('14:30-18:00','旅行活动',TRAVEL),
                S('18:00-19:30','晚餐+休息',LIFE),
                S('19:30-22:00','自由/日记',FREE),
                S('22:00-22:30','阅读',READ), S('22:30','就寝',LIFE),
            ]
        return base
    if t in ('I','N'):  # 英语单课
        return [
            S('8:00-8:30','起床洗漱',LIFE),
            S('8:30-11:30','英语课(3h)',ENG),
            S('11:30-12:30','休息',REST),
            S('12:30-13:00','午餐',LIFE), S('13:00-14:00','午休',REST),
            S('14:00-17:00','英语课外作业(3h)',HW),
            S('17:00-18:00','自由活动',FREE),
            S('18:00-19:30','晚餐+休息',LIFE),
            S('19:30-20:00','英语单词(30min)',ENG),
            S('20:00-20:30','英语朗读(30min)',ENG),
            S('20:30-22:00','自由/阅读(1.5h)',FREE),
            S('22:00-22:30','阅读',READ), S('22:30','就寝',LIFE),
        ]
    if t == 'JB':  # 英语休息+篮球
        return [
            S('8:00-8:30','起床洗漱',LIFE),
            S('8:30-10:30','自由学习/复习(2h)',FREE),
            S('10:30-12:00','篮球训练(1.5h)',BB),
            S('12:00-12:30','休息换衣',REST),
            S('12:30-13:00','午餐',LIFE), S('13:00-14:00','午休',REST),
            S('14:00-16:00','自由学习(2h)',FREE),
            S('16:00-18:00','自由活动',FREE),
            S('18:00-19:30','晚餐+休息',LIFE),
            S('19:30-20:00','英语单词(30min)',ENG),
            S('20:00-20:30','英语朗读(30min)',ENG),
            S('20:30-22:00','自由(1.5h)',FREE),
            S('22:00-22:30','阅读',READ), S('22:30','就寝',LIFE),
        ]
    if t == 'J':  # 英语休息(无篮球)
        return [
            S('8:00-8:30','起床洗漱',LIFE),
            S('8:30-10:30','自由学习/复习(2h)',FREE),
            S('10:30-12:30','自由活动',FREE),
            S('12:30-13:00','午餐',LIFE), S('13:00-14:00','午休',REST),
            S('14:00-16:00','自由学习(2h)',FREE),
            S('16:00-18:00','自由活动',FREE),
            S('18:00-19:30','晚餐+休息',LIFE),
            S('19:30-20:00','英语单词(30min)',ENG),
            S('20:00-20:30','英语朗读(30min)',ENG),
            S('20:30-22:00','自由(1.5h)',FREE),
            S('22:00-22:30','阅读',READ), S('22:30','就寝',LIFE),
        ]
    if t == 'K':  # 英语+数学(地狱模式)
        return [
            S('8:00-8:30','起床洗漱',LIFE),
            S('8:30-11:30','英语课(3h)',ENG),
            S('11:30-12:30','英语课外作业Part1(1h)',HW),
            S('12:30-13:00','午餐',LIFE), S('13:00-13:30','短休',REST),
            S('13:30-15:30','数学课(2h)',MATH),
            S('15:30-17:30','数学课外作业(2h)',HW),
            S('17:30-18:00','休息',REST),
            S('18:00-19:30','晚餐+休息',LIFE),
            S('19:30-21:00','英语课外作业Part2(1.5h)',HW),
            S('21:00-21:30','英语单词+朗读(30min)',ENG),
            S('21:30-22:00','自由/休息',FREE),
            S('22:00-22:30','阅读',READ), S('22:30','就寝',LIFE),
        ]
    if t == 'L':  # 数学休息(仅英语)
        return [
            S('8:00-8:30','起床洗漱',LIFE),
            S('8:30-11:30','英语课(3h)',ENG),
            S('11:30-12:30','休息',REST),
            S('12:30-13:00','午餐',LIFE), S('13:00-14:00','午休',REST),
            S('14:00-17:00','英语课外作业(3h)',HW),
            S('17:00-18:00','自由活动',FREE),
            S('18:00-19:30','晚餐+休息',LIFE),
            S('19:30-20:00','英语单词(30min)',ENG),
            S('20:00-20:30','英语朗读(30min)',ENG),
            S('20:30-22:00','自由/阅读(1.5h)',FREE),
            S('22:00-22:30','阅读',READ), S('22:30','就寝',LIFE),
        ]
    if t == 'M':  # 英语休息+数学
        return [
            S('8:00-8:30','起床洗漱',LIFE),
            S('8:30-10:30','自由/复习(2h)',FREE),
            S('10:30-12:30','自由活动',FREE),
            S('12:30-13:00','午餐',LIFE), S('13:00-13:30','短休',REST),
            S('13:30-15:30','数学课(2h)',MATH),
            S('15:30-17:30','数学课外作业(2h)',HW),
            S('17:30-18:00','休息',REST),
            S('18:00-19:30','晚餐+休息',LIFE),
            S('19:30-20:00','英语单词(30min)',ENG),
            S('20:00-20:30','英语朗读(30min)',ENG),
            S('20:30-22:00','自由(1.5h)',FREE),
            S('22:00-22:30','阅读',READ), S('22:30','就寝',LIFE),
        ]
    if t == 'MB':  # 英语休息+篮球+数学
        return [
            S('8:00-8:30','起床洗漱',LIFE),
            S('8:30-10:30','自由/复习(2h)',FREE),
            S('10:30-12:00','篮球训练(1.5h)',BB),
            S('12:00-12:30','休息换衣',REST),
            S('12:30-13:00','午餐',LIFE), S('13:00-13:30','短休',REST),
            S('13:30-15:30','数学课(2h)',MATH),
            S('15:30-17:30','数学课外作业(2h)',HW),
            S('17:30-18:00','休息',REST),
            S('18:00-19:30','晚餐+休息',LIFE),
            S('19:30-20:00','英语单词(30min)',ENG),
            S('20:00-20:30','英语朗读(30min)',ENG),
            S('20:30-22:00','自由(1.5h)',FREE),
            S('22:00-22:30','阅读',READ), S('22:30','就寝',LIFE),
        ]
    if t == 'O':  # 自由
        return [
            S('8:00-8:30','起床洗漱',LIFE),
            S('8:30-12:30','自由活动',FREE),
            S('12:30-13:00','午餐',LIFE), S('13:00-14:00','午休',REST),
            S('14:00-18:00','自由活动',FREE),
            S('18:00-19:30','晚餐+休息',LIFE),
            S('19:30-22:00','自由/准备开学',FREE),
            S('22:00-22:30','阅读',READ), S('22:30','就寝',LIFE),
        ]
    return []

CAT_CSS = {
    LIFE: 'background:#6b7280;color:#fff;',
    REST: 'background:#e5e7eb;color:#4b5563;',
    MATH: 'background:#8b5cf6;color:#fff;',
    CH:   'background:#f97316;color:#fff;',
    ENG:  'background:#22c55e;color:#fff;',
    HW:   'background:#eab308;color:#1f2937;',
    BB:   'background:#ef4444;color:#fff;',
    TRAVEL:'background:#10b981;color:#fff;',
    FREE: 'background:#d1d5db;color:#374151;',
    READ: 'background:#3b82f6;color:#fff;',
}

CAT_NAME = {
    LIFE:'生活', REST:'休息', MATH:'数学', CH:'语文', ENG:'英语',
    HW:'作业', BB:'篮球', TRAVEL:'旅行', FREE:'自由', READ:'阅读',
}

TYPE_NAMES = {
    'A':'练字+篮球','B':'练字(周末)','C':'豆神+练字+篮球','D':'豆神+练字',
    'E':'豆神+篮球','F':'豆神only','G':'篮球(豆神休)','H':'旅行',
    'I':'英语单课','J':'英语休','JB':'英语休+篮球','K':'英语+数学(地狱)',
    'L':'数学休(仅英语)','M':'英语休+数学','MB':'英语休+篮球+数学','O':'自由',
    'N':'英语收尾',
}

def is_weekend(wd):
    return wd in ('六','日')

def gen_day_summary(d):
    mo, da, wd, t, p = d
    sched = gen(t, p)
    # Extract key events for compact view
    events = []
    for time, act, cat in sched:
        if cat in (MATH, CH, ENG, HW, BB, TRAVEL):
            short = act[:12] if len(act) > 12 else act
            events.append(f'<span class="mini-evt" style="{CAT_CSS[cat]}">{short}</span>')
    type_name = TYPE_NAMES.get(t, t)
    weekend_cls = ' weekend' if is_weekend(wd) else ''
    return f'''<div class="cal-day{weekend_cls}">
        <div class="cal-date">{mo}/{da} <span class="cal-wd">{wd}</span></div>
        <div class="cal-type">{type_name}</div>
        <div class="cal-evts">{''.join(events)}</div>
      </div>'''

def gen_day_detail(d, idx):
    mo, da, wd, t, p = d
    sched = gen(t, p)
    type_name = TYPE_NAMES.get(t, t)
    weekend_cls = ' weekend' if is_weekend(wd) else ''
    today_cls = ' today' if (mo == 7 and da == 11 and idx == 0) else ''

    # Group by period
    morning = []; afternoon = []; evening = []; other = []
    for time, act, cat in sched:
        # Parse start hour
        parts = time.split('-')
        start = parts[0].strip()
        if ':' in start:
            h = int(start.split(':')[0])
        elif start == '22:30':
            h = 23
        else:
            h = 0
        row = f'<tr><td class="td-time">{time}</td><td class="td-act"><span class="cat-tag" style="{CAT_CSS[cat]}">{CAT_NAME[cat]}</span> {act}</td></tr>'
        if 8 <= h < 13:
            morning.append(row)
        elif 14 <= h < 19:
            afternoon.append(row)
        elif 19 <= h <= 23:
            evening.append(row)
        else:
            other.append(row)

    def period_table(title, rows, cls):
        if not rows:
            return ''
        return f'<div class="period {cls}"><div class="period-title">{title}</div><table class="slot-table"><tbody>{"".join(rows)}</tbody></table></div>'

    # Generate text summary
    summary_parts = []
    for time, act, cat in sched:
        if cat in (MATH, CH, ENG, HW, BB, TRAVEL) and 'Part' not in act:
            summary_parts.append(f'{time} {act}')
    summary = '；'.join(summary_parts[:6])
    if len(summary_parts) > 6:
        summary += f'；等{len(summary_parts)}项'

    return f'''<div class="day-card{weekend_cls}{today_cls}" id="day-{mo}-{da}">
        <div class="day-card-header">
          <span class="dc-date">{mo}月{da}日</span>
          <span class="dc-wd">星期{wd}</span>
          <span class="dc-type">{type_name}</span>
        </div>
        <div class="periods">
          {period_table('上午 8:30-12:30', morning, 'morning')}
          {period_table('下午 14:00-18:00', afternoon, 'afternoon')}
          {period_table('晚上 19:30-22:30', evening, 'evening')}
        </div>
        <div class="day-summary"><b>当日说明：</b>{summary}</div>
      </div>'''

def main():
    # CSS
    css = """
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:'PingFang SC','Microsoft YaHei',sans-serif;background:#1a1a2e;color:#e0e0e0;padding:16px;line-height:1.6;font-size:13px}
.container{max-width:1300px;margin:0 auto}
.header{background:linear-gradient(135deg,#4f46e5,#7c3aed);color:#fff;padding:20px 28px;border-radius:12px;margin-bottom:16px;box-shadow:0 4px 16px rgba(79,70,229,0.3)}
.header h1{font-size:22px;margin-bottom:4px}
.header .sub{font-size:13px;opacity:.9}
.legend{display:flex;gap:8px;flex-wrap:wrap;margin-top:10px;font-size:11px}
.legend span{padding:3px 8px;border-radius:8px}
.block{background:#16213e;border-radius:10px;padding:18px 22px;margin-bottom:16px;box-shadow:0 2px 8px rgba(0,0,0,0.2)}
.block-title{font-size:17px;font-weight:bold;color:#818cf8;margin-bottom:10px;padding-bottom:6px;border-bottom:2px solid #1e293b}
.block-sub{color:#94a3b8;font-size:12px;margin-bottom:12px}
/* Framework table */
.fw-table{width:100%;border-collapse:collapse;font-size:12px}
.fw-table th,.fw-table td{border:1px solid #334155;padding:5px 8px;text-align:center}
.fw-table th{background:#4f46e5;color:#fff}
.fw-table tr:nth-child(even){background:#1e293b}
.fw-table .period-m{background:rgba(99,102,241,0.1)}
.fw-table .period-a{background:rgba(245,158,11,0.1)}
.fw-table .period-e{background:rgba(59,130,246,0.1)}
/* Calendar grid */
.cal-grid{display:grid;grid-template-columns:repeat(7,1fr);gap:3px;background:#0f172a;padding:3px;border-radius:8px}
.cal-head{background:#4f46e5;color:#fff;text-align:center;padding:5px;font-weight:bold;font-size:11px;border-radius:4px}
.cal-empty{background:transparent;min-height:60px}
.cal-day{background:#1e293b;border-radius:5px;padding:5px;min-height:70px;border-left:3px solid #334155;font-size:10px}
.cal-day.weekend{background:#292524;border-left-color:#f59e0b}
.cal-date{font-size:12px;font-weight:bold;color:#e2e8f0}
.cal-day.weekend .cal-date{color:#fbbf24}
.cal-wd{font-size:9px;color:#64748b}
.cal-type{font-size:9px;color:#818cf8;margin:2px 0}
.cal-evts{display:flex;flex-direction:column;gap:1px}
.mini-evt{display:block;padding:1px 3px;border-radius:2px;font-size:9px;line-height:1.2;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
/* Day cards */
.day-card{background:#16213e;border-radius:10px;padding:14px 18px;margin-bottom:12px;border-left:4px solid #334155}
.day-card.weekend{border-left-color:#f59e0b}
.day-card.today{border-left-color:#22c55e;box-shadow:0 0 0 2px rgba(34,197,94,0.3)}
.day-card-header{display:flex;align-items:center;gap:10px;margin-bottom:10px;padding-bottom:6px;border-bottom:1px solid #1e293b}
.dc-date{font-size:16px;font-weight:bold;color:#e2e8f0}
.dc-wd{font-size:12px;color:#64748b}
.dc-type{font-size:11px;color:#818cf8;background:rgba(129,140,248,0.15);padding:2px 8px;border-radius:8px}
.periods{display:grid;grid-template-columns:1fr 1fr 1fr;gap:10px}
.period{background:#0f172a;border-radius:6px;padding:8px 10px}
.period.morning{border-top:2px solid #6366f1}
.period.afternoon{border-top:2px solid #f59e0b}
.period.evening{border-top:2px solid #3b82f6}
.period-title{font-size:11px;font-weight:bold;color:#94a3b8;margin-bottom:4px}
.slot-table{width:100%;border-collapse:collapse;font-size:11px}
.slot-table td{padding:2px 4px;border-bottom:1px solid #1e293b;vertical-align:top}
.td-time{color:#64748b;white-space:nowrap;width:80px;font-size:10px}
.td-act{color:#cbd5e1}
.cat-tag{display:inline-block;padding:1px 5px;border-radius:3px;font-size:9px;margin-right:4px;white-space:nowrap}
.day-summary{margin-top:8px;padding:6px 10px;background:rgba(129,140,248,0.08);border-radius:4px;font-size:11px;color:#94a3b8;line-height:1.5}
/* Progress */
.progress-grid{display:grid;grid-template-columns:1fr 1fr;gap:12px}
.prog-item{background:#0f172a;border-radius:8px;padding:10px 14px}
.prog-item h4{color:#818cf8;font-size:13px;margin-bottom:6px}
.prog-item .bar{height:8px;background:#1e293b;border-radius:4px;overflow:hidden;margin:4px 0}
.prog-item .bar-fill{height:100%;border-radius:4px}
.prog-item .info{font-size:11px;color:#64748b}
/* Notes */
.note{padding:8px 12px;border-radius:6px;margin:6px 0;font-size:12px;border-left:3px solid}
.note.danger{background:rgba(239,68,68,0.1);border-left-color:#ef4444;color:#fca5a5}
.note.warn{background:rgba(245,158,11,0.1);border-left-color:#f59e0b;color:#fcd34d}
.note.good{background:rgba(34,197,94,0.1);border-left-color:#22c55e;color:#86efac}
.note.info{background:rgba(59,130,246,0.1);border-left-color:#3b82f6;color:#93c5fd}
/* Basketball schedule */
.bb-list{display:grid;grid-template-columns:repeat(5,1fr);gap:6px;margin:8px 0}
.bb-item{background:#0f172a;border-radius:6px;padding:6px 8px;text-align:center;font-size:11px;border:1px solid #1e293b}
.bb-item .bb-date{color:#fca5a5;font-weight:bold}
.bb-item .bb-time{color:#64748b;font-size:10px}
@media(max-width:900px){.periods{grid-template-columns:1fr}.progress-grid{grid-template-columns:1fr}.bb-list{grid-template-columns:repeat(3,1fr)}}
"""

    # Calendar grid
    # 7/11 is Saturday. Start weeks on Saturday.
    cal_rows = []
    for i in range(0, len(days), 7):
        week = days[i:i+7]
        row = ''.join(gen_day_summary(d) for d in week)
        # Pad if less than 7
        for _ in range(7 - len(week)):
            row += '<div class="cal-day cal-empty"></div>'
        cal_rows.append(row)

    cal_html = '<div class="cal-grid">'
    cal_html += '<div class="cal-head">周六</div><div class="cal-head">周日</div><div class="cal-head">周一</div><div class="cal-head">周二</div><div class="cal-head">周三</div><div class="cal-head">周四</div><div class="cal-head">周五</div>'
    for row in cal_rows:
        cal_html += row
    cal_html += '</div>'

    # Day details
    details_html = ''.join(gen_day_detail(d, i) for i, d in enumerate(days))

    # Basketball schedule
    bb_dates = [
        (7,11,'六'),(7,13,'一'),(7,15,'三'),(7,17,'五'),(7,19,'日'),
        (7,21,'二'),(7,23,'四'),(7,25,'六'),(8,13,'四'),(8,19,'三'),
    ]
    bb_html = '<div class="bb-list">'
    for i,(m,d,w) in enumerate(bb_dates,1):
        bb_html += f'<div class="bb-item"><div class="bb-date">第{i}次</div><div class="bb-date">{m}/{d}({w})</div><div class="bb-time">10:30-12:00</div></div>'
    bb_html += '</div>'

    # Progress section
    prog_html = f'''
<div class="progress-grid">
  <div class="prog-item">
    <h4>📐 数学预习（8单元）</h4>
    <div class="bar"><div class="bar-fill" style="width:100%;background:#8b5cf6"></div></div>
    <div class="info">7.11 U1 → 7.12 U2 → 7.14 U3 → 7.16 U4 → 7.18 U5 → 7.19 U6 → 7.20 U7 → 7.22 U8<br>✅ 全部7月22日前完成</div>
  </div>
  <div class="prog-item">
    <h4>📖 语文背诵（8单元）</h4>
    <div class="bar"><div class="bar-fill" style="width:100%;background:#f97316"></div></div>
    <div class="info">7.11 U1 → 7.12 U2 → 7.18 U3 → 7.19 U4 → 7.20 U5 → 7.21 U6 → 7.22 U7 → 7.23 U8<br>✅ 全部7月23日前完成</div>
  </div>
  <div class="prog-item">
    <h4>🔤 英语每日练习</h4>
    <div class="bar"><div class="bar-fill" style="width:100%;background:#22c55e"></div></div>
    <div class="info">每天：单词30min + 朗读30min = 1h<br>外研版五上 M1-M10 课文朗读+单词记忆<br>8月英语课期间已在课内覆盖</div>
  </div>
  <div class="prog-item">
    <h4>🏀 篮球训练（10次）</h4>
    <div class="bar"><div class="bar-fill" style="width:100%;background:#ef4444"></div></div>
    <div class="info">7.11起隔日一次，10:30-12:00<br>7月8次 + 8月2次(8/13、8/19英语休)<br>旅行期间(7/27、7/29)视情况安排</div>
  </div>
  <div class="prog-item">
    <h4>✍️ 练字课</h4>
    <div class="bar"><div class="bar-fill" style="width:100%;background:#06b6d4"></div></div>
    <div class="info">7.6-7.17 每日14:30-16:00 + 作业2h<br>共12天，已含在7.11-7.17排期中</div>
  </div>
  <div class="prog-item">
    <h4>📝 豆神语文课</h4>
    <div class="bar"><div class="bar-fill" style="width:100%;background:#f97316"></div></div>
    <div class="info">7.13-7.25 每日9:00-10:30 + 作业1h<br>7.19休息，共12天<br>作业安排在晚上19:30-20:30</div>
  </div>
</div>'''

    # Framework table
    fw_html = '''
<table class="fw-table">
<tr><th>时段</th><th>时间</th><th>内容</th></tr>
<tr><td class="period-m">起床</td><td>8:00-8:30</td><td>起床、洗漱</td></tr>
<tr class="period-m"><td rowspan="4">上午</td><td>8:30-9:00</td><td>英语单词记忆(30min)</td></tr>
<tr class="period-m"><td>9:00-10:30</td><td>豆神语文课 / 数学预习 / 自由学习</td></tr>
<tr class="period-m"><td>10:30-12:00</td><td>篮球训练(隔日) / 数学预习 / 自由</td></tr>
<tr class="period-m"><td>12:00-12:30</td><td>休息缓冲</td></tr>
<tr><td>午餐</td><td>12:30-13:00</td><td>午餐</td></tr>
<tr><td>午休</td><td>13:00-14:00</td><td>午休</td></tr>
<tr class="period-a"><td rowspan="3">下午</td><td>14:00-16:00</td><td>练字课(7.6-7.17) / 英语课(8月) / 数学预习 / 语文背诵</td></tr>
<tr class="period-a"><td>16:00-18:00</td><td>课外作业 / 数学预习 / 自由活动</td></tr>
<tr class="period-a"><td>18:00</td><td>→ 晚餐+休息</td></tr>
<tr><td>晚餐</td><td>18:00-19:30</td><td>晚餐、休息、洗澡</td></tr>
<tr class="period-e"><td rowspan="4">晚上</td><td>19:30-20:30</td><td>豆神作业(1h) / 英语单词+朗读 / 自由</td></tr>
<tr class="period-e"><td>20:30-22:00</td><td>语文背诵 / 数学练习 / 课外作业</td></tr>
<tr class="period-e"><td>22:00-22:30</td><td>📖 固定阅读时间(30min)</td></tr>
<tr class="period-e"><td>22:30</td><td>就寝</td></tr>
</table>'''

    # Type summary table
    type_summaries = [
        ('A','练字+篮球','7.11','8:30-10:30数学 | 10:30-12:00篮球 | 14:30-16:00练字 | 19:30-21:30语文背诵'),
        ('B','练字(周末)','7.12','8:30-10:30数学 | 14:30-16:00练字 | 19:30-21:30语文背诵'),
        ('C','豆神+练字+篮球','7.13,15,17','9:00-10:30豆神 | 10:30-12:00篮球 | 14:30-16:00练字 | 19:30-20:30豆神作业'),
        ('D','豆神+练字','7.14,16','9:00-10:30豆神 | 10:30-12:30数学 | 14:30-16:00练字 | 19:30-20:30豆神作业'),
        ('E','豆神+篮球','7.21,23,25','9:00-10:30豆神 | 10:30-12:00篮球 | 14:00-16:00语文背诵'),
        ('F','豆神only','7.18,20,22,24','9:00-10:30豆神 | 10:30-12:30数学 | 14:00-16:00语文背诵'),
        ('G','篮球(豆神休)','7.19','8:30-10:30数学 | 10:30-12:00篮球 | 14:00-16:00语文背诵'),
        ('H','旅行','7.26-7.31','旅行活动 + 英语单词/朗读 + 阅读'),
        ('I','英语单课','8.1-8.12,8.14,8.28-29','8:30-11:30英语课 | 14:00-17:00英语作业 | 19:30-20:30单词+朗读'),
        ('JB','英语休+篮球','8.13','10:30-12:00篮球 | 其余自由'),
        ('K','英语+数学(地狱)','8.15-18,20,22-24,26-27','8:30-11:30英语 | 13:30-15:30数学 | 作业+阅读'),
        ('L','数学休(仅英语)','8.21','8:30-11:30英语 | 14:00-17:00英语作业'),
        ('MB','英语休+篮球+数学','8.19','10:30-12:00篮球 | 13:30-15:30数学 | 15:30-17:30数学作业'),
        ('M','英语休+数学','8.25','13:30-15:30数学 | 15:30-17:30数学作业'),
        ('O','自由','8.30-8.31','自由活动 / 准备开学'),
    ]
    ts_html = '<table class="fw-table"><tr><th>类型</th><th>名称</th><th>日期</th><th>核心安排</th></tr>'
    for code, name, dates, desc in type_summaries:
        ts_html += f'<tr><td style="text-align:center;font-weight:bold;color:#818cf8">{code}</td><td style="text-align:center">{name}</td><td style="text-align:center;font-size:11px">{dates}</td><td style="font-size:11px">{desc}</td></tr>'
    ts_html += '</table>'

    # Notes
    notes_html = '''
<div class="note danger">⚠️ <b>8.15-8.27 地狱期</b>：每天英语3h课+3h作业+数学2h课+2h作业=10h被占满。此期间仅安排阅读(22:00-22:30)，不安排其他课程。所有预习任务必须在此之前完成。</div>
<div class="note warn">⚠️ <b>篮球冲突处理</b>：豆神日(7.13,15,17,21,23,25)先上豆神(9:00-10:30)→直接去篮球(10:30-12:00)→豆神作业下移到晚上(19:30-20:30)。8月英语课(8:30-11:30)与篮球(10:30-12:00)冲突，8月仅安排英语休息日(8/13、8/19)打篮球。旅行期间(7/27、7/29)视情况，可取消。</div>
<div class="note good">✅ <b>7月完成目标</b>：数学8单元(7.11-7.22) + 语文8单元(7.11-7.23) + 每日英语1h，全部在7月内完成。8月仅跟课外班+作业+阅读。</div>
<div class="note info">📌 <b>每日最低保证</b>（即使再忙）：①英语单词30min ②英语朗读30min ③阅读30min(22:00-22:30)</div>
<div class="note info">📌 <b>周末缓冲</b>：7.12(日)、7.18(六)、7.19(日)、7.25(六)、8.2(日)、8.9(日)、8.16(日)、8.23(日)、8.30(日)安排较多自由时间</div>
<div class="note info">📌 <b>旅行建议</b>：7.26-7.31(6天)是唯一无固定课的连续窗口。旅行期间保持英语单词30min+朗读30min+阅读30min即可，其余放松。</div>
<div class="note warn">⚠️ <b>关于7.10和7.17</b>：已确认无学而思课程。7.17为豆神+练字+篮球(类型C)，7.10为今天，不计入排期。</div>
'''

    # Chinese units detail
    ch_html = '<table class="fw-table"><tr><th>单元</th><th>必背内容</th><th>计划日期</th><th>时长</th></tr>'
    ch_schedule = [
        (1, '古人谈读书 + 观书有感', '7.11(六)'),
        (2, '语文园地二（成语积累）', '7.12(日)'),
        (3, '语文园地三（名言警句）', '7.18(六)'),
        (4, '古诗三首（示儿·题临安邸·己亥杂诗）+ 少年中国说节选', '7.19(日)'),
        (5, '语文园地四（成语积累）', '7.20(一)'),
        (6, '语文园地六·乞巧', '7.21(二)'),
        (7, '古诗三首（山居秋暝·枫桥夜泊·早春呈水部张十八员外）+ 白鹭', '7.22(三)'),
        (8, '渔歌子 + 游子吟', '7.23(四)'),
    ]
    for u, content, date in ch_schedule:
        ch_html += f'<tr><td style="text-align:center;font-weight:bold">第{u}单元</td><td>{content}</td><td style="text-align:center">{date}</td><td style="text-align:center">2h</td></tr>'
    ch_html += '</table>'

    # Math units detail
    math_schedule = [
        (1, '7.11(六)'), (2, '7.12(日)'), (3, '7.14(二)'), (4, '7.16(四)'),
        (5, '7.18(六)'), (6, '7.19(日)'), (7, '7.20(一)'), (8, '7.22(三)'),
    ]
    mth_html = '<table class="fw-table"><tr><th>单元</th><th>内容</th><th>计划日期</th><th>时长</th></tr>'
    for u, date in math_schedule:
        mth_html += f'<tr><td style="text-align:center;font-weight:bold">第{u}单元</td><td>{math_units[u]}</td><td style="text-align:center">{date}</td><td style="text-align:center">2h</td></tr>'
    mth_html += '</table>'

    # Build full HTML
    html = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>杨子禺暑假详细月历表 2026</title>
<style>{css}</style>
</head>
<body>
<div class="container">

<div class="header">
  <h1>📅 杨子禺 2026 暑假详细月历表</h1>
  <div class="sub">7月11日 — 8月31日 | 每日分上午/下午/晚上三个时段 | 含详细时间安排</div>
  <div class="legend">
    <span style="{CAT_CSS[MATH]}">数学</span>
    <span style="{CAT_CSS[CH]}">语文</span>
    <span style="{CAT_CSS[ENG]}">英语</span>
    <span style="{CAT_CSS[HW]}">作业</span>
    <span style="{CAT_CSS[BB]}">篮球</span>
    <span style="{CAT_CSS[TRAVEL]}">旅行</span>
    <span style="{CAT_CSS[READ]}">阅读</span>
    <span style="{CAT_CSS[FREE]}">自由</span>
    <span style="{CAT_CSS[REST]}">休息</span>
  </div>
</div>

<div class="block">
  <div class="block-title">一、每日基础作息框架</div>
  <div class="block-sub">固定时间锚点：8:00起床 | 12:30午餐 | 13:00-14:00午休 | 18:00晚餐 | 22:00-22:30阅读 | 22:30就寝</div>
  {fw_html}
</div>

<div class="block">
  <div class="block-title">二、日类型总览（{len(type_summaries)}种）</div>
  <div class="block-sub">根据当天是否有课外班，分为不同日类型，每种类型有固定的时间模板</div>
  {ts_html}
</div>

<div class="block">
  <div class="block-title">三、月历总览</div>
  <div class="block-sub">每格显示当天核心安排（颜色对应科目），下方为每日详细时间表</div>
  {cal_html}
</div>

<div class="block">
  <div class="block-title">四、篮球训练安排（共10次）</div>
  <div class="block-sub">7月11日起隔日一次，10:30-12:00。豆神日先上课再打球，作业下移到晚上。8月仅在英语休息日安排。</div>
  {bb_html}
</div>

<div class="block">
  <div class="block-title">五、各科进度计划</div>
  {prog_html}
</div>

<div class="block">
  <div class="block-title">六、语文必背课文进度（8单元）</div>
  <div class="block-sub">参考文件：26新版五年级语文上册暑假预习必背课文内容+闯关表</div>
  {ch_html}
</div>

<div class="block">
  <div class="block-title">七、数学预习进度（8单元）</div>
  <div class="block-sub">每次至少2小时，全部在7月22日前完成</div>
  {mth_html}
</div>

<div class="block">
  <div class="block-title">八、每日详细时间安排（含说明）</div>
  <div class="block-sub">每按上午(8:30-12:30) / 下午(14:00-18:00) / 晚上(19:30-22:30) 三个时段展示，含每项具体时间</div>
  {details_html}
</div>

<div class="block">
  <div class="block-title">九、关键提醒与注意事项</div>
  {notes_html}
</div>

</div>
</body>
</html>'''

    outpath = r'C:\Users\ytf20\Desktop\杨子禺暑假\暑假详细月历表.html'
    with open(outpath, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f'Done! {len(html)} chars, {len(days)} days')

if __name__ == '__main__':
    main()
