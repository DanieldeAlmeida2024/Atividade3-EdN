"""Testes reais para os exercícios de área, IMC e ano bissexto."""
import importlib.util
import math
import pathlib
import subprocess
import sys
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]

def importar(nome):
    arquivo = ROOT / nome
    spec = importlib.util.spec_from_file_location(nome.replace(".py", ""), arquivo)
    modulo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modulo)
    return modulo

area = importar("areaDeCircunferencia.py")
imc = importar("calculadoraIMC.py")
bissexto = importar("verificadorAnoBissexto.py")
temperatura = importar("conversorTemperatura.py")


class RegrasTestes(unittest.TestCase):
    def test_area_calculo(self):
        self.assertAlmostEqual(12.5663706, area.calcular_area(2))
        self.assertEqual(0, area.calcular_area(0))

    def test_area_rejeita_raio_invalido(self):
        for raio in (-1, float('nan'), float('inf')):
            with self.subTest(raio=raio), self.assertRaises(ValueError):
                area.calcular_area(raio)

    def test_imc_calculo_e_classificacao_de_fronteiras(self):
        self.assertAlmostEqual(25.0, imc.calcular_imc(100, 2.0))
        self.assertEqual("Abaixo do peso", imc.classificar_imc(18.49))
        self.assertEqual("Peso normal", imc.classificar_imc(18.5))
        self.assertEqual("Sobrepeso", imc.classificar_imc(25.0))
        self.assertEqual("Obeso", imc.classificar_imc(30.0))

    def test_imc_nao_divide_por_zero(self):
        for peso, altura in ((70, 0), (-1, 1.7), (80, -1.7),
                             (float('nan'), 2), (80, float('inf'))):
            with self.subTest(peso=peso, altura=altura), self.assertRaises(ValueError):
                imc.calcular_imc(peso, altura)

    def test_conversor_temperatura_zero_absoluto_e_tres_unidades(self):
        self.assertAlmostEqual(32.0, temperatura.converter_temperaturas(1, 0)["Fahrenheit"])
        self.assertAlmostEqual(273.15, temperatura.converter_temperaturas(1, 0)["Kelvin"])
        self.assertAlmostEqual(100.0, temperatura.converter_temperaturas(2, 212)["Celsius"])
        self.assertAlmostEqual(-273.15, temperatura.converter_temperaturas(3, 0)["Celsius"])
        self.assertAlmostEqual(-459.67, temperatura.converter_temperaturas(3, 0)["Fahrenheit"])

    def test_conversor_rejeita_estados_fisicamente_impossiveis(self):
        for unidade, valor in ((1, -273.16), (2, -459.68), (3, -0.1),
                               (1, float('nan')), (3, float('inf')), (True, 100),
                               (4, 20), (1, True), (1, 1e308)):
            with self.subTest(unidade=unidade, valor=valor):
                with self.assertRaises(ValueError):
                    temperatura.converter_temperaturas(unidade, valor)

    def test_cli_conversor_trata_entrada_invalida_sem_traceback(self):
        resultado = subprocess.run(
            [sys.executable, str(ROOT / "conversorTemperatura.py")],
            input="3\\n-5\\n", capture_output=True, text=True, timeout=10
        )
        self.assertNotEqual(0, resultado.returncode)
        self.assertIn("Erro:", resultado.stderr)
        self.assertNotIn("Traceback", resultado.stderr)

    def test_bissexto_seculo_e_ano_comum(self):
        self.assertTrue(bissexto.eh_bissexto(2000))
        self.assertTrue(bissexto.eh_bissexto(2024))
        self.assertFalse(bissexto.eh_bissexto(1900))
        self.assertFalse(bissexto.eh_bissexto(2023))

    def test_bissexto_ano_invalido(self):
        for ano in (0, -400, True, '2024'):
            with self.subTest(ano=ano), self.assertRaises(ValueError):
                bissexto.eh_bissexto(ano)

    def test_cli_area_respeita_quatro_casas(self):
        p = subprocess.run([sys.executable, str(ROOT / "areaDeCircunferencia.py")],
                           input="2\n", capture_output=True, text=True, timeout=10)
        self.assertEqual(0, p.returncode, p.stderr)
        self.assertIn("A=12.5664", p.stdout)

    def test_cli_imc_rejeita_altura_zero_sem_traceback(self):
        p = subprocess.run([sys.executable, str(ROOT / "calculadoraIMC.py")],
                           input="80\n0\n", capture_output=True, text=True, timeout=10)
        self.assertNotEqual(0, p.returncode)
        self.assertIn("Erro:", p.stderr)
        self.assertNotIn("Traceback", p.stderr)


if __name__ == "__main__":
    unittest.main()
