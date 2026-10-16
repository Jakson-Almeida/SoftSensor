"""Tabela diária de DBO, DQO e SST para os modelos de soft sensor.

SST no arquivo se chama SS. SSV (sólidos voláteis) e as colunas RD-* (desempenho)
não entram: são outras grandezas.

Faltantes não são interpolados. Cada linha é uma análise de laboratório, e há
buracos de vários dias seguidos. A tabela de modelagem fica só com os dias em
que DBO, DQO e SST existem em todos os pontos medidos.
"""

from pathlib import Path

import pandas as pd

COLUNAS = [
    "dia",
    "Q-E", "ZN-E", "PH-E", "DBO-E", "DQO-E", "SS-E", "SSV-E", "SED-E", "COND-E",
    "PH-P", "DBO-P", "SS-P", "SSV-P", "SED-P", "COND-P",
    "PH-D", "DBO-D", "DQO-D", "SS-D", "SSV-D", "SED-D", "COND-D",
    "PH-S", "DBO-S", "DQO-S", "SS-S", "SSV-S", "SED-S", "COND-S",
    "RD-DBO-P", "RD-SS-P", "RD-SED-P", "RD-DBO-S", "RD-DQO-S",
    "RD-DBO-G", "RD-DQO-G", "RD-SS-G", "RD-SED-G",
]

# Mesma análise em pontos diferentes da planta. Não há DQO no primário.
DBO = ["DBO-E", "DBO-P", "DBO-D", "DBO-S"]
DQO = ["DQO-E", "DQO-D", "DQO-S"]
SST = ["SS-E", "SS-P", "SS-D", "SS-S"]
PARAMETROS = DBO + DQO + SST
ALVO = "DBO-S"


def localizar_dados() -> Path:
    aqui = Path(__file__).resolve().parent
    candidatos = [
        aqui.parent / "data" / "water-treatment-plant" / "water-treatment.data",
        Path("data") / "water-treatment-plant" / "water-treatment.data",
    ]
    for caminho in candidatos:
        if caminho.exists():
            return caminho
    raise FileNotFoundError("Não encontrei data/water-treatment-plant/water-treatment.data.")


def carregar() -> pd.DataFrame:
    df = pd.read_csv(localizar_dados(), header=None, names=COLUNAS, na_values="?")
    df["data"] = pd.to_datetime(df["dia"].str.replace("D-", "", regex=False), format="%d/%m/%y")
    return df.sort_values("data").reset_index(drop=True)


def tabela_modelagem() -> pd.DataFrame:
    """Dias com DBO, DQO e SST completos, em ordem cronológica."""
    df = carregar()
    return df.dropna(subset=PARAMETROS).loc[:, ["data", *PARAMETROS]].reset_index(drop=True)


if __name__ == "__main__":
    bruto = carregar()
    tabela = tabela_modelagem()
    print(f"dias no arquivo: {len(bruto)}")
    print(f"dias completos em DBO, DQO e SST: {len(tabela)}")
    print(f"alvo: {ALVO}")
