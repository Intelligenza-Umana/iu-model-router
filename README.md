# IU Model Router

*Human intelligence. Artificial assistance.*

A model-routing skill for coding agents by [Intelligenza Umana](https://github.com/fabiozagaria/intelligenza-umana). It guides model choice using complexity, project context, risk and cost. It supports light, standard and advanced subtasks, user overrides, verification and escalation.

## Claude Code

Run `claude --plugin-dir /path/to/iu-model-router`, then invoke `/iu-model-router:model-routing` or ask Claude to route a task by complexity. The plugin includes agents using Claude's `haiku`, `sonnet` and `opus` aliases. Models must be available to your account. Claude Code settings, permissions and overrides can affect the model used.

## Codex

Install the shared skill for your user:

```sh
mkdir -p ~/.agents/skills/model-routing
cp /path/to/iu-model-router/skills/model-routing/SKILL.md ~/.agents/skills/model-routing/SKILL.md
```

Restart Codex and invoke `$model-routing` or ask it to choose models. Codex can use native subagents and their model settings when the client, account, instructions and session permit delegation. Configure or request models available in your environment. The Claude-specific agents do not configure Codex.

## Behavior and limits

The host decides when to invoke the skill and whether to delegate. Model selection depends on the host's capabilities, configuration and available models. The skill does not force a switch of the main session model or route between providers. Subagent calls have their own context and token costs, so a cheaper model does not guarantee a lower total bill. Review results and measure usage in your provider's dashboard.

For example, ask the agent to use model routing to inspect a project, make a small documentation change and assess whether the authentication flow needs a more capable model. Project rules take priority over apparent simplicity.

## Sources

- [Codex skills](https://developers.openai.com/codex/skills)
- [Codex subagents](https://developers.openai.com/codex/agent-configuration/subagents)
- [Claude Code plugins](https://code.claude.com/docs/en/plugins/create)
- [Claude Code subagents](https://code.claude.com/docs/en/sub-agents)

An independent project in the Intelligenza Umana ecosystem.
