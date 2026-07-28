#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""暑假详细月历表 v3 - 集中型学习方案"""

CN = ["第一单元：古人谈读书+观书有感","第二单元：语文园地二（成语）","第三单元：语文园地三（名言警句）","第四单元：古诗三首（示儿/题临安邸/己亥杂诗）+少年中国说","第五单元：语文园地四（成语）","第六单元：语文园地六（乞巧）","第七单元：古诗三首（山居秋暝/枫桥夜泊/早春呈水部张十八员外）","第八单元：渔歌子+游子吟"]
MATH = ["第一单元：小数乘法","第二单元：位置","第三单元：小数除法","第四单元：可能性","第五单元：简易方程","第六单元：多边形的面积","第七单元：数学广角","第八单元：总复习"]
EN = ["U1","U2","U3","U4","U5","U6"]

BK = {"7/11":1,"7/13":2,"7/15":3,"7/17":4,"7/19":5,"7/21":6,"7/23":7,"7/25":8,"8/13":9,"8/19":10}

# Chinese unit schedule (date -> unit index 0-7)
CN_S = {"7/11":0,"7/14":1,"7/16":2,"7/18":3,"7/19":4,"7/20":5,"7/22":6,"7/24":7}
# Math unit schedule
MATH_S = {"7/11":0,"7/12":1,"7/18":2,"7/19":3,"7/20":4,"7/21":5,"7/22":6,"7/23":7,"7/24":"总复习","7/25":"查漏补缺"}
# English unit schedule (2 days per unit)
EN_S = {"7/11":0,"7/12":0,"7/13":1,"7/14":1,"7/15":2,"7/16":2,"7/17":3,"7/18":3,"7/19":4,"7/20":4,"7/21":5,"7/22":5,"7/23":"复习","7/24":"复习","7/25":"复习"}

def B(p,s,e,t,d,c):
    return {"p":p,"s":s,"e":e,"t":t,"d":d,"c":c}

def LU(): return B("休息","12:30","13:00","午餐","利用时间听英语音频","meal")
def NA(): return B("休息","13:00","14:00","午休","","rest")
def DI(t="18:00"): return B("休息",t,"19:30" if t=="18:00" else "19:30","晚餐+洗澡","利用时间听英语","meal")
def RD(): return B("晚上","22:00","22:30","阅读","学校推荐书目 30min","reading")
def EN_BK(): return B("下午","16:00","16:30","休息娱乐","观看游戏/视频 30min","free")
def BF(): return B("休息","12:00","12:30","缓冲休息","","rest")

def cn_blk(date, period="上午", s="10:30", e="12:00"):
    u = CN_S.get(date)
    if u is None: return None
    return B(period,s,e,"语文背诵",CN[u],"chinese")

def math_label(date):
    u = MATH_S.get(date)
    if u is None: return None
    return MATH[u] if isinstance(u,int) else f"数学{u}"

def math_blk(date, s="14:00", e="16:00", period="下午"):
    label = math_label(date)
    if label is None: return None
    return B(period,s,e,"数学预习",label,"math")

def en_str(date):
    u = EN_S.get(date)
    if u is None: return None
    if u == "复习": return "英语复习 单词+朗读背诵"
    return f"{EN[u]} 单词记忆+课文朗读背诵"

# Phase info
PHASES = [
    ("阶段1：起步期","7/11-7/12","语文U1 + 数学U1-U2 + 英语U1","自由学习日，建立学习节奏"),
    ("阶段2：豆神+练字期","7/13-7/17","豆神课+练字课+英语U2-U4","三重任务期，语文背诵穿插进行"),
    ("阶段3：集中突破期","7/18-7/25","语文U4-U8 + 数学U3-U8 + 英语U4-U6","练字结束，全力推进预习"),
    ("阶段4：旅行期","7/26-7/31","旅行+英语复习","放松身心，每日1h英语保持"),
    ("阶段5：英语课期","8/1-8/14","英语课外班+作业+其他任务","每天6h英语，穿插作文/思维导图"),
    ("阶段6：地狱期","8/15-8/27","英语课+数学课+作业","每天10h，仅安排阅读"),
    ("阶段7：收尾期","8/28-8/31","英语课+收心准备","逐步调整作息"),
]

def gen_day(date, wd):
    """Generate blocks and note for a day"""
    bk_n = BK.get(date)
    is_sat = wd == "六"
    is_sun = wd == "日"
    is_weekend = is_sat or is_sun
    
    # Check date ranges
    # July 11-25: study period
    # July 26-31: travel
    # Aug 1-14: English class (rest: 8/13)
    # Aug 15-27: English+Math class (rest: 8/19 EN, 8/21 Math, 8/25 EN)
    # Aug 28-29: English class only
    # Aug 30-31: wind down
    
    m = int(date.split("/")[0])
    d = int(date.split("/")[1])
    
    blocks = []
    note = ""
    dtype = ""
    
    if m == 7 and d <= 25:
        # ===== JULY STUDY PERIOD =====
        has_cn = date in CN_S
        has_math = date in MATH_S
        en = en_str(date)
        has_ds = (m == 7 and 13 <= d <= 25 and d != 19)  # 豆神 7/13-7/25, rest 7/19
        has_calli = (m == 7 and 13 <= d <= 17)  # 练字 7/13-7/17
        
        if has_ds and has_calli and bk_n:
            # Type: 豆神+练字+篮球
            dtype = "豆神+练字+篮球"
            blocks.append(B("上午","09:00","10:30","豆神语文课","上课","class"))
            blocks.append(B("上午","10:30","12:00","篮球训练",f"第{bk_n}次","basketball"))
            blocks.append(B("休息","12:00","12:30","回家休息","","rest"))
            blocks.append(LU()); blocks.append(NA())
            blocks.append(B("下午","14:00","14:30","课前准备","","rest"))
            blocks.append(B("下午","14:30","16:00","练字课","上课","calligraphy"))
            blocks.append(EN_BK())
            blocks.append(B("下午","16:30","18:30","练字作业","课后练习 2h","hw"))
            blocks.append(DI("18:30"))
            blocks.append(B("晚上","19:30","20:30","豆神作业","课后作业 1h","hw"))
            if en:
                blocks.append(B("晚上","20:30","21:30","英语",en,"english"))
            blocks.append(B("晚上","21:30","22:00","缓冲洗漱","","rest"))
            blocks.append(RD())
            note = f"豆神+练字+篮球三重日。{en if en else ''}安排在晚上。练字作业2h是重点。"
            
        elif has_ds and has_calli and not bk_n:
            # Type: 豆神+练字
            dtype = "豆神+练字"
            blocks.append(B("上午","09:00","10:30","豆神语文课","上课","class"))
            cn = cn_blk(date)
            if cn: blocks.append(cn)
            blocks.append(BF())
            blocks.append(LU()); blocks.append(NA())
            blocks.append(B("下午","14:00","14:30","课前准备","","rest"))
            blocks.append(B("下午","14:30","16:00","练字课","上课","calligraphy"))
            blocks.append(EN_BK())
            blocks.append(B("下午","16:30","18:30","练字作业","课后练习 2h","hw"))
            blocks.append(DI("18:30"))
            blocks.append(B("晚上","19:30","20:30","豆神作业","课后作业 1h","hw"))
            if en:
                blocks.append(B("晚上","20:30","21:30","英语",en,"english"))
            blocks.append(B("晚上","21:30","22:00","缓冲洗漱","","rest"))
            blocks.append(RD())
            cn_note = f"语文背诵{CN[CN_S[date]]}。" if has_cn else ""
            note = f"豆神+练字日。{cn_note}上午背诵，下午练字，晚上英语。"
            
        elif has_ds and not has_calli and bk_n:
            # Type: 豆神+篮球 (no 练字)
            dtype = "豆神+篮球"
            blocks.append(B("上午","09:00","10:30","豆神语文课","上课","class"))
            blocks.append(B("上午","10:30","12:00","篮球训练",f"第{bk_n}次","basketball"))
            blocks.append(B("休息","12:00","12:30","回家休息","","rest"))
            blocks.append(LU()); blocks.append(NA())
            mb = math_blk(date, "14:00", "16:00")
            if mb: blocks.append(mb)
            blocks.append(EN_BK())
            blocks.append(B("下午","16:30","18:00","数学练习","配套练习题巩固","math"))
            blocks.append(DI())
            blocks.append(B("晚上","19:30","20:30","豆神作业","课后作业 1h","hw"))
            if en:
                blocks.append(B("晚上","20:30","21:30","英语",en,"english"))
            blocks.append(B("晚上","21:30","22:00","缓冲洗漱","","rest"))
            blocks.append(RD())
            math_note = f"数学{math_label(date)}。" if has_math else ""
            note = f"豆神+篮球日。{math_note}下午集中数学预习+练习。"
            
        elif has_ds and not has_calli and not bk_n:
            # Type: 豆神 only
            dtype = "豆神"
            blocks.append(B("上午","09:00","10:30","豆神语文课","上课","class"))
            cn = cn_blk(date)
            if cn: blocks.append(cn)
            else:
                # No Chinese, add English in morning
                if en:
                    blocks.append(B("上午","10:30","12:00","英语",en,"english"))
            blocks.append(BF())
            blocks.append(LU()); blocks.append(NA())
            mb = math_blk(date, "14:00", "16:00")
            if mb: blocks.append(mb)
            blocks.append(EN_BK())
            blocks.append(B("下午","16:30","18:00","数学练习","配套练习题巩固" if has_math else "自主任务","math" if has_math else "school"))
            blocks.append(DI())
            if is_sat:
                blocks.append(B("晚上","19:30","20:30","豆神作业","课后作业 1h","hw"))
                if en:
                    blocks.append(B("晚上","20:30","21:30","英语",en,"english"))
                blocks.append(B("晚上","21:30","22:00","周末自由","","free"))
            else:
                blocks.append(B("晚上","19:30","20:30","豆神作业","课后作业 1h","hw"))
                if en:
                    blocks.append(B("晚上","20:30","21:30","英语",en,"english"))
                blocks.append(B("晚上","21:30","22:00","缓冲洗漱","","rest"))
            blocks.append(RD())
            cn_note = f"语文{CN[CN_S[date]]}，" if has_cn else ""
            math_note = f"数学{math_label(date)}，" if has_math else ""
            note = f"豆神日。{cn_note}{math_note}下午集中数学。"
            
        elif not has_ds and bk_n:
            # Type: Free + basketball (7/11, 7/19)
            dtype = "自由学习+篮球"
            cn = cn_blk(date, "上午", "09:00", "10:30")
            if cn: blocks.append(cn)
            blocks.append(B("上午","10:30","12:00","篮球训练",f"第{bk_n}次","basketball"))
            blocks.append(BF())
            blocks.append(LU()); blocks.append(NA())
            if en:
                blocks.append(B("下午","14:00","15:00","英语",en,"english"))
            mb = math_blk(date, "15:00", "17:00")
            if mb: blocks.append(mb)
            blocks.append(B("下午","17:00","17:30","休息娱乐","观看游戏/视频 30min","free"))
            if is_sat:
                blocks.append(B("下午","17:30","18:00","自由","周六放松","free"))
                blocks.append(DI())
                blocks.append(B("晚上","19:30","22:00","周末自由","周六晚上放松","free"))
            else:
                blocks.append(B("下午","17:30","18:00","自主任务","作文/思维导图","school"))
                blocks.append(DI())
                blocks.append(B("晚上","19:30","21:00","自主复习","回顾当日内容","school"))
                blocks.append(B("晚上","21:00","22:00","自由","","free"))
            blocks.append(RD())
            cn_note = f"语文{CN[CN_S[date]]}，" if has_cn else ""
            math_note = f"数学{math_label(date)}，" if has_math else ""
            note = f"自由+篮球日。{cn_note}{math_note}上午背诵+篮球，下午数学。"
            
        else:
            # Type: Free study, no basketball (7/12)
            dtype = "自由学习"
            if en:
                blocks.append(B("上午","09:00","10:00","英语",en,"english"))
            if has_cn:
                blocks.append(B("上午","10:00","12:00","语文复习",CN[CN_S.get(date,0)] if date in CN_S else "巩固复习","chinese"))
            else:
                blocks.append(B("上午","10:00","12:00","自主任务","作文/思维导图","school"))
            blocks.append(BF())
            blocks.append(LU()); blocks.append(NA())
            mb = math_blk(date, "14:00", "16:00")
            if mb: blocks.append(mb)
            else:
                blocks.append(B("下午","14:00","16:00","自主任务","作文/思维导图","school"))
            blocks.append(EN_BK())
            blocks.append(B("下午","16:30","18:00","自主任务","作文/思维导图/复习","school"))
            blocks.append(DI())
            blocks.append(B("晚上","19:30","21:00","自主复习","回顾当日内容","school"))
            blocks.append(B("晚上","21:00","22:00","自由","","free"))
            blocks.append(RD())
            math_note = f"数学{math_label(date)}，" if has_math else ""
            note = f"自由学习日。{math_note}上午英语+语文复习，下午数学。"
            
    elif m == 7 and 26 <= d <= 31:
        # ===== TRAVEL =====
        dtype = "旅行"
        blocks.append(B("上午","08:00","12:00","旅行活动","享受旅途","travel"))
        blocks.append(LU()); blocks.append(NA())
        blocks.append(B("下午","14:00","18:00","旅行活动","游览/体验","travel"))
        blocks.append(DI())
        blocks.append(B("晚上","19:30","20:30","英语复习","单词+朗读 1h","english"))
        blocks.append(B("晚上","20:30","22:00","自由","旅行休闲","free"))
        blocks.append(RD())
        note = "旅行日。保持每日1h英语复习习惯，其余时间放松。"
        
    elif m == 8 and d <= 29:
        # ===== AUGUST =====
        en_rest = d in [13, 19, 25]
        math_start = d >= 15
        math_rest = d == 21
        has_math_class = math_start and d <= 27 and not math_rest
        has_en_class = not en_rest
        
        if has_en_class and has_math_class:
            # Hell mode: English + Math class
            dtype = "英语+数学课"
            blocks.append(B("上午","08:00","08:30","起床早餐","","rest"))
            blocks.append(B("上午","08:30","11:30","英语课外班","上课 3h","class"))
            blocks.append(B("休息","11:30","12:30","回家休息","","rest"))
            blocks.append(LU()); blocks.append(NA())
            blocks.append(B("下午","13:30","15:30","数学课外班","上课 2h","class"))
            blocks.append(B("下午","15:30","17:30","数学作业","课后作业 2h","hw"))
            blocks.append(B("下午","17:30","18:00","缓冲休息","","rest"))
            blocks.append(B("休息","18:00","19:00","晚餐+洗澡","利用时间听英语","meal"))
            blocks.append(B("晚上","19:00","22:00","英语作业","课后作业 3h","hw"))
            blocks.append(RD())
            note = "地狱模式：英语3h+数学2h+作业5h=10h。仅安排阅读，不做其他。"
            
        elif has_en_class and not has_math_class and math_start and math_rest:
            # English class, Math rest (8/21)
            dtype = "英语课（数学休息）"
            blocks.append(B("上午","08:00","08:30","起床早餐","","rest"))
            blocks.append(B("上午","08:30","11:30","英语课外班","上课 3h","class"))
            blocks.append(B("休息","11:30","12:30","回家休息","","rest"))
            blocks.append(LU()); blocks.append(NA())
            blocks.append(B("下午","14:00","17:00","英语作业","课后作业 3h","hw"))
            blocks.append(B("下午","17:00","17:30","休息娱乐","观看游戏/视频 30min","free"))
            blocks.append(B("下午","17:30","18:00","自由","","free"))
            blocks.append(DI())
            blocks.append(B("晚上","19:30","22:00","自由","数学休息日，轻松一下","free"))
            blocks.append(RD())
            note = "数学休息日。英语课+作业后，晚上自由。"
            
        elif not has_en_class and has_math_class:
            # English rest, Math class (8/19, 8/25)
            dtype = "英语休息+数学课"
            if bk_n:
                blocks.append(B("上午","09:00","10:30","篮球训练",f"第{bk_n}次","basketball"))
                blocks.append(B("上午","10:30","12:00","自由","","free"))
            else:
                blocks.append(B("上午","09:00","12:00","自由","英语休息日","free"))
            blocks.append(BF())
            blocks.append(LU()); blocks.append(NA())
            blocks.append(B("下午","13:30","15:30","数学课外班","上课 2h","class"))
            blocks.append(B("下午","15:30","17:30","数学作业","课后作业 2h","hw"))
            blocks.append(B("下午","17:30","18:00","休息娱乐","观看游戏/视频 30min","free"))
            blocks.append(DI())
            blocks.append(B("晚上","19:30","22:00","自由","英语休息日","free"))
            blocks.append(RD())
            bk_note = f"篮球第{bk_n}次，" if bk_n else ""
            note = f"英语休息日。{bk_note}数学课+作业后自由。"
            
        elif has_en_class and not math_start:
            # English class only (8/1-8/14, not rest)
            dtype = "英语课"
            blocks.append(B("上午","08:00","08:30","起床早餐","","rest"))
            blocks.append(B("上午","08:30","11:30","英语课外班","上课 3h","class"))
            blocks.append(B("休息","11:30","12:30","回家休息","","rest"))
            blocks.append(LU()); blocks.append(NA())
            blocks.append(B("下午","14:00","17:00","英语作业","课后作业 3h","hw"))
            blocks.append(B("下午","17:00","17:30","休息娱乐","观看游戏/视频 30min","free"))
            if is_sat:
                blocks.append(B("下午","17:30","18:00","自由","周六","free"))
                blocks.append(DI())
                blocks.append(B("晚上","19:30","22:00","周末自由","","free"))
            else:
                blocks.append(B("下午","17:30","18:00","缓冲","","rest"))
                blocks.append(DI())
                blocks.append(B("晚上","19:30","21:00","其他任务","作文/思维导图/非遗","school"))
                blocks.append(B("晚上","21:00","22:00","自由","","free"))
            blocks.append(RD())
            note = "英语课日。上午上课，下午作业，晚上其他任务或自由。"
            
        elif not has_en_class and not math_start:
            # English rest day, no math (8/13)
            dtype = "英语休息"
            if bk_n:
                blocks.append(B("上午","09:00","10:30","篮球训练",f"第{bk_n}次","basketball"))
                blocks.append(B("上午","10:30","12:00","自由","","free"))
            else:
                blocks.append(B("上午","09:00","12:00","自由","英语休息日","free"))
            blocks.append(BF())
            blocks.append(LU()); blocks.append(NA())
            blocks.append(B("下午","14:00","16:00","其他任务","作文/思维导图","school"))
            blocks.append(EN_BK())
            blocks.append(B("下午","16:30","18:00","自由","","free"))
            blocks.append(DI())
            blocks.append(B("晚上","19:30","22:00","自由","","free"))
            blocks.append(RD())
            bk_note = f"篮球第{bk_n}次，" if bk_n else ""
            note = f"英语休息日。{bk_note}可安排其他任务或休息。"
            
        elif has_en_class and not has_math_class and not math_start:
            # This shouldn't happen, but handle gracefully
            dtype = "英语课"
            blocks.append(B("上午","08:30","11:30","英语课外班","上课","class"))
            blocks.append(LU()); blocks.append(NA())
            blocks.append(B("下午","14:00","17:00","英语作业","3h","hw"))
            blocks.append(EN_BK())
            blocks.append(DI())
            blocks.append(B("晚上","19:30","22:00","自由","","free"))
            blocks.append(RD())
            note = "英语课日。"
            
    elif m == 8 and d >= 28:
        # Wind down
        if d <= 29:
            dtype = "英语课+收尾"
            blocks.append(B("上午","08:00","08:30","起床早餐","","rest"))
            blocks.append(B("上午","08:30","11:30","英语课外班","上课 3h","class"))
            blocks.append(B("休息","11:30","12:30","回家休息","","rest"))
            blocks.append(LU()); blocks.append(NA())
            blocks.append(B("下午","14:00","16:00","英语作业","2h","hw"))
            blocks.append(EN_BK())
            if is_sat:
                blocks.append(B("下午","16:30","18:00","自由","周六","free"))
                blocks.append(DI())
                blocks.append(B("晚上","19:30","22:00","周末自由","","free"))
            else:
                blocks.append(B("下午","16:30","18:00","自由","","free"))
                blocks.append(DI())
                blocks.append(B("晚上","19:30","22:00","自由","收心调整","free"))
            blocks.append(RD())
            note = "英语课最后两天。作业完成后自由活动，逐步调整作息。"
        else:
            # 8/30-8/31: fully free
            dtype = "收心准备"
            blocks.append(B("上午","09:00","10:00","英语复习","单词+朗读 1h","english"))
            blocks.append(B("上午","10:00","12:00","整理学习用品","准备开学","school"))
            blocks.append(BF())
            blocks.append(LU()); blocks.append(NA())
            blocks.append(B("下午","14:00","18:00","自由","假期最后放松","free"))
            blocks.append(DI())
            blocks.append(B("晚上","19:30","22:00","自由","调整作息","free"))
            blocks.append(RD())
            note = "收心准备日。整理学习用品，调整作息，准备开学。"
    
    return blocks, note, dtype

# All days data
WEEKDAYS = "一二三四五六日"
def get_wd(m, d):
    # 2026 calendar
    # 7/11 = Saturday(六)
    base = {"7/11":"六","7/12":"日","7/13":"一","7/14":"二","7/15":"三","7/16":"四","7/17":"五",
            "7/18":"六","7/19":"日","7/20":"一","7/21":"二","7/22":"三","7/23":"四","7/24":"五","7/25":"六",
            "7/26":"日","7/27":"一","7/28":"二","7/29":"三","7/30":"四","7/31":"五",
            "8/1":"六","8/2":"日","8/3":"一","8/4":"二","8/5":"三","8/6":"四","8/7":"五",
            "8/8":"六","8/9":"日","8/10":"一","8/11":"二","8/12":"三","8/13":"四","8/14":"五",
            "8/15":"六","8/16":"日","8/17":"一","8/18":"二","8/19":"三","8/20":"四","8/21":"五",
            "8/22":"六","8/23":"日","8/24":"一","8/25":"二","8/26":"三","8/27":"四",
            "8/28":"五","8/29":"六","8/30":"日","8/31":"一"}
    return base.get(f"{m}/{d}", "?")

CAT_COLORS = {
    "chinese":"#e67e22","english":"#27ae60","math":"#8e44ad","basketball":"#c0392b",
    "calligraphy":"#d4a017","free":"#7f8c8d","rest":"#95a5a6","meal":"#bdc3c7",
    "reading":"#2980b9","hw":"#d4a017","class":"#e67e22","school":"#1abc9c","travel":"#43a047"
}
CAT_NAMES = {
    "chinese":"语文","english":"英语","math":"数学","basketball":"篮球",
    "calligraphy":"练字","free":"自由","rest":"休息","meal":"餐",
    "reading":"阅读","hw":"作业","class":"课程","school":"自主","travel":"旅行"
}

def gen_html():
    # Generate all days
    all_days = []
    for m in [7, 8]:
        if m == 7:
            for d in range(11, 32):
                date = f"7/{d}"
                wd = get_wd(m, d)
                blocks, note, dtype = gen_day(date, wd)
                all_days.append((date, wd, dtype, blocks, note))
        else:
            for d in range(1, 32):
                date = f"8/{d}"
                wd = get_wd(m, d)
                blocks, note, dtype = gen_day(date, wd)
                all_days.append((date, wd, dtype, blocks, note))
    
    # CSS
    css = """
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:'PingFang SC','Microsoft YaHei',sans-serif;background:#f0f2f5;color:#2a2a2a;padding:20px;line-height:1.6;font-size:14px}
.container{max-width:1400px;margin:0 auto}
.header{background:linear-gradient(135deg,#5b6ef5,#7b8ff5);color:#fff;padding:28px 36px;border-radius:14px;margin-bottom:20px;box-shadow:0 6px 24px rgba(91,110,245,.25)}
.header h1{font-size:28px;margin-bottom:8px}
.header .sub{font-size:15px;opacity:.9}
.legend{display:flex;gap:8px;flex-wrap:wrap;margin-top:14px;font-size:12px}
.legend span{background:rgba(255,255,255,.2);padding:4px 12px;border-radius:12px}
.block{background:#fff;border-radius:12px;padding:24px 28px;margin-bottom:20px;box-shadow:0 2px 10px rgba(0,0,0,.06)}
.block-title{font-size:20px;font-weight:bold;color:#5b6ef5;margin-bottom:16px;padding-bottom:10px;border-bottom:2px solid #eef1f8}
.phase-grid{display:grid;grid-template-columns:repeat(2,1fr);gap:12px}
.phase-card{background:#f8f9fc;border-radius:10px;padding:14px 18px;border-left:4px solid #5b6ef5}
.phase-card h4{font-size:15px;margin-bottom:4px}
.phase-card .dates{font-size:12px;color:#888;margin-bottom:4px}
.phase-card .focus{font-size:13px;color:#444;line-height:1.5}
.cal-grid{display:grid;grid-template-columns:repeat(7,1fr);gap:3px;background:#e6eaf3;padding:3px;border-radius:8px}
.cal-head{background:#5b6ef5;color:#fff;text-align:center;padding:8px 4px;font-weight:bold;font-size:12px;border-radius:4px}
.cal-day{background:#fff;border-radius:5px;padding:5px;min-height:72px;font-size:10px;border-left:3px solid #ddd;position:relative}
.cal-day .num{font-weight:bold;font-size:12px}
.cal-day .wd{font-size:9px;color:#999}
.cal-day.weekend{background:#fff8e6;border-left-color:#f5a623}
.cal-day.travel{background:#e8f5e9;border-left-color:#43a047}
.cal-day.hell{background:#fde8e8;border-left-color:#e74c3c}
.cal-day.rest{background:#f0f7ff;border-left-color:#3498db}
.cal-day .tag{display:block;padding:1px 3px;border-radius:2px;font-size:8px;margin:1px 0;color:#fff;text-align:center}
.day-card{background:#f8f9fc;border-radius:10px;margin-bottom:14px;overflow:hidden;border:1px solid #e8eaf0}
.day-card-header{background:linear-gradient(135deg,#5b6ef5,#7b8ff5);color:#fff;padding:8px 16px;display:flex;align-items:center;gap:10px}
.day-card-header .date{font-size:16px;font-weight:bold}
.day-card-header .wd{font-size:13px;opacity:.9}
.day-card-header .type{font-size:12px;background:rgba(255,255,255,.2);padding:2px 8px;border-radius:8px;margin-left:auto}
.day-card-body{padding:10px 16px}
.period-label{font-size:11px;font-weight:bold;color:#888;margin:8px 0 4px;padding-bottom:2px;border-bottom:1px dashed #ddd}
.period-label:first-child{margin-top:0}
.time-row{display:flex;align-items:flex-start;gap:8px;padding:3px 0;font-size:12px}
.time-row .time{min-width:100px;color:#666;font-size:11px;white-space:nowrap}
.time-row .task{font-weight:600;min-width:75px}
.time-row .detail{color:#888;flex:1;font-size:11px}
.day-note{background:#fff8e1;border-left:3px solid #f5a623;padding:6px 10px;margin:6px 16px 10px;font-size:11px;border-radius:4px}
.tracking-table{width:100%;border-collapse:collapse;margin:10px 0;font-size:12px}
.tracking-table th,.tracking-table td{border:1px solid #e1e5ed;padding:6px 8px;text-align:left}
.tracking-table th{background:#5b6ef5;color:#fff;font-weight:bold}
.tracking-table tr:nth-child(even){background:#f8f9fc}
.note-box{background:#f8f9fc;border-radius:8px;padding:12px 16px;margin:8px 0;font-size:13px;line-height:1.7}
.note-box.warning{background:#fde8e8;border-left:3px solid #e74c3c}
.note-box.tip{background:#e8f5e9;border-left:3px solid #43a047}
.note-box.info{background:#e3f2fd;border-left:3px solid #2196f3}
@media(max-width:768px){.phase-grid{grid-template-columns:1fr}.cal-grid{grid-template-columns:repeat(7,1fr);font-size:9px}.time-row{flex-direction:column;gap:2px}.time-row .time{min-width:auto}}
"""
    
    # Build HTML
    parts = []
    parts.append(f"<!DOCTYPE html><html lang='zh'><head><meta charset='utf-8'><meta name='viewport' content='width=device-width,initial-scale=1'><title>暑假详细月历表</title><style>{css}</style></head><body><div class='container'>")
    
    # Header
    parts.append("""
    <div class="header">
        <h1>📋 杨子禺 2026 暑假详细月历表</h1>
        <div class="sub">7月11日 — 8月31日 | 集中型学习方案 | 每日分时段详细安排</div>
        <div class="legend">
            <span style="background:#e67e22">语文背诵/豆神</span>
            <span style="background:#27ae60">英语</span>
            <span style="background:#8e44ad">数学</span>
            <span style="background:#c0392b">篮球</span>
            <span style="background:#d4a017">练字/作业</span>
            <span style="background:#43a047">旅行</span>
            <span style="background:#7f8c8d">自由/休息</span>
            <span style="background:#2980b9">阅读</span>
        </div>
    </div>
    """)
    
    # Phase overview
    parts.append('<div class="block"><div class="block-title">一、集中学习阶段概览</div><div class="phase-grid">')
    for name, dates, focus, desc in PHASES:
        parts.append(f'<div class="phase-card"><h4>{name}</h4><div class="dates">{dates}</div><div class="focus"><strong>重点：</strong>{focus}<br>{desc}</div></div>')
    parts.append('</div></div>')
    
    # Calendar grid
    parts.append('<div class="block"><div class="block-title">二、月历总览</div>')
    # July calendar
    parts.append('<h4 style="margin-bottom:8px;color:#5b6ef5">7月</h4>')
    parts.append('<div class="cal-grid">')
    for h in ["日","一","二","三","四","五","六"]:
        parts.append(f'<div class="cal-head">{h}</div>')
    # 7/11 is Saturday, so 5 empty cells before it (Sun-Thu)
    for i in range(5):
        parts.append('<div class="cal-day" style="background:transparent;border:none;min-height:30px"></div>')
    for d in range(11, 32):
        date = f"7/{d}"
        wd = get_wd(7, d)
        is_weekend = wd in ["六","日"]
        is_travel = 26 <= d <= 31
        cls = "cal-day"
        if is_weekend: cls += " weekend"
        if is_travel: cls += " travel"
        tags = []
        if date in CN_S: tags.append(f'<span class="tag" style="background:#e67e22">语{CN_S[date]+1}</span>')
        if date in MATH_S: 
            mu = MATH_S[date]
            tag_text = f"数{mu+1}" if isinstance(mu,int) else "数复"
            tags.append(f'<span class="tag" style="background:#8e44ad">{tag_text}</span>')
        if date in EN_S:
            eu = EN_S[date]
            tag_text = f"英{EN[eu]}" if eu != "复习" else "英复"
            tags.append(f'<span class="tag" style="background:#27ae60">{tag_text}</span>')
        if date in BK: tags.append(f'<span class="tag" style="background:#c0392b">篮{BK[date]}</span>')
        if 13 <= d <= 17: tags.append(f'<span class="tag" style="background:#d4a017">练字</span>')
        if 13 <= d <= 25 and d != 19: tags.append(f'<span class="tag" style="background:#e67e22">豆神</span>')
        if is_travel: tags.append(f'<span class="tag" style="background:#43a047">旅行</span>')
        parts.append(f'<div class="{cls}"><div class="num">{d} <span class="wd">{wd}</span></div>{"".join(tags)}</div>')
    parts.append('</div>')
    
    # August calendar
    parts.append('<h4 style="margin:16px 0 8px;color:#5b6ef5">8月</h4>')
    parts.append('<div class="cal-grid">')
    for h in ["日","一","二","三","四","五","六"]:
        parts.append(f'<div class="cal-head">{h}</div>')
    # 8/1 is Saturday
    for i in range(6):
        parts.append('<div class="cal-day" style="background:transparent;border:none;min-height:30px"></div>')
    for d in range(1, 32):
        date = f"8/{d}"
        wd = get_wd(8, d)
        is_weekend = wd in ["六","日"]
        en_rest = d in [13,19,25]
        math_class = 15 <= d <= 27 and d != 21
        en_class = d <= 29 and not en_rest
        cls = "cal-day"
        if is_weekend: cls += " weekend"
        if en_class and math_class: cls += " hell"
        elif en_rest and not math_class and d <= 14: cls += " rest"
        elif en_rest and math_class: cls += " rest"
        elif en_class and d >= 28: cls += " rest"
        tags = []
        if date in BK: tags.append(f'<span class="tag" style="background:#c0392b">篮{BK[date]}</span>')
        if en_class and d <= 14: tags.append(f'<span class="tag" style="background:#27ae60">英课</span>')
        if math_class: tags.append(f'<span class="tag" style="background:#8e44ad">数课</span>')
        if en_class and d >= 15 and not math_class: tags.append(f'<span class="tag" style="background:#27ae60">英课</span>')
        if en_class and d >= 28: tags.append(f'<span class="tag" style="background:#27ae60">英课</span>')
        if en_rest: tags.append(f'<span class="tag" style="background:#7f8c8d">休</span>')
        if d == 21: tags.append(f'<span class="tag" style="background:#7f8c8d">数休</span>')
        if d >= 30: tags.append(f'<span class="tag" style="background:#43a047">收心</span>')
        parts.append(f'<div class="{cls}"><div class="num">{d} <span class="wd">{wd}</span></div>{"".join(tags)}</div>')
    parts.append('</div></div>')
    
    # Daily details
    parts.append('<div class="block"><div class="block-title">三、每日详细安排（分时段）</div>')
    parts.append('<div class="note-box info"><strong>时间框架：</strong>上午 09:00-12:30 | 午餐 12:30-13:00 | 午休 13:00-14:00 | 下午 14:00-18:00 | 晚餐 18:00-19:30 | 晚上 19:30-22:30 | 阅读 22:00-22:30 | 就寝 22:30<br><strong>原则：</strong>每个学习时段≥1h，同一项目连续多日完成，上午语文/英语（记忆类），下午数学（理解类），每天30min娱乐休息，利用用餐时间听英语</div>')
    
    for date, wd, dtype, blocks, note in all_days:
        parts.append(f'<div class="day-card"><div class="day-card-header"><span class="date">{date}</span><span class="wd">周{wd}</span><span class="type">{dtype}</span></div><div class="day-card-body">')
        
        # Group by period
        current_period = None
        for b in blocks:
            p = b["p"]
            if p != current_period:
                if p != "休息":
                    parts.append(f'<div class="period-label">{p}</div>')
                current_period = p
            
            color = CAT_COLORS.get(b["c"], "#666")
            parts.append(f'<div class="time-row"><span class="time">{b["s"]}-{b["e"]}</span><span class="task" style="color:{color}">{b["t"]}</span><span class="detail">{b["d"]}</span></div>')
        
        if note:
            parts.append(f'<div class="day-note">{note}</div>')
        parts.append('</div></div>')
    
    parts.append('</div>')
    
    # Task tracking
    parts.append('<div class="block"><div class="block-title">四、任务进度追踪</div>')
    
    # Chinese tracking
    parts.append('<h4 style="margin-bottom:8px;color:#e67e22">语文背诵 8 单元</h4><table class="tracking-table"><tr><th>单元</th><th>内容</th><th>计划日期</th><th>状态</th></tr>')
    cn_dates = {"7/11":"7/11(六)","7/14":"7/14(二)","7/16":"7/16(四)","7/18":"7/18(六)","7/19":"7/19(日)","7/20":"7/20(一)","7/22":"7/22(三)","7/24":"7/24(五)"}
    for i, unit in enumerate(CN):
        d = [k for k,v in CN_S.items() if v == i]
        d_str = cn_dates.get(d[0], d[0]) if d else "—"
        parts.append(f'<tr><td>第{i+1}单元</td><td>{unit}</td><td>{d_str}</td><td>⬜ 待完成</td></tr>')
    parts.append('</table>')
    
    # Math tracking
    parts.append('<h4 style="margin:16px 0 8px;color:#8e44ad">数学预习 8 单元</h4><table class="tracking-table"><tr><th>单元</th><th>内容</th><th>计划日期</th><th>状态</th></tr>')
    math_dates_map = {}
    for date, u in MATH_S.items():
        if isinstance(u, int):
            math_dates_map[u] = date
    for i, unit in enumerate(MATH):
        d = math_dates_map.get(i, "—")
        parts.append(f'<tr><td>第{i+1}单元</td><td>{unit}</td><td>{d}</td><td>⬜ 待完成</td></tr>')
    parts.append('</table>')
    
    # English tracking
    parts.append('<h4 style="margin:16px 0 8px;color:#27ae60">英语 6 单元（朗读+背诵+单词）</h4><table class="tracking-table"><tr><th>单元</th><th>计划日期</th><th>朗读</th><th>背诵</th><th>单词</th></tr>')
    en_dates_map = {}
    for date, u in EN_S.items():
        if isinstance(u, int):
            if u not in en_dates_map:
                en_dates_map[u] = []
            en_dates_map[u].append(date)
    for i in range(6):
        dates = en_dates_map.get(i, ["—","—"])
        d_str = " + ".join(dates) if dates[0] != "—" else "—"
        parts.append(f'<tr><td>{EN[i]}</td><td>{d_str}</td><td>⬜</td><td>⬜</td><td>⬜</td></tr>')
    parts.append('</table>')
    
    # Basketball tracking
    parts.append('<h4 style="margin:16px 0 8px;color:#c0392b">篮球训练 10 次</h4><table class="tracking-table"><tr><th>次数</th><th>日期</th><th>时间</th><th>状态</th></tr>')
    for date, n in sorted(BK.items(), key=lambda x: x[1]):
        wd = get_wd(int(date.split("/")[0]), int(date.split("/")[1]))
        parts.append(f'<tr><td>第{n}次</td><td>{date} (周{wd})</td><td>10:30-12:00</td><td>⬜ 待完成</td></tr>')
    parts.append('</table>')
    
    parts.append('</div>')
    
    # Notes section
    parts.append("""
    <div class="block">
        <div class="block-title">五、说明与注意事项</div>
        
        <div class="note-box info">
            <strong>集中学习原则：</strong><br>
            1. <strong>同一项目连续完成：</strong>语文背诵连续8天完成8个单元（7/11-7/24），数学连续8天完成8个单元（7/11-7/23），英语每单元2天连续完成<br>
            2. <strong>不每天做所有项目：</strong>豆神+练字日（7/13-7/17）不做数学，专注豆神+练字+英语<br>
            3. <strong>上午记忆，下午理解：</strong>上午安排语文背诵和英语单词/朗读，下午安排数学预习<br>
            4. <strong>每个时段≥1h：</strong>避免频繁切换，英语单词+朗读合并为1h，不拆成两个30min<br>
            5. <strong>每天30min娱乐：</strong>下午16:00-16:30观看游戏/视频，作为学习间隙奖励<br>
            6. <strong>利用用餐时间：</strong>午餐和晚餐时播放英语音频，潜移默化
        </div>
        
        <div class="note-box tip">
            <strong>7月完成所有预习：</strong><br>
            • 语文8单元背诵：7/11-7/24 完成（每天1单元，1.5-2h）<br>
            • 数学8单元预习：7/11-7/23 完成（每天1单元，2h+练习1.5h）<br>
            • 英语6单元：7/11-7/22 完成（每单元2天，1h/天）<br>
            • 7/25前全部完成，7/26-7/31 旅行无压力
        </div>
        
        <div class="note-box warning">
            <strong>⚠️ 关键风险点：</strong><br>
            1. <strong>8/15-8/27 地狱期：</strong>每天英语课3h+数学课2h+英语作业3h+数学作业2h=10h，仅能安排阅读<br>
            2. <strong>篮球与豆神冲突处理：</strong>豆神日先上课(9:00-10:30)再打篮球(10:30-12:00)，豆神作业下移到晚上<br>
            3. <strong>练字日(7/13-7/17)最忙：</strong>豆神+练字+篮球+作业，数学暂停，专注当前任务<br>
            4. <strong>8月起篮球与英语课冲突：</strong>8月篮球仅安排在英语休息日(8/13, 8/19)
        </div>
        
        <div class="note-box">
            <strong>每日时间框架：</strong><br>
            • 08:00 起床 | 09:00 开始学习 | 12:00-12:30 缓冲<br>
            • 12:30-13:00 午餐（听英语音频）| 13:00-14:00 午休<br>
            • 14:00-18:00 下午学习（含30min娱乐休息）<br>
            • 18:00-19:30 晚餐+洗澡（听英语音频）<br>
            • 19:30-22:00 晚上学习/作业 | 22:00-22:30 阅读 | 22:30 就寝
        </div>
        
        <div class="note-box">
            <strong>英语学习内容（6单元）：</strong><br>
            每单元包含：①课文朗读 ②课文背诵 ③单词记忆<br>
            每日1h = 单词记忆30min + 朗读背诵30min<br>
            每单元2天 = 2h，6单元共12h，7/11-7/22完成<br>
            7/23-7/25 复习巩固3天<br>
            旅行期间(7/26-7/31)每日1h复习保持<br>
            8月英语课外班期间，课外班+作业已覆盖练习量
        </div>
        
        <div class="note-box">
            <strong>周末安排：</strong><br>
            • 周六：上午正常学习，下午16:30后自由，晚上自由<br>
            • 周日：可安排学习或休息，作为缓冲日<br>
            • 旅行期间(7/26-7/31)全部为旅行日
        </div>
    </div>
    """)
    
    parts.append('</div></body></html>')
    
    return "".join(parts)

if __name__ == "__main__":
    html = gen_html()
    path = r"C:\Users\ytf20\Desktop\杨子禺暑假\暑假详细月历表.html"
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Generated {len(html)} bytes, {html.count(chr(10))} lines")
