with open(r'D:\myweb\laohuochezhan\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. 在CSS部分添加附件下载区域样式（在页脚样式之前）
css_attachments = '''
  /* 资料附件下载 */
  .attachments-section {
    background: rgba(32,33,36,0.5);
    border: 1px solid rgba(255,255,255,0.06);
    border-radius: 16px;
    padding: 36px;
    margin-bottom: 40px;
  }
  .attachments-title {
    font-size: 18px;
    font-weight: 600;
    color: #e8eaed;
    margin-bottom: 20px;
    display: flex;
    align-items: center;
    gap: 8px;
  }
  .attachment-item {
    display: flex;
    align-items: center;
    gap: 16px;
    padding: 16px 20px;
    background: rgba(255,255,255,0.03);
    border: 1px solid rgba(255,255,255,0.06);
    border-radius: 12px;
    margin-bottom: 12px;
    transition: all 0.25s ease;
    text-decoration: none;
  }
  .attachment-item:hover {
    background: rgba(26,115,232,0.08);
    border-color: rgba(26,115,232,0.3);
    transform: translateY(-1px);
  }
  .attachment-icon {
    width: 44px;
    height: 44px;
    background: rgba(26,115,232,0.12);
    border-radius: 10px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 20px;
    flex-shrink: 0;
  }
  .attachment-info {
    flex: 1;
    min-width: 0;
  }
  .attachment-name {
    font-size: 14px;
    font-weight: 600;
    color: #e8eaed;
    margin-bottom: 4px;
  }
  .attachment-meta {
    font-size: 12px;
    color: #9aa0a6;
    margin-bottom: 4px;
  }
  .attachment-desc {
    font-size: 12px;
    color: #80868b;
    line-height: 1.5;
  }
  .attachment-download {
    font-size: 13px;
    color: #8ab4f8;
    font-weight: 500;
    flex-shrink: 0;
    display: flex;
    align-items: center;
    gap: 4px;
  }
  @media (max-width: 640px) {
    .attachments-section { padding: 24px; }
    .attachment-item { flex-wrap: wrap; }
    .attachment-download { width: 100%; text-align: right; margin-top: 8px; }
  }

'''

# 在页脚样式之前插入附件样式
css_insert_point = content.find('  /* 页脚 */')
if css_insert_point > -1:
    content = content[:css_insert_point] + css_attachments + content[css_insert_point:]
    print('CSS样式添加成功')
else:
    print('未找到CSS插入点')

# 2. 在项目信息之后、页脚之前插入附件下载区域HTML
html_attachments = '''
  <!-- 资料附件下载 -->
  <div class="attachments-section">
    <div class="attachments-title">📎 资料附件下载</div>

    <a href="attachments/老火车站片区_街道社区调研表格模板.docx" class="attachment-item" download>
      <div class="attachment-icon">📄</div>
      <div class="attachment-info">
        <div class="attachment-name">老火车站片区_街道社区调研表格模板.docx</div>
        <div class="attachment-meta">上传时间：2026年9月6日 · 文件大小：约50KB</div>
        <div class="attachment-desc">街道社区调研表格模板，含通知正文+4张调研表格：①小区楼栋问题统计表（24项指标）②小区配套设施问题统计表（22项指标）③社区配套设施统计表（15项指标）④街道配套设施问题统计表（14项指标）。适用于梧桐、肖家园、菱角山3个街道及白竹亭、又一村、活龙井、文昌阁4个社区调研填报。</div>
      </div>
      <div class="attachment-download">下载 ↓</div>
    </a>

  </div>

'''

# 在页脚注释之前插入
html_insert_point = content.find('  <!-- 页脚 -->')
if html_insert_point > -1:
    content = content[:html_insert_point] + html_attachments + content[html_insert_point:]
    print('HTML附件区域添加成功')
else:
    print('未找到HTML插入点')

with open(r'D:\myweb\laohuochezhan\index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print(f'完成，文件大小: {len(content)} 字符')
