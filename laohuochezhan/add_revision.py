with open('guide.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 修改记录HTML
revision_html = '''
  <!-- 修改记录 -->
  <div class="section" id="revision">
    <div class="section-title"><span class="num">0</span>修改记录</div>
    <div class="desc">记录文档各版本的修改内容，方便前后对比。</div>
    <div class="table-wrap">
      <table>
        <thead><tr><th style="width:80px">版本</th><th style="width:120px">日期</th><th>修改内容摘要</th></tr></thead>
        <tbody>
          <tr>
            <td style="text-align:center;font-weight:bold;color:#8ab4f8">V1.0</td>
            <td style="text-align:center">2026-08</td>
            <td>初版生成，包含部门资料调取清单、街道社区调研、现场踏勘清单、调研流程四大部分。</td>
          </tr>
          <tr>
            <td style="text-align:center;font-weight:bold;color:#8ab4f8">V2.0</td>
            <td style="text-align:center">2026-09-06</td>
            <td>
              <strong>第一部分大改：</strong>10个部门全称，新增第三次全国国土调查、国资委、水利局；资料归属修正（城市更新专项规划/体检报告/住房发展规划/历史文化保护规划→住建局，违章建筑→街道社区，停车设施/老旧管网/老旧泵站→城管局，消防栓→水务公司）；去掉重要程度标记改用序号；每项标注文件格式要求。<br><br>
              <strong>第二部分重写：</strong>街道社区合并为联合座谈，分收集资料（6类）/了解诉求（4方面）/配合踏勘（3方面）三大块，每项标注"是否有此资料"，标准模板表格用户附后。<br><br>
              <strong>第三、四部分：</strong>保留原有内容。<br><br>
              <strong>排版：</strong>正式公文格式，黑体标题+宋体正文，表格表头浅蓝底色。
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>

'''

# 在目录结束后、第一部分前插入
insert_point = content.find('  <!-- 第一部分 -->')
if insert_point > -1:
    content = content[:insert_point] + revision_html + content[insert_point:]
    print('修改记录插入成功')
else:
    print('未找到插入点')

# 在目录中加修改记录链接
toc_old = '''      <li><a href="#part1">第一部分 · 部门资料调取清单 <span class="toc-num">10+5部门</span></a></li>'''
toc_new = '''      <li><a href="#revision">修改记录 <span class="toc-num">V2.0</span></a></li>
      <li><a href="#part1">第一部分 · 部门资料调取清单 <span class="toc-num">10+5部门</span></a></li>'''

if toc_old in content:
    content = content.replace(toc_old, toc_new)
    print('目录链接添加成功')
else:
    print('未找到目录链接')

with open('guide.html', 'w', encoding='utf-8') as f:
    f.write(content)

print(f'完成，文件大小: {len(content)} 字符')
