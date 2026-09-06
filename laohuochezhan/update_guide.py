import re

with open('guide.html', 'r', encoding='utf-8') as f:
    content = f.read()

# ===== 新的第一部分HTML =====
new_part1 = '''  <!-- 第一部分 -->
  <div class="section" id="part1">
    <div class="section-title"><span class="num">1</span>部门资料调取清单</div>
    <div class="desc">原则：只向部门索要他们能提供的文件、图纸、台账、批复等正式资料。需要现场核实的内容不在此列，详见第三部分。各项资料按序号排列，标注文件格式要求。</div>

    <div class="sub-title">主要部门（10个）</div>

    <!-- 1. 自然资源和规划局 -->
    <div class="collapse open">
      <div class="collapse-header" onclick="toggleCollapse(this)">
        <span class="name">🏛️ 永州市自然资源和规划局</span>
        <span class="arrow">▶</span>
      </div>
      <div class="collapse-body">
        <div class="collapse-inner">
          <p style="font-size:13px;color:#9aa0a6;margin-bottom:10px;">对接方向：国土空间规划、控规、用地、地籍、影像、地形、三调</p>
          <div class="table-wrap">
            <table>
              <thead><tr><th style="width:40px">序号</th><th style="width:160px">资料名称</th><th>需获取的具体内容与格式要求</th></tr></thead>
              <tbody>
                <tr><td style="text-align:center">1</td><td class="doc-name">永州市国土空间总体规划</td><td>涉及片区的功能定位、用地布局、三条控制线、重大设施布局。要求提供批复文本PDF+规划图纸PDF+矢量数据（Shapefile/GeoJSON）。</td></tr>
                <tr><td style="text-align:center">2</td><td class="doc-name">老火车站片区控制性详细规划</td><td>控规文本+分图图则+矢量数据，核实版本是否最新、是否已批复。要求提供文本PDF+图则PDF+用地红线CAD（DWG）+指标Excel。</td></tr>
                <tr><td style="text-align:center">3</td><td class="doc-name">第三次全国国土调查数据及年度变更调查数据</td><td>片区范围内地类、面积、分布数据。要求提供三调原始数据库（GDB）+变更调查Excel+地类图斑矢量（Shapefile）。</td></tr>
                <tr><td style="text-align:center">4</td><td class="doc-name">综合交通专项规划</td><td>涉及片区的道路网络等级、交叉口规划、交通设施布局、轨道交通预留。要求提供文本PDF+图纸PDF+道路红线CAD。</td></tr>
                <tr><td style="text-align:center">5</td><td class="doc-name">片区现状高清影像图</td><td>最新航拍影像，要求提供TIFF/IMG格式带坐标信息（WGS84/CGCS2000），分辨率优于0.5米。可补充2010、2015、2020年历史影像做对比。</td></tr>
                <tr><td style="text-align:center">6</td><td class="doc-name">片区现状高清地形图</td><td>CAD格式，含等高线、标高、现状地物、道路、建筑、管线。要求提供DWG格式（2010版及以下兼容），含高程点和等高线。（已有：老火车站1(全).dwg，需核实是否最新）</td></tr>
                <tr><td style="text-align:center">7</td><td class="doc-name">现状用地数据</td><td>GIS矢量数据，各地块用地性质（GB/T 21010-2017）、面积、权属单位。要求提供Shapefile/GeoJSON格式，属性表完整。</td></tr>
                <tr><td style="text-align:center">8</td><td class="doc-name">土地权属数据</td><td>国有/集体土地权属、宗地划分、已出让/划拨情况、土地使用证信息。要求提供宗地矢量（Shapefile）+权属台账Excel。</td></tr>
                <tr><td style="text-align:center">9</td><td class="doc-name">闲置土地清单</td><td>片区范围内闲置土地位置、面积、闲置原因、闲置时间、处置情况。要求提供清单Excel+位置矢量（Shapefile/KML）。</td></tr>
                <tr><td style="text-align:center">10</td><td class="doc-name">低效用地清单</td><td>片区范围内低效用地位置、面积、用地性质、再开发潜力评估。要求提供清单Excel+位置矢量。</td></tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </div>

    <!-- 2. 住房和城乡建设局 -->
    <div class="collapse">
      <div class="collapse-header" onclick="toggleCollapse(this)">
        <span class="name">🏗️ 永州市住房和城乡建设局</span>
        <span class="arrow">▶</span>
      </div>
      <div class="collapse-body">
        <div class="collapse-inner">
          <p style="font-size:13px;color:#9aa0a6;margin-bottom:10px;">对接方向：城市更新、住房发展、历史文化保护、危房、老旧小区、市政基础设施、房屋权属</p>
          <div class="table-wrap">
            <table>
              <thead><tr><th style="width:40px">序号</th><th style="width:160px">资料名称</th><th>需获取的具体内容与格式要求</th></tr></thead>
              <tbody>
                <tr><td style="text-align:center">1</td><td class="doc-name">永州市城市更新专项规划</td><td>专项规划全文+图纸+项目清单，含片区定位、更新策略、更新单元划分、项目库。要求提供批复文本PDF+图纸PDF+项目清单Excel。</td></tr>
                <tr><td style="text-align:center">2</td><td class="doc-name">永州市城市体检报告</td><td>57项指标Excel原始数据+附图矢量，含生态宜居、健康舒适、安全韧性、交通便捷、风貌特色、整洁有序、多元包容、创新活力8大维度评价结论及问题清单。要求提供报告PDF+指标Excel+附图矢量。</td></tr>
                <tr><td style="text-align:center">3</td><td class="doc-name">永州市住房发展规划</td><td>住房供应总量、结构、布局，老旧小区改造规模与时序，保障性住房布局。要求提供文本PDF+图纸PDF+项目清单Excel。</td></tr>
                <tr><td style="text-align:center">4</td><td class="doc-name">历史文化保护规划</td><td>历史建筑、历史文化街区、传统风貌建筑名单及保护范围、建设控制地带、修缮要求。要求提供文本PDF+保护范围矢量（Shapefile）+名单Excel。</td></tr>
                <tr><td style="text-align:center">5</td><td class="doc-name">危房鉴定数据</td><td>片区内C/D级危房及疑似危房的位置、面积、结构、年代、鉴定等级、鉴定机构、鉴定时间。要求提供鉴定报告PDF+清单Excel+位置矢量。</td></tr>
                <tr><td style="text-align:center">6</td><td class="doc-name">老旧小区改造计划</td><td>本片区已改造/正在改造/计划改造的小区清单及改造内容、投资、工期。要求提供清单Excel（含小区名称、地址、户数、改造内容、投资、年份）。</td></tr>
                <tr><td style="text-align:center">7</td><td class="doc-name">加装电梯数据</td><td>片区内已加装电梯数量、位置、4-6层住宅清单、加装条件评估、补贴政策。要求提供清单Excel。</td></tr>
                <tr><td style="text-align:center">8</td><td class="doc-name">基础设施更新改造实施方案</td><td>已有PDF（267页），需提取86个项目完整Excel清单+附表，含供水、排水、燃气、电力、道路、照明等改造项目位置、内容、投资、工期。要求提供项目清单Excel+位置矢量。</td></tr>
                <tr><td style="text-align:center">9</td><td class="doc-name">住建系统十五五期间对该区域的项目清单及建设内容</td><td>住建系统"十五五"期间涉及本片区的老旧小区改造、市政基础设施、公共服务设施、住房保障等项目清单。要求提供项目清单Excel（含项目名称、位置、内容、投资、工期、责任单位）。</td></tr>
                <tr><td style="text-align:center">10</td><td class="doc-name">房屋权属关系相关资料</td><td>片区内公房、单位自管房、房改房、廉租房、公租房等权属情况，产权单位、管理单位、使用状况。要求提供权属台账Excel。</td></tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </div>

    <!-- 3. 城市管理和综合执法局 -->
    <div class="collapse">
      <div class="collapse-header" onclick="toggleCollapse(this)">
        <span class="name">🚦 永州市城市管理和综合执法局</span>
        <span class="arrow">▶</span>
      </div>
      <div class="collapse-body">
        <div class="collapse-inner">
          <p style="font-size:13px;color:#9aa0a6;margin-bottom:10px;">对接方向：环境卫生、停车设施、市政老旧管网、老旧泵站、环卫设施</p>
          <div class="table-wrap">
            <table>
              <thead><tr><th style="width:40px">序号</th><th style="width:160px">资料名称</th><th>需获取的具体内容与格式要求</th></tr></thead>
              <tbody>
                <tr><td style="text-align:center">1</td><td class="doc-name">环境卫生专项规划</td><td>垃圾收集、转运、处理设施布局，垃圾分类规划，公厕布局。要求提供文本PDF+图纸PDF+设施清单Excel。</td></tr>
                <tr><td style="text-align:center">2</td><td class="doc-name">停车设施数据</td><td>片区内公共停车场位置、泊位数量、收费标准、经营主体；路内停车泊位位置、数量、收费时段。要求提供清单Excel+位置矢量（Shapefile/KML）。</td></tr>
                <tr><td style="text-align:center">3</td><td class="doc-name">老旧管网现状及改造计划</td><td>片区内给水、排水、燃气、电力、电信老旧管网走向、管径、材质、建成年代、漏损情况、改造计划。要求提供管网CAD（DWG）+台账Excel。</td></tr>
                <tr><td style="text-align:center">4</td><td class="doc-name">老旧泵站清单</td><td>片区内雨水泵站、污水泵站位置、规模、建成年代、运行状况、改造需求。要求提供清单Excel+位置矢量。</td></tr>
                <tr><td style="text-align:center">5</td><td class="doc-name">环卫设施数据</td><td>垃圾转运站、公厕、垃圾分类收集点、环卫工作站位置、数量、服务范围。要求提供清单Excel+位置矢量。</td></tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </div>

    <!-- 4. 教育局 -->
    <div class="collapse">
      <div class="collapse-header" onclick="toggleCollapse(this)">
        <span class="name">🎓 永州市教育局</span>
        <span class="arrow">▶</span>
      </div>
      <div class="collapse-body">
        <div class="collapse-inner">
          <p style="font-size:13px;color:#9aa0a6;margin-bottom:10px;">对接方向：教育设施布局、统计数据、改造计划</p>
          <div class="table-wrap">
            <table>
              <thead><tr><th style="width:40px">序号</th><th style="width:160px">资料名称</th><th>需获取的具体内容与格式要求</th></tr></thead>
              <tbody>
                <tr><td style="text-align:center">1</td><td class="doc-name">教育设施专项规划</td><td>幼儿园、小学、中学布局及学位配置规划，服务半径划分，新建/改扩建学校计划。要求提供文本PDF+图纸PDF+学校清单Excel。</td></tr>
                <tr><td style="text-align:center">2</td><td class="doc-name">片区教育设施统计数据</td><td>片区内各幼儿园、小学、中学位置、规模（班级数、学位数）、在校学生数、办学性质（公办/民办）、招生范围、占地面积、建筑面积。要求提供统计Excel+位置矢量。</td></tr>
                <tr><td style="text-align:center">3</td><td class="doc-name">本片区教育设施改造计划</td><td>薄弱学校改造、扩容提质、运动场改造、校舍安全等项目清单及内容、投资、工期。要求提供项目清单Excel。</td></tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </div>

    <!-- 5. 卫生健康委员会 -->
    <div class="collapse">
      <div class="collapse-header" onclick="toggleCollapse(this)">
        <span class="name">🏥 永州市卫生健康委员会</span>
        <span class="arrow">▶</span>
      </div>
      <div class="collapse-body">
        <div class="collapse-inner">
          <p style="font-size:13px;color:#9aa0a6;margin-bottom:10px;">对接方向：医疗卫生设施布局、统计数据、改造计划</p>
          <div class="table-wrap">
            <table>
              <thead><tr><th style="width:40px">序号</th><th style="width:160px">资料名称</th><th>需获取的具体内容与格式要求</th></tr></thead>
              <tbody>
                <tr><td style="text-align:center">1</td><td class="doc-name">医疗卫生设施专项规划</td><td>医院、社区卫生服务中心、诊所布局规划，服务半径划分，床位数配置标准。要求提供文本PDF+图纸PDF+机构清单Excel。</td></tr>
                <tr><td style="text-align:center">2</td><td class="doc-name">片区医疗卫生设施统计数据</td><td>片区内各医院、社区卫生服务中心、诊所位置、等级、床位数、服务人口、科室设置、运营状况、占地面积、建筑面积。要求提供统计Excel+位置矢量。</td></tr>
                <tr><td style="text-align:center">3</td><td class="doc-name">本片区医疗卫生设施改造计划</td><td>社区卫生服务中心提质、基层医疗设施完善、公共卫生设施建设等项目清单。要求提供项目清单Excel。</td></tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </div>

    <!-- 6. 民政局 -->
    <div class="collapse">
      <div class="collapse-header" onclick="toggleCollapse(this)">
        <span class="name">🤝 永州市民政局</span>
        <span class="arrow">▶</span>
      </div>
      <div class="collapse-body">
        <div class="collapse-inner">
          <p style="font-size:13px;color:#9aa0a6;margin-bottom:10px;">对接方向：养老服务、社区服务、社会福利</p>
          <div class="table-wrap">
            <table>
              <thead><tr><th style="width:40px">序号</th><th style="width:160px">资料名称</th><th>需获取的具体内容与格式要求</th></tr></thead>
              <tbody>
                <tr><td style="text-align:center">1</td><td class="doc-name">养老服务设施专项规划</td><td>养老院、日间照料中心、养老服务站、嵌入式养老机构布局规划，床位数配置标准，服务半径。要求提供文本PDF+图纸PDF+设施清单Excel。</td></tr>
                <tr><td style="text-align:center">2</td><td class="doc-name">养老机构及日间照料中心数据</td><td>片区内养老院、日间照料中心、养老服务站位置、床位数、运营主体（公办/民办/公建民营）、收费标准、服务人群、入住率。要求提供清单Excel+位置矢量。</td></tr>
                <tr><td style="text-align:center">3</td><td class="doc-name">社区服务设施配置</td><td>各社区服务中心位置、面积、功能配置（党群服务、政务服务、文化活动、卫生计生、养老助残等）、运营状况。要求提供清单Excel+位置矢量。</td></tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </div>

    <!-- 7. 消防救援支队 -->
    <div class="collapse">
      <div class="collapse-header" onclick="toggleCollapse(this)">
        <span class="name">🚒 永州市消防救援支队</span>
        <span class="arrow">▶</span>
      </div>
      <div class="collapse-body">
        <div class="collapse-inner">
          <p style="font-size:13px;color:#9aa0a6;margin-bottom:10px;">对接方向：消防设施布局、消防站数据</p>
          <div class="table-wrap">
            <table>
              <thead><tr><th style="width:40px">序号</th><th style="width:160px">资料名称</th><th>需获取的具体内容与格式要求</th></tr></thead>
              <tbody>
                <tr><td style="text-align:center">1</td><td class="doc-name">消防设施专项规划</td><td>消防站布局规划、消防通道规划、消防供水规划、消防装备配置标准。要求提供文本PDF+图纸PDF+消防站清单Excel。</td></tr>
                <tr><td style="text-align:center">2</td><td class="doc-name">消防站数据</td><td>片区内及周边消防站位置、管辖范围、装备配置、人员编制、出警时间。要求提供清单Excel+位置矢量。</td></tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </div>

    <!-- 8. 水利局 -->
    <div class="collapse">
      <div class="collapse-header" onclick="toggleCollapse(this)">
        <span class="name">🌊 永州市水利局</span>
        <span class="arrow">▶</span>
      </div>
      <div class="collapse-body">
        <div class="collapse-inner">
          <p style="font-size:13px;color:#9aa0a6;margin-bottom:10px;">对接方向：防洪排涝</p>
          <div class="table-wrap">
            <table>
              <thead><tr><th style="width:40px">序号</th><th style="width:160px">资料名称</th><th>需获取的具体内容与格式要求</th></tr></thead>
              <tbody>
                <tr><td style="text-align:center">1</td><td class="doc-name">防洪排涝专项规划</td><td>防洪标准、排涝分区、排涝泵站布局、防洪堤线、内涝风险点、防洪应急预案。要求提供文本PDF+图纸PDF+泵站清单Excel+风险点矢量。</td></tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </div>

    <!-- 9. 国资委 -->
    <div class="collapse">
      <div class="collapse-header" onclick="toggleCollapse(this)">
        <span class="name">🏢 永州市人民政府国有资产监督管理委员会</span>
        <span class="arrow">▶</span>
      </div>
      <div class="collapse-body">
        <div class="collapse-inner">
          <p style="font-size:13px;color:#9aa0a6;margin-bottom:10px;">对接方向：闲置国有资产、市属企业闲置资产</p>
          <div class="table-wrap">
            <table>
              <thead><tr><th style="width:40px">序号</th><th style="width:160px">资料名称</th><th>需获取的具体内容与格式要求</th></tr></thead>
              <tbody>
                <tr><td style="text-align:center">1</td><td class="doc-name">闲置公共建筑台账</td><td>片区内市属国有闲置公共建筑位置、面积、产权单位、现状用途、闲置原因、闲置时间、处置意向。要求提供台账Excel+位置矢量。</td></tr>
                <tr><td style="text-align:center">2</td><td class="doc-name">市属企业闲置建筑及土地清单</td><td>片区内市属国有企业闲置厂房、仓库、办公用房、土地位置、面积、产权、现状、处置意向。要求提供清单Excel+位置矢量。（注：老火车站片区可能涉及铁路系统资产，需另行对接铁路部门；集体企业和民营企业闲置资产需通过街道社区了解）</td></tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </div>

    <!-- 10. 公安局/统计局 -->
    <div class="collapse">
      <div class="collapse-header" onclick="toggleCollapse(this)">
        <span class="name">👥 永州市公安局 / 永州市统计局</span>
        <span class="arrow">▶</span>
      </div>
      <div class="collapse-body">
        <div class="collapse-inner">
          <p style="font-size:13px;color:#9aa0a6;margin-bottom:10px;">对接方向：人口、户籍数据</p>
          <div class="table-wrap">
            <table>
              <thead><tr><th style="width:40px">序号</th><th style="width:160px">资料名称</th><th>需获取的具体内容与格式要求</th></tr></thead>
              <tbody>
                <tr><td style="text-align:center">1</td><td class="doc-name">人口资料</td><td>分社区：居住户数、户籍人口、常住人口、老年人口（60岁以上/65岁以上）、租住人口、流动人口、人口结构（年龄/性别/学历）。要求提供统计Excel，数据年份统一，口径标注清楚。</td></tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </div>

    <div class="sub-title">建议咨询的部门（非必须，视情况了解）</div>
    <div class="table-wrap">
      <table>
        <thead><tr><th style="width:180px">部门</th><th>建议咨询内容</th></tr></thead>
        <tbody>
          <tr><td class="doc-name">永州市发展和改革委员会</td><td>各部门"十五五"期间涉及本片区的建设项目计划汇总、重大项目立项信息</td></tr>
          <tr><td class="doc-name">永州市商务局</td><td>商业网点规划、重点市场经营数据、农贸市场布局</td></tr>
          <tr><td class="doc-name">各专项规划编制单位</td><td>涉及本片区的交通、市政、公服等专项规划具体要求、规划范围、实施时序</td></tr>
          <tr><td class="doc-name">体检报告编制单位</td><td>57项指标Excel原始数据+附图矢量、指标计算口径、问题清单详细说明</td></tr>
          <tr><td class="doc-name">水务公司/自来水公司</td><td>片区内给水管网详细走向、管径、阀门、消防栓位置、供水压力、漏损点（消防栓一般在水务公司）</td></tr>
          <tr><td class="doc-name">燃气公司</td><td>片区内燃气管网走向、管径、调压站位置、建成年代、安全隐患点</td></tr>
          <tr><td class="doc-name">电力公司</td><td>片区内电力管网走向、变电站位置、配电设施、老旧线路改造计划</td></tr>
        </tbody>
      </table>
    </div>
  </div>

'''

# 替换第一部分
# 找到第一部分开始和第二部分开始的位置
part1_start = content.find('  <!-- 第一部分 -->')
part2_start = content.find('  <!-- 第二部分 -->')

if part1_start > -1 and part2_start > -1:
    content = content[:part1_start] + new_part1 + content[part2_start:]
    print('第一部分替换成功')
else:
    print(f'未找到标记: part1_start={part1_start}, part2_start={part2_start}')

# ===== 修改第二部分：街道社区增加违章建筑、社区情况汇总表、小区情况表 =====
# 找到街道层面"向街道索要的资料"表格，在后面增加
street_old = '''        <div class="table-wrap">
      <table>
        <thead><tr><th style="width:60px">重要程度</th><th style="width:120px">资料名称</th><th>具体内容</th></tr></thead>
        <tbody>
          <tr><td class="imp">🔴</td><td class="doc-name">社区详细情况</td><td>各社区面积、人口户数、包含小区数量、辖区单位</td></tr>
          <tr><td class="imp">🔴</td><td class="doc-name">人口资料</td><td>分社区：居住户数、户籍/常住/老年/租住人口</td></tr>
          <tr><td class="imp">🔴</td><td class="doc-name">小区清单</td><td>片区内所有小区/宿舍名称、地址、户数、楼栋数、建成年代、产权单位</td></tr>
          <tr><td class="imp">🟡</td><td class="doc-name">街道建设项目计划</td><td>街道牵头或涉及的老旧小区改造、环境整治、基础设施项目</td></tr>
          <tr><td class="imp">🟢</td><td class="doc-name">低保/特困/残疾人数据</td><td>脱敏统计数据，用于社会民生分析</td></tr>
        </tbody>
      </table>
    </div>'''

street_new = '''        <div class="table-wrap">
      <table>
        <thead><tr><th style="width:40px">序号</th><th style="width:140px">资料名称</th><th>具体内容与格式要求</th></tr></thead>
        <tbody>
          <tr><td style="text-align:center">1</td><td class="doc-name">社区情况汇总表</td><td>各社区面积、人口户数、包含小区数量、辖区单位、社区工作力量、存在的主要问题。要求提供Excel汇总表。</td></tr>
          <tr><td style="text-align:center">2</td><td class="doc-name">人口资料</td><td>分社区：居住户数、户籍人口、常住人口、老年人口（60+/65+）、租住人口、流动人口。要求提供Excel，数据年份和口径标注清楚。</td></tr>
          <tr><td style="text-align:center">3</td><td class="doc-name">小区清单</td><td>片区内所有小区/宿舍名称、地址、户数、楼栋数、建成年代、产权单位、物业管理情况。要求提供Excel清单。</td></tr>
          <tr><td style="text-align:center">4</td><td class="doc-name">每个小区的情况表</td><td>逐小区台账：基本信息、建筑状况、基础设施、道路交通、公共服务、环境卫生、消防安全、适老化、物业管理、居民意愿、存在问题。要求提供Excel，每个小区一行或一个工作表。</td></tr>
          <tr><td style="text-align:center">5</td><td class="doc-name">违章建筑调查清单</td><td>片区内违章建筑位置、面积、类型、建设时间、当事人、处理情况。由街道城管中队或社区提供，要求提供Excel清单+大致位置。</td></tr>
          <tr><td style="text-align:center">6</td><td class="doc-name">企业闲置建筑信息</td><td>辖区内集体企业、民营企业闲置厂房、仓库、办公用房位置、面积、产权、现状、处置意向。要求提供Excel清单。</td></tr>
          <tr><td style="text-align:center">7</td><td class="doc-name">街道建设项目计划</td><td>街道牵头或涉及的老旧小区改造、环境整治、基础设施项目清单。要求提供Excel。</td></tr>
          <tr><td style="text-align:center">8</td><td class="doc-name">低保/特困/残疾人数据</td><td>脱敏统计数据，分社区数量，用于社会民生分析。要求提供Excel。</td></tr>
        </tbody>
      </table>
    </div>'''

if street_old in content:
    content = content.replace(street_old, street_new)
    print('街道层面资料表格替换成功')
else:
    print('未找到街道层面资料表格，尝试模糊匹配...')
    # 尝试找到"向街道索要的资料"后面的表格
    idx = content.find('向街道索要的资料')
    if idx > -1:
        print(f'找到"向街道索要的资料" at {idx}')
        print(content[idx:idx+200])

# 社区层面也类似修改
community_old = '''        <div class="table-wrap">
      <table>
        <thead><tr><th style="width:60px">重要程度</th><th style="width:120px">资料名称</th><th>具体内容</th></tr></thead>
        <tbody>
          <tr><td class="imp">🔴</td><td class="doc-name">小区逐栋台账</td><td>每个小区：楼栋数、单元数、户数、建成年代、结构、质量、产权</td></tr>
          <tr><td class="imp">🔴</td><td class="doc-name">小区基础设施现状</td><td>供水、排水、供电、燃气、道路、照明、环卫、消防情况</td></tr>
          <tr><td class="imp">🟡</td><td class="doc-name">小区物业情况</td><td>有无物业、物业费标准、业委会、收缴率</td></tr>
          <tr><td class="imp">🟡</td><td class="doc-name">特殊群体台账</td><td>低保户、特困户、残疾人、独居老人数量（脱敏）</td></tr>
          <tr><td class="imp">🟢</td><td class="doc-name">社区历史与文化</td><td>老地名、特色街巷、历史故事</td></tr>
        </tbody>
      </table>
    </div>'''

community_new = '''        <div class="table-wrap">
      <table>
        <thead><tr><th style="width:40px">序号</th><th style="width:140px">资料名称</th><th>具体内容与格式要求</th></tr></thead>
        <tbody>
          <tr><td style="text-align:center">1</td><td class="doc-name">小区逐栋台账</td><td>每个小区：楼栋数、单元数、户数、建成年代、结构、质量、产权、层数。要求提供Excel。</td></tr>
          <tr><td style="text-align:center">2</td><td class="doc-name">小区基础设施现状</td><td>供水方式、排水（雨污分流/合流）、供电、燃气有无、道路、照明、环卫、消防情况。要求提供Excel。</td></tr>
          <tr><td style="text-align:center">3</td><td class="doc-name">小区物业情况</td><td>有无物业、物业用房、门卫、物业费标准、业委会、收缴率、监控。要求提供Excel。</td></tr>
          <tr><td style="text-align:center">4</td><td class="doc-name">特殊群体台账</td><td>低保户、特困户、残疾人、独居老人数量（脱敏），主要分布在哪些小区。要求提供Excel。</td></tr>
          <tr><td style="text-align:center">5</td><td class="doc-name">违章建筑信息</td><td>辖区内违章建筑位置、面积、类型、建设时间、当事人、处理情况。要求提供Excel清单。</td></tr>
          <tr><td style="text-align:center">6</td><td class="doc-name">社区历史与文化</td><td>老地名、特色街巷、历史故事、传统风貌建筑、非物质文化遗产。要求提供文字资料。</td></tr>
        </tbody>
      </table>
    </div>'''

if community_old in content:
    content = content.replace(community_old, community_new)
    print('社区层面资料表格替换成功')
else:
    print('未找到社区层面资料表格')

with open('guide.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('guide.html 修改完成')
print(f'文件大小: {len(content)} 字符')
