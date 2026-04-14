# Hermes 官方插件结构说明

根据 Hermes 官方文档：
https://hermes-agent.nousresearch.com/docs/guides/build-a-hermes-plugin

## 官方标准结构

```
my-plugin/
├── plugin.yaml        # 插件清单 (YAML 格式)
└── src/
    └── __init__.py    # 插件入口点
```

### plugin.yaml

```yaml
name: my-plugin
version: 1.0.0
description: My plugin description
entry_point: src/__init__.py
```

**注意：** 官方使用 YAML 格式，不是 JSON！

### src/__init__.py

```python
def register(ctx):
    """注册插件"""
    ctx.register_hook(
        event='session_start',
        handler=session_start_handler
    )
    
    ctx.register_tool(
        name='my_tool',
        description='Tool description',
        handler=my_tool_handler,
        parameters={
            "type": "object",
            "properties": {
                "arg1": {"type": "string", "description": "Argument 1"}
            }
        }
    )
```

## Superpowers 插件结构

```
.hermes-plugin/
├── plugin.yaml        # 插件清单
├── README.md          # 文档
├── INSTALL.md         # 安装指南
├── STRUCTURE.md       # 本文件
└── src/
    └── __init__.py    # 插件入口点
```

### plugin.yaml

```yaml
name: superpowers
version: 5.0.7
description: Core skills library for Hermes Agent: TDD, debugging, collaboration patterns, and proven techniques
entry_point: src/__init__.py
```

### src/__init__.py

```python
def register(ctx):
    # 注册 Hook
    ctx.register_hook(event='session_start', handler=session_start)
    ctx.register_hook(event='pre_llm_call', handler=pre_llm_call)
    
    # 注册技能目录
    skills_dir = Path(__file__).parent.parent / "skills"
    ctx.register_skills_directory(str(skills_dir))
```

## 关键区别

| 项目 | 官方示例 | Superpowers 实现 |
|------|---------|-----------------|
| plugin.yaml | ✅ | ✅ |
| src/__init__.py | ✅ | ✅ |
| register() 函数 | ✅ | ✅ |
| Hook 注册 | ✅ | ✅ |
| 工具注册 | 示例有 | 不需要（使用技能系统） |
| 技能目录注册 | 可选 | ✅ |

## 为什么没有 Python 包结构？

官方文档中的插件是**直接由 Hermes 发现并加载**的，不需要通过 pip 安装。

Hermes 会：
1. 扫描插件目录
2. 读取 plugin.yaml
3. 加载 entry_point 指定的 Python 文件
4. 调用 `register(ctx)` 函数

所以不需要：
- ❌ pyproject.toml
- ❌ setup.py
- ❌ 包目录结构

## 核心要求

1. **plugin.yaml 必须有**：
   - `name` — 插件名称
   - `entry_point` — Python 入口文件路径

2. **src/__init__.py 必须有**：
   - `register(ctx)` 函数 — Hermes 调用此函数注册插件

3. **可选**：
   - `session_start(ctx)` — 会话开始 Hook
   - `pre_llm_call(ctx, messages)` — LLM 调用前 Hook
   - 工具定义和处理器

## 参考

- [Hermes 官方插件文档](https://hermes-agent.nousresearch.com/docs/guides/build-a-hermes-plugin)
- [Calculator 插件示例](https://hermes-agent.nousresearch.com/docs/guides/build-a-hermes-plugin#step-1-create-the-plugin-directory)
