# Hermes 插件适配完成

## 概述

已成功为 Superpowers 项目创建符合 Hermes 官方标准的插件适配。

**Fork 仓库**: https://github.com/xsean2020/superpowers

**插件位置**: `.hermes-plugin/` 目录

**官方文档**: https://hermes-agent.nousresearch.com/docs/guides/build-a-hermes-plugin

## 快速开始

### 安装插件

```bash
cd ~/superpowers/.hermes-plugin
pip3 install -e .
```

### 验证安装

```bash
# 测试 Python 导入
cd ~/superpowers/.hermes-plugin
PYTHONPATH=. python3 -c "from hermes_superpowers_plugin import register; print('OK')"

# 在 Hermes 中使用
hermes "Tell me about your superpowers"
```

## 创建的文件

```
.hermes-plugin/
├── plugin.json                       # Hermes 插件清单
├── pyproject.toml                    # Python 包配置
├── setup.py                          # 安装脚本（兼容老版本 pip）
├── README.md                         # 插件使用说明
├── INSTALL.md                        # 详细安装指南
├── HERMES-ADAPTATION-SUMMARY.md      # 适配总结文档
├── .gitignore                        # Git 忽略文件
├── hermes_superpowers_plugin/
│   └── __init__.py                   # Python 包入口点
└── src/
    └── __init__.py                   # 插件注册和 Hook 实现
```

## 核心功能

### 1. 插件注册

```python
def register(ctx):
    # 注册 Hook
    ctx.register_hook(event='session_start', handler=session_start_handler)
    ctx.register_hook(event='pre_llm_call', handler=pre_llm_call_handler)
    
    # 注册技能目录
    ctx.register_skills_directory(str(skills_dir))
```

### 2. Bootstrap 注入

在会话开始时自动注入：
- `using-superpowers` 技能完整内容
- Hermes 工具映射表
- 使用说明

### 3. 技能目录自动发现

自动查找并注册：
1. 插件包内的 skills 目录
2. `~/.hermes/skills/superpowers/`
3. `~/.hermes/superpowers/skills/`
4. `~/superpowers/skills/`

## Hermes 官方标准符合性

| 要求 | 实现 | 状态 |
|------|------|------|
| plugin.json | ✅ `.hermes-plugin/plugin.json` | ✅ |
| entry_point | ✅ `src/__init__.py` | ✅ |
| register() | ✅ `def register(ctx)` | ✅ |
| Hook 系统 | ✅ session_start + pre_llm_call | ✅ |
| Python 包 | ✅ pyproject.toml + setup.py | ✅ |

## 工具映射

| Claude Code | Hermes |
|-------------|--------|
| `TodoWrite` | `todo` |
| `Task` | `delegate_task` |
| `Read` | `read_file` |
| `Write` | `write_file` |
| `Edit` | `patch` |
| `Bash` | `terminal` |
| `Grep`/`Glob` | `search_files` |

## 提供的技能

- brainstorming
- writing-plans
- subagent-driven-development
- test-driven-development
- systematic-debugging
- verification-before-completion
- requesting-code-review
- receiving-code-review
- using-git-worktrees
- finishing-a-development-branch
- writing-skills
- using-superpowers
- dispatching-parallel-agents
- executing-plans

## 测试状态

```
✅ Python 导入成功
✅ Bootstrap 生成成功 (5850 字符)
✅ 插件结构完整
✅ 文档齐全
```

## 下一步

1. ⏭️ 在 Hermes 中测试插件加载
2. ⏭️ 验证 bootstrap 注入功能
3. ⏭️ 测试技能自动发现
4. ⏭️ （可选）发布到 PyPI

## 参考资源

- **Hermes 官方插件文档**: https://hermes-agent.nousresearch.com/docs/guides/build-a-hermes-plugin
- **Hermes Agent GitHub**: https://github.com/nousresearch/hermes-agent
- **Superpowers 原版**: https://github.com/obra/superpowers
- **本 Fork**: https://github.com/xsean2020/superpowers

## 总结

✅ **标准化插件结构** — 完全符合 Hermes 官方标准  
✅ **完整 Hook 实现** — session_start + pre_llm_call  
✅ **技能目录注册** — 自动发现 Superpowers 技能  
✅ **Bootstrap 注入** — 在会话开始时注入上下文  
✅ **pip 分发支持** — 可通过 pip install 安装  
✅ **详细文档** — README + INSTALL + 适配总结  

---

**适配完成时间**: 2024-04-14  
**适配版本**: 5.0.7  
**Hermes 兼容性**: 符合最新官方标准
