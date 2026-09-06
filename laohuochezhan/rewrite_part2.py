with open('guide.html', 'r', encoding='utf-8') as f:
    content = f.read()

new_part2 = '''  <!-- 第二部分 -->
  <div class="section" id="part2">
    <div class="section-title"><span class="num">2</span>街道与社区调研</div>
    <div class="desc">街道和社区是城市更新工作的第一线，所有改造项目申报、计划上报、居民协调都经过他们之手，对辖区情况最了解。建议组织街道和社区联合座谈，以<strong>收集资料、了解情况、了解诉求</strong>为主，同时为后续现场踏勘做准备。以下资料请街道社区尽量提供原件或已有台账，不需要专门整理，有相关或相近的资料都可以提供。</div>

    <div class="sub-title">一、需要收集的资料清单</div>
    <p style="font-size:13px;color:#9aa0a6;margin-bottom:14px;">以下资料类型请街道社区确认是否有，如有请尽量提供原件或电子件，不需要重新整理。</p>

    <!-- 1. 小区基础资料 -->
    <div class="collapse open">
      <div class="collapse-header" onclick="toggleCollapse(this)">
        <span class="name">🏘️ 1. 小区基础资料</span>
        <span class="arrow">▶</span>
      </div>
      <div class="collapse-body">
        <div class="collapse-inner">
          <div class="table-wrap">
            <table>
              <thead><tr><th style="width:40px">序号</th><th style="width:150px">资料类型</th><th>具体内容与格式要求</th></tr></thead>
              <tbody>
                <tr><td style="text-align:center">1</td><td class="doc-name">各小区基本情况表</td><td>小区名称、地址、所属社区、户数、楼栋数、建成年代、产权单位、物业管理情况。是否有此资料？如有请提供Excel或纸质表格。</td></tr>
                <tr><td style="text-align:center">2</td><td class="doc-name">小区逐栋台账</td><td>每个小区的楼栋数、单元数、层数、结构类型、建筑质量、产权情况。是否有此资料？</td></tr>
                <tr><td style="text-align:center">3</td><td class="doc-name">小区基础设施现状</td><td>供水方式、排水（雨污分流/合流）、供电、燃气有无、道路、照明、环卫、消防情况。是否有此资料？</td></tr>
                <tr><td style="text-align:center">4</td><td class="doc-name">小区物业情况</td><td>有无物业、物业用房、门卫、物业费标准、业委会成立情况、收缴率、监控设施。是否有此资料？</td></tr>
                <tr><td style="text-align:center">5</td><td class="doc-name">小区改造历史</td><td>各小区是否已改造、改造年份、改造内容、资金来源、居民出资情况。是否有此资料？</td></tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </div>

    <!-- 2. 社区基础资料 -->
    <div class="collapse">
      <div class="collapse-header" onclick="toggleCollapse(this)">
        <span class="name">👥 2. 社区基础资料</span>
        <span class="arrow">▶</span>
      </div>
      <div class="collapse-body">
        <div class="collapse-inner">
          <div class="table-wrap">
            <table>
              <thead><tr><th style="width:40px">序号</th><th style="width:150px">资料类型</th><th>具体内容与格式要求</th></tr></thead>
              <tbody>
                <tr><td style="text-align:center">1</td><td class="doc-name">社区情况汇总表</td><td>各社区面积、人口户数、包含小区数量、辖区单位、社区工作力量、存在的主要问题。是否有此资料？</td></tr>
                <tr><td style="text-align:center">2</td><td class="doc-name">人口资料</td><td>分社区：居住户数、户籍人口、常住人口、老年人口（60+/65+）、租住人口、流动人口。数据年份和口径请标注清楚。是否有此资料？</td></tr>
                <tr><td style="text-align:center">3</td><td class="doc-name">特殊群体台账</td><td>低保户、特困户、残疾人、独居老人数量及主要分布小区（脱敏统计）。是否有此资料？</td></tr>
                <tr><td style="text-align:center">4</td><td class="doc-name">社区服务设施配置</td><td>各社区服务中心位置、面积、功能配置（党群服务、政务服务、文化活动、卫生计生、养老助残等）、运营状况。是否有此资料？</td></tr>
                <tr><td style="text-align:center">5</td><td class="doc-name">社区历史与文化</td><td>老地名、特色街巷、历史故事、传统风貌建筑、非物质文化遗产。是否有相关文字或图片资料？</td></tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </div>

    <!-- 3. 违章建筑信息 -->
    <div class="collapse">
      <div class="collapse-header" onclick="toggleCollapse(this)">
        <span class="name">🚫 3. 违章建筑信息</span>
        <span class="arrow">▶</span>
      </div>
      <div class="collapse-body">
        <div class="collapse-inner">
          <div class="table-wrap">
            <table>
              <thead><tr><th style="width:40px">序号</th><th style="width:150px">资料类型</th><th>具体内容与格式要求</th></tr></thead>
              <tbody>
                <tr><td style="text-align:center">1</td><td class="doc-name">违章建筑台账</td><td>辖区内违章建筑位置、面积、类型、建设时间、当事人、处理情况（已拆除/待拆除/已处罚/历史遗留）。由街道城管中队或社区提供。是否有此台账？</td></tr>
                <tr><td style="text-align:center">2</td><td class="doc-name">小区内私搭乱建情况</td><td>各小区内私搭乱建的分布、数量、典型情况，居民反映强烈的违建点位。是否有相关记录？</td></tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </div>

    <!-- 4. 已开展及拟开展的更新项目 -->
    <div class="collapse">
      <div class="collapse-header" onclick="toggleCollapse(this)">
        <span class="name">🏗️ 4. 已开展及拟开展的更新项目</span>
        <span class="arrow">▶</span>
      </div>
      <div class="collapse-body">
        <div class="collapse-inner">
          <div class="table-wrap">
            <table>
              <thead><tr><th style="width:40px">序号</th><th style="width:150px">资料类型</th><th>具体内容与格式要求</th></tr></thead>
              <tbody>
                <tr><td style="text-align:center">1</td><td class="doc-name">老旧小区改造项目清单</td><td>已改造/正在改造/计划改造的老旧小区清单，含小区名称、改造年份、改造内容、投资金额、资金来源、工期、实施单位。所有要改造的项目、报的计划都经过街道社区之手，请尽量提供完整清单。是否有此资料？</td></tr>
                <tr><td style="text-align:center">2</td><td class="doc-name">已开展的环境整治项目</td><td>已实施的道路整治、绿化提升、外立面改造、照明改造等环境整治项目清单及内容。是否有此资料？</td></tr>
                <tr><td style="text-align:center">3</td><td class="doc-name">基础设施改造项目</td><td>供水、排水、燃气、电力、通信等基础设施改造项目清单，含位置、内容、投资、工期。是否有此资料？</td></tr>
                <tr><td style="text-align:center">4</td><td class="doc-name">上级已安排及拟安排项目</td><td>上级部门已下达或拟下达涉及本片区的项目，含项目名称、来源渠道、内容、投资、时间节点、责任单位。是否有相关通知或计划文件？</td></tr>
                <tr><td style="text-align:center">5</td><td class="doc-name">项目申报材料</td><td>各类项目的申报材料、实施方案、可研报告、初步设计等。是否有相关文件？</td></tr>
                <tr><td style="text-align:center">6</td><td class="doc-name">加装电梯数据</td><td>已加装电梯数量、位置、4-6层住宅清单、加装条件评估、补贴政策。是否有此资料？</td></tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </div>

    <!-- 5. 相关规划和体检资料 -->
    <div class="collapse">
      <div class="collapse-header" onclick="toggleCollapse(this)">
        <span class="name">📋 5. 相关规划和体检资料</span>
        <span class="arrow">▶</span>
      </div>
      <div class="collapse-body">
        <div class="collapse-inner">
          <div class="table-wrap">
            <table>
              <thead><tr><th style="width:40px">序号</th><th style="width:150px">资料类型</th><th>具体内容与格式要求</th></tr></thead>
              <tbody>
                <tr><td style="text-align:center">1</td><td class="doc-name">城市体检相关资料</td><td>城市体检报告中涉及本街道/社区的内容，指标数据、问题清单、整改建议。街道社区作为基层单位，应该有详细资料或反馈意见。是否有此资料？</td></tr>
                <tr><td style="text-align:center">2</td><td class="doc-name">城市更新专项规划相关资料</td><td>城市更新专项规划中涉及本片区的内容，更新单元划分、更新策略、项目库。是否有相关文件或图纸？</td></tr>
                <tr><td style="text-align:center">3</td><td class="doc-name">片区体检和策划资料</td><td>是否有针对本片区的体检报告、策划方案、前期研究等资料？如有请提供。</td></tr>
                <tr><td style="text-align:center">4</td><td class="doc-name">各类专项规划相关内容</td><td>综合交通、环境卫生、公共服务设施、住房发展、历史文化保护等专项规划中涉及本片区的内容。是否有相关文件？</td></tr>
                <tr><td style="text-align:center">5</td><td class="doc-name">街道社区规划和计划</td><td>街道国民经济和社会发展计划、社区发展规划、年度工作计划等。是否有相关文件？</td></tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </div>

    <!-- 6. 其他资料 -->
    <div class="collapse">
      <div class="collapse-header" onclick="toggleCollapse(this)">
        <span class="name">📎 6. 其他资料</span>
        <span class="arrow">▶</span>
      </div>
      <div class="collapse-body">
        <div class="collapse-inner">
          <div class="table-wrap">
            <table>
              <thead><tr><th style="width:40px">序号</th><th style="width:150px">资料类型</th><th>具体内容与格式要求</th></tr></thead>
              <tbody>
                <tr><td style="text-align:center">1</td><td class="doc-name">企业闲置建筑信息</td><td>辖区内集体企业、民营企业闲置厂房、仓库、办公用房位置、面积、产权、现状、处置意向。是否有相关信息？</td></tr>
                <tr><td style="text-align:center">2</td><td class="doc-name">房屋权属情况</td><td>辖区内公房、单位自管房、房改房、廉租房、公租房等权属情况，产权单位、管理单位、使用状况。是否有相关台账？</td></tr>
                <tr><td style="text-align:center">3</td><td class="doc-name">危房及安全隐患信息</td><td>辖区内疑似危房、安全隐患建筑、消防隐患点、内涝点等位置和情况。街道社区在第一线掌握的信息最全面，请尽量提供。是否有相关记录？</td></tr>
                <tr><td style="text-align:center">4</td><td class="doc-name">街道建设项目计划</td><td>街道牵头或涉及的各类建设项目清单，含项目名称、位置、内容、投资、工期。是否有此资料？</td></tr>
                <tr><td style="text-align:center">5</td><td class="doc-name">其他相关资料</td><td>街道社区认为与城市更新相关的其他资料，如居民意见汇总、信访记录、12345热线反映问题等。如有请提供。</td></tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </div>

    <div class="sub-title">二、需要了解的情况和诉求</div>
    <p style="font-size:13px;color:#9aa0a6;margin-bottom:14px;">通过座谈了解街道社区的工作重点、上级项目安排、居民诉求和推进难点，这些信息对策划方案至关重要。</p>

    <div class="sub-sub-title">1. 街道社区工作重点和计划</div>
    <ul class="bullet-list">
      <li>当前街道社区在城市更新、老旧小区改造方面的工作重点是什么？</li>
      <li>已开展了哪些工作？进展如何？取得了哪些成效？</li>
      <li>下一步工作计划是什么？有哪些拟推进的项目？</li>
      <li>街道社区在城市更新中的角色和权限有哪些？需要哪些支持？</li>
    </ul>

    <div class="sub-sub-title">2. 上级项目安排</div>
    <ul class="bullet-list">
      <li>上级部门已安排或拟安排涉及本片区的项目有哪些？</li>
      <li>项目来源渠道是什么？（中央/省/市/区资金，专项债，PPP等）</li>
      <li>项目的时间节点、申报要求、竞争情况如何？</li>
      <li>有哪些项目是街道社区正在争取或拟申报的？</li>
      <li>上级对本片区有什么定位和要求？</li>
    </ul>

    <div class="sub-sub-title">3. 居民诉求</div>
    <ul class="bullet-list">
      <li>居民反映最集中的问题是什么？（供水、排水、停车、物业、安全、环境等）</li>
      <li>不同小区、不同人群的诉求有什么差异？</li>
      <li>居民对城市更新和老旧小区改造的意愿如何？支持度怎样？</li>
      <li>居民出资意愿如何？能接受的出资比例是多少？</li>
      <li>居民最希望改造的内容是什么？最担心的问题是什么？</li>
      <li>特殊群体（老人、残疾人、低保户、租户）有哪些特殊需求？</li>
    </ul>

    <div class="sub-sub-title">4. 推进难点</div>
    <ul class="bullet-list">
      <li>推进城市更新和老旧小区改造的主要困难是什么？</li>
      <li>产权协调方面有哪些难点？（单位产权、公房、私房混合等）</li>
      <li>资金筹措方面有哪些困难？居民出资、社会资本参与情况如何？</li>
      <li>居民意见统一方面有哪些问题？反对改造的原因是什么？</li>
      <li>有哪些历史遗留问题需要解决？</li>
      <li>物业管理方面有哪些痛点？</li>
    </ul>

    <div class="sub-title">三、配合现场踏勘</div>
    <p style="font-size:13px;color:#9aa0a6;margin-bottom:14px;">街道社区的配合是现场踏勘顺利进行的关键，首先要确认基础信息，然后协调带路和联系相关方。</p>

    <div class="sub-sub-title">1. 基础信息确认</div>
    <ul class="bullet-list">
      <li>确认各小区的准确名称、范围、边界（避免"有名无实"或"有实无名"）</li>
      <li>确认小区与社区的对应关系，特别是边界交叉区域</li>
      <li>确认疑似危房、重点问题小区的准确位置</li>
      <li>确认单位大院、企业厂区的准确范围和产权单位</li>
      <li>确认历史建筑、文保单位、传统街巷的准确位置</li>
      <li>核实已有资料中小区名称、地址的准确性，补充缺失信息</li>
    </ul>

    <div class="sub-sub-title">2. 协调配合</div>
    <ul class="bullet-list">
      <li>安排社区工作人员带路，熟悉小区内部情况</li>
      <li>联系小区物业、业委会、单位产权人，协调进入小区内部</li>
      <li>协调进入重点建筑、疑似危房内部查看</li>
      <li>联系知情居民、老住户了解小区历史和问题</li>
      <li>协调厂区、铁路等特殊区域的进入</li>
    </ul>

    <div class="sub-sub-title">3. 现场核实</div>
    <ul class="bullet-list">
      <li>核实已有资料的准确性，发现不一致的当场记录</li>
      <li>补充资料中缺失的信息（建筑质量、基础设施状况等）</li>
      <li>记录现场发现的新问题、新情况</li>
      <li>拍摄现场照片，每个小区至少4张（入口、整体、典型问题、周边）</li>
      <li>用GPS或GIS平台记录每个调查点的经纬度</li>
    </ul>
  </div>

'''

# 替换第二部分
part2_start = content.find('  <!-- 第二部分 -->')
part3_start = content.find('  <!-- 第三部分 -->')

if part2_start > -1 and part3_start > -1:
    content = content[:part2_start] + new_part2 + content[part3_start:]
    print('第二部分替换成功')
    print(f'新文件大小: {len(content)} 字符')
else:
    print(f'未找到标记: part2_start={part2_start}, part3_start={part3_start}')

with open('guide.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('guide.html 更新完成')
