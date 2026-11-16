# 字体

页面已从 Google Fonts 加载 Inter 与 Noto Sans SC。不要再嵌一份字体文件。

栈：Inter, "Noto Sans SC", "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei UI", "Microsoft YaHei", system-ui, sans-serif。

| 位置 | 大小 | 字重 |
| --- | --- | --- |
| 日程标题 | 15px | 650 |
| 日程正文、按钮、日期 | 13px | 400 |
| Description 标签 | 13px | 500，色 `#8b9198` |
| 设置悬停 | 13px | 400，色 `#1d1d1f` |
| 设置当前页 | 13px | 650，色 `#3c7a94` |

同一块详情里不要再出现 12px 和 16px。标题保持 15px，不要为了“统一”收成 13px。

`font: inherit` 会清掉前面的 `font-size`。写在按钮上时，下一行必须把字号写回去。
