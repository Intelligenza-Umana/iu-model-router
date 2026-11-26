import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parent.parent


class PackageTests(unittest.TestCase):
    def test_manifest_and_skill_are_discoverable(self):
        manifest = json.loads((ROOT / '.claude-plugin/plugin.json').read_text())
        self.assertEqual(manifest['name'], 'model-router')
        self.assertTrue(manifest['version'])
        skill = (ROOT / 'skills/model-routing/SKILL.md').read_text()
        self.assertTrue(skill.startswith('---\nname: model-routing\ndescription: '))

    def test_agents_define_distinct_models(self):
        for tier, model in [('light', 'haiku'), ('standard', 'sonnet'), ('advanced', 'opus')]:
            agent = (ROOT / f'agents/{tier}.md').read_text()
            frontmatter = agent.split('---', 2)[1]
            self.assertIn(f'name: {tier}\n', frontmatter)
            self.assertIn(f'model: {model}\n', frontmatter)
            self.assertIn('description:', frontmatter)


if __name__ == '__main__':
    unittest.main()
