window.COURSE = window.COURSE || [];

/* ============ 第 5 课 ============ */
window.COURSE.push({
  id:"l5", mod:3, emoji:"🧰",
  title:"第 5 课 · 编程工具箱",
  sub:"工欲善其事，必先识其器。这一课认识编程常用软件——每个工具：是什么、用来干嘛、适合谁。",
  cards:[
    {tag:"工具卡 1", title:"VS Code —— 世界上最流行的代码编辑器", ac:"blue", html:`
      <table class="tbl">
        <tr><th style="width:100px">是什么</th><td>微软出品的<b>免费</b>代码编辑器（全称 Visual Studio Code），全球程序员使用率第一</td></tr>
        <tr><th>用来干嘛</th><td>写代码（所有语言通吃）、运行调试、管理项目文件；靠海量插件无限扩展</td></tr>
        <tr><th>适合谁</th><td>所有人。轻量、免费、中文界面，小白的标准起点</td></tr>
        <tr><th>上手难度</th><td>★★☆☆☆（装好 + 装个中文插件 + 装个 Python 插件即可开工）</td></tr>
      </table>
      <p>认知点：<strong>编辑器 ≠ 语言</strong>。VS Code 只是「写字台」，Python 才是「笔」——第 6 课我们会把两者都装好。</p>
      <div class="tip"><b>容易搞混：</b>「Visual Studio」（不带 Code）是另一个更重型的软件，主打 C++/C# 大型开发。小白装 <b>VS Code</b> 就对了。</div>
    `},
    {tag:"工具卡 2", title:"Jupyter Notebook —— 边写边看的实验本", ac:"amber", html:`
      <table class="tbl">
        <tr><th style="width:100px">是什么</th><td>把代码切成一小格一小格执行的「笔记本」，代码、运行结果、文字笔记混排在同一页</td></tr>
        <tr><th>用来干嘛</th><td>数据分析、科研计算的标配：跑一步看一步图，特别适合探索数据</td></tr>
        <tr><th>适合谁</th><td>要处理数据/做科研的同学（理工科、经管统计方向重点关注）</td></tr>
        <tr><th>上手难度</th><td>★★☆☆☆（VS Code 里装个插件就能用）</td></tr>
      </table>
      <p>它改变了工作方式：传统脚本要「整个跑完才见结果」，Notebook 可以「跑一格、看一眼、再写下一格」——试错成本极低。</p>
    `},
    {tag:"工具卡 3", title:"在线编程平台 —— 浏览器里直接写，零安装", ac:"green", html:`
      <p>不想折腾安装？打开浏览器就能写代码：</p>
      <table class="tbl">
        <tr><th>平台</th><th>特点</th></tr>
        <tr><td><b>腾讯云 Cloud Studio</b></td><td>国内访问快，浏览器版 VS Code，免费额度够学习用</td></tr>
        <tr><td><b>Replit</b></td><td>老牌在线 IDE，支持几十种语言，社区活跃</td></tr>
        <tr><td><b>Google Colab</b></td><td>在线 Jupyter + 免费 GPU，跑 AI 模型入门首选（需科学上网）</td></tr>
      </table>
      <p>适用场景：临时试一段代码、电脑配置差、还没装好本地环境的过渡期。<strong>正经长期学习还是建议装本地环境</strong>（第 6 课）。</p>
    `},
    {tag:"工具卡 4", title:"AI 编程工具集 —— 三种形态，三种玩法", ac:"pink", html:`
      <p>AI 编程工具已经分化出三个梯队，按「AI 自主程度」从低到高：</p>
      <table class="tbl">
        <tr><th>形态</th><th>代表</th><th>玩法</th></tr>
        <tr><td><b>① 对话式</b><br>（问答型）</td><td>ChatGPT、Claude、DeepSeek、腾讯元宝</td><td>聊天窗口里问代码问题、贴报错求救、让它写代码片段——自己复制回去运行</td></tr>
        <tr><td><b>② IDE 内置式</b><br>（副驾驶型）</td><td>GitHub Copilot、Cursor、CodeBuddy、通义灵码</td><td>住在编辑器里：你写一半它补全，选中代码让它改，Tab 键接受建议</td></tr>
        <tr><td><b>③ 智能体式</b><br>（自动驾驶型）</td><td><b>WorkBuddy</b>、Codex、Claude Code</td><td>你描述任务，它自己拆解、写代码、运行、调试、交结果——全程可以不碰代码</td></tr>
      </table>
      <div class="quote">发现了吗？你现在正在用的 WorkBuddy 就是第 ③ 类。这门课的所有作业本质上是在训练你使用「智能体式 AI 编程」——你已经身处最前沿的编程方式里了。</div>
    `},
    {tag:"工具卡 5", title:"怎么选：小白起步推荐组合", ac:"cyan", html:`
      <p>阶段化配置，不要一次装一堆：</p>
      <table class="tbl">
        <tr><th>阶段</th><th>组合</th><th>说明</th></tr>
        <tr><td><b>现在（第 1~5 课）</b></td><td>WorkBuddy 就够了</td><td>对话内出题、写码、运行、批改全搞定，零安装</td></tr>
        <tr><td><b>第 6 课起</b></td><td>Python + VS Code + WorkBuddy</td><td>本机能跑代码了，WorkBuddy 变成你的教练和救火队</td></tr>
        <tr><td><b>进阶（开学后）</b></td><td>再加：Jupyter 插件 / Copilot 类补全</td><td>按需添置，用到再装</td></tr>
      </table>
      <div class="warn"><b>防坑提醒：</b>不要在入门期研究「哪个工具最强」——工具焦虑是最典型的拖延。VS Code + Python 这套组合已经服务了几千万人，直接用。</div>
    `}
  ],
  practice:{
    intro:"这课作业很轻：认识工具 + 第一次安装体验，为第 6 课的重头戏热身。",
    tasks:[
      {name:"作业 1 · 安装 VS Code", desc:"去官网 code.visualstudio.com 下载安装（免费）。装好后打开它，在扩展商店（左侧四个方块图标）搜索并安装「Chinese (Simplified)」中文语言包。卡住了就问 WorkBuddy。",
       prompt:"我正在安装 VS Code，遇到了问题：【描述你卡在哪一步，可贴截图】。我是 Windows 系统、编程零基础，请一步步教我解决。"},
      {name:"作业 2 · 用 VS Code 看一次代码", desc:"让 WorkBuddy 把之前课程里生成过的任意代码存成文件，然后用 VS Code 打开它，体验语法高亮——不同颜色分别是什么成分？",
       prompt:"请把一段 15 行左右、带中文注释的 Python 示例代码保存为一个 .py 文件到我的桌面（或告诉我怎么保存），我要用刚装好的 VS Code 打开看看语法高亮效果。然后告诉我：VS Code 里代码的不同颜色一般代表什么成分？"},
      {name:"作业 3 · 工具观念自查", desc:"用自己的话向 WorkBuddy 总结，让它批改。",
       prompt:"我总结一下三类 AI 编程工具的区别，你看我理解得对不对，有错请纠正：对话式是【我的理解】；IDE内置式是【我的理解】；智能体式是【我的理解】。另外用你（WorkBuddy）和用 VS Code 写代码分别适合什么情况？"}
    ],
    pass:"VS Code 安装成功并变成中文界面；能说出三类 AI 编程工具的区别。"
  }
});

/* ============ 第 6 课 ============ */
window.COURSE.push({
  id:"l6", mod:3, emoji:"🚀",
  title:"第 6 课 · 让代码跑起来",
  sub:"里程碑课程：今天你的电脑将第一次运行你自己的程序。环境、运行、调试，一次讲透。",
  cards:[
    {tag:"卡片 1", title:"什么是「环境」：为什么代码复制过来跑不了", ac:"cyan", html:`
      <p>新手最大的困惑：「我把代码复制到电脑上了，为什么跑不了？」</p>
      <p>因为代码只是<strong>剧本</strong>，你的电脑还缺<strong>剧组</strong>——能读懂并执行这个剧本的软件。这套软件就叫「<strong>运行环境</strong>」。</p>
      <table class="tbl">
        <tr><th>你要跑</th><th>需要的环境</th></tr>
        <tr><td>Python 代码（.py）</td><td>Python 解释器（去官网装）</td></tr>
        <tr><td>网页（.html）</td><td>浏览器（你已经有了！所以网页入门零门槛）</td></tr>
        <tr><td>C 代码（.c）</td><td>编译器（如 gcc），先编译成 .exe 再跑</td></tr>
        <tr><td>Java 代码（.java）</td><td>JDK（Java 开发工具包）</td></tr>
      </table>
      <p>延伸概念：程序还可能依赖<strong>第三方库</strong>（别人的轮子）——环境 = 解释器/编译器 + 所有依赖的库。「在我电脑上能跑，在你电脑上跑不了」99% 是环境差异。</p>
    `},
    {tag:"卡片 2", title:"动手：安装 Python（跟着做）", ac:"green", html:`
      <p>Windows 安装 Python 标准流程：</p>
      <ol>
        <li>打开官网 <code class="inl">python.org/downloads</code>，点黄色大按钮下载最新版</li>
        <li>运行安装包，<strong>⚠️ 最关键一步：勾选底部的「Add Python to PATH」</strong>（不勾后面全是坑）</li>
        <li>点 Install Now，等进度条走完</li>
        <li>验证：按 <code class="inl">Win+R</code> 输入 cmd 回车，在黑窗口输入 <code class="inl">python --version</code>，显示版本号（如 Python 3.13.x）= 安装成功 🎉</li>
      </ol>
      <div class="tip"><b>PATH 是什么？</b>系统的「常用联系人列表」。加入 PATH 后，你在任何地方喊一声 python，系统都知道去哪找它。</div>
      <p>然后给 VS Code 装上 Python 插件：扩展商店搜「Python」，装微软官方那个（下载量第一）。</p>
    `},
    {tag:"卡片 3", title:"第一次运行：Hello World 仪式", ac:"amber", html:`
      <p>全世界程序员的入门仪式——让程序说出第一句话：</p>
      <ol>
        <li>VS Code 里新建文件，命名 <code class="inl">hello.py</code>（注意后缀）</li>
        <li>输入这两行：</li>
      </ol>
      <pre class="code"><span class="f">print</span>(<span class="s">"Hello, World! 我的第一个程序"</span>)
<span class="f">print</span>(<span class="s">"1 + 1 ="</span>, <span class="n">1</span> + <span class="n">1</span>)</pre>
      <ol start="3">
        <li>点右上角的 ▶️ 运行按钮（或终端里输入 <code class="inl">python hello.py</code>）</li>
        <li>下方终端出现输出 → <strong>恭喜，你的电脑执行了你的第一条指令</strong> 🎉</li>
      </ol>
      <div class="quote">这一刻的意义：你和计算机的关系从「使用它的软件」变成了「命令它做事」。</div>
    `},
    {tag:"卡片 4", title:"装轮子：pip install 在干嘛", ac:"purple", html:`
      <p><code class="inl">pip</code> 是 Python 自带的「应用商店」，负责下载安装第三方库：</p>
      <pre class="code"><span class="c"># 在终端（黑窗口）里输入，不是在 .py 文件里！</span>
pip install requests      <span class="c"># 装"网络请求"库</span>
pip install pandas        <span class="c"># 装"表格处理"库</span>
pip list                  <span class="c"># 看看已经装了哪些库</span></pre>
      <p>流程：终端里 <code class="inl">pip install 库名</code> 下载安装 → 代码里 <code class="inl">import 库名</code> 使用。<strong>「No module named xxx」报错 = 轮子没装</strong>，pip install 一下就好。</p>
      <div class="tip"><b>下载慢？</b>用国内镜像：<code class="inl">pip install pandas -i https://pypi.tuna.tsinghua.edu.cn/simple</code>（清华源，速度飞起）</div>
    `},
    {tag:"卡片 5", title:"调试三板斧：程序出错了怎么办", ac:"red", html:`
      <p>代码跑不通是常态，按顺序用三板斧：</p>
      <ol>
        <li><strong>第一斧 · 读报错</strong>：从报错信息最后一行看起——错误类型 + 行号，一半的问题看一眼就明白（拼写错误、少个冒号、文件名不对）</li>
        <li><strong>第二斧 · print 大法</strong>：在可疑位置插 <code class="inl">print(变量名)</code>，把程序运行到那一步的「内心状态」打印出来看——数据是不是你以为的样子？</li>
        <li><strong>第三斧 · 丢给 AI</strong>：前两斧没解决，把<strong>完整代码 + 完整报错信息</strong>一起贴给 WorkBuddy，通常秒解</li>
      </ol>
      <div class="warn"><b>新手常见五大报错速查：</b><br>
      ① <b>SyntaxError</b> 语法错误 → 少了冒号/括号/引号；<br>
      ② <b>NameError</b> 名字未定义 → 变量名拼错了；<br>
      ③ <b>IndentationError</b> 缩进错误 → 空格没对齐；<br>
      ④ <b>ModuleNotFoundError</b> → 库没装，去 pip install；<br>
      ⑤ <b>FileNotFoundError</b> → 文件路径/文件名写错了。</div>
    `},
    {tag:"卡片 6", title:"终端扫盲：黑窗口不可怕，5 个命令就够", ac:"blue", html:`
      <p>终端（命令行/黑窗口）= 用打字代替点鼠标来操作电脑。看起来吓人，常用的就这几个：</p>
      <table class="tbl">
        <tr><th>命令</th><th>作用</th><th>例子</th></tr>
        <tr><td><code class="inl">cd 路径</code></td><td>进入某个文件夹（change directory）</td><td><code class="inl">cd Desktop</code> 进入桌面</td></tr>
        <tr><td><code class="inl">dir</code>（Win）/ <code class="inl">ls</code>（Mac）</td><td>列出当前文件夹里有什么</td><td>看看文件在不在</td></tr>
        <tr><td><code class="inl">python 文件名.py</code></td><td>运行 Python 脚本</td><td><code class="inl">python hello.py</code></td></tr>
        <tr><td><code class="inl">pip install 库名</code></td><td>安装库</td><td><code class="inl">pip install pandas</code></td></tr>
        <tr><td><code class="inl">cls</code>（Win）/ <code class="inl">clear</code>（Mac）</td><td>清屏</td><td>屏幕乱了擦干净</td></tr>
      </table>
      <p>好消息：VS Code 内置了终端（菜单 → 终端 → 新建终端），不用单独开黑窗口。</p>
    `}
  ],
  practice:{
    intro:"本课程第一个「离巢」作业——从 WorkBuddy 的对话里走出来，在你自己的电脑上跑通程序。这是全课程最重要的一次动手。",
    tasks:[
      {name:"作业 1 · 本机跑通第一个脚本 ⭐⭐", desc:"装好 Python + VS Code 后，让 WorkBuddy 给你一个小脚本，在自己电脑上跑起来。",
       prompt:"我已经装好了 Python 和 VS Code。请给我一个 15 行以内的有趣 Python 小脚本（比如：随机生成今日运势/幸运数字），并给我从「新建文件」到「运行成功」的完整步骤清单。我会在自己电脑上操作，遇到问题随时回来问你。"},
      {name:"作业 2 · 故意踩坑训练", desc:"让 WorkBuddy 埋一个雷，你在本机踩中它，然后用调试三板斧拆弹。",
       prompt:"请给我一段 10 行左右、故意埋了 1 个错误的 Python 代码（错误类型从：拼写错误/缺冒号/缩进错误 里随机选）。不要告诉我错在哪。我会在自己电脑上运行它，根据报错信息自己定位和修复。我实在找不到时会回来找你要提示（提示也请一步步给，别直接说答案）。"},
      {name:"作业 3 · 第一次 pip", desc:"体验安装轮子 + 使用轮子的完整流程。",
       prompt:"请教我在终端里用 pip 安装一个对新手友好又好玩的库（你来推荐，比如能在终端输出彩色文字或艺术字的），然后给我一段 5 行以内的代码用上它。我在本机操作，装完跑通后向你汇报结果。"}
    ],
    pass:"你自己的电脑上独立跑通了至少一个脚本；独立（或在提示下）修好了 1 个 Bug；成功 pip 装过 1 个库。"
  }
});

/* ============ 第 7 课 ============ */
window.COURSE.push({
  id:"l7", mod:3, emoji:"📦",
  title:"第 7 课 · 代码的家：托管、打包与发布",
  sub:"代码写完只是一半——存在哪、怎么协作、怎么交给别人用？这一课打通「最后一公里」。",
  cards:[
    {tag:"卡片 1", title:"为什么需要代码托管", ac:"cyan", html:`
      <p>三个真实痛点：</p>
      <ul>
        <li>💥 <strong>电脑坏了代码全没</strong> → 需要云端备份</li>
        <li>😵 <strong>「最终版_改2_真最终版.py」</strong> → 需要版本管理（随时回到任何历史版本）</li>
        <li>👥 <strong>多人改同一份代码打架</strong> → 需要协作机制</li>
      </ul>
      <p>解决这三件事的系统就叫<strong>代码托管</strong>。顺便你还得到了第四个宝藏：<strong>开源世界</strong>——全球程序员公开的代码宝库，随便逛、随便学、随便用。</p>
    `},
    {tag:"卡片 2", title:"Git 和 GitHub 是什么关系", ac:"purple", html:`
      <p>经典混淆，一句话分清：<strong>Git 是工具（装在你电脑上的版本管理软件），GitHub 是网站（云端存放 Git 仓库的平台）</strong>。类比：Git 是相机，GitHub 是相册网站。国内还有 Gitee（码云），访问更快。</p>
      <p>入门只需三个词：</p>
      <table class="tbl">
        <tr><th>词</th><th>意思</th><th>类比</th></tr>
        <tr><td><b>仓库 repo</b></td><td>一个项目的家（代码+全部历史）</td><td>一个项目文件夹</td></tr>
        <tr><td><b>提交 commit</b></td><td>给当前进度拍一张「存档快照」</td><td>游戏存档</td></tr>
        <tr><td><b>克隆 clone</b></td><td>把云端仓库完整下载到本地</td><td>下载整个项目</td></tr>
      </table>
      <pre class="code"><span class="c"># 最常用的一条命令：把别人的开源项目下载下来</span>
git clone https://github.com/用户名/项目名.git</pre>
      <div class="tip"><b>对小白的现实意义：</b>短期内你不需要精通 Git，但你要会 <b>clone</b>——因为大量好玩的开源项目、老师给的课程代码，都放在 GitHub/Gitee 上等你下载。</div>
    `},
    {tag:"卡片 3", title:"程序怎么交给别人用：三条路", ac:"amber", html:`
      <table class="tbl">
        <tr><th>方式</th><th>做法</th><th>适合</th></tr>
        <tr><td><b>① 直接发脚本</b></td><td>把 .py 文件发过去</td><td>对方也装了 Python（同学之间）</td></tr>
        <tr><td><b>② 打包成 exe</b></td><td>用 PyInstaller 把脚本连同环境打成一个 .exe，对方双击就能跑</td><td>对方是纯小白（爸妈、朋友）</td></tr>
        <tr><td><b>③ 部署成网页</b></td><td>把程序放到服务器/静态托管平台，发个链接就能用</td><td>想给所有人用（最酷）</td></tr>
      </table>
      <pre class="code"><span class="c"># 打包 exe 就两步（终端里）：</span>
pip install pyinstaller
pyinstaller -F my_tool.py     <span class="c"># -F = 打成单个exe文件，产物在 dist 文件夹</span></pre>
      <p>网页部署的免费选择：GitHub Pages（静态页）、Vercel、腾讯 EdgeOne Pages 等——第 8 课选项目 B 的同学会实际用到。</p>
    `},
    {tag:"卡片 4", title:"一图看懂完整链路", ac:"green", html:`
      <p>把这几课串起来，一个程序的完整生命周期是：</p>
      <pre class="code">💡 想清楚需求 (第4课)
   ↓
✍️ 写代码 / 让AI写 (WorkBuddy · VS Code)
   ↓
🚀 本机跑通 + 调试 (第6课: 环境 · pip · 三板斧)
   ↓
☁️ 托管备份 (git commit → push 到 GitHub/Gitee)
   ↓
📦 交付 (发脚本 / 打包exe / 部署网页)
   ↓
😎 别人用上了你做的东西</pre>
      <div class="quote">走完一遍这条链路（哪怕是最小的项目），你对「软件是怎么来的」的理解就超过 90% 的普通人了。第 8 课我们就走这一遍。</div>
    `}
  ],
  practice:{
    intro:"两个实战：下载别人的项目跑起来 + 把自己的脚本打包给别人。完成后你就打通了「取」和「予」双向链路。",
    tasks:[
      {name:"作业 1 · Clone 一个开源项目", desc:"体验「从开源世界取货」的完整流程。",
       prompt:"请帮我找一个适合零基础练手的 Python 开源小项目（在 GitHub 或 Gitee 上，最好是小游戏或趣味工具，依赖少的），然后带我一步步操作：安装 git → clone 下来 → 装依赖 → 跑起来。我每完成一步向你汇报，卡住了你帮我排查。"},
      {name:"作业 2 · 打包一个 exe 送人 ⭐", desc:"把第 6 课跑通的脚本打包成 exe，发给一个没装 Python 的朋友/家人，让 ta 双击运行。",
       prompt:"我想把我的 Python 脚本打包成 exe 发给没装 Python 的朋友。请带我用 PyInstaller 操作：安装 → 打包命令 → 在哪找到产物 → 发送前要注意什么（比如杀毒软件误报怎么解释）。我的脚本功能是：【简单描述你的脚本】"},
      {name:"作业 3 · 概念自查", desc:"用类比讲清三个词，检验是否真懂。",
       prompt:"我用自己的话解释这三个概念，你判断我是否真的理解，有偏差请纠正：① Git 和 GitHub 的区别是【我的理解】；② commit 是【我的理解】；③ 把程序交给别人用有三种方式，分别是【我的理解】。"}
    ],
    pass:"clone 并跑通了一个开源项目；你打包的 exe 在别人的电脑上真的跑起来了。"
  }
});
