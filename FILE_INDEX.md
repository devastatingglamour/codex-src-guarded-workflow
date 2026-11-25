# 文件与目录索引 / File and Directory Index

本索引覆盖仓库内所有已跟踪文件及目录。GitHub 文件列表旁的说明属于提交信息；此处提供稳定的中英双语用途说明。 / This index covers every tracked file and directory. GitHub's file-list descriptions are commit messages; this document provides stable bilingual purpose descriptions.

| 路径 / Path | 简介 / Description |
|---|---|
| `.agents/` | Agent 配置与可复用技能 / Agent configuration and reusable skills |
| `.agents/plugins/` | 本地插件市场配置 / Local plugin marketplace configuration |
| `.agents/skills/` | 随仓库分发的技能 / Skills distributed with the repository |
| `.agents/skills/src-bug-bounty/` | SRC 漏洞赏金测试技能 / SRC bug bounty testing skill |
| `.agents/skills/src-bug-bounty/references/` | 技能参考手册 / Skill reference guides |
| `.codex-plugin/` | Codex 插件元数据 / Codex plugin metadata |
| `.github/` | GitHub 自动化配置 / GitHub automation configuration |
| `.github/workflows/` | 持续集成与发布工作流 / CI and release workflows |
| `config/` | 配置模板 / Configuration templates |
| `knowledge/` | 漏洞分类与路由知识库 / Vulnerability and routing knowledge base |
| `knowledge/classes/` | 按漏洞类别组织的检测手册 / Vulnerability-class detection playbooks |
| `migration/` | 跨机器迁移包 / Cross-machine migration package |
| `runs/` | 每次测试的运行数据目录 / Per-run testing data directory |
| `schemas/` | JSON 数据结构定义 / JSON data schemas |
| `scripts/` | 范围、请求、证据和报告工具 / Scope, request, evidence, and report utilities |
| `server/` | MCP 服务与侦察工具 / MCP server and reconnaissance tools |
| `skills/` | 聊天入口技能及参考资料 / Chat entry skill and references |
| `skills/src-bug-bounty/` | SRC 测试工作流技能 / SRC testing workflow skill |
| `skills/src-bug-bounty/references/` | 工作流参考手册 / Workflow reference guides |
| `templates/` | 线索、发现和报告模板 / Clue, finding, and report templates |
| `tests/` | 自动化测试 / Automated tests |
| `.agents/plugins/marketplace.json` | Agent 技能或插件配置 / Agent skill or plugin configuration |
| `.agents/skills/src-bug-bounty/SKILL.md` | 可迁移的 Codex 技能说明 / Portable Codex skill instructions |
| `.agents/skills/src-bug-bounty/references/agentic-workflow-security.md` | 技能或迁移参考文档 / Skill or migration reference documentation |
| `.agents/skills/src-bug-bounty/references/expert-routing.md` | 技能或迁移参考文档 / Skill or migration reference documentation |
| `.agents/skills/src-bug-bounty/references/report-checklist.md` | 技能或迁移参考文档 / Skill or migration reference documentation |
| `.agents/skills/src-bug-bounty/references/scope-and-evidence.md` | 技能或迁移参考文档 / Skill or migration reference documentation |
| `.agents/skills/src-bug-bounty/references/secskills-integration.md` | 技能或迁移参考文档 / Skill or migration reference documentation |
| `.agents/skills/src-bug-bounty/references/vulnerability-playbook.md` | 技能或迁移参考文档 / Skill or migration reference documentation |
| `.codex-plugin/plugin.json` | Codex 插件清单 / Codex plugin manifest |
| `.github/workflows/release.yml` | GitHub 自动化工作流 / GitHub automation workflow |
| `.github/workflows/ci.yml` | 在 Windows runner 执行测试、版本检查和构建 / Run tests, version checks, and builds on a Windows runner |
| `.gitignore` | Git 忽略规则 / Git ignore rules |
| `AGENTS.md` | Agent 工作规则与安全边界 / Agent rules and safety boundaries |
| `FILE_INDEX.md` | 全部文件与目录的中英双语简介 / Bilingual descriptions for all files and directories |
| `LICENSE` | 项目许可证 / Project license |
| `README.md` | 项目介绍、安装方法与文件索引 / Project overview, installation, and file index |
| `THIRD_PARTY_NOTICES.md` | 第三方来源与许可说明 / Third-party source and license notices |
| `config/scope.example.yaml` | 授权范围配置示例 / Authorized scope configuration example |
| `install.ps1` | install.ps1 安装或构建脚本 / install.ps1 installation or build script |
| `install.sh` | install.sh 安装或构建脚本 / install.sh installation or build script |
| `knowledge/capability-radar.json` | 侦察能力或专家路由数据 / Reconnaissance capability or expert-routing data |
| `knowledge/classes/agentic_workflow_security.json` | agentic_workflow_security 漏洞检测手册 / agentic_workflow_security vulnerability playbook |
| `knowledge/classes/auth_bypass.json` | auth_bypass 漏洞检测手册 / auth_bypass vulnerability playbook |
| `knowledge/classes/auth_session.json` | auth_session 漏洞检测手册 / auth_session vulnerability playbook |
| `knowledge/classes/business_logic.json` | business_logic 漏洞检测手册 / business_logic vulnerability playbook |
| `knowledge/classes/cache_host_header.json` | cache_host_header 漏洞检测手册 / cache_host_header vulnerability playbook |
| `knowledge/classes/cloud_storage.json` | cloud_storage 漏洞检测手册 / cloud_storage vulnerability playbook |
| `knowledge/classes/command_injection.json` | command_injection 漏洞检测手册 / command_injection vulnerability playbook |
| `knowledge/classes/cors.json` | cors 漏洞检测手册 / cors vulnerability playbook |
| `knowledge/classes/csrf.json` | csrf 漏洞检测手册 / csrf vulnerability playbook |
| `knowledge/classes/deserialization.json` | deserialization 漏洞检测手册 / deserialization vulnerability playbook |
| `knowledge/classes/file_upload.json` | file_upload 漏洞检测手册 / file_upload vulnerability playbook |
| `knowledge/classes/graphql.json` | graphql 漏洞检测手册 / graphql vulnerability playbook |
| `knowledge/classes/http_request_smuggling.json` | http_request_smuggling 漏洞检测手册 / http_request_smuggling vulnerability playbook |
| `knowledge/classes/idor_bola.json` | idor_bola 漏洞检测手册 / idor_bola vulnerability playbook |
| `knowledge/classes/information_disclosure.json` | information_disclosure 漏洞检测手册 / information_disclosure vulnerability playbook |
| `knowledge/classes/llm_prompt_injection.json` | llm_prompt_injection 漏洞检测手册 / llm_prompt_injection vulnerability playbook |
| `knowledge/classes/nosql_injection.json` | nosql_injection 漏洞检测手册 / nosql_injection vulnerability playbook |
| `knowledge/classes/oauth_jwt.json` | oauth_jwt 漏洞检测手册 / oauth_jwt vulnerability playbook |
| `knowledge/classes/open_redirect.json` | open_redirect 漏洞检测手册 / open_redirect vulnerability playbook |
| `knowledge/classes/path_traversal.json` | path_traversal 漏洞检测手册 / path_traversal vulnerability playbook |
| `knowledge/classes/race_condition.json` | race_condition 漏洞检测手册 / race_condition vulnerability playbook |
| `knowledge/classes/sql_injection.json` | sql_injection 漏洞检测手册 / sql_injection vulnerability playbook |
| `knowledge/classes/ssrf.json` | ssrf 漏洞检测手册 / ssrf vulnerability playbook |
| `knowledge/classes/ssti.json` | ssti 漏洞检测手册 / ssti vulnerability playbook |
| `knowledge/classes/tenant_isolation.json` | tenant_isolation 漏洞检测手册 / tenant_isolation vulnerability playbook |
| `knowledge/classes/websocket.json` | websocket 漏洞检测手册 / websocket vulnerability playbook |
| `knowledge/classes/xss.json` | xss 漏洞检测手册 / xss vulnerability playbook |
| `knowledge/expert-routes.json` | 侦察能力或专家路由数据 / Reconnaissance capability or expert-routing data |
| `mcp.json` | mcp.json 结构化配置或数据 / mcp.json structured configuration or data |
| `migration/README.md` | 技能或迁移参考文档 / Skill or migration reference documentation |
| `migration/install.ps1` | 迁移包文件 / Migration package file |
| `migration/install.sh` | 迁移包文件 / Migration package file |
| `plugin.json` | plugin.json 结构化配置或数据 / plugin.json structured configuration or data |
| `requirements.txt` | Python 依赖清单 / Python dependency list |
| `runs/.gitkeep` | 项目文件 / Project file |
| `schemas/finding.schema.json` | finding.schema.json 数据格式校验定义 / finding.schema.json data validation schema |
| `schemas/scope.schema.json` | scope.schema.json 数据格式校验定义 / scope.schema.json data validation schema |
| `scripts/build_release.ps1` | build_release.ps1 工具脚本 / build_release.ps1 utility script |
| `scripts/check_scope.py` | check_scope.py 工具脚本 / check_scope.py utility script |
| `scripts/guarded_http.py` | guarded_http.py 工具脚本 / guarded_http.py utility script |
| `scripts/new_run.py` | new_run.py 工具脚本 / new_run.py utility script |
| `scripts/render_report.py` | render_report.py 工具脚本 / render_report.py utility script |
| `scripts/scope_rules.py` | scope_rules.py 工具脚本 / scope_rules.py utility script |
| `scripts/validate_finding.py` | validate_finding.py 工具脚本 / validate_finding.py utility script |
| `scripts/check_version.py` | 校验插件与 MCP 服务版本一致 / Check plugin and MCP server version consistency |
| `server/intel_tools.py` | intel_tools.py MCP 或侦察服务模块 / intel_tools.py MCP or reconnaissance module |
| `server/src_guarded_mcp.py` | src_guarded_mcp.py MCP 或侦察服务模块 / src_guarded_mcp.py MCP or reconnaissance module |
| `server/surface_tools.py` | surface_tools.py MCP 或侦察服务模块 / surface_tools.py MCP or reconnaissance module |
| `skills/src-bug-bounty/SKILL.md` | 可迁移的 Codex 技能说明 / Portable Codex skill instructions |
| `skills/src-bug-bounty/references/agentic-workflow-security.md` | 技能或迁移参考文档 / Skill or migration reference documentation |
| `skills/src-bug-bounty/references/expert-routing.md` | 技能或迁移参考文档 / Skill or migration reference documentation |
| `skills/src-bug-bounty/references/report-checklist.md` | 技能或迁移参考文档 / Skill or migration reference documentation |
| `skills/src-bug-bounty/references/scope-and-evidence.md` | 技能或迁移参考文档 / Skill or migration reference documentation |
| `skills/src-bug-bounty/references/secskills-integration.md` | 技能或迁移参考文档 / Skill or migration reference documentation |
| `skills/src-bug-bounty/references/vulnerability-playbook.md` | 技能或迁移参考文档 / Skill or migration reference documentation |
| `templates/clueboard.md` | clueboard.md 文档或数据模板 / clueboard.md document or data template |
| `templates/finding.example.json` | finding.example.json 文档或数据模板 / finding.example.json document or data template |
| `templates/report.md` | report.md 文档或数据模板 / report.md document or data template |
| `tests/test_mcp_server.py` | 对应模块的自动化测试 / Automated tests for the related module |
| `tests/test_workflow.py` | 对应模块的自动化测试 / Automated tests for the related module |

<!-- 用途：全部文件与目录的中英双语简介 / Bilingual descriptions for all files and directories | -->
