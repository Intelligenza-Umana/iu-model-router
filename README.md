# IU Model Router

*Human intelligence. Artificial assistance.*

A model-routing skill for coding agents by [Intelligenza Umana](https://github.com/Intelligenza-Umana/intelligenza-umana). It guides model choice using complexity, project context, risk and cost. It suggests light, standard or advanced subtasks and asks the host to verify delegated work and escalate when appropriate.

## Requirements and status

Codex or Claude Code, an authenticated account and access to the desired models. This is an early version (0.1.0).

**Verified on Claude Code 2.1.332**, in a headless run (`claude -p`) with the plugin loaded: the skill was discovered, a README typo was routed to `iu-light` and a JWT review to `iu-advanced`, and the session trace showed those subagents running on Haiku 5.5 and Opus 5.5 while the main session stayed on Sonnet 5.5. **Not verified:** Codex, other Claude Code versions, and sessions where the account lacks one of the three models. The host may still restrict or ignore delegation or model requests.

## Claude Code

Install from the marketplace (Claude Code 2.1.275 or later), inside a session:

```text
/plugin install iu-model-router --marketplace Intelligenza-Umana/iu-model-router
```

Or from a terminal:

```sh
claude plugin marketplace add Intelligenza-Umana/iu-model-router
claude plugin install iu-model-router@iu-model-router
```

To try it without installing, clone the repository and load it for one session:

```sh
git clone https://github.com/Intelligenza-Umana/iu-model-router.git
cd iu-model-router
claude --plugin-dir .
```

Invoke `/iu-model-router:model-routing` or ask Claude to route a task by complexity. The included agents use Claude's `haiku`, `sonnet` and `opus` aliases. Models must be available to your account. Claude Code settings, permissions and model overrides can affect the model used. The `--plugin-dir` option loads the plugin for the session.

## Codex

Clone the repository (see above), then install the shared skill for your user:

```sh
mkdir -p ~/.agents/skills/model-routing
cp -n skills/model-routing/SKILL.md ~/.agents/skills/model-routing/SKILL.md
```

On systems where `cp -n` is unavailable, copy the file without overwriting an existing installation. Review any existing skill before replacing it. Restart Codex, then invoke `$model-routing` or ask it to choose models. Codex can use native subagents and their model settings when the client, account, instructions and session permit delegation. Configure or request models available in your environment. The Claude-specific agents do not configure Codex.

## Behavior and limits

The host decides when to invoke the skill and whether to delegate. Model selection depends on the host's capabilities, configuration and available models. The skill does not force a switch of the main session model or route between providers. Subagent calls have their own context and token costs, so a cheaper model does not guarantee a lower total bill. Review results and measure usage in your provider's dashboard.

For example, ask the agent to use model routing to inspect a project, make a small documentation change and assess whether the authentication flow needs a more capable model. Project rules take priority over apparent simplicity.

## Verification and contributions

Run `python3 -m unittest discover -s tests -v` to check the packaged manifest, skill and agent definitions. These checks do not execute a real agent session. Report reproducible problems through GitHub issues. For security issues, follow the [Intelligenza Umana security policy](https://github.com/Intelligenza-Umana/intelligenza-umana/blob/main/SECURITY.md).

## Sources

- [Codex skills](https://developers.openai.com/codex/skills)
- [Codex subagents](https://developers.openai.com/codex/agent-configuration/subagents)
- [Claude Code plugins](https://code.claude.com/docs/en/plugins/create)
- [Claude Code subagents](https://code.claude.com/docs/en/sub-agents)

An independent project in the Intelligenza Umana ecosystem. Distributed under the [MIT license](LICENSE).
