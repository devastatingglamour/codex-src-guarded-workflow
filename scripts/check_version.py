"""Check that plugin and MCP server version declarations agree."""

import ast
import json
import pathlib


root = pathlib.Path(__file__).resolve().parents[1]
plugin = json.loads((root / "plugin.json").read_text(encoding="utf-8"))["version"]
codex = json.loads((root / ".codex-plugin/plugin.json").read_text(encoding="utf-8"))["version"]
server_tree = ast.parse((root / "server/src_guarded_mcp.py").read_text(encoding="utf-8"))
server = next(
    ast.literal_eval(node.value)
    for node in server_tree.body
    if isinstance(node, ast.Assign)
    and any(isinstance(target, ast.Name) and target.id == "SERVER_VERSION" for target in node.targets)
)

versions = {"plugin": plugin, "codex-plugin": codex, "MCP server": server}
if len(set(versions.values())) != 1:
    raise SystemExit(f"Version mismatch: {versions}")

print(f"Version consistency OK: {plugin}")
