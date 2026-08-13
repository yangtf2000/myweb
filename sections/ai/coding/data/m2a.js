window.COURSE = window.COURSE || [];

/* ============ 第 2 课 ============ */
window.COURSE.push({
  id:"l2", mod:2, emoji:"🔤",
  title:"第 2 课 · 看懂代码的最小词汇表",
  sub:"扫盲核心课。学完这 8 张卡片，任何语言的代码你都能看出个大概——因为所有语言的骨架都是这几样东西。",
  cards:[
    {tag:"卡片 1", title:"程序是什么：一份给计算机看的菜谱", ac:"cyan", html:`
      <p>把程序想象成一份菜谱：<strong>从上往下、一步一步执行的指令清单</strong>。</p>
      <pre class="code"><span class="c"># 「西红柿炒蛋」菜谱 vs 程序</span>
<span class="c"># 1. 打两个鸡蛋      →  取数据</span>
<span class="c"># 2. 如果没有葱，跳过撒葱花  →  条件判断</span>
<span class="c"># 3. 翻炒 30 下       →  循环</span>
<span class="c"># 4. 按「炒蛋标准流程」处理  →  调用函数</span></pre>
      <p>计算机唯一的特点是：<strong>绝对听话，绝对死板</strong>。菜谱写错一个字，人能猜出你的意思，计算机不能——这就是为什么会有 Bug。</p>
      <div class="tip"><b>读代码心法：</b>从上往下读，遇到不认识的词跳过去，先抓住「输入是什么 → 处理了什么 → 输出是什么」。</div>
    `},
    {tag:"卡片 2", title:"变量：给数据起名字的盒子", ac:"blue", html:`
      <p>变量 = 一个<strong>贴了名字标签的盒子</strong>，里面装数据。之后想用这个数据，喊名字就行。</p>
      <pre class="code">name = <span class="s">"小明"</span>        <span class="c"># 盒子叫 name，里面装文字"小明"</span>
age = <span class="n">18</span>             <span class="c"># 盒子叫 age，里面装数字 18</span>
age = age + <span class="n">1</span>       <span class="c"># 取出 18，加 1，把 19 放回盒子</span>
scores = [<span class="n">92</span>, <span class="n">85</span>, <span class="n">77</span>]  <span class="c"># 盒子里也能装一串数据（列表）</span></pre>
      <p>认代码技巧：看到 <code class="inl">xxx = yyy</code>，读作「把 yyy 装进名叫 xxx 的盒子」。<strong>等号在编程里不是"相等"，是"装入"。</strong></p>
    `},
    {tag:"卡片 3", title:"条件判断：程序的岔路口", ac:"purple", html:`
      <p><code class="inl">if / else</code> 就是「如果……就……否则……」，让程序会看情况办事：</p>
      <pre class="code"><span class="k">if</span> score >= <span class="n">60</span>:
    <span class="f">print</span>(<span class="s">"及格了！"</span>)      <span class="c"># 条件成立走这条路</span>
<span class="k">else</span>:
    <span class="f">print</span>(<span class="s">"下学期再见"</span>)    <span class="c"># 条件不成立走这条路</span></pre>
      <p>生活中的对应物到处都是：自动门（<em>如果</em>有人靠近<em>就</em>开门）、验证码（<em>如果</em>输对了<em>就</em>放行）。</p>
      <p>认代码技巧：看到 <code class="inl">if</code> 就知道——<strong>下面的代码分岔了，不是每一行都会执行</strong>。</p>
    `},
    {tag:"卡片 4", title:"循环：让机器替你重复干活", ac:"pink", html:`
      <p>循环是编程的灵魂——<strong>人类最讨厌重复，机器最擅长重复</strong>。</p>
      <pre class="code"><span class="k">for</span> student <span class="k">in</span> class_list:      <span class="c"># 对名单里的每个学生……</span>
    <span class="f">send_email</span>(student)          <span class="c"># ……发一封邮件</span>

<span class="k">while</span> temperature < <span class="n">100</span>:        <span class="c"># 只要水温没到 100 度……</span>
    <span class="f">keep_heating</span>()               <span class="c"># ……就继续加热</span></pre>
      <ul>
        <li><code class="inl">for</code>：「对这一堆东西，每个都来一遍」——次数明确</li>
        <li><code class="inl">while</code>：「只要条件还成立，就一直做」——次数看情况</li>
      </ul>
      <p>认代码技巧：看到 <code class="inl">for</code> / <code class="inl">while</code>，就知道<strong>它下面缩进的部分会被执行很多遍</strong>——这往往就是程序「省人力」的核心所在。</p>
    `},
    {tag:"卡片 5", title:"函数：打包好的功能块", ac:"green", html:`
      <p>把一段常用的操作打包、起个名字，以后一喊名字就执行——这就是函数。</p>
      <pre class="code"><span class="k">def</span> <span class="f">make_coffee</span>(sugar):        <span class="c"># 定义一个函数，叫 make_coffee</span>
    <span class="f">grind_beans</span>()               <span class="c"># 磨豆子</span>
    <span class="f">brew</span>()                      <span class="c"># 冲泡</span>
    <span class="f">add_sugar</span>(sugar)            <span class="c"># 按要求加糖</span>
    <span class="k">return</span> <span class="s">"你的咖啡好了"</span>      <span class="c"># 交出结果</span>

<span class="f">make_coffee</span>(<span class="n">2</span>)                  <span class="c"># 调用它：来杯两块糖的咖啡</span></pre>
      <ul>
        <li>括号里的东西叫<strong>参数</strong>——同一台咖啡机，糖量可以每次不同</li>
        <li><code class="inl">return</code> 是<strong>交货</strong>——函数干完活把结果递出来</li>
      </ul>
      <p>认代码技巧：<code class="inl">名字(东西)</code> 这个长相 = 调用函数，读作「用<em>东西</em>去执行<em>名字</em>这个功能」。<code class="inl">print("hi")</code> 就是「用 "hi" 执行打印功能」。</p>
    `},
    {tag:"卡片 6", title:"库/包：别人造好的轮子", ac:"amber", html:`
      <p>你想画图表，不用从「怎么画一个像素」学起——早有人写好了完整的画图工具包，你<strong>拿来就用</strong>。这些打包好的工具叫<strong>库（library）/ 包（package）</strong>。</p>
      <pre class="code"><span class="k">import</span> pandas            <span class="c"># 搬来"表格处理"工具箱</span>
<span class="k">import</span> matplotlib        <span class="c"># 搬来"画图"工具箱</span>

data = pandas.<span class="f">read_excel</span>(<span class="s">"成绩.xlsx"</span>)   <span class="c"># 用它读 Excel，一行搞定</span></pre>
      <p>这就是为什么 Python 能「几行代码干大事」——它有全世界最丰富的库生态。<strong>会找轮子、会用轮子，比会造轮子重要得多。</strong></p>
      <p>认代码技巧：文件开头一堆 <code class="inl">import xxx</code>，等于这段代码的「食材采购清单」——看它 import 了什么，基本能猜到程序是干嘛的（import matplotlib ≈ 要画图了）。</p>
    `},
    {tag:"卡片 7", title:"报错与 Bug：程序不听话时它在说什么", ac:"red", html:`
      <p>先纠正心态：<strong>报错不是失败，是程序在跟你说话</strong>。职业程序员每天也在和报错打交道。</p>
      <pre class="code">Traceback (most recent call last):
  File <span class="s">"test.py"</span>, line <span class="n">3</span>, in &lt;module&gt;
    <span class="f">print</span>(scroe)
<span class="k">NameError</span>: name <span class="s">'scroe'</span> is not defined</pre>
      <p>读报错三步法（从下往上读）：</p>
      <ol>
        <li><strong>最后一行是诊断书</strong>：NameError = 名字错误，'scroe' 没有定义（其实是把 score 拼错了）</li>
        <li><strong>line 3 是案发地点</strong>：错误发生在第 3 行</li>
        <li><strong>看不懂就复制整段报错去问 AI</strong>——这是 AI 时代最快的调试方式</li>
      </ol>
      <div class="tip"><b>黑话扫盲：</b>Bug（虫子）= 程序错误，源自 1947 年一只真飞蛾卡在计算机里；Debug（除虫）= 找错改错。</div>
    `},
    {tag:"卡片 8", title:"高频黑话速查表", ac:"cyan", html:`
      <p>听人聊技术时的「防懵词典」，混个眼熟即可：</p>
      <table class="tbl">
        <tr><th>黑话</th><th>人话</th></tr>
        <tr><td><b>编译 vs 解释</b></td><td>编译=整本菜谱先翻译成机器语言再执行（C/C++，快）；解释=边读边翻译边执行（Python，灵活）</td></tr>
        <tr><td><b>前端 vs 后端</b></td><td>前端=你看得见的界面；后端=背后干活的服务器逻辑和数据</td></tr>
        <tr><td><b>IDE</b></td><td>集成开发环境=程序员的「全能写字台」（写代码+运行+调试一体，如 VS Code）</td></tr>
        <tr><td><b>API</b></td><td>程序之间的「服务窗口」——你的程序去窗口喊一嗓子，对方把数据递出来</td></tr>
        <tr><td><b>开源</b></td><td>代码公开、人人可看可用可改（免费轮子的来源）</td></tr>
        <tr><td><b>数据库</b></td><td>专门存数据的仓库软件，用 SQL 语言跟它对话</td></tr>
        <tr><td><b>算法</b></td><td>解决问题的具体步骤套路（同一件事，好算法快 1000 倍）</td></tr>
        <tr><td><b>部署</b></td><td>把程序放到服务器上，让所有人都能访问</td></tr>
      </table>
    `}
  ],
  practice:{
    intro:"词汇表背不背无所谓，能认出来才算数。让 WorkBuddy 当出题官，玩三轮「代码猜猜猜」。",
    tasks:[
      {name:"作业 1 · 代码猜猜猜", desc:"让 WorkBuddy 出题，你来猜。猜错没关系，讲解才是重点。",
       prompt:"我刚学了变量、if判断、for循环、函数这些概念。请给我出题：给我 3 段 5 行以内的 Python 小代码，一段一段来。每段我先猜它是干嘛的，我猜完你再公布答案并逐行讲解。开始出第一题吧。"},
      {name:"作业 2 · 成分指认", desc:"像语文课划句子成分一样，指认代码成分。",
       prompt:"请写一段 15 行左右的 Python 小程序（内容要同时包含：变量、for循环、if判断、函数定义和调用、import 一个库），先带中文注释给我看一遍；然后把注释全部去掉重新贴一遍，我来逐行指认每行是什么成分（变量赋值/循环/判断/函数……），我说完你批改。"},
      {name:"作业 3 · 读一次报错", desc:"主动体验一次报错，学会从报错信息里找线索。",
       prompt:"请写一段 6 行左右、故意含有 1 个错误的 Python 代码，先运行给我看报错信息，但不要告诉我错在哪。我根据报错信息猜错误原因，猜完你再讲解，并教我这类报错以后怎么快速定位。"}
    ],
    pass:"作业 1 的 3 段代码猜对 2 段；作业 2 的成分指认正确率过半。"
  }
});
