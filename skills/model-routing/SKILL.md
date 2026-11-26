---
name: model-routing
description: Choose an appropriate model for a coding task or subtask based on complexity, project context, risk and cost. Use when asked to route work, optimize model use, or select a lighter or stronger agent.
---

# Model routing

Assess the task, project instructions and relevant context. Honor the user's model choice, project constraints, tool permissions and instructions governing delegation.

1. Choose a level based on the most demanding part. Light suits bounded, reversible work with obvious verification. Standard suits ordinary implementation, debugging and review. Advanced suits ambiguous architecture, security-sensitive work, migrations, concurrency, data integrity and difficult failures.
2. Increase the level when project rules or context identify sensitive code. A short request alone does not imply a simple task.
3. State the level and a brief reason when useful. Respect any explicit model override.
4. If delegation is permitted and appropriate, use the host's native subagent mechanism with an available model. Claude Code provides light, standard and advanced agents with corresponding model aliases. In Codex request an available subagent model or use configured custom agents. The host can restrict model selection and delegation.
5. Give the subagent a bounded task, context and expected result. Review its work and run relevant verification. If insufficient, retry with a stronger available model or handle the task directly.
6. If the host cannot apply the chosen model, continue with the current model and report the limitation. Never claim a switch happened without confirmation from the host.

Avoid spawning agents just to classify a trivial task. Extra agents consume tokens. Do not assume cross-provider routing, automatic switching of the current session, fixed prices or availability of a specific model.
