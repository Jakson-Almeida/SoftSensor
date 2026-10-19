# Base de dados

Os modelos usam o conjunto Water Treatment Plant: medições diárias de uma estação de tratamento de esgoto urbano. O arquivo foi doado em junho de 1993 por Manel Poch (Universitat Autònoma de Barcelona). O objetivo original é classificar o estado operacional da planta para detectar falhas. Aqui o mesmo arquivo serve para estimar a DBO da entrada.

Fonte: [Water Treatment Plant](https://archive.ics.uci.edu/dataset/106/water+treatment+plant), UCI Machine Learning Repository. DOI [10.24432/C5FS4C](https://doi.org/10.24432/C5FS4C). Licença [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).

Citação: Poch, M. (1993). Water Treatment Plant [Dataset]. UCI Machine Learning Repository. https://doi.org/10.24432/C5FS4C.

## Arquivo

| Arquivo | Conteúdo |
| --- | --- |
| `data/water-treatment-plant/water-treatment.data` | 527 linhas, uma por dia. |
| `data/water-treatment-plant/water-treatment.names` | Descrição, estatísticas, faltantes e classes. |
| `data/water-treatment-plant/Index` | Índice original do diretório UCI (1993–1996). |

Cada linha tem 39 campos separados por vírgula: a data (`D-d/m/aa`) e os 38 atributos abaixo. Valor ausente é `?`. As unidades não estão documentadas na UCI nem em `water-treatment.names`.

As linhas não estão em ordem de calendário. Ordenadas pela data, vão de 1 de janeiro de 1990 a 30 de outubro de 1991, com dias sem registro. A página da UCI marca o conjunto como sem valores ausentes; o arquivo tem `?` em quase todos os atributos.

A classe operacional não é uma coluna. As 13 classes (situação normal, problemas no decantador secundário, sobrecarga de sólidos, tempestade e outras) estão descritas por intervalos de datas na seção 9 de `water-treatment.names`. Os modelos não usam essas classes.

## Parâmetros

São 38 atributos numéricos e contínuos. O sufixo é o ponto de medição: **E** entrada da planta, **P** entrada do decantador primário, **D** entrada do decantador secundário, **S** saída. O prefixo **RD** é desempenho (*rendimiento*), em percentual segundo a faixa dos valores (cerca de 0 a 100).

Não há DQO no primário. **SS** é sólidos em suspensão (o SST usado nos modelos). **SSV** é a fração volátil, outra grandeza. Não há coluna de amônio, nitrogênio amoniacal ou nitrogênio total.

| # | Coluna | Descrição | Nos modelos | Mín. | Máx. | Média | Faltantes |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: |
| 1 | Q-E | Vazão de entrada | — | 10000 | 60081 | 37226,56 | 18 |
| 2 | ZN-E | Zinco na entrada | — | 0,1 | 33,5 | 2,36 | 3 |
| 3 | PH-E | pH na entrada | — | 6,9 | 8,7 | 7,81 | 0 |
| 4 | DBO-E | DBO na entrada | Alvo | 31 | 438 | 188,71 | 23 |
| 5 | DQO-E | DQO na entrada | Entrada | 81 | 941 | 406,89 | 6 |
| 6 | SS-E | Sólidos em suspensão na entrada | Entrada | 98 | 2008 | 227,44 | 1 |
| 7 | SSV-E | Sólidos voláteis na entrada | — | 13,2 | 85,0 | 61,39 | 11 |
| 8 | SED-E | Sedimentos na entrada | — | 0,4 | 36 | 4,59 | 25 |
| 9 | COND-E | Condutividade na entrada | — | 651 | 3230 | 1478,62 | 0 |
| 10 | PH-P | pH no primário | — | 7,3 | 8,5 | 7,83 | 0 |
| 11 | DBO-P | DBO no primário | — | 32 | 517 | 206,20 | 40 |
| 12 | SS-P | Sólidos em suspensão no primário | — | 104 | 1692 | 253,95 | 0 |
| 13 | SSV-P | Sólidos voláteis no primário | — | 7,1 | 93,5 | 60,37 | 11 |
| 14 | SED-P | Sedimentos no primário | — | 1,0 | 46,0 | 5,03 | 24 |
| 15 | COND-P | Condutividade no primário | — | 646 | 3170 | 1496,03 | 0 |
| 16 | PH-D | pH no secundário | — | 7,1 | 8,4 | 7,81 | 0 |
| 17 | DBO-D | DBO no secundário | — | 26 | 285 | 122,34 | 28 |
| 18 | DQO-D | DQO no secundário | — | 80 | 511 | 274,04 | 9 |
| 19 | SS-D | Sólidos em suspensão no secundário | — | 49 | 244 | 94,22 | 2 |
| 20 | SSV-D | Sólidos voláteis no secundário | — | 20,2 | 100 | 72,96 | 13 |
| 21 | SED-D | Sedimentos no secundário | — | 0,0 | 3,5 | 0,41 | 25 |
| 22 | COND-D | Condutividade no secundário | — | 85 | 3690 | 1490,56 | 0 |
| 23 | PH-S | pH na saída | — | 7,0 | 9,7 | 7,70 | 1 |
| 24 | DBO-S | DBO na saída | — | 3 | 320 | 19,98 | 23 |
| 25 | DQO-S | DQO na saída | — | 9 | 350 | 87,29 | 18 |
| 26 | SS-S | Sólidos em suspensão na saída | — | 6 | 238 | 22,23 | 5 |
| 27 | SSV-S | Sólidos voláteis na saída | — | 29,2 | 100 | 80,15 | 17 |
| 28 | SED-S | Sedimentos na saída | — | 0,0 | 3,5 | 0,03 | 28 |
| 29 | COND-S | Condutividade na saída | — | 683 | 3950 | 1494,81 | 1 |
| 30 | RD-DBO-P | Desempenho de DBO no primário | — | 0,6 | 79,1 | 39,08 | 62 |
| 31 | RD-SS-P | Desempenho de SS no primário | — | 5,3 | 96,1 | 58,51 | 4 |
| 32 | RD-SED-P | Desempenho de sedimentos no primário | — | 7,7 | 100 | 90,55 | 27 |
| 33 | RD-DBO-S | Desempenho de DBO no secundário | — | 8,2 | 94,7 | 83,44 | 40 |
| 34 | RD-DQO-S | Desempenho de DQO no secundário | — | 1,4 | 96,8 | 67,67 | 26 |
| 35 | RD-DBO-G | Desempenho global de DBO | — | 19,6 | 97 | 89,01 | 36 |
| 36 | RD-DQO-G | Desempenho global de DQO | — | 19,2 | 98,1 | 77,85 | 25 |
| 37 | RD-SS-G | Desempenho global de SS | — | 10,3 | 99,4 | 88,96 | 8 |
| 38 | RD-SED-G | Desempenho global de sedimentos | — | 36,4 | 100 | 99,08 | 31 |

Mínimo, máximo e média vêm de `water-treatment.names`. A contagem de faltantes foi conferida em `water-treatment.data` (527 linhas, 39 campos em todas).

## O que entra nos modelos

O alvo é `DBO-E`. As entradas são `DQO-E` e `SS-E`, as duas medidas do mesmo ponto. Ficam 498 dias em que as três existem juntas. Os 29 dias com alguma delas ausente saem da tabela. Não há interpolação.

Uma das redes também guarda as 10 últimas `DBO-E` de laboratório, sempre de dias anteriores ao dia estimado. A DBO do próprio dia não entra como entrada.

O restante do arquivo fica de fora: vazão, zinco, pH, sedimentos, condutividade, SSV, as medidas no primário, no secundário e na saída, os desempenhos RD e as classes operacionais. `DBO-S`, a DBO do efluente, não é o alvo destes modelos.
