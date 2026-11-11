# Condicionais, datas e classificações numéricas

**1.0.0 — 11/11/2026 — código `1785b33bb05e6e43ccd253f6f676e98092676c2f`**. Relato de inspeção, não de execução funcional.

## Visão do projeto
7 programas Python independentes, organizados em arquivos/pastas; são exercícios de linha de comando, não um serviço web. Os scripts fazem leitura/escrita padrão com `input()`/`print()`. Não foi identificada persistência compartilhada.

## Especificação observada
| Fonte | Fluxo / regra efetiva | Critério de aceitação/limite |
|---|---|---|
| `verificadorAnoBissexto.py` | Ano múltiplo de 400, ou de 4 mas não 100 | 1900 não, 2000 e 2024 sim |
| `calculadoraIMC.py` | IMC = peso/(altura²); classes <18,5, <25, <30, restante | Altura zero gera divisão por zero; limites 18,5/25/30 |
| `classificadorDeIdade.py` | Faixas idade<=12; <=17; <=59; 60+ | 12/13, 17/18, 59/60; negativo cai em criança |
| `conversorTemperatura.py` | Conversão de temperatura | Pontos de congelamento e ebulição |
| `calculadoraComissao.py` | Cálculo de remuneração variável | Zero, positivo e negativo |
| `calculadoraMedia.py` | Média aritmética | Conferir divisão / quantidade zero |
| `areaDeCircunferencia.py` | Área do círculo | Raio zero e negativo |

## Decisões, dívida técnica e segurança
A fórmula de ano bissexto segue calendário gregoriano; já os outros scripts não validam todo domínio numérico. O IMC com altura zero e a idade negativa são lacunas reais. Não usar a classificação de IMC como diagnóstico médico.

Para testes automatizados, isolar funções e substituir `input()` por sequências controladas; não reescrever o comportamento por conveniência. Execute o exercício principal por `python verificadorAnoBissexto.py`. A pasta `tests/` atual trata primordialmente estrutura documental. A versão do Python, entrada e stdout precisam ser registradas para confirmar casos.
