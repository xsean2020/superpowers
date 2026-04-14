# Superpowers Plugin for Hermes Agent

Minimal plugin following the official Hermes specification:
https://hermes-agent.nousresearch.com/docs/guides/build-a-hermes-plugin

## Structure

```
.hermes-plugin/
├── plugin.yaml        # Plugin manifest (YAML format)
└── __init__.py        # Plugin entry point with register() function
```

## plugin.yaml

```yaml
name: superpowers
version: 5.0.7
description: "Core skills library for Hermes Agent: TDD, debugging, collaboration patterns, and proven techniques"
```

## Installation

### Method 1: Plugin directory (for Hermes plugin system)

```bash
# Clone the repository
git clone https://github.com/xsean2020/superpowers.git ~/.hermes/superpowers

# Copy plugin to Hermes plugins directory
cp -r ~/.hermes/superpowers/.hermes-plugin ~/.hermes/plugins/superpowers

# Restart Hermes
```

### Method 2: Direct skills symlink (Recommended for now)

Since this plugin requires the skills directory to be present:

```bash
# Clone the repository
git clone https://github.com/xsean2020/superpowers.git ~/.hermes/superpowers

# Create skills symlink
mkdir -p ~/.hermes/skills
ln -s ~/.hermes/superpowers/skills ~/.hermes/skills/superpowers

# Restart Hermes
```

## Features

### Hooks

- **on_session_start** — Logs plugin activation and finds skills directory
- **pre_llm_call** — Injects bootstrap context with using-superpowers skill content

### Bootstrap Injection

The plugin injects:
1. Complete `using-superpowers` skill content
2. Hermes tool mapping (Claude Code → Hermes)
3. Usage instructions

### Tool Mapping

| Claude Code | Hermes |
|-------------|--------|
| `TodoWrite` | `todo` |
| `Task` | `delegate_task` |
| `Read` | `read_file` |
| `Write` | `write_file` |
| `Edit` | `patch` |
| `Bash` | `terminal` |
| `Grep`/`Glob` | `search_files` |

## Testing

```bash
# Test the plugin module
cd ~/.hermes/plugins/superpowers
python3 -c "import __init__; print('OK')"

# Test bootstrap generation
python3 -c "from __init__ import get_bootstrap_content; b = get_bootstrap_content(); print('Bootstrap:', len(b) if b else 0, 'chars')"
```

## Official Hermes Plugin Specification

This plugin follows the official structure:

```yaml
name: superpowers
version: 5.0.7
description: "Core skills library for Hermes Agent"
```

```python
# __init__.py
def register(ctx):
    ctx.register_hook(event='on_session_start', handler=session_start)
    ctx.register_hook(event='pre_llm_call', handler=pre_llm_call)
    ctx.register_skills_directory(str(skills_dir))
```

## Skills Provided

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

## References

- [Hermes Plugin Documentation](https://hermes-agent.nousresearch.com/docs/guides/build-a-hermes-plugin)
- [Superpowers](https://github.com/obra/superpowers)
- [Hermes Agent](https://github.com/nousresearch/hermes-agent)

## License

MIT License
