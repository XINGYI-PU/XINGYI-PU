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

致谢下方使用访客徽章，Profile Views 使用你提供的红色小章鱼图片，搭配 [Moe Counter](https://count.getloli.com/) 的 normal-1 数字主题；沿用原计数器 ID。两个服务分别计数，数值不一定相同；它们记录图片请求，受 GitHub 缓存和重复访问影响，不等于独立访客人数。计数从各自首次收到请求开始，未套用参考主页的起始日期。这里没有使用原例中的 Glitch 计数器。

若图片无法显示：先检查 Actions 日志；确认图片已生成、仓库允许 Actions 写入、默认分支未阻止机器人提交；Metrics 失败时检查 `METRICS_TOKEN` 是否过期。第三方访问计数和 Star History 图片还依赖各自服务的可用性。
