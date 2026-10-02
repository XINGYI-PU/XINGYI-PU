# XINGYI-PU 的 GitHub Profile README

这是可复制到个人主页仓库的独立文件包。README 包含技术栈表格、截图中的三种贡献可视化、致谢与访问徽章、Star History、Profile Views。

## 启用步骤

1. 创建或打开公开仓库 `XINGYI-PU/XINGYI-PU`。
2. 将本文件夹内的 `README.md` 和 `.github/workflows/profile-images.yml` 复制到该仓库的相同路径。不要复制外层的 `docs/github-profile/XINGYI-PU` 路径。`SETUP.md` 可按需保留。
3. 技术栈已根据你的五个公开项目填写；后续按项目变化更新即可。
4. 为等距日历创建一个 Personal access token (classic)，仅展示公开数据时不勾选 scopes。进入主页仓库的 `Settings → Secrets and variables → Actions → New repository secret`，名称填 `METRICS_TOKEN`，值填 token。token 只存入 Secret。生成图像的写入权限由工作流自带的 `GITHUB_TOKEN` 提供。详见 [Metrics 官方设置说明](https://github.com/lowlighter/metrics/blob/master/.github/readme/partials/documentation/setup/action.md)。
5. 进入 `Actions → Update Profile Images → Run workflow`，选择默认分支并运行。成功后会出现下列文件，README 就能展示你的真实数据。

```text
assets/github-snake.svg
assets/github-snake-dark.svg
profile-3d-contrib/profile-green-animate.svg
github-metrics.svg
```

工作流每天 UTC 18:00（韩国时间次日 03:00）自动更新，也支持手动运行。首次上传 README 会触发一次运行；若尚未设置 Secret，设置完成后重新运行即可。图片生成前会暂时显示缺失图片。工作流使用仓库所有者的用户名，无须在 YAML 中手动替换。

## 三张图对应的组件

| 参考截图              | 本包组件                                                                                            | 数据内容                                         |
| --------------------- | --------------------------------------------------------------------------------------------------- | ------------------------------------------------ |
| 贪吃蛇                | [Platane/snk](https://github.com/Platane/snk)                                                       | 动画形式的 GitHub 贡献图，紫色蛇身；支持明暗主题 |
| 3D 图＋环形图＋雷达图 | [GitHub Profile 3D Contrib](https://github.com/yoshi389111/github-profile-3d-contrib)               | 绿色 3D 贡献柱、语言分布、活动雷达和统计         |
| 等距日历＋提交统计    | [Metrics isocalendar](https://github.com/lowlighter/metrics/tree/master/source/plugins/isocalendar) | 全年贡献日历和连续提交、每日提交统计             |

图片使用你的账户数据生成，数量、语言比例和柱形高度不会沿用参考截图。实际渲染由组件版本与可访问的 GitHub 数据决定。本地已检查文件格式和路径，尚未在你的 GitHub 仓库执行工作流。

## Star History 和访问计数

Star History 默认跟踪 `XINGYI-PU/XINGYI-PU` 仓库收到的 Star。若想展示某个项目，替换 README 中全部 `XINGYI-PU/XINGYI-PU`（包括明暗主题图片 URL 和跳转链接）；没有 Star 时图表可能为空。

致谢下方的访客徽章和 Profile Views 章鱼计数器使用同一个 visitor-badge.laobi.icu 计数 ID（XINGYI-PU.XINGYI-PU）。章鱼图片由 Update Octopus Counter 工作流每小时同步，初始补齐七位数字；每位数字的形象固定。这个服务记录图片请求，受缓存、重复访问及自动同步请求影响，不等于独立访客人数。原 Moe Counter 服务阻止了自动读取，已不再使用其计数数据。

若图片无法显示：先检查 Actions 日志；确认图片已生成、仓库允许 Actions 写入、默认分支未阻止机器人提交；Metrics 失败时检查 `METRICS_TOKEN` 是否过期。第三方访问计数和 Star History 图片还依赖各自服务的可用性。

## 章鱼数字主题

0：原章鱼；1：招手；2：大笑；3：惊讶；4：睡觉；5：哭泣；6：生气；7：爱心；8：疑惑；9：跳舞。

复制文件包时，也需上传 `render_counter.py`、`assets/octopus-digits/`、`assets/octopus-counter.png` 和 `.github/workflows/octopus-counter.yml`。新工作流无需额外 Secret，定时在每小时第 17 分钟执行（GitHub 可能延迟）；手动运行可立即同步。数据源失败时任务报错并保留最后一次成功生成的计数图片，不会伪造或重置数字。
