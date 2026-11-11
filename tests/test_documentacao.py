import ast
import unittest
from pathlib import Path
RAIZ=Path(__file__).resolve().parents[1]
class TestesAtividade(unittest.TestCase):
    def test_documentos(self):
        for item in ('README.md','AGENTS.md','docs/REQUISITOS.md','docs/ARQUITETURA.md','docs/UML.puml','docs/PLANO_TESTES.md'):
            with self.subTest(item=item): self.assertTrue((RAIZ/item).is_file())
    def test_sintaxe_python(self):
        scripts=[p for p in RAIZ.rglob('*.py') if 'tests' not in p.parts]
        self.assertTrue(scripts)
        for p in scripts:
            with self.subTest(p=p): ast.parse(p.read_text(encoding='utf-8-sig'))
