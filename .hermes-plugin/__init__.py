"""
Superpowers Plugin for Hermes Agent

Official plugin following Hermes specification:
https://hermes-agent.nousresearch.com/docs/guides/build-a-hermes-plugin
"""

import json
from pathlib import Path


def get_bootstrap_content():
    """Load and format the using-superpowers skill content for bootstrap injection."""
    possible_paths = [
        Path(__file__).parent.parent / "skills" / "using-superpowers" / "SKILL.md",
        Path.home() / ".hermes" / "skills" / "superpowers" / "using-superpowers" / "SKILL.md",
        Path.home() / ".hermes" / "superpowers" / "skills" / "using-superpowers" / "SKILL.md",
        Path.home() / "superpowers" / "skills" / "using-superpowers" / "SKILL.md",
    ]
    
    skill_path = None
    for path in possible_paths:
        if path.exists():
            skill_path = path
            break
    
    if not skill_path:
        return None
    
    content = skill_path.read_text(encoding='utf-8')
    
    # Extract body (strip YAML frontmatter)
    if content.startswith('---'):
        parts = content.split('---', 2)
        body = parts[2].strip() if len(parts) >= 3 else content
    else:
        body = content
    
    tool_mapping = """
**Tool Mapping for Hermes:**
- `TodoWrite` → `todo`
- `Task` → `delegate_task`
- `Read` → `read_file`
- `Write` → `write_file`
- `Edit` → `patch`
- `Bash` → `terminal`
- `Grep`/`Glob` → `search_files`
- `WebFetch` → `browser_navigate` + `browser_snapshot`
"""
    
    return f"""<EXTREMELY_IMPORTANT>
You have Superpowers.

**The using-superpowers skill content is included below. It is ALREADY LOADED - you are currently following it. Do NOT load it again.**

{body}

{tool_mapping}
</EXTREMELY_IMPORTANT>"""


def pre_llm_call(ctx, messages):
    """
    Hook: pre_llm_call
    Inject bootstrap context into the first message of a session.
    """
    bootstrap = get_bootstrap_content()
    if not bootstrap:
        return
    
    # Only inject once per session
    for msg in messages:
        if msg.get('role') == 'user':
            content = msg.get('content', '')
            if isinstance(content, str) and 'EXTREMELY_IMPORTANT' in content:
                return
    
    # Inject as system message at the beginning
    if messages and messages[0].get('role') != 'system':
        messages.insert(0, {
            'role': 'system',
            'content': bootstrap
        })


def session_start(ctx):
    """
    Hook: on_session_start
    Called when a new session starts.
    """
    print("[Superpowers] Plugin activated")
    
    skills_dir = Path(__file__).parent.parent / "skills"
    if not skills_dir.exists():
        skills_dir = Path.home() / ".hermes" / "superpowers" / "skills"
    
    if skills_dir.exists():
        print(f"[Superpowers] Skills directory: {skills_dir}")


def register(ctx):
    """
    Register Superpowers plugin with Hermes.
    
    This function is called by Hermes when the plugin is loaded.
    """
    # Register hooks (positional arguments, not keyword)
    ctx.register_hook('on_session_start', session_start)
    ctx.register_hook('pre_llm_call', pre_llm_call)
    
    # Register skills directory
    skills_dir = Path(__file__).parent.parent / "skills"
    if not skills_dir.exists():
        skills_dir = Path.home() / ".hermes" / "superpowers" / "skills"
    
    if skills_dir.exists():
        ctx.register_skills_directory(str(skills_dir))
        print(f"[Superpowers] Registered skills directory: {skills_dir}")
    
    print("[Superpowers] Plugin registration complete")
