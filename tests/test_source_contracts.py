#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-3.0-or-later
"""Source-only checks. Does not connect to a printer, CUPS, GTK or the network."""
import ast
from pathlib import Path
import stat
from types import SimpleNamespace
import unittest

ROOT=Path(__file__).resolve().parents[1]
NAME="brother-dcp-l2665dw-manager"
SOURCE=(ROOT/NAME).read_text(encoding="utf8")
TREE=ast.parse(SOURCE)

def extract_translation(lang):
    relevant=[]
    for node in TREE.body:
        if isinstance(node,ast.Assign) and any(
            isinstance(target,ast.Name) and target.id in {"ACTIVE_LANGUAGE","TRANSLATIONS"}
            for target in node.targets
        ):
            relevant.append(node)
        elif isinstance(node,ast.FunctionDef) and node.name=="tr":
            relevant.append(node)
    assert len(relevant)==4,len(relevant)
    module=ast.fix_missing_locations(ast.Module(body=relevant,type_ignores=[]))
    scope={"_locale_os":SimpleNamespace(environ={"LANG":lang})}
    exec(compile(module,NAME,"exec"),scope)
    return scope

class SourceContracts(unittest.TestCase):
    def test_python_launcher_and_parse(self):
        self.assertTrue(SOURCE.startswith("#!/usr/bin/python3\n"))
        self.assertIn("# SPDX-License-Identifier: GPL-3.0-or-later",SOURCE[:100])
        self.assertTrue((ROOT/NAME).stat().st_mode & stat.S_IXUSR)

    def test_bilingual_locale(self):
        self.assertEqual(extract_translation("it_IT.UTF-8")["ACTIVE_LANGUAGE"],"it")
        self.assertEqual(extract_translation("en_GB.UTF-8")["ACTIVE_LANGUAGE"],"en")
        self.assertEqual(extract_translation("de_DE.UTF-8")["ACTIVE_LANGUAGE"],"en")
        self.assertEqual(extract_translation("it_IT.UTF-8")["tr"]("Stampa"),"Stampa")

    def test_english_controls(self):
        tr=extract_translation("en_US.UTF-8")["tr"]
        expected={
            "Stampante CUPS:":"CUPS printer:",
            "Apri Web Brother":"Open Brother web interface",
            "Verifica stato":"Refresh status",
            "Stampa":"Printing",
            "Manutenzione":"Maintenance",
            "Solo fronte":"Single-sided",
            "Fronte-retro lato lungo":"Two-sided (long edge)",
            "Fronte-retro lato corto":"Two-sided (short edge)",
            "Apri stato toner e gestione Brother":"Open Brother toner status and management",
        }
        for source,translated in expected.items():
            with self.subTest(label=source):
                self.assertEqual(tr(source),translated)

    def test_duplex_and_language_controls_present(self):
        for mark in ("self.duplex = Gtk.ComboBoxText()",
                     "language_select.append('it', 'Italiano')",
                     "language_select.append('en', 'English')",
                     "language_select.connect('changed', self.change_language)",
                     "'Duplex=' + duplex",):
            self.assertIn(mark,SOURCE)

    def test_debian_builder_version_and_portability(self):
        builder=(ROOT/"build-deb.sh").read_text(encoding="utf8")
        self.assertIn("VERSION=0.2.1",builder)
        self.assertIn("Version: 0.2.1",builder)
        self.assertIn('./brother-dcp-l2665dw-manager_0.2.1_all.deb',builder)
        self.assertNotIn('/home/giu/',builder)

if __name__=="__main__":
    unittest.main()
