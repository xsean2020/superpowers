# Hermes 插件安装指南

## 官方标准结构

根据 Hermes 官方文档，插件结构应该非常简单：

```
.hermes-plugin/
├── plugin.yaml        # 插件清单 (YAML 格式)
└── src/
    └── __init__.py    # 插件入口点
```

## plugin.yaml

```yaml
name: superpowers
version: 5.0.7
description: Core skills library for Hermes Agent
entry_point: src/__init__.py
```

**字段说明：**
- `name` — 插件名称
- `version` — 版本号
- `description` — 插件描述
- `entry_point` — Python 入口文件路径

## 安装方式

### 方式 1: 技能符号链接（当前推荐）

由于 Hermes 的插件发现机制可能还在发展中，目前最可靠的方式是直接使用技能符号链接：

```bash
# 1. 克隆 Superpowers 仓库
git clone https://github.com/xsean2020/superpowers.git ~/.hermes/superpowers

# 2. 创建技能符号链接
mkdir -p ~/.hermes/skills
ln -s ~/.hermes/superpowers/skills ~/.hermes/skills/superpowers

# 3. 重启 Hermes
```

**优点：**
- ✅ 简单直接
- ✅ 技能即时可用
- ✅ 不需要 Python 包知识

**缺点：**
- ❌ 没有 bootstrap 注入
- ❌ 没有 Hook 支持

### 方式 2: 插件目录放置（当 Hermes 支持时）

当 Hermes 支持 plugin.json 自动发现时：

```bash
# 1. 克隆 Superpowers 仓库
git clone https://github.com/xsean2020/superpowers.git ~/.hermes/superpowers

# 2. 复制插件目录到 Hermes 插件目录
cp -r ~/.hermes/superpowers/.hermes-plugin ~/.hermes/plugins/superpowers

# 3. 重启 Hermes
```

**优点：**
- ✅ 完整功能（Hook + Bootstrap）
- ✅ 符合官方标准

**缺点：**
- ⚠️ 依赖 Hermes 插件发现功能

### 方式 3: 混合方式（推荐用于开发）

结合两种方式的优势：

```bash
# 1. 克隆 Superpowers 仓库
git clone https://github.com/xsean2020/superpowers.git ~/.hermes/superpowers

# 2. 创建技能符号链接
mkdir -p ~/.hermes/skills
ln -s ~/.hermes/superpowers/skills ~/.hermes/skills/superpowers

# 3. 复制插件目录（当 Hermes 支持时自动激活）
mkdir -p ~/.hermes/plugins
cp -r ~/.hermes/superpowers/.hermes-plugin ~/.hermes/plugins/superpowers

# 4. 重启 Hermes
```

## 验证安装

### 检查技能

在 Hermes 中询问：
```
你有哪些技能？
```

应该看到 Superpowers 技能列表。

### 检查插件

如果 Hermes 支持插件发现：
```bash
ls -la ~/.hermes/plugins/
```

应该看到 `superpowers/` 目录。

### 测试 Bootstrap

在 Hermes 中询问：
```
什么是 Superpowers？
```

如果 Bootstrap 注入成功，Agent 应该详细解释 Superpowers 工作流。

## 插件结构说明

### plugin.json

```json
{
  "name": "superpowers",
  "version": "5.0.7",
  "description": "Core skills library for Hermes Agent",
  "entry_point": "src/__init__.py"
}
```

- `name`: 插件名称
- `version`: 版本号
- `description`: 描述
- `entry_point`: Python 入口文件

### src/__init__.py

包含：
- `register(ctx)` — 插件注册函数（必需）
- `session_start(ctx)` — 会话开始 Hook
- `pre_llm_call(ctx, messages)` — LLM 调用前 Hook
- `get_bootstrap_content()` — 生成 Bootstrap 内容

## 故障排查

### 技能未找到

```bash
# 检查符号链接
ls -la ~/.hermes/skills/superpowers

# 检查 SKILL.md 文件
ls ~/.hermes/skills/superpowers/*/SKILL.md | head -3
```

### 插件未加载

```bash
# 检查插件目录
ls -la ~/.hermes/plugins/

# 检查 plugin.json
cat ~/.hermes/plugins/superpowers/plugin.json
```

### Bootstrap 未注入

检查 `src/__init__.py` 中的 `pre_llm_call` Hook 是否正确注册。

## 更新

```bash
# 拉取最新代码
cd ~/.hermes/superpowers
git pull

# 重启 Hermes
```

## 参考

- [Hermes 官方插件文档](https://hermes-agent.nousresearch.com/docs/guides/build-a-hermes-plugin)
- [Superpowers 仓库](https://github.com/xsean2020/superpowers)
