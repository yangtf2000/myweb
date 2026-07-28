window.COURSE = window.COURSE || [];

/* ============ 第 3 课 ============ */
window.COURSE.push({
  id:"l3", mod:2, emoji:"🌍",
  title:"第 3 课 · 编程语言地图",
  sub:"语言卡片集（本课程最厚的一课，可分两天看）。每张卡片都是同一个结构：身份证 → 主战场 → 长相特征 → 代码解剖图 → 常用命令速查 → 一句话点评。目标：见到代码能认出语言、猜出用途。",
  cards:[
    {tag:"语言卡 1 · Python", title:"Python 🐍 —— 万金油，小白的第一语言", ac:"green", html:`
      <table class="tbl">
        <tr><th style="width:110px">身份证</th><td>1991 年生 · <b>解释型</b>（写完就能跑）· 语法接近英语 · 难度 ★☆☆☆☆</td></tr>
        <tr><th>主战场</th><td>数据分析、AI/机器学习、自动化脚本、爬虫、科学计算。<b>ChatGPT 的训练代码、豆瓣网站、大量科研论文的图</b>都出自它。</td></tr>
      </table>
      <p><strong>长相特征（一眼认出它）：</strong></p>
      <ul>
        <li>靠<em>缩进</em>（空 4 格）表示层级，<strong>没有花括号 { }，行尾没有分号 ;</strong></li>
        <li>注释用 <code class="inl">#</code> 开头</li>
        <li>关键词都是小写英文单词：<code class="inl">def</code> <code class="inl">if</code> <code class="inl">for</code> <code class="inl">import</code></li>
      </ul>
      <p><strong>代码解剖图</strong>——一个「成绩单统计」小程序，逐行看懂：</p>
      <div class="anat">
        <div class="hd">代码</div><div class="hd">这行在干嘛</div>
        <div class="cl">scores = [92, 85, 58, 77, 66]</div><div class="an">变量：把 5 个成绩装进名叫 scores 的列表</div>
        <div class="cl">passed = 0</div><div class="an">变量：准备一个计数器，从 0 开始</div>
        <div class="cl">for s in scores:</div><div class="an">循环：对列表里每个成绩 s，都执行下面缩进的代码</div>
        <div class="cl">    if s >= 60:</div><div class="an">判断：如果这个成绩及格了……</div>
        <div class="cl">        passed = passed + 1</div><div class="an">……计数器就加 1（注意两层缩进=两层嵌套）</div>
        <div class="cl">avg = sum(scores) / len(scores)</div><div class="an">调用函数：sum 求和、len 数个数，算出平均分</div>
        <div class="cl">print("及格人数:", passed)</div><div class="an">输出：把结果打印到屏幕 → 及格人数: 4</div>
        <div class="cl">print("平均分:", avg)</div><div class="an">输出：→ 平均分: 75.6</div>
      </div>
      <p><strong>常用命令速查：</strong></p>
      <table class="tbl">
        <tr><th>想干嘛</th><th>写法</th><th>白话解读</th></tr>
        <tr><td>输出</td><td><code class="inl">print("你好")</code></td><td>往屏幕上打印东西</td></tr>
        <tr><td>输入</td><td><code class="inl">name = input("请输入:")</code></td><td>等用户敲键盘，结果装进 name</td></tr>
        <tr><td>判断</td><td><code class="inl">if x > 0: ... else: ...</code></td><td>如果…否则…（注意冒号和缩进）</td></tr>
        <tr><td>循环</td><td><code class="inl">for i in range(10):</code></td><td>重复 10 次（i 从 0 数到 9）</td></tr>
        <tr><td>函数</td><td><code class="inl">def hello(name):</code></td><td>def = define，定义一个功能块</td></tr>
        <tr><td>装轮子</td><td><code class="inl">pip install pandas</code></td><td>在终端里下载安装第三方库</td></tr>
        <tr><td>运行</td><td><code class="inl">python 文件名.py</code></td><td>在终端里让脚本跑起来</td></tr>
      </table>
      <div class="quote">一句话点评：能用最少的代码干最多的事，AI 时代的「普通话」。非计算机专业只学一门语言的话，就是它。</div>
    `},
    {tag:"语言卡 2 · 网页三件套", title:"HTML + CSS + JavaScript 🌐 —— 网页世界的铁三角", ac:"amber", html:`
      <table class="tbl">
        <tr><th style="width:110px">身份证</th><td>HTML(1993)/CSS(1996)/JS(1995) · JS 为<b>解释型</b> · 浏览器就能跑，零安装 · 难度 ★★☆☆☆</td></tr>
        <tr><th>主战场</th><td>一切网页和网页应用。<b>你现在看的这个课程页面，就是这三件套写的！</b>微信小程序、很多桌面应用（如 VS Code 本身）也是 JS 写的。</td></tr>
      </table>
      <p><strong>关键认知：它们是一伙的，分工明确——</strong></p>
      <ul>
        <li><strong class="hl-a">HTML</strong> = 骨架（页面上有什么：标题、按钮、图片）</li>
        <li><strong class="hl-g">CSS</strong> = 皮肤（长什么样：颜色、大小、位置）</li>
        <li><strong class="hl-p">JavaScript</strong> = 动作（会做什么：点击、跳转、计算）</li>
      </ul>
      <p><strong>长相特征：</strong>HTML 全是 <code class="inl">&lt;尖括号标签&gt;</code> 成对出现；CSS 是 <code class="inl">选择器 { 属性: 值; }</code>；JS 有花括号和分号，关键词 <code class="inl">let / const / function</code>。</p>
      <p><strong>代码解剖图</strong>——一个「点按钮变颜色」的完整网页（三种代码同框）：</p>
      <div class="anat">
        <div class="hd">代码</div><div class="hd">这行在干嘛</div>
        <div class="cl">&lt;h1 id="title"&gt;你好，世界&lt;/h1&gt;</div><div class="an">HTML：放一个大标题，取名 title 方便 JS 找到它</div>
        <div class="cl">&lt;button onclick="change()"&gt;点我&lt;/button&gt;</div><div class="an">HTML：放一个按钮，点击时执行 change 函数</div>
        <div class="cl">&lt;style&gt;</div><div class="an">CSS 区域开始（皮肤部分）</div>
        <div class="cl">  h1 { color: white; }</div><div class="an">CSS：所有 h1 标题的文字设成白色</div>
        <div class="cl">&lt;/style&gt;</div><div class="an">CSS 区域结束</div>
        <div class="cl">&lt;script&gt;</div><div class="an">JS 区域开始（动作部分）</div>
        <div class="cl">function change() {</div><div class="an">JS：定义 change 函数（花括号包住函数体）</div>
        <div class="cl">  let t = document.getElementById("title");</div><div class="an">JS：在页面里找到那个叫 title 的标题，存进变量 t</div>
        <div class="cl">  t.style.color = "hotpink";</div><div class="an">JS：把它的文字颜色改成粉色——页面立刻变化！</div>
        <div class="cl">}</div><div class="an">函数结束</div>
        <div class="cl">&lt;/script&gt;</div><div class="an">JS 区域结束</div>
      </div>
      <p><strong>JS 常用命令速查：</strong></p>
      <table class="tbl">
        <tr><th>想干嘛</th><th>写法</th><th>白话解读</th></tr>
        <tr><td>输出(调试用)</td><td><code class="inl">console.log("hi")</code></td><td>打印到浏览器控制台（按 F12 能看到）</td></tr>
        <tr><td>变量</td><td><code class="inl">let x = 5; const y = 10;</code></td><td>let 可变，const 不可变</td></tr>
        <tr><td>函数</td><td><code class="inl">function add(a,b){ return a+b; }</code></td><td>用花括号包住函数体</td></tr>
        <tr><td>找页面元素</td><td><code class="inl">document.getElementById("id")</code></td><td>「在文档里按 id 找元素」——JS 操作网页的起手式</td></tr>
        <tr><td>响应点击</td><td><code class="inl">btn.onclick = function(){...}</code></td><td>给按钮绑定「被点击时做什么」</td></tr>
      </table>
      <div class="quote">一句话点评：想「做出来的东西能立刻给别人看」，学它。一个 .html 文件双击就能跑，成就感来得最快。</div>
    `},
    {tag:"语言卡 3 · C / C++", title:"C / C++ ⚡ —— 性能之王，离机器最近", ac:"blue", html:`
      <table class="tbl">
        <tr><th style="width:110px">身份证</th><td>C(1972)/C++(1985) · <b>编译型</b>（先整体翻译成机器码再跑）· 手动管理内存 · 难度 ★★★★★</td></tr>
        <tr><th>主战场</th><td>操作系统（Windows/Linux 内核）、游戏引擎（Unreal）、嵌入式/单片机、高频交易。<b>追求极致速度的地方都是它。</b>工科生的单片机课大概率用 C。</td></tr>
      </table>
      <p><strong>长相特征：</strong>① <code class="inl">#include</code> 开头；② 花括号 <code class="inl">{ }</code> 和分号 <code class="inl">;</code> 满天飞；③ <strong>变量必须先声明类型</strong>（int 整数 / float 小数 / char 字符）；④ 必有一个 <code class="inl">main</code> 函数作为入口。</p>
      <p><strong>代码解剖图</strong>——C 版「猜数字」核心片段，和 Python 对照看：</p>
      <div class="anat">
        <div class="hd">代码</div><div class="hd">这行在干嘛</div>
        <div class="cl">#include &lt;stdio.h&gt;</div><div class="an">搬来「标准输入输出」工具箱（相当于 Python 的 import）</div>
        <div class="cl">int main() {</div><div class="an">主函数：程序从这里开始执行（C 程序的固定仪式）</div>
        <div class="cl">    int answer = 42;</div><div class="an">变量：装个整数。注意必须写明 int（整数类型）</div>
        <div class="cl">    int guess = 0;</div><div class="an">再声明一个整数变量，存用户猜的数</div>
        <div class="cl">    while (guess != answer) {</div><div class="an">循环：只要没猜中就一直转（!= 表示不等于）</div>
        <div class="cl">        scanf("%d", &amp;guess);</div><div class="an">输入：读用户敲的数字（写法确实很怪，先眼熟）</div>
        <div class="cl">        printf("再猜!\\n");</div><div class="an">输出：打印提示（\\n 表示换行）</div>
        <div class="cl">    }</div><div class="an">循环体结束（C 用花括号而不是缩进划范围）</div>
        <div class="cl">    printf("猜对了!\\n");</div><div class="an">跳出循环，说明猜中了</div>
        <div class="cl">    return 0;</div><div class="an">向系统报告「正常结束」（0 = 一切顺利）</div>
        <div class="cl">}</div><div class="an">主函数结束</div>
      </div>
      <p><strong>常用命令速查：</strong></p>
      <table class="tbl">
        <tr><th>想干嘛</th><th>写法</th><th>白话解读</th></tr>
        <tr><td>输出</td><td><code class="inl">printf("分数是 %d", score);</code></td><td>%d 是占位符：这里填一个整数</td></tr>
        <tr><td>变量</td><td><code class="inl">int a = 5; float b = 3.14;</code></td><td>先说类型再起名，类型定了就不能变</td></tr>
        <tr><td>判断/循环</td><td><code class="inl">if (x&gt;0) {...}  for (int i=0; i&lt;10; i++) {...}</code></td><td>条件必须加圆括号，范围用花括号</td></tr>
        <tr><td>编译</td><td><code class="inl">gcc hello.c -o hello</code></td><td>把源代码翻译成可执行文件（Python 没有这步）</td></tr>
        <tr><td>运行</td><td><code class="inl">./hello</code></td><td>执行刚编译出来的程序</td></tr>
      </table>
      <div class="quote">一句话点评：编程界的「手动挡赛车」——难开，但懂它才真正理解计算机在干什么。小白不必学，但要认得出。</div>
    `},
    {tag:"语言卡 4 · Java", title:"Java ☕ —— 企业级老将，稳字当头", ac:"red", html:`
      <table class="tbl">
        <tr><th style="width:110px">身份证</th><td>1995 年生 · <b>编译+虚拟机</b>（一次编写，到处运行）· 万物皆类(class) · 难度 ★★★★☆</td></tr>
        <tr><th>主战场</th><td>大型企业后端（银行、电商、12306）、安卓 App（老一代）。<b>淘宝、美团的后端大量是 Java。</b>招聘量常年第一梯队。</td></tr>
      </table>
      <p><strong>长相特征：</strong>① 一切代码都包在 <code class="inl">class</code> 里；② 关键词又多又长（public static void...）；③ 花括号+分号；④ 变量要声明类型（和 C 一样）。识别口诀：<strong>看到 <code class="inl">public class</code> 和 <code class="inl">System.out.println</code>，必是 Java。</strong></p>
      <p><strong>代码解剖图</strong>——最小可运行程序，感受它的「仪式感」：</p>
      <div class="anat">
        <div class="hd">代码</div><div class="hd">这行在干嘛</div>
        <div class="cl">public class Hello {</div><div class="an">定义一个类（Java 规定：代码必须住在类里面）</div>
        <div class="cl">    public static void main(String[] args) {</div><div class="an">主方法：固定咒语，程序入口（先背下来别纠结）</div>
        <div class="cl">        String name = "世界";</div><div class="an">变量：声明一个字符串（String = 文字类型）</div>
        <div class="cl">        System.out.println("你好, " + name);</div><div class="an">输出：打印「你好, 世界」（+ 号拼接文字）</div>
        <div class="cl">    }</div><div class="an">主方法结束</div>
        <div class="cl">}</div><div class="an">类结束——同样功能 Python 只要 2 行，Java 要 6 行</div>
      </div>
      <p><strong>常用命令速查：</strong><code class="inl">System.out.println()</code> 输出 · <code class="inl">int / String / double</code> 类型声明 · <code class="inl">javac Hello.java</code> 编译 · <code class="inl">java Hello</code> 运行</p>
      <div class="quote">一句话点评：像西装革履的国企员工——规矩多、啰嗦，但极其可靠。将来想进大厂做后端再学它不迟。</div>
    `},
    {tag:"语言卡 5 · SQL", title:"SQL 🗃️ —— 和数据库对话的语言", ac:"purple", html:`
      <table class="tbl">
        <tr><th style="width:110px">身份证</th><td>1974 年生 · 不是通用编程语言，是<b>查询语言</b> · 一句话=一条完整指令 · 难度 ★★☆☆☆</td></tr>
        <tr><th>主战场</th><td>一切「从数据库里找数据」的场合。<b>产品经理、运营、财务、数据分析师用得比程序员还多</b>——很多岗位的招聘要求就一条技术技能：会 SQL。</td></tr>
      </table>
      <p><strong>关键认知：</strong>SQL 不是「编程序」，是「<strong>提问题</strong>」。你用接近英语的句子向数据库提问，它把答案（表格）递给你。</p>
      <p><strong>长相特征：</strong>关键词习惯全大写（SELECT / FROM / WHERE），一眼看去像英语填空题。</p>
      <p><strong>代码解剖图</strong>——一句典型查询，逐词拆解：</p>
      <div class="anat">
        <div class="hd">代码</div><div class="hd">这个词在干嘛</div>
        <div class="cl">SELECT name, score</div><div class="an">「我要看这两列」：姓名和成绩</div>
        <div class="cl">FROM students</div><div class="an">「从 students 这张表里找」</div>
        <div class="cl">WHERE score &gt; 90</div><div class="an">「只要成绩大于 90 的行」（筛选条件）</div>
        <div class="cl">ORDER BY score DESC</div><div class="an">「按成绩从高到低排」（DESC=降序）</div>
        <div class="cl">LIMIT 10;</div><div class="an">「只给我前 10 名」——整句连读就是一个完整问题</div>
      </div>
      <p><strong>常用命令速查：</strong></p>
      <table class="tbl">
        <tr><th>想干嘛</th><th>写法</th><th>白话解读</th></tr>
        <tr><td>查数据</td><td><code class="inl">SELECT * FROM 表</code></td><td>* = 所有列，整表拿来</td></tr>
        <tr><td>筛条件</td><td><code class="inl">WHERE age &gt;= 18 AND city='北京'</code></td><td>多条件用 AND / OR 连接</td></tr>
        <tr><td>统计</td><td><code class="inl">SELECT COUNT(*), AVG(score) FROM 表</code></td><td>数个数、算平均，还有 SUM/MAX/MIN</td></tr>
        <tr><td>分组</td><td><code class="inl">GROUP BY 班级</code></td><td>按班级分别统计（Excel 数据透视表既视感）</td></tr>
        <tr><td>加数据</td><td><code class="inl">INSERT INTO 表 VALUES (...)</code></td><td>往表里插一行新记录</td></tr>
      </table>
      <div class="quote">一句话点评：性价比之王——学一个下午就能用，用一辈子。未来不管什么岗位，会 SQL 都是加分项。</div>
    `},
    {tag:"语言卡 6 · 速览", title:"其他语言一句话速览 🎯", ac:"cyan", html:`
      <p>这些语言不用学，认识长相、知道定位即可：</p>
      <table class="tbl">
        <tr><th>语言</th><th>一句话定位</th><th>长相特征（一行示例）</th></tr>
        <tr><td><b>Go</b></td><td>云时代新贵，服务器端简洁高效（Docker、K8s 都是它写的）</td><td><code class="inl">func main() { fmt.Println("hi") }</code></td></tr>
        <tr><td><b>Swift</b></td><td>苹果御用：iPhone/Mac App 开发</td><td><code class="inl">var name = "hi"; print(name)</code></td></tr>
        <tr><td><b>Kotlin</b></td><td>安卓官方推荐语言，Java 的年轻继任者</td><td><code class="inl">fun main() { println("hi") }</code></td></tr>
        <tr><td><b>C#</b></td><td>微软系 + Unity 游戏开发主力</td><td><code class="inl">Console.WriteLine("hi");</code></td></tr>
        <tr><td><b>MATLAB</b></td><td>工科课程标配：矩阵计算、仿真</td><td><code class="inl">x = [1 2 3]; plot(x)</code></td></tr>
        <tr><td><b>R</b></td><td>统计学专业最爱：统计分析与作图</td><td><code class="inl">mean(c(92, 85, 77))</code></td></tr>
        <tr><td><b>Rust</b></td><td>C++ 的安全版挑战者，近年最受喜爱语言</td><td><code class="inl">fn main() { println!("hi"); }</code></td></tr>
      </table>
    `},
    {tag:"语言卡 7 · 辨认训练", title:"辨认训练：靠长相认语言 🔍", ac:"pink", html:`
      <p>把「识别特征」浓缩成一张速查表——以后看到代码，先扫这几个特征：</p>
      <table class="tbl">
        <tr><th>看到什么</th><th>基本就是</th></tr>
        <tr><td>没有花括号、靠缩进分层、<code class="inl">def</code> / <code class="inl">import</code></td><td><b class="hl-g">Python</b></td></tr>
        <tr><td>满屏 <code class="inl">&lt;标签&gt;内容&lt;/标签&gt;</code></td><td><b class="hl-a">HTML</b></td></tr>
        <tr><td><code class="inl">选择器 { 颜色: 值; }</code>，没有逻辑只有样式</td><td><b class="hl-a">CSS</b></td></tr>
        <tr><td><code class="inl">function</code> / <code class="inl">let</code> / <code class="inl">console.log</code> / <code class="inl">document.</code></td><td><b class="hl-a">JavaScript</b></td></tr>
        <tr><td><code class="inl">#include</code> / <code class="inl">printf</code> / <code class="inl">int main()</code></td><td><b class="hl-p">C</b>（有 cout / class 则是 C++）</td></tr>
        <tr><td><code class="inl">public class</code> / <code class="inl">System.out.println</code></td><td><b class="hl-p">Java</b></td></tr>
        <tr><td>大写的 <code class="inl">SELECT ... FROM ... WHERE</code></td><td><b class="hl-v">SQL</b></td></tr>
      </table>
      <div class="tip"><b>本课作业里有实战：</b>让 WorkBuddy 出 5 段无标注代码考你——现在这张表就是你的备考资料。</div>
    `},
    {tag:"语言卡 8 · 选择指南", title:"「我该看哪种语言？」对号入座 🧭", ac:"green", html:`
      <table class="tbl">
        <tr><th>你是 / 你想</th><th>推荐路线</th></tr>
        <tr><td>理工科（非计算机）</td><td><b>Python</b>（数据处理+科研作图）＋ 课内可能遇到 C / MATLAB</td></tr>
        <tr><td>经管 / 商科</td><td><b>Python + SQL</b>（数据分析黄金组合，求职硬通货）</td></tr>
        <tr><td>文科 / 社科</td><td><b>Python</b>（文本分析、问卷统计、爬资料）</td></tr>
        <tr><td>医学 / 生物</td><td><b>Python 或 R</b>（实验数据、生信分析）</td></tr>
        <tr><td>想做个网页 / 小程序给别人玩</td><td><b>HTML + CSS + JavaScript</b></td></tr>
        <tr><td>想做游戏</td><td>先玩 <b>Python</b>（pygame 小游戏）→ 认真做再学 C# (Unity)</td></tr>
        <tr><td>就想懂点编程、不确定用途</td><td><b>Python</b>，闭眼选</td></tr>
      </table>
      <div class="warn"><b>防坑提醒：</b>入门阶段千万别同时学两门语言——概念会打架。选定一门，其他的「认识长相」就够了。</div>
    `}
  ],
  practice:{
    intro:"语言地图看完了，来三连击：认语言 → 比语言 → 改代码跑通。全程 WorkBuddy 陪练。",
    tasks:[
      {name:"作业 1 · 语言辨认赛", desc:"先复习「辨认训练」卡片，然后开考。目标：5 段认对 3 段。",
       prompt:"考考我认编程语言的能力：随机给我 5 段不同语言的短代码（从 Python、JavaScript、HTML、C、Java、SQL 里选），不要说是什么语言，一段一段来让我猜。每段我猜完你公布答案，并指出这段代码的识别特征是什么。"},
      {name:"作业 2 · 三语对比", desc:"同一件事三种写法并排看，语言的「性格差异」立刻显形。",
       prompt:"请用 Python、JavaScript、C 三种语言分别实现同一个功能：输出 1 到 10 之间的所有偶数。三段代码并排展示（各自加中文注释），然后给我讲：三者在写法上最明显的 3 个差异是什么？为什么 C 看起来最啰嗦？"},
      {name:"作业 3 · 第一次改代码 ⭐", desc:"从「看懂」到「敢改」的关键一步。改错了也没关系，让 WorkBuddy 告诉你为什么。",
       prompt:"写一个 10 行以内的 Python 小程序：我输入名字，它输出一句个性化的欢迎语。先运行给我看效果。然后我会提出一个修改要求（比如：把欢迎语输出三遍、加上当前时间），我自己动手改代码贴给你，你帮我运行验证改得对不对，错了告诉我错哪了但先别直接给答案。"}
    ],
    pass:"5 段代码认对 3 段；成功亲手改对一处代码并验证跑通。"
  }
});
