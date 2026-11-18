---
name: src-bug-bounty
description: Runs an authorized SRC asset from a chat-provided URL through scoped setup, a cross-session clueboard, JS/API reconnaissance, expert route selection, human-gated validation, evidence checks, and report drafting. / 从聊天提供的授权 SRC 资产开始，通过范围设置、跨会话线索板、JS/API 侦察、专家路由选择、人工审批验证、证据检查和报告草稿执行 SRC 黑盒测试。Use when the user provides a domestic SRC asset, asks for black-box Web/API reconnaissance, or wants Codex to operate an authorized bug bounty workflow without manually running CLI tools. / 用户提供国内 SRC 资产，要求黑盒 Web/API 侦察，或希望 Codex 在无需手动运行 CLI 工具的情况下运行授权漏洞赏金工作流时使用。
---

# SRC Guarded Workflow / SRC Guarded 工作流

## Chat-first experience / 聊天优先体验

The user should normally provide only:

- The SRC program name or policy URL. / SRC 项目名称或策略 URL。
- One asset URL or host that is explicitly in scope. / 一个明确在范围内的资产 URL 或主机。
- Confirmation that the asset is authorized. / 确认该资产已获授权。

Do not make the user type shell commands. Use the `srcGuardedWorkflow` MCP tools for setup, reconnaissance, requests, evidence, validation, and report drafting. / 不要让用户输入 shell 命令。使用 `srcGuardedWorkflow` MCP 工具进行设置、侦察、请求、证据、验证和报告草稿。

## Mandatory first step / 强制第一步

If the user provides an asset without a program/policy and authorization confirmation, ask one concise question:

> 请给我这个资产所属的 SRC 项目/规则链接，并确认该资产在授权范围内；确认后我会自动建立范围并开始被动侦察。

Never begin active requests merely because a host is publicly reachable. / 仅因为主机公开可达，就不要开始主动请求。

## One-message start / 一条消息启动

When the program, asset, and authorization are present, call `src_start` with the asset, program, policy URL, `authorization_confirmed: true`, and an optional minimal scope override. / 当程序、资产和授权都就绪，带资产、程序、策略 URL、`authorization_confirmed: true` 和可选的最小范围覆盖调用 `src_start`。

Then summarize:

- Run ID and output directory. / 运行 ID 和输出目录。
- `CLUEBOARD.md` path and the current focus. / `CLUEBOARD.md` 路径和当前焦点。
- DNS/IP observations. / DNS/IP 观察。
- Certificate-transparency observations, if available. / 证书透明度观察（如有）。
- Baseline HTTP status and security-relevant headers. / 基线 HTTP 状态和安全相关响应头。
- Candidate attack-surface areas, separated into observed facts and hypotheses. / 候选攻击面区域，按观察事实和假设分开。

## Clueboard and expert routing / 线索板与专家路由

Use `src_clueboard` as the run-level working memory: / 将 `src_clueboard` 用作运行级工作内存：

- Read it before the first active action in a target session. / 目标会话的第一次主动操作前先读取。
- Set one concrete current focus. / 设定一个具体的当前焦点。
- Append durable hosts, paths, authentication notes, hypotheses, and negative evidence in the same turn. / 在同一轮内追加持久的主机、路径、鉴权笔记、假设和否定证据。
- Never store full cookies, tokens, credentials, HARs, JS bundles, or real user data. / 永远不要存储完整 Cookie、令牌、凭据、HAR、JS 包或真实用户数据。

Before testing a feature, call `src_hunt_route` with the feature or observed signal. Then call `src_vuln_playbook` with a returned class ID or a narrower keyword. Use the returned `signals`, `safe_tests`, `confirm`, and `false_positives`; do not invent a generic checklist when a specific playbook exists. / 测试功能前，用功能或观察信号调用 `src_hunt_route`，再用返回的类 ID 或更窄关键词调用 `src_vuln_playbook`。使用返回的 `signals`、`safe_tests`、`confirm` 和 `false_positives`；有具体 Playbook 时不要自编通用检查表。

Routes marked `manual_only` are handoffs. Do not pretend this black-box Web/API workflow can automate mobile reverse engineering, Windows reverse engineering, or source-code audit. / 标记为 `manual_only` 的路由是手交路径。不要假装这个黑盒 Web/API 工作流能自动化移动逆向、Windows 逆向或源码审计。

This routing and clueboard model is adapted from CK-Skills under its MIT license. Read [references/expert-routing.md](references/expert-routing.md) for the integration boundaries and route index. / 此路由和线索板模型按 CK-Skills MIT 许可改编。集成边界和路由索引见 [references/expert-routing.md](references/expert-routing.md)。

## Vulnerability priority / 漏洞优先级

1. Tenant isolation, IDOR/BOLA, authentication, and session boundaries. / 1. 租户隔离、IDOR/BOLA、身份验证和会话边界。
2. SSRF, file upload, deserialization, command injection, and injection families. / 2. SSRF、文件上传、反序列化、命令注入和注入家族。
3. Business logic, race conditions, GraphQL, OAuth/JWT, and path traversal. / 3. 业务逻辑、竞态、GraphQL、OAuth/JWT 和路径穿越。
4. XSS, CSRF, CORS, open redirect, WebSocket, cloud storage, and information disclosure. / 4. XSS、CSRF、CORS、开放重定向、WebSocket、云存储和信息泄露。
5. Cache/host-header and request-smuggling only in controlled or lab environments. / 5. 缓存/Host 头和请求走私仅在受控或实验室环境中。

Every active test must follow this loop: falsification control -> baseline -> one-variable hypothesis -> minimum probe -> compare -> confirm or reject. If only a signal is observed, record it as `candidate` or `suspected`, never `verified`. / 每次主动测试必须遵循：证伪控制 -> 基线 -> 单变量假设 -> 最小探测 -> 对比 -> 确认或拒绝。若只观察到信号，记录为 `candidate` 或 `suspected`，绝不记录为 `verified`。

Read [references/vulnerability-playbook.md](references/vulnerability-playbook.md) for the full detection rules. / 完整检测规则见 [references/vulnerability-playbook.md](references/vulnerability-playbook.md)。

## Information gathering pipeline / 信息搜集流程

Use this order and keep each stage bounded: / 按此顺序，每阶段保持边界：

1. `src_start`: passive DNS/CT reconnaissance, one baseline `GET`, and clueboard initialization. / 1. `src_start`：被动 DNS/CT 侦察，一次基线 `GET`，并初始化线索板。
2. `src_clueboard`: read the board and set the current focus. / 2. `src_clueboard`：读取板面并设定当前焦点。
3. `src_asset_intel`: query configured FOFA/Shodan/Quake/Hunter/ZoomEye/urlscan providers with a domain, certificate, or exact asset query. Every result is marked `in_scope` or out-of-scope; only in-scope leads may be tested. / 3. `src_asset_intel`：用域名、证书或精确资产查询配置的 FOFA/Shodan/Quake/Hunter/ZoomEye/urlscan。每条结果标记 `in_scope` 或范围外；只测试范围内的线索。
4. `src_js_inventory`: fetch the baseline page and a bounded set of same-origin JS assets; extract endpoints, parameters, source maps, and API hints. This is active and requires a batch approval because it fetches multiple assets. / 4. `src_js_inventory`：获取基线页面和有限的同源 JS 资产；提取端点、参数、Source maps 和 API 提示。这是主动请求，需要批量批准。
5. Manual browser or Burp/Caido exploration: log in with the approved test account, walk real user flows, and capture the resulting traffic. Save the HAR under `evidence/`; then call `src_import_har`. / 5. 浏览器或 Burp/Caido 人工探索：用批准的测试账号登录，走真实用户流程，捕获结果流量。将 HAR 保存在 `evidence/` 下；再调用 `src_import_har`。
6. `src_path_probe`: probe only explicit paths discovered from JS, HTML, HAR, or business flows. Maximum 25 paths, no wordlist brute force, and a batch approval is required. / 6. `src_path_probe`：仅探测从 JS、HTML、HAR 或业务流程发现的明确路径。最多 25 条，无字典暴力破解，需要批量批准。
7. `src_port_probe`: check only ports already listed in `allowed_ports`. Maximum 20 ports, no internet-wide port scan, and a batch approval is required. / 7. `src_port_probe`：仅检查 `allowed_ports` 中已列出的端口。最多 20 个，无全网端口扫描，需要批量批准。
8. Build a feature map: authentication, object IDs, upload/import, exports, URL fetches, payments, approvals, invitations, and state transitions. / 8. 建立功能图：身份验证、对象 ID、上传/导入、导出、URL 抓取、支付、审批、邀请和状态转换。
9. For each feature, call `src_hunt_route`, then `src_vuln_playbook`, and test one hypothesis at a time. / 9. 每个功能先调用 `src_hunt_route`，再调用 `src_vuln_playbook`，一次测试一个假设。

New hosts, URLs, IPs, or API domains extracted from JS remain leads until their scope status is confirmed. The “可疑站点搜索” step does not allow scanning arbitrary internet hosts or expanding beyond the program's asset list. / 从 JS 提取的新主机、URL、IP 或 API 域名在范围状态确认前仍是线索。“可疑站点搜索”步骤不允许扫描任意互联网主机或超出程序资产列表。

## Tool coordination / 工具协调

- Discovery: `src_start`, `src_passive_recon`, `src_asset_intel`, `src_js_inventory`, `src_import_har`. / 发现：`src_start`、`src_passive_recon`、`src_asset_intel`、`src_js_inventory`、`src_import_har`。
- Cross-session memory: `src_clueboard` read, graph, append, set_focus, add_fact, add_intent, add_hint, update_intent. / 跨会话记忆：`src_clueboard` 读取、图、追加、设焦点、添加事实、添加意图、添加提示、更新意图。
- Inventory: `src_status`, `attack-surface.md`, `evidence/js-inventory.json`, `evidence/har-inventory.json`. / 清单：`src_status`、`attack-surface.md`、`evidence/js-inventory.json`、`evidence/har-inventory.json`。
- Bounded scanning: `src_path_probe`, `src_port_probe` only after batch approval. / 受限扫描：`src_path_probe`、`src_port_probe` 仅在批量批准后。
- Request testing: `src_http` for one request at a time; no ad hoc client. / 请求测试：`src_http` 一次一个请求；无临时客户端。
- Expert routing: `src_hunt_route`. / 专家路由：`src_hunt_route`。
- Classification: `src_vuln_playbook`. / 分类：`src_vuln_playbook`。
- Evidence: `src_save_finding`, `src_validate_finding`, `src_render_report`. / 证据：`src_save_finding`、`src_validate_finding`、`src_render_report`。
- Tool installation: `src_tool_status`, then `src_install_tool` only with explicit confirmation. / 工具安装：`src_tool_status`，然后仅在明确确认后调用 `src_install_tool`。

## Common false-positive traps / 常见误报陷阱

- A reflection is not XSS; execution context must be proven. / 反射不是 XSS；必须证明执行上下文。
- A CORS header is not a finding without readable authenticated data. / CORS 头不是发现，除非可读取经过身份验证的数据。
- A 500 error is not injection; the response must change deterministically with a controlled input. / 500 错误不是注入；响应必须受控输入决定性变化。
- An ID change is not IDOR unless two identities prove object ownership boundaries. / ID 变更不是 IDOR，除非两个身份证明对象归属边界。
- A public file or route is not sensitive disclosure without sensitive content or impact. / 公开文件或路径不是敏感泄露，除非有敏感内容或影响。
- A front-end route guard bypass is not backend authorization failure. / 前端路由守卫绕过不是后端鉴权失败。
- Client-side encryption or a publicly retrievable key is not authentication. / 客户端加密或公开可取的密钥不是鉴权。
- A self-XSS, logout CSRF, missing header, banner, or clickjacking-only issue is usually noise unless chained to real impact. / 自 XSS、登出 CSRF、缺失头、横幅或仅点击劫持问题通常是噪声，除非串联到真实影响。

## Workflow after `src_start` / `src_start` 后的工作流

1. Use `src_status` to inspect the run. / 1. 用 `src_status` 检查运行。
2. Use `src_clueboard` to read the board and set one concrete focus. / 2. 用 `src_clueboard` 读取板面并设定具体焦点。
3. Build a small attack-surface list in `attack-surface.md`. / 3. 在 `attack-surface.md` 中建立小攻击面列表。
4. Prefer manual, low-impact analysis over broad scanning. / 4. 优先手工低影响分析，而非宽扫描。
5. Call `src_hunt_route` for the next feature or signal. / 5. 为下一功能或信号调用 `src_hunt_route`。
6. Call `src_vuln_playbook` for the selected class. / 6. 为选定类调用 `src_vuln_playbook`。
7. For any active test beyond baseline `GET`/`HEAD`/`OPTIONS`, call `src_request_approval`. / 7. 超出基线 `GET`/`HEAD`/`OPTIONS` 的任何主动测试，先调用 `src_request_approval`。
8. Show the returned approval code and ask the user to reply exactly `APPROVE <code>`. / 8. 显示返回的批准码，请用户回复 `APPROVE <code>`。
9. After the exact reply, call `src_confirm_approval`, then `src_http` with the approval code. / 9. 收到精确回复后，调用 `src_confirm_approval`，再用批准码调用 `src_http`。
10. Append observed facts, failed hypotheses, negative evidence, and the next focus with `src_clueboard` before the turn ends. / 10. 轮结束前用 `src_clueboard` 追加观察事实、失败假设、否定证据和下一焦点。
11. Record a lead with `src_save_finding` in `candidate` status. / 11. 用 `src_save_finding` 记录 `candidate` 状态的线索。
12. Use `src_validate_finding` only when the finding has real evidence and human verification. / 12. 仅在发现有真实证据和人工验证时使用 `src_validate_finding`。
13. Use `src_render_report` only after validation; the output is a draft, not an automatic submission. / 13. 验证后再用 `src_render_report`；输出是草稿，不是自动提交。

## Tool policy / 工具策略

- Baseline target traffic must use `src_http`, which enforces scope, rate limiting, redirect scope checks, request logging, and approval gates. / 基线目标流量必须使用 `src_http`，它强制执行范围、速率限制、重定向范围检查、请求日志和审批门禁。
- `ffuf`, `nuclei`, `sqlmap`, brute force, DoS, persistence, lateral movement, and real-user data access are never automatic. / `ffuf`、`nuclei`、`sqlmap`、暴力破解、DoS、持久化、横向移动和真实用户数据访问从不自动。
- Call `src_tool_status` before using an optional CLI tool. / 使用可选 CLI 工具前先调用 `src_tool_status`。
- Call `src_install_tool` only with `confirm: true` after the user has agreed to install the named official tool. Do not install unapproved binaries or random GitHub projects. / 用户同意安装命名的官方工具后，且仅在 `confirm: true` 时调用 `src_install_tool`。不要安装未批准的二进制文件或随机 GitHub 项目。
- Burp/Caido remains manual for complex flows. Do not direct the browser at out-of-scope hosts. / Burp/Caido 仍用于复杂流程的人工操作。不要将浏览器指向范围外主机。

## Stop conditions / 停止条件

Stop and report the exact reason when:

- Scope or authorization is missing. / 范围或授权缺失。
- A redirect leaves the approved host/path. / 重定向超出批准主机/路径。
- A response appears to contain another user's data, another tenant's data, credentials, or internal infrastructure. / 响应似乎包含另一个用户的数据、另一个租户的数据、凭据或内部基础设施。
- The target becomes unstable or shows signs of business impact. / 目标不稳定或出现业务影响迹象。
- The next action needs a write, upload, authentication challenge, SSRF, deserialization, credential use, exploit chain, or WAF/rate-limit evasion without an approved code. / 下一操作需要写入、上传、认证挑战、SSRF、反序列化、凭据使用、利用链或 WAF/速率限制绕过，但没有批准码。
- You cannot prove that the program permits the activity. / 无法证明程序允许该操作。

## Evidence rules / 证据规则

- Try to falsify normal behavior before treating a signal as a defect. Record the negative-control test and its result. / 在将信号当作缺陷前先尝试伪造正常行为。记录控制测试及结果。
- Use only actual MCP/HTTP evidence stored under the run directory. / 仅使用运行目录下实际的 MCP/HTTP 证据。
- Redact cookies, authorization headers, tokens, API keys, session IDs, and personal data. / 脱敏 Cookie、授权头、令牌、API 密钥、会话 ID 和个人数据。
- A verified finding requires a real request/response pair, reproducible steps, concrete impact, and an independent oracle or human reviewer. The model that proposed the finding cannot award the final verdict. / 已验证的发现需要实际请求/响应对、可复现步骤、具体影响，以及独立 oracle 或人工审核者。提出发现的模型不能自行给出最终裁决。
- Never auto-submit a report to the SRC platform. / 永不自动向 SRC 平台提交报告。

## Outputs / 输出

The MCP server writes to `runs/<program>/<timestamp>/` with `evidence/`, `candidates/`, `reports/`, `logs/`, `run.json`, `notes.md`, `CLUEBOARD.md`, `CLUEBOARD.json`, and `attack-surface.md`. / MCP 服务器写入 `runs/<program>/<timestamp>/`，包含 `evidence/`、`candidates/`、`reports/`、`logs/`、`run.json`、`notes.md`、`CLUEBOARD.md`、`CLUEBOARD.json` 和 `attack-surface.md`。

<!-- 用途：可迁移的 Codex 技能说明 / Portable Codex skill instructions | -->
