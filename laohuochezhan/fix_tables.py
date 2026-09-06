with open('guide.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

street_new = '''    <div class="table-wrap">
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
    </div>
'''

community_new = '''    <div class="table-wrap">
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
    </div>
'''

print('街道表格起始行:', lines[741].strip()[:50])
print('街道表格结束行:', lines[752].strip()[:50])

new_lines = lines[:741] + [street_new] + lines[753:]
print(f'街道替换后行数: {len(new_lines)}')

content = ''.join(new_lines)
comm_start = content.find('小区逐栋台账')
print(f'社区表格关键词位置: {comm_start}')

if comm_start > -1:
    # 往前找到表格开始
    table_start = content.rfind('<div class="table-wrap">', 0, comm_start)
    print(f'社区表格开始位置: {table_start}')
    # 往后找到表格结束
    table_end = content.find('</div>\n\n    <div class="sub-sub-title">社区座谈', table_start)
    print(f'社区表格结束位置: {table_end}')
    if table_start > -1 and table_end > -1:
        content = content[:table_start] + community_new + content[table_end:]
        print('社区表格替换成功')

with open('guide.html', 'w', encoding='utf-8') as f:
    f.write(content)

print(f'完成，文件大小: {len(content)} 字符')
