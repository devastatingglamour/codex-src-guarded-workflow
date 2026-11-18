# 变更日志 / Changelog

本项目所有显著变更均记录于此。

All notable changes to `src-guarded-workflow` are documented here.

## [0.7.3] - 2026-11-18

### 文档 / Documentation

- 新增覆盖所有已跟踪文件与目录的中英双语索引，并修正 README 索引入口。 / Added a Chinese-English index covering every tracked file and directory, and fixed the README index entry.
- 将 Codex 插件清单描述补为中英双语。 / Made the Codex plugin manifest description bilingual.

## [0.7.2] - 2026-11-10

### 修复 / Fixed

- 使 `src_hunt_route` 返回稳定的 `status: ok` 和独立的 `result_type: expert_route`。 / Made `src_hunt_route` return a stable `status: ok` result and a separate `result_type: expert_route`.
- 将默认路由响应改为单条最佳匹配，避免 MCP 客户端超时。 / Flattened the default route response to one best match to avoid MCP client timeouts.
- 新增服务器端 MCP 调用时序元数据，不记录请求内容或敏感信息。 / Added server-side MCP call timing metadata without logging request content or secrets.

### 工具 / Tooling

- 新增 `scripts/build_release.ps1`，用于确定性发布打包。 / Added `scripts/build_release.ps1` for deterministic release packaging.
- 新增标签触发的 GitHub Actions，完成测试、构建并发布迁移包和便携包 ZIP。 / Added a GitHub Actions tag workflow that tests, builds, and publishes migration and portable ZIP assets.

## [0.7.1] - 2026-11-10

### 修复 / Fixed

- 为插件 MCP 配置添加必需的 `$schema`，使 Codex 加载 `srcGuardedWorkflow`。 / Added the required `$schema` to plugin MCP configuration so Codex loads `srcGuardedWorkflow`.
- 修正插件/市场安装路径。 / Corrected marketplace/plugin installation paths.
- 验证 `src_tool_status` 可通过本地插件调用。 / Verified live `src_tool_status` calls through the local plugin.

## [0.7.0] - 2026-11-10

### 新增 / Added

- `src_skill_audit` 第三方 Skill 和插件静态供应链审计。 / `src_skill_audit` static supply-chain audit for third-party Skills and plugins.
- `CLUEBOARD.json` 中的 Fact-Intent-Hint 图，并为 `src_clueboard` 新增图操作。 / Fact-Intent-Hint graph in `CLUEBOARD.json`, with graph actions on `src_clueboard`.
- `agentic_workflow_security` Playbook 类和专家路由。 / `agentic_workflow_security` playbook class and expert route.
- 构建与购买对比及外部工具评估的能力雷达。 / Capability radar for build-versus-buy and external tool evaluation.
- SecSkills 和附加设计参考及第三方通告。 / SecSkills and additional design references with third-party notices.

## [0.6.0] - 2026-11-09

### 新增 / Added

- 源自 CK-Skills 的专家路由。 / Expert routing derived from CK-Skills.
- 跨会话 Markdown 线索板和否定证据工作流。 / Cross-session Markdown clueboard and negative-evidence workflow.
- JS 优先侦察、伪造优先、覆盖度和报告门禁的附加指南。 / Additional guidance for JS-first reconnaissance, falsification, coverage, and report gates.

## 版本规则 / Versioning rules

- PATCH：兼容性修复、文档更新和小行为调整。 / Patch versions: compatibility fixes, documentation, and small behavior corrections.
- MINOR：新增 Playbook、专家路由、工具或工作流能力。 / Minor versions: new playbooks, routes, tools, or workflow capabilities.
- MAJOR：破坏兼容性的插件 API、Scope 格式、MCP 契约或审批语义变更。 / Major versions: breaking plugin APIs, scope formats, MCP contracts, or approval semantics.

发布前： / Before a release:

1. 更新 `plugin.json`、`.codex-plugin/plugin.json` 和 `server/src_guarded_mcp.py` 版本值。 / Update `plugin.json`, `.codex-plugin/plugin.json`, and `server/src_guarded_mcp.py` version values.
2. 运行 `python -m unittest discover -s tests -v`。 / Run `python -m unittest discover -s tests -v`.
3. 运行 Skill 验证器。 / Run the skill validator.
4. 重建迁移包和便携包。 / Rebuild migration and portable artifacts.
5. 提交、打 `vX.Y.Z` 标签、推送分支和标签，并创建 GitHub Release。 / Commit, tag `vX.Y.Z`, push the branch and tag, and create a GitHub Release.
