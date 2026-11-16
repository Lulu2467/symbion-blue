# 踩过的坑

只记已经发生过的。每条写清错在哪、后果、正确做法。

## 高频

### 选择器写进 `#teamHost` 后又加 `html[data-theme="blue"]`

原生 CSS 嵌套会把它存成 `& html...`，规则不生效。群组新建弹层因此拉成整条会话的宽度（约 1067px），不是 680px。

正确：嵌套里只写 `.gi-sheet` 这类类，让它变成 `#teamHost .gi-sheet`。

### 后面的 `font: inherit` 把字号清掉

`button.kd-act` 写在 `.kd-row` 之后，又更具体。Upload file 和 Meeting 从 13px 回到父级 16px。

正确：`font: inherit` 下一行重新写 `font-size: 13px; font-weight: 400`。

### 没加蓝色前缀，绿色一起变

`:root` 的绿色是产品的另一套主题。改到不带 `html[data-theme="blue"]` 的规则，绿色首页会跟着变。

正确：蓝色覆盖只写在蓝色选择器下。离开蓝色时收起 `#railMeMenu`。

### 用 `getBoundingClientRect` 当 CSS 像素

这一页画布是缩放的。量到的 13px 空隙，实际 CSS 可以是约 27px。

正确：看 computed padding / font-size。截图只用来看齐不齐。

## 中频

### 设置项悬停盖不住当前页

`[aria-current="page"]` 比 `:hover` 更具体。当前页一块底色，悬停另一块，看起来像两套高亮。

正确：悬停和当前页都用底 `#f6f7f8`。悬停字 `#1d1d1f`、字重 400。当前页字 `#3c7a94`、字重 650。当前页的悬停要单独写一条，否则会掉回黑字。

### 蓝色 Summon 规则里写了 `display`

`.dir-summon` 默认 `display: none`，卡片悬停才变成 `inline-flex`。蓝色规则若再写 `display: inline-flex`，按钮会一直出现。

正确：蓝色只改尺寸、颜色、圆角。显示时机留给原来的悬停规则。个人页头部那条单独写 `display: inline-flex` 是对的，因为那里本来就要露出来。

### 中文在胶囊里偏上

字框垂直居中后，墨迹仍高约 1px。「进入」和 Summon 看起来不在正中。

正确：高度 32px，`padding: 1px 16px 0`，`line-height: 1`，`inline-flex` 居中。

## 低频

### 菜单图标按 SVG 原稿写死 200px

账户菜单的 Cosmos 用 1024 viewBox。宽高由 CSS 收成 16px，`fill="currentColor"` 才能在悬停时变青。

正确：不要把导出 SVG 的 `width="200"` 写进按钮。

### 添加好友底部再放一个 Close

右上角已经有 ×。底部 Close 是多余的一层。

正确：`:has(#friendResults)` 时隐藏 `.sheet-actions`。× 仍然关闭。

### 拉取公开仓库时把整份文件内容 GET 下来

contents 接口的响应会把凭证打进终端。

正确：用 git tree 拿 sha，再 PUT。`index.html` 和 `H2-B-switching-twin-prototype.html` 必须是同一份字节。第一次 PUT 之后要重新取 tree，再 PUT 第二个文件。
