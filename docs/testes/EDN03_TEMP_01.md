# EDN03-TEMP-01 — Limites físicos e entradas do conversor

14/11/2026 · `conversorTemperatura.py`.

## Defeito encontrado
O script anterior permitia Kelvin negativo, Celsius e Fahrenheit abaixo do zero absoluto, valores NaN/infinito e opção de menu inválida sem informar erro. Importar o arquivo em um teste também tentava ler `input()` imediatamente.

## Correção e casos
- Função pura `converter_temperaturas` com validação de opção, tipos e finitude.
- Zero absoluto aceito: 0 Kelvin = -273.15 °C = -459.67 °F; valores inferiores rejeitados.
- Proteção contra overflow de cálculos com números muito grandes.
- CLI mantém saída textual das três opções e retorna mensagem sem traceback ao receber entrada inválida/EOF.
- Testes unitários de conversão e CLI em subprocesso. Nenhuma biblioteca externa adicionada.
