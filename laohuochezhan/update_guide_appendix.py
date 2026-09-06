# -*- coding: utf-8 -*-
# 修改指导手册网页版：添加附件部分

with open(r'D:\myweb\laohuochezhan\guide.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. 在目录中添加附件链接
old_toc = '''      <li><a href="#part4">第四部分 · 调研流程与注意事项 <span class="toc-num">5阶段</span></a></li>
    </ul>'''

new_toc = '''      <li><a href="#part4">第四部分 · 调研流程与注意事项 <span class="toc-num">5阶段</span></a></li>
      <li><a href="#appendix">附件 · 调研表格模板下载 <span class="toc-num">4张表格</span></a></li>
    </ul>'''

if old_toc in content:
    content = content.replace(old_toc, new_toc)
    print('目录附件链接添加成功')
else:
    print('未找到目录插入点')

# 2. 在修改记录中添加V2.1版本
old_revision = '''          <tr>
            <td style="text-align:center;font-weight:bold;color:#8ab4f8">V2.0</td>
            <td style="text-align:center">2026-09-06</td>
            <td>大改：部门分类修正（10个主要部门全称+新归属），街道社区合并为联合座谈（收集资料/了解诉求/配合踏勘三大块），增加修改记录页，正式排版。</td>
          </tr>
        </tbody>'''

new_revision = '''          <tr>
            <td style="text-align:center;font-weight:bold;color:#8ab4f8">V2.0</td>
            <td style="text-align:center">2026-09-06</td>
            <td>大改：部门分类修正（10个主要部门全称+新归属），街道社区合并为联合座谈（收集资料/了解诉求/配合踏勘三大块），增加修改记录页，正式排版。</td>
          </tr>
          <tr>
            <td style="text-align:center;font-weight:bold;color:#34a853">V2.1</td>
            <td style="text-align:center">2026-09-06</td>
            <td>新增附件部分：街道社区调研表格模板（含通知正文+4张调研表格）下载链接，目录同步更新。</td>
          </tr>
        </tbody>'''

if old_revision in content:
    content = content.replace(old_revision, new_revision)
    print('修改记录V2.1添加成功')
else:
    print('未找到修改记录插入点')

# 3. 在第四部分之后、返回顶部按钮之前，添加附件部分
old_ending = '''  </div>

</div>

<!-- 返回顶部 -->'''

appendix_html = '''  </div>

  <!-- 附件 -->
  <div class="section" id="appendix">
    <div class="section-title"><span class="num">5</span>附件 · 调研表格模板下载</div>
    <div class="desc">本手册配套提供街道社区调研表格模板，包含通知正文及4张标准化调研表格，可直接用于梧桐、肖家园、菱角山3个街道及白竹亭、又一村、活龙井、文昌阁4个社区的调研填报。</div>

    <div class="table-wrap">
      <table>
        <thead><tr><th style="width:80px">序号</th><th>表格名称</th><th style="width:100px">指标数</th><th style="width:120px">适用对象</th></tr></thead>
        <tbody>
          <tr>
            <td style="text-align:center">1</td>
            <td>小区楼栋问题统计表</td>
            <td style="text-align:center">24项</td>
            <td style="text-align:center">各小区</td>
          </tr>
          <tr>
            <td style="text-align:center">2</td>
            <td>小区配套设施问题统计表</td>
            <td style="text-align:center">22项</td>
            <td style="text-align:center">各小区</td>
          </tr>
          <tr>
            <td style="text-align:center">3</td>
            <td>社区配套设施统计表</td>
            <td style="text-align:center">15项</td>
            <td style="text-align:center">各社区</td>
          </tr>
          <tr>
            <td style="text-align:center">4</td>
            <td>街道配套设施问题统计表</td>
            <td style="text-align:center">14项</td>
            <td style="text-align:center">各街道</td>
          </tr>
        </tbody>
      </table>
    </div>

    <div style="background:linear-gradient(135deg,#e8f5e9 0%,#c8e6c9 100%);border-radius:12px;padding:28px;margin-top:24px;text-align:center;">
      <div style="font-size:18px;font-weight:700;color:#2e7d32;margin-bottom:10px;">📄 下载调研表格模板</div>
      <div style="font-size:14px;color:#388e3c;margin-bottom:18px;">含通知正文 + 4张标准化调研表格，可直接编辑使用</div>
      <a href="attachments/老火车站片区_街道社区调研表格模板.docx" class="download-btn" download style="display:inline-block;background:#2e7d32;color:white;padding:14px 36px;border-radius:8px;text-decoration:none;font-size:15px;font-weight:600;transition:all 0.25s ease;">
        ⬇ 下载 Word 文档
      </a>
      <div style="font-size:12px;color:#66bb6a;margin-top:12px;">文件格式：DOCX · 文件大小：约25KB · 更新时间：2026年9月6日</div>
    </div>

    <div class="desc" style="margin-top:20px;font-size:12px;color:#9aa0a6;">
      <strong>使用说明：</strong>本表格模板由项目组根据湘乡市城市体检调研表格模板改编，表头保留"体检内容/体检指标/指标填报"等原表述（本项目包含城市体检、片区策划、实施方案等多方面内容）。各街道社区填报时，请根据实际情况如实填写，不确定的数据标注"待核实"。
    </div>
  </div>

</div>

<!-- 返回顶部 -->'''

if old_ending in content:
    content = content.replace(old_ending, appendix_html)
    print('附件部分添加成功')
else:
    print('未找到附件插入点')

with open(r'D:\myweb\laohuochezhan\guide.html', 'w', encoding='utf-8') as f:
    f.write(content)

print(f'指导手册网页版修改完成，文件大小: {len(content)} 字符')
