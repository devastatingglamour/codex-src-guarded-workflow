# 授权 SRC 工作流规则 / Authorized SRC Workflow Rules

本工作区实现面向明确授权 SRC 程序的人工门禁黑盒安全测试工作流。

This workspace implements a human-gated black-box security testing workflow for explicitly authorized SRC programs.

## 首选界面 / Preferred interface

当 `srcGuardedWorkflow` MCP 服务器可用时，使用其工具（`src_start`、`src_clueboard`、`src_hunt_route`、`src_http`、`src_request_approval`、`src_confirm_approval`、`src_validate_finding`、`src_render_report`），而不是让用户运行命令行工具。本目录中的脚本是确定性回退和测试用表面。

When the `srcGuardedWorkflow` MCP server is available, use its tools (`src_start`, `src_clueboard`, `src_hunt_route`, `src_http`, `src_request_approval`, `src_confirm_approval`, `src_validate_finding`, `src_render_report`) instead of asking the user to run command-line tools. The scripts in this directory are the deterministic fallback and test surface.

用户应能在聊天中提供程序、策略 URL 和授权资产，然后让 MCP 工作流完成范围设置、被动侦察和低影响基线。不要把它变成一串 shell 命令。

The user should be able to provide a program, policy URL, and authorized asset in chat, then let the MCP workflow perform scoped setup, passive reconnaissance, and the low-impact baseline. Do not turn that into a list of shell commands.

## 不可违背的边界 / Non-negotiable boundaries

- 仅测试活跃 `scope.yaml` 中明确列出的资产。 / Test only assets explicitly listed in the active `scope.yaml`.
- 在任何主动请求前先阅读目标程序的当前策略。若策略与本地配置冲突，采用更严格的规则并停止。 / Read the target program's current policy before any active request. If the policy and local configuration conflict, use the stricter rule and stop.
- 不要仅因为公共主机可达就对其测试。公开可达不等于授权。 / Never test a public host merely because it is reachable. Public availability is not authorization.
- 不要运行批量扫描、暴力破解、密码喷洗、DoS、压力测试、持久化、横向移动或破坏性载荷。 / Do not run batch scans, brute force, password spraying, DoS, stress tests, persistence, lateral movement, or destructive payloads.
- 不要访问、下载、保留或报告真实用户数据。使用测试账号和证明影响所需的最少证据。 / Do not access, download, retain, or report real user data. Use test accounts and the minimum evidence needed to prove impact.
- 不要部署 shell、后门、定时任务或持久化。 / Do not deploy shells, backdoors, scheduled tasks, or persistence.
- 不要联系程序批准渠道外的用户、客户、员工或第三方。 / Do not contact users, customers, employees, or third parties outside the program's approved channel.
- 未经书面授权，不要发布或共享目标信息。 / Do not publish or share target information without written authorization.

## 必需执行路径 / Required execution path

1. 确认 `scope.yaml` 存在、属于当前程序且 `authorization_confirmed: true`。 / Confirm that `scope.yaml` exists, belongs to the current program, and has `authorization_confirmed: true`.
2. 用 `scripts/new_run.py` 创建运行；这也会创建 `CLUEBOARD.md`。 / Create a run with `scripts/new_run.py`; this also creates `CLUEBOARD.md`.
3. 在主动测试前先读取线索板并设定具体当前焦点。 / Read the clueboard and set one concrete current focus before active testing.
4. 对所有目标 HTTP 流量使用 `scripts/guarded_http.py`。它强制执行主机/路径/方法范围、速率限制、重定向检查、脱敏和审批门禁。 / Use `scripts/guarded_http.py` for all target HTTP traffic. It enforces host/path/method scope, rate limits, redirect checks, redaction, and approval gates.
5. 先做被动侦察和只读请求（`GET`、`HEAD`、`OPTIONS`）。 / Start with passive reconnaissance and read-only requests (`GET`, `HEAD`, `OPTIONS`).
6. 用 `src_hunt_route` 选择专家知识路由及其 Playbook 类别。 / Use `src_hunt_route` to select the expert knowledge route and its playbook classes.
7. 先把发现记录为 `candidate`。候选是假设，不是漏洞。 / Record findings as `candidate` first. A candidate is a hypothesis, not a vulnerability.
8. 写请求或高风险验证前停止并取得明确的人工批准。用户必须从自己的 shell 中提供批准令牌；绝不读取、打印、生成或推断它。 / Before a write request or high-risk validation, stop and obtain explicit human approval. The user must provide the approval token from their own shell; never read, print, generate, or infer it.
9. 进行独立的审核者伪造验证：验证范围、请求/响应证据、可复现性、影响、数据最小化和可能重复。 / Use an independent reviewer pass to falsify the finding: verify scope, request/response evidence, reproducibility, impact, data minimization, and possible duplication.
10. 在同一轮内将假设、否定证据和覆盖度写回线索板。 / Write hypotheses, negative evidence, and coverage back to the clueboard in the same turn.
11. 渲染报告前运行 `scripts/validate_finding.py`。 / Run `scripts/validate_finding.py` before rendering a report.
12. 不要自动提交报告。人工操作员必须审查并提交。 / Never submit a report automatically. The human operator must review and submit it.

安装第三方 Skill 或插件前，使用 `src_skill_audit`、检查发现，并要求人工批准后再执行。 / Before installing a third-party Skill or plugin, use `src_skill_audit`, inspect the findings, and require human approval before execution.

## 工具策略 / Tool policy

`scripts/guarded_http.py` 是默认且必须的 HTTP 客户端。 / `scripts/guarded_http.py` is the default and required HTTP client.

不要用 `curl`、`Invoke-WebRequest`、直接浏览器自动化或临时脚本绕过它发送目标流量。 / Do not bypass it with `curl`, `Invoke-WebRequest`, direct browser automation, or ad hoc scripts for target traffic.

`subfinder`、`httpx`、`dnsx`、`katana`、`gau`、`ffuf`、`nuclei` 是可选的发现辅助，不是授权。仅在程序规则允许特定活动且人工操作员已批准运行时使用。 / `subfinder`, `httpx`, `dnsx`, `katana`, `gau`, `ffuf`, and `nuclei` are optional discovery aids, not authorization. Use them only when the program rules allow the specific activity and the human operator has approved the run.

扫描器只产生线索。不要把扫描器匹配当作已确认漏洞。 / Scanners produce leads only. Never report a scanner match as a confirmed vulnerability.

Burp Suite 或 Caido 可用于人工审查和证据捕获，但请求必须在范围和速率限制内。 / Burp Suite or Caido may be used for manual review and evidence capture, but requests must remain within scope and rate limits.

## 证据规则 / Evidence rules

已验证的发现必须包含实际请求/响应对、复现步骤、前置条件、具体影响声明和人工验证标记。 / A verified finding must have an actual request/response pair, reproduction steps, preconditions, a concrete impact statement, and a human verification marker.

在将信号当作缺陷前先尝试伪造正常行为；在 CLUEBOARD.md 中记录控制测试。 / Try to falsify normal behavior before treating a signal as a defect; record the control test in CLUEBOARD.md.

绝不编造请求、响应、状态码、截图、载荷、时间戳或影响。 / Never invent a request, response, status code, screenshot, payload, timestamp, or impact.

脱敏 cookies、授权头、API 密钥、CSRF 令牌、会话标识符和个人数据。 / Redact cookies, authorization headers, API keys, CSRF tokens, session identifiers, and personal data.

若证据暗示访问另一个租户、另一个用户、内部基础设施、凭据或敏感生产数据，立即停止并仅保留程序要求的最少证明。 / If evidence suggests access to another tenant, another user, internal infrastructure, credentials, or sensitive production data, stop immediately and preserve only the minimum proof required by the program.

## 停止条件 / Stop conditions

出现下列任一情况时立即停止并向人工操作员报告原因：

- 请求或重定向将超出配置范围。 / A request or redirect would leave the configured scope.
- 目标返回似乎属于真实用户或另一个租户的数据。 / The target returns data that appears to belong to a real user or another tenant.
- 目标出现不稳定、速率限制或业务影响迹象。 / The target shows signs of instability, rate limiting, or business impact.
- 测试需要写入、上传、认证挑战、SSRF、反序列化、凭据使用或利用链。 / A test would require a write, upload, auth challenge, SSRF, deserialization, credential use, or exploit chaining.
- 不确定程序是否允许该操作。 / You are unsure whether the program permits the action.

## 输出契约 / Output contract

每个运行位于 `runs/<program>/<timestamp>/`，包含 `evidence/`、`candidates/`、`reports/`、`logs/`、`run.json`、`notes.md`、`CLUEBOARD.md` 和 `attack-surface.md`。发现使用 `schemas/finding.schema.json` 中的架构。 / Every run lives under `runs/<program>/<timestamp>/` with `evidence/`, `candidates/`, `reports/`, `logs/`, `run.json`, `notes.md`, `CLUEBOARD.md`, and `attack-surface.md`. Findings use the schema in `schemas/finding.schema.json`.
