# Testes específicos de Atividade3-EdN

**1.0.0 — 11/11/2026 — código `1785b33bb05e6e43ccd253f6f676e98092676c2f`**. Relato de inspeção, não de execução funcional.

## Matriz por exercício
| Caso | Arquivo | Entrada e resultado esperado | Evidência |
|---|---|---|---|
| EDT-01 | `verificadorAnoBissexto.py` | 1900 não, 2000 e 2024 sim | A executar |
| EDT-02 | `calculadoraIMC.py` | Altura zero gera divisão por zero; limites 18,5/25/30 | A executar |
| EDT-03 | `classificadorDeIdade.py` | 12/13, 17/18, 59/60; negativo cai em criança | A executar |
| EDT-04 | `conversorTemperatura.py` | Pontos de congelamento e ebulição | A executar |
| EDT-05 | `calculadoraComissao.py` | Zero, positivo e negativo | A executar |
| EDT-06 | `calculadoraMedia.py` | Conferir divisão / quantidade zero | A executar |
| EDT-07 | `areaDeCircunferencia.py` | Raio zero e negativo | A executar |

## Negativos e não regressão
NT-01: texto não numérico nas leituras. NT-02: números negativos, zero e limites citados nos scripts. NT-03: saída em português e controle de laço/encerramento. NT-04: avaliar `EOFError` e `KeyboardInterrupt` quando o processo for automatizado.

## Execução
```bash
python verificadorAnoBissexto.py
python -m unittest discover -s tests -v
```

Casos EDT-* são planejados e não estão cobertos integralmente pelos testes documentais. O registro de cada teste deve conter SHA, stdin, stdout, código de saída, PASS/FAIL/BLOCKED e decisão sobre bugs conhecidos.
