// 网站内容配置：板块与文章清单
// 扩容方式：加板块 = 在 SECTIONS 里加一段；加文章 = 在对应板块的 articles 里加一行。
// 字段：id title subtitle tag visibility zone(首页分区: public 公共 / private 私人)
//       articles: [{slug, title, date(提交时间), tag(关键字), icon(图标key), desc(简介), detail(详细简介绍), issue(期号), chart(图表数据)}]
// chart: {caption, bars:[{l,v,u}]}
window.SECTIONS = [
  {
    id: 'policy',
    title: '政策周报',
    subtitle: '城市建设与更新领域的政策动态与解读，按周归档。',
    tag: '公开',
    visibility: 'public',
    zone: 'public',
    articles: [
      {
        slug: '2026-08-17', title: '城建政策周报 · 第四期', date: '2026.08.17', tag: '周报', icon: 'policy',
        issue: '第四期',
        desc: '城市更新"十五五"规划量化盘子首披露 + 湖南三年行动方案通过 + 衡阳更新大盘落地。',
        detail: '本期主线：央视首披露《城市更新"十五五"规划》量化盘子（五年15万亿、上半年近1万亿）；湖南8/10省政府常务会议原则通过《湖南省城市更新三年行动实施方案（2026—2028年）》；衡阳本周聚焦——珠晖区老火车站/城北片区EPC招标、"十五五"拟改390个老旧小区惠及6.9万户。',
        chart: { caption: '城市更新"十五五"规划量化盘子', bars: [
          { l: '五年总投资', v: 15, u: '万亿' }, { l: '上半年已完成', v: 1, u: '万亿' },
          { l: '超长期国债管网', v: 1600, u: '亿' }, { l: '中央预算内', v: 970, u: '亿' },
          { l: '衡阳老旧小区', v: 390, u: '个' }
        ] }
      },
      {
        slug: '2026-08-10', title: '城建政策周报 · 第三期', date: '2026.08.10', tag: '周报', icon: 'policy',
        issue: '第三期',
        desc: '居民端资金破冰 + 八月资金窗口开启 + 株洲项目集中落地。',
        detail: '本期主线：居民端资金破冰（公积金条例拓宽提取）+ 八月资金窗口开启（专项债高峰、8000 亿政策性金融工具）+ 株洲项目集中落地。三条资金流在下半年交汇，是近年城市更新融资最优窗口之一。',
        chart: { caption: '本期三条资金流交汇（亿元）', bars: [
          { l: '专项债', v: 44000, u: '亿' }, { l: '政策性金融工具', v: 8000, u: '亿' },
          { l: '超长期特别国债', v: 1600, u: '亿' }, { l: '中央预算内', v: 970, u: '亿' },
          { l: '以工代赈', v: 395, u: '亿' }
        ] }
      },
      {
        slug: '2026-08-03', title: '城建政策周报 · 第二期', date: '2026.08.03', tag: '周报', icon: 'policy',
        issue: '第二期',
        desc: '六张网推进与增量政策窗口开启，地下管网列席中央部署。',
        detail: '六张网推进与增量政策窗口开启，地下管网首次列席中央部署；湘潭、株洲项目加速落地，中央财政、专项债、政策性金融工具同步放量。',
        chart: { caption: '城市更新资金总盘（亿元）', bars: [
          { l: '专项债额度', v: 44000, u: '亿' }, { l: '政策性金融工具', v: 8000, u: '亿' },
          { l: '两重特别国债', v: 8000, u: '亿' }, { l: '国开行贷款', v: 7863, u: '亿' },
          { l: '中央财政', v: 3100, u: '亿' }
        ] }
      },
      {
        slug: '2026-07-27', title: '城建政策周报 · 第一期', date: '2026.07.27', tag: '周报', icon: 'policy',
        issue: '第一期',
        desc: '十五五规划定调城市更新，六张网纳入基建，资金总盘开启。',
        detail: '十五五规划定调城市更新，六张网纳入基建盘子，城市更新资金总盘开启；长沙、湘潭率先落地，湖南累计改造 1246 个老旧小区。',
        chart: { caption: '湖南城市更新进度（截至本期）', bars: [
          { l: '老旧小区', v: 1246, u: '个' }, { l: '加装电梯', v: 900, u: '台' },
          { l: '争取资金', v: 149, u: '亿' }, { l: '惠及居民', v: 15, u: '万户' }
        ] }
      }
    ]
  },
  {
    id: 'work',
    title: '工作存档',
    subtitle: '需提交保存的城市规划成果，留档备查。',
    tag: '公开',
    visibility: 'public',
    zone: 'public',
    articles: [
      { slug: 'city-health',   title: '城市体检 AI 生成指南',     date: '2026.07', tag: '指南', icon: 'city-health',   desc: '从框架到成稿，用 AI 高效产出城市体检报告。', detail: '覆盖城市体检的指标体系、问题诊断与成稿路径，给出可直接复用的 AI 提示词与模板，把一份体检报告的生产周期压到最短。' },
      { slug: 'special-plan',  title: '城市更新专项规划 AI 编制指南',     date: '2026.07', tag: '指南', icon: 'special-plan',  desc: '专项规划编制全流程的 AI 辅助方法与模板。', detail: '从现状评估、目标定位到项目库与近期行动，梳理专项规划编制的 AI 辅助方法，附章节结构与范例。' },
      { slug: 'fund-apply',    title: '城市更新资金申报查询手册',        date: '2026.07', tag: '手册', icon: 'fund-apply',    desc: '资金申报口径与查询要点，便于随时备查。', detail: '归集专项债、政策性金融工具、中央预算内投资等资金渠道的申报口径与查询路径，做成可随时翻查的手册。' },
      { slug: 'district-plan', title: '城市更新片区策划 AI 指南',       date: '2026.06', tag: '指南', icon: 'district-plan', desc: '片区策划报告的 AI 生成思路、结构与范例。', detail: '围绕片区策划的定位、容量、业态与实施，给出 AI 生成的思路、报告结构与可套用范例。' },
      { slug: 'ai-design',     title: 'AI 工具策划设计指南',   date: '2026.07', tag: '指南', icon: 'ai-design',     desc: '梳理策划、设计环节里能落地的 AI 工具与用法。', detail: '面向策划与设计环节，盘点可用的 AI 工具与组合打法，附实操路径与产出示例，让 AI 真正进到工作流里。' },
      { slug: 'planning-ai',   title: '规划设计 AI 一页纸', date: '2026.06', tag: '笔记', icon: 'planning-ai',   desc: '规划设计业务里的 AI 技术要点，一页速览。', detail: '把规划设计业务的 AI 技术要点压缩成一页：能力边界、适用场景、工具清单与落地建议，方便快速建立全局认知。' },
      { slug: 'community-report', title: '完整社区建设策划与实施研究报告', date: '2026.08', tag: '报告', icon: 'district-plan', desc: '政策依据 · 技术标准 · 经验案例 · 编制大纲。', detail: '完整社区建设从政策到落地的系统研究报告：政策沿革、技术标准、申报流程、资金来源、经验案例与策划编制大纲，含湘国差异对比与住建部可复制经验清单，多章节深色高对比网页版。' }
    ]
  },
  {
    id: 'ai',
    title: 'AI 札记',
    subtitle: 'AI 与技术教学的点滴沉淀，未必专业，重在使用。',
    tag: '公开',
    visibility: 'public',
    zone: 'public',
    articles: [
      { slug: 'ai-agent',      title: 'AI-Agent 教学指南',    date: '2026.07', tag: '教学', icon: 'ai-agent',      desc: '面向零基础，讲清智能体的概念、搭建与教学示范。', detail: '从"什么是智能体"到最小可跑的搭建步骤，配教学示范，帮零基础读者建立可操作的认知。' },
      { slug: 'coding',        title: '编程思维速成',      date: '2026.07', tag: '教学', icon: 'coding',        desc: '用最少的概念建立编程思维，适合入门与教学。', detail: '用最少的概念串起变量、循环、函数与调试，建立编程直觉，适合入门教学与自学。' }
    ]
  },
  {
    id: 'kids',
    title: '给孩子',
    subtitle: '为娃准备的内容，可分享链接。',
    tag: '公开',
    visibility: 'public',
    zone: 'private',
    articles: [
      { slug: 'freshman',        title: '新生暑假指南',      date: '2026.07', tag: '指南', icon: 'freshman',        desc: '写给准大一新生的暑期安排与入学准备建议。', detail: '面向准大一新生，梳理暑期该做的准备、入学清单与心态调整，帮娃平稳过渡到大学生活。' },
      { slug: 'yangziyu-summer', title: '杨子禺暑假计划表',   date: '2026.07', tag: '手作', icon: 'yangziyu-summer', desc: '为杨子禺定制的暑期学习安排与课程排期。', detail: '为杨子禺量身定制的暑期排期，含学习节奏、课程与休息安排，可随时对照执行。' },
      { slug: 'food-drug-env',   title: '食药环侦查 AI 应用指南',   date: '2026.07', tag: '指南', icon: 'food-drug-env',   desc: '把 AI 用到食药环场景，给孩子讲清可复用的思路与模板。', detail: '用孩子能懂的方式，把 AI 拆进食药环侦查场景，给出可复用的思路、模板与小练习。' },
      { slug: 'birthday-card',   title: '贺卡',               date: '2026.07', tag: '贺卡', icon: 'birthday-card',   desc: '可分享的电子贺卡，点开即见。', detail: '一张可分享的电子贺卡，点开即见，适合节日与生日祝福。' },
      { slug: 'birthday-game',   title: '休闲小游戏',         date: '2026.07', tag: '游戏', icon: 'birthday-game',   desc: '为孩子准备的小游戏，轻松一刻。', detail: '一个轻量的休闲小游戏，给孩子在碎片时间放松一下，点开即玩。' },
      { slug: 'prime-hunter',    title: '质数小游戏',         date: '2026.07', tag: '游戏', icon: 'prime-hunter',    desc: '在网格中找出质数，练眼力也练数感。', detail: '在网格里快速识别质数，既练眼力也练数感，适合当数学小练手。' },
      { slug: 'daily-todo',      title: 'todolist',           date: '2026.07', tag: '自用', icon: 'daily-todo',     desc: '每日待办与节奏管理清单。', detail: '一份每日待办与节奏管理清单，帮娃把一天安排得清清楚楚。' },
      { slug: 'summer-reading',  title: '字里行间 · 消暑纳凉（美文读书）', date: '2026.07', tag: '美文', icon: 'summer-reading', desc: '14 期消暑美文，配朗读音频，给孩子的一方清凉书房。', detail: '14 期消暑美文，配朗读音频，给孩子在夏天的一方清凉书房，可听可读。' }
    ]
  },
  {
    id: 'essays',
    title: '散文 · 手记',
    subtitle: '写给自己的字。关于父亲，关于送别，关于散场。',
    tag: '散文',
    visibility: 'public',
    zone: 'private',
    articles: [
      { slug: 'sanchang', title: '散场', date: '2026.08', tag: '散文', icon: 'sanchang', desc: '父子一场的记忆：父亲扛着黑箱子送我上学，我坐在车里送儿子离开。', detail: '从三十多年前父亲肩上的黑樟木箱，到如今带轮子的硬壳箱；从一个"噢"，到另一个"噢"。远送于野，瞻望弗及。' }
    ]
  },
  {
    id: 'private',
    title: '私人手记',
    subtitle: '不愿示人的字，仅直链可达。',
    tag: '仅直链',
    visibility: 'private',
    zone: 'private',
    articles: [
      { slug: 'shanxi-travel', title: '山西旅行计划', date: '2026.07', tag: '游记', icon: 'shanxi-travel', desc: '一家四口的五台山还愿之旅，含行程与花销。', detail: '一家四口的五台山还愿之旅，含每日行程、交通与花销测算，方便照着走。' }
    ]
  },
  {
    id: 'wechat',
    title: '微信公众号',
    subtitle: '已发布的公众号文章归档，便于随时取用。',
    tag: '公开',
    visibility: 'public',
    zone: 'private',
    articles: [
      { slug: '开学季', title: '大学开学季：父母说1500够，孩子说3000不够', date: '2026.08', tag: '公众号', icon: 'wechat', desc: '生活费之争背后的代际认知差异，一篇写给父母也写给孩子的话。', detail: '从开学季生活费之争切入，谈代际认知差异与沟通，一篇写给父母也写给孩子的话。' },
      { slug: '长鑫',   title: '长鑫引爆万亿浮盈：政府股权投资的逻辑与误区', date: '2026.08', tag: '公众号', icon: 'changxin', desc: '从长鑫案例拆解政府股权投资的底层逻辑与常见误读。', detail: '以长鑫案例拆解政府股权投资的底层逻辑、估值方法与常见误读，厘清"管资本"与"管企业"的分野。' },
      { slug: '原拆原建', title: '原拆原建：城市更新的第三条路径', date: '2026.07', tag: '研究', icon: 'yuanchai', desc: '政策演进、实践模式与市县推进的城市更新研究。', detail: '系统梳理原拆原建模式的政策演进、八类典型案例与三种主要路径，为市县推进危旧房改造提供参考。' }
    ]
  }
];
