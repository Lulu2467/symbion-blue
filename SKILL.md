---
name: symbion-blue
description: >-
  Maintains the blue Symbion home (html[data-theme="blue"]) in
  homepage/H2-B-switching-twin-prototype.html and
  https://lulu2467.github.io/symbion-web/. Use when editing the blue theme,
  蓝色, 平时在用, Home, Cosmo, Community, Kanban, settings, or the account menu.
  Do not use it for the green theme.
argument-hint: "[screen or component]"
license: MIT
metadata:
  author: Reddick
  version: 1.0.2
---

# Symbion 蓝色版

只改 `html[data-theme="blue"]`。不新做一页，不动绿色。

## Source of Truth

https://lulu2467.github.io/symbion-web/

稿：`homepage/H2-B-switching-twin-prototype.html`（与仓库 `index.html` 同一份）

色值：[assets/design-tokens/tokens.json](assets/design-tokens/tokens.json)

## Stack

一份 HTML。蓝色覆盖 `--green*`。Inter + Noto Sans SC。无组件库。

## When to use

1. 改蓝色首页、Cosmo、Community、Kanban、设置、账户菜单。
2. 核对按钮、图标、悬停。
3. 确认绿色没被带上。

## Workflow

1. 只打开 Routing 里点名的文件。
2. 选择器放在蓝色下。嵌进 `#teamHost` 时不要再写 `html[...]`。
3. 改现有控件。没后端就置灰，不写假成功。
4. 浏览器里点通。用 computed style 量尺寸。
5. 跑 `python scripts/check-blue.py <稿路径>`。
6. 用户没说别动 Git，就把同一份推到两个公开文件。

## Output

`:root` 的 `--green` 仍是 `#008b68`。用中文说明改了哪一块。公开页更新后给硬刷新地址。

## Routing

| 何时 | 文件 |
| --- | --- |
| 颜色 | [colors.md](references/foundations/colors.md) |
| 字号 | [font.md](references/foundations/font.md) |
| 间距 | [spacing.md](references/foundations/spacing.md) |
| 圆角 | [border-radius.md](references/foundations/border-radius.md) |
| 某一屏 | [pc.md](references/pages/pc.md) |
| 设置导航 | [settings-nav.md](references/components/settings-nav.md) |
| 日程详情 | [event-detail.md](references/components/event-detail.md) |
| 添加好友 | [add-friend.md](references/components/add-friend.md) |
| Cosmos 图标 | [cosmos-icon.md](references/components/cosmos-icon.md) |
| 按钮 | [button.md](references/components/button.md) |
| 说法 | [ui-prototype.md](references/prompts/ui-prototype.md) |
| 正例 | [capsule-button.css](examples/good-cases/capsule-button.css) |
| 反例 | [nested-selector.css](examples/bad-cases/nested-selector.css) |
| 坑 | [gotchas.md](gotchas.md) |

## Limit

绿色、假数据、假成功不做。坑见 [gotchas.md](gotchas.md)。没有单独手机页，见 [mobile.md](references/pages/mobile.md)。
