import importlib.util
import json
from pathlib import Path
import shutil
import tempfile
import unittest

source = Path(__file__).resolve().parents[1] / 'install.py'
spec = importlib.util.spec_from_file_location('installer', source)
m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)


class TestInstaller(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name) / 'repo'
        self.target = Path(self.tmp.name) / 'skills'
        for name in m.REQUIRED:
            folder = self.root / 'skills' / name
            folder.mkdir(parents=True)
            (folder / 'SKILL.md').write_text('---\nname: %s\n---\n' % name, encoding='utf-8')

    def tearDown(self):
        self.tmp.cleanup()

    def test_installs_all_required_skills(self):
        code, _ = m.install(self.root, self.target)
        self.assertEqual(code, 0)
        for name in m.REQUIRED:
            self.assertTrue((self.target / name / 'SKILL.md').is_file(), name)
        self.assertEqual(m.owned(self.target), set(m.REQUIRED))

    def test_eagle_skills_are_installed_with_bundle(self):
        code, _ = m.install(self.root, self.target)
        self.assertEqual(code, 0)
        for name in m.EAGLE:
            self.assertTrue((self.target / name / 'SKILL.md').is_file())
            self.assertIn(name, m.owned(self.target))
        status_code, lines = m.status(self.target)
        self.assertEqual(status_code, 0)
        self.assertFalse(any('選配 eagle' in line for line in lines))

    def test_shipped_gsap_bundle_and_relative_links(self):
        import re
        repo = source.parent
        names = {'gsap-' + suffix for suffix in (
            'core', 'timeline', 'scrolltrigger', 'performance',
            'plugins', 'utils', 'react', 'frameworks')}
        self.assertTrue(names.issubset(m.sources(repo)))
        for mode in ('copy', 'symlink'):
            with self.subTest(mode=mode):
                target = self.target / mode
                code, _ = m.install(repo, target, mode=mode)
                self.assertEqual(code, 0)
                for name in names:
                    installed = target / name / 'SKILL.md'
                    self.assertEqual(installed.read_bytes(),
                                     (repo / 'skills' / name / 'SKILL.md').read_bytes())
                route = target / m.REQUIRED[0] / 'references' / 'gsap-skills.md'
                links = re.findall(r'\]\((../../gsap-[^)]+)\)', route.read_text())
                self.assertEqual(len(links), len(names))
                for link in links:
                    self.assertTrue((route.parent / link).is_file(), link)

    def test_existing_foreign_gsap_is_not_overwritten(self):
        existing = self.target / 'gsap-core'
        existing.mkdir(parents=True)
        document = existing / 'SKILL.md'
        document.write_text('existing installation', encoding='utf-8')
        code, _ = m.install(source.parent, self.target, mode='copy')
        self.assertEqual(code, 1)
        self.assertEqual(document.read_text(), 'existing installation')
        self.assertNotIn('gsap-core', m.owned(self.target))

    def test_legacy_redirect_is_not_installed(self):
        old = self.root / 'skills' / 'visual-solution-page-builder'
        old.mkdir()
        (old / 'SKILL.md').write_text('legacy redirect', encoding='utf-8')
        code, _ = m.install(self.root, self.target, mode='copy')
        self.assertEqual(code, 0)
        self.assertFalse((self.target / old.name).exists())

    def test_legacy_install_is_reported_without_removal(self):
        m.install(self.root, self.target, mode='copy')
        old = self.target / 'visual-solution-page-builder'
        old.mkdir()
        (old / 'SKILL.md').write_text('legacy', encoding='utf-8')
        data = m.read_manifest(self.target)
        data['skills'].append(old.name)
        (self.target / m.MANIFEST).write_text(json.dumps(data), encoding='utf-8')
        code, lines = m.status(self.target)
        self.assertEqual(code, 0)
        self.assertTrue(any('[歷史殘留]' in line for line in lines))
        self.assertTrue((old / 'SKILL.md').exists())

    def test_name_mismatch_is_flagged(self):
        odd = self.root / 'skills' / m.REQUIRED[0] / 'SKILL.md'
        odd.write_text('---\nname: another-name\n---\n', encoding='utf-8')
        code, lines = m.install(self.root, self.target)
        self.assertEqual(code, 0)
        self.assertTrue(any('[提醒]' in line and 'name: another-name' in line for line in lines))

    def test_unrelated_skill_folder_is_not_installed(self):
        odd = self.root / 'skills' / 'unrelated-skill'
        odd.mkdir()
        (odd / 'SKILL.md').write_text('---\nname: unrelated-skill\n---\n', encoding='utf-8')
        code, _ = m.install(self.root, self.target)
        self.assertEqual(code, 0)
        self.assertFalse((self.target / odd.name).exists())

    def test_dry_run_writes_nothing(self):
        code, _ = m.install(self.root, self.target, dry_run=True)
        self.assertEqual(code, 0)
        self.assertFalse(self.target.exists())

    def test_rerun_is_idempotent(self):
        m.install(self.root, self.target)
        code, lines = m.install(self.root, self.target)
        self.assertEqual(code, 0)
        self.assertEqual(sum(1 for line in lines if line.startswith('[更新]')), len(m.REQUIRED))
        self.assertEqual(m.owned(self.target), set(m.REQUIRED))

    def test_foreign_folder_is_kept(self):
        stranger = self.target / m.REQUIRED[0]
        stranger.mkdir(parents=True)
        keep = stranger / 'someone-elses.md'
        keep.write_text('do not touch', encoding='utf-8')
        code, lines = m.install(self.root, self.target)
        self.assertEqual(code, 1)
        self.assertEqual(keep.read_text(encoding='utf-8'), 'do not touch')
        self.assertTrue(any('[跳過]' in line for line in lines))

    def test_missing_required_skill_aborts(self):
        shutil.rmtree(self.root / 'skills' / m.REQUIRED[0])
        code, lines = m.install(self.root, self.target)
        self.assertEqual(code, 1)
        self.assertFalse(self.target.exists())
        self.assertIn('中止', lines[0])

    def test_copy_mode_is_independent_of_source(self):
        m.install(self.root, self.target, mode='copy')
        shutil.rmtree(self.root)
        self.assertTrue((self.target / m.REQUIRED[0] / 'SKILL.md').is_file())
        self.assertEqual(json.loads((self.target / m.MANIFEST).read_text(encoding='utf-8'))['mode'], 'copy')

    def test_status_reports_incomplete_install(self):
        m.install(self.root, self.target)
        m.remove(self.target / m.REQUIRED[0])
        code, lines = m.status(self.target)
        self.assertEqual(code, 1)
        self.assertTrue(any('[未安裝]' in line for line in lines))

    def test_uninstall_only_removes_tracked_entries(self):
        other = self.target / 'page-composer'
        other.mkdir(parents=True)
        (other / 'SKILL.md').write_text('unrelated skill', encoding='utf-8')
        m.install(self.root, self.target)
        code, _ = m.uninstall(self.target)
        self.assertEqual(code, 0)
        self.assertTrue((other / 'SKILL.md').is_file())
        self.assertFalse((self.target / m.MANIFEST).exists())
        for name in m.REQUIRED:
            self.assertFalse((self.target / name).exists(), name)
        self.assertTrue((self.root / 'skills' / m.REQUIRED[0] / 'SKILL.md').is_file())

    def test_setup_case_writes_settings(self):
        case = Path(self.tmp.name) / '年年有餘'
        case.mkdir(parents=True)
        code, _ = m.setup_case(case)
        self.assertEqual(code, 0)
        data = json.loads((case / '.claude' / 'settings.json').read_text(encoding='utf-8'))
        self.assertEqual(data['permissions']['defaultMode'], 'acceptEdits')
        self.assertIn('Bash(git reset --hard*)', data['permissions']['deny'])

    def test_setup_case_keeps_existing_settings_and_succeeds(self):
        case = Path(self.tmp.name) / '案件'
        (case / '.claude').mkdir(parents=True)
        settings = case / '.claude' / 'settings.json'
        settings.write_text('{"permissions": {"allow": ["Read"]}}', encoding='utf-8')
        code, lines = m.setup_case(case)
        self.assertEqual(code, 0)
        self.assertTrue(any('[跳過]' in line for line in lines))
        self.assertEqual(json.loads(settings.read_text(encoding='utf-8')),
                         {'permissions': {'allow': ['Read']}})

    def test_setup_case_rejects_missing_folder(self):
        code, _ = m.setup_case(Path(self.tmp.name) / '不存在')
        self.assertEqual(code, 1)

    def test_setup_case_dry_run_writes_nothing(self):
        case = Path(self.tmp.name) / '試跑'
        case.mkdir(parents=True)
        code, _ = m.setup_case(case, dry_run=True)
        self.assertEqual(code, 0)
        self.assertFalse((case / '.claude').exists())


    def _git(self, path, *args):
        import subprocess
        subprocess.run(('git', '-C', str(path)) + args, capture_output=True, check=True)

    def test_update_without_git_tells_user_manual_route(self):
        code, lines = m.update(self.root, self.target)
        self.assertEqual(code, 1)
        self.assertIn('不是 git clone', '\n'.join(lines))

    def test_update_explains_sandbox_fetch_head_error(self):
        from unittest.mock import patch
        failure = "error: cannot open '.git/FETCH_HEAD': Operation not permitted"
        with patch.object(m, 'git', side_effect=[
            (True, str(self.root)), (True, '0123456789abcdef'), (False, failure)
        ]):
            code, lines = m.update(self.root, self.target)
        output = '\n'.join(lines)
        self.assertEqual(code, 1)
        self.assertIn('執行環境', output)
        self.assertIn('不代表遠端 repo 拒絕存取', output)
        self.assertIn('--target', output)

    def test_update_pulls_new_commits_and_reports_them(self):
        import subprocess
        origin = Path(self.tmp.name) / 'origin'
        subprocess.run(('git', 'init', '-q', '--bare', str(origin)), check=True)
        self._git(self.root, 'init', '-qb', 'main')
        self._git(self.root, 'config', 'user.email', 't@t')
        self._git(self.root, 'config', 'user.name', 't')
        self._git(self.root, 'add', '-A')
        self._git(self.root, 'commit', '-qm', 'init')
        self._git(self.root, 'remote', 'add', 'origin', str(origin))
        self._git(self.root, 'push', '-q', '-u', 'origin', 'main')
        # 同事端：另一份 clone，模擬維護者推了新版
        other = Path(self.tmp.name) / 'other'
        subprocess.run(('git', 'clone', '-q', str(origin), str(other)), check=True)
        self._git(other, 'config', 'user.email', 't@t')
        self._git(other, 'config', 'user.name', 't')
        (other / 'skills' / m.REQUIRED[0] / 'SKILL.md').write_text('---\nname: %s\n---\n新規則\n' % m.REQUIRED[0], encoding='utf-8')
        self._git(other, 'commit', '-aqm', '新增規則')
        self._git(other, 'push', '-q')

        code, lines = m.update(self.root, self.target)
        out = '\n'.join(lines)
        self.assertEqual(code, 0)
        self.assertIn('新增規則', out)
        self.assertIn('新規則', (self.root / 'skills' / m.REQUIRED[0] / 'SKILL.md').read_text(encoding='utf-8'))

    def test_update_reports_already_latest(self):
        import subprocess
        origin = Path(self.tmp.name) / 'origin2'
        subprocess.run(('git', 'init', '-q', '--bare', str(origin)), check=True)
        self._git(self.root, 'init', '-qb', 'main')
        self._git(self.root, 'config', 'user.email', 't@t')
        self._git(self.root, 'config', 'user.name', 't')
        self._git(self.root, 'add', '-A')
        self._git(self.root, 'commit', '-qm', 'init')
        self._git(self.root, 'remote', 'add', 'origin', str(origin))
        self._git(self.root, 'push', '-q', '-u', 'origin', 'main')
        code, lines = m.update(self.root, self.target)
        self.assertEqual(code, 0)
        self.assertIn('已經是最新版', '\n'.join(lines))

    def test_manifest_tracks_eagle_skills(self):
        code, _ = m.install(self.root, self.target, mode='copy')
        self.assertEqual(code, 0)
        self.assertTrue(set(m.EAGLE).issubset(m.owned(self.target)))


if __name__ == '__main__':
    unittest.main()
