# -*- coding: utf-8 -*-
# 修改首页：添加甲方提供基础资料清单入口和附件下载链接

with open(r'D:\myweb\laohuochezhan\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. 在工具列表中添加甲方提供基础资料清单入口（在已有资料清单之后）
tool_entry = '''
    <a href="materials.html" class="tool-item" style="--accent:#00897b; --icon-bg:rgba(0,137,123,0.15);">
      <div class="tool-icon">📋</div>
      <div class="tool-body">
        <div class="tool-name">甲方提供基础资料清单</div>
        <div class="tool-desc">项目启动阶段甲方原始提供的基础资料文件汇总，7大类16份（套），含规划成果、GIS数据、图件资料、现状统计、资源资产、调研资料、对标案例，每份标注完整名称、格式、大小及内容概述。</div>
        <div class="tool-tags">
          <span class="tool-tag">基础资料</span>
          <span class="tool-tag">甲方提供</span>
          <span class="tool-tag">7大类16份</span>
          <span class="tool-tag">内容概述</span>
        </div>
      </div>
      <div class="tool-arrow">→</div>
    </a>
'''

# 在已有资料清单的</a>之后、</div>（tools-list结束）之前插入
marker = '''      <div class="tool-arrow">→</div>
    </a>
  </div>

  <!-- 项目信息 -->'''

if marker in content:
    content = content.replace(marker, tool_entry + '''  </div>

  <!-- 项目信息 -->''')
    print('工具列表入口添加成功')
else:
    print('未找到工具列表插入点')

# 2. 在资料附件下载区域添加Word文档下载链接
attachment_entry = '''
    <a href="attachments/老火车站片区_甲方提供基础资料清单.docx" class="attachment-item" download>
      <div class="attachment-icon">📋</div>
      <div class="attachment-info">
        <div class="attachment-name">老火车站片区_甲方提供基础资料清单.docx</div>
        <div class="attachment-meta">上传时间：2026年9月6日 · 文件大小：约50KB</div>
        <div class="attachment-desc">甲方提供基础资料清单，7大类16份（套），含规划成果、GIS空间数据、图件资料、现状统计数据、资源资产、调研资料、对标案例，每份资料标注完整名称、格式、大小及内容概述，附待补充资料清单（14项）。</div>
      </div>
      <div class="attachment-download">下载 ↓</div>
    </a>
'''

# 在街道社区调研表格模板的</a>之后、</div>（attachments-section结束）之前插入
marker2 = '''      <div class="attachment-download">下载 ↓</div>
    </a>

  </div>

  <!-- 页脚 -->'''

if marker2 in content:
    content = content.replace(marker2, attachment_entry + '''  </div>

  <!-- 页脚 -->''')
    print('资料附件下载链接添加成功')
else:
    print('未找到附件下载插入点')

with open(r'D:\myweb\laohuochezhan\index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print(f'首页修改完成，文件大小: {len(content)} 字符')
