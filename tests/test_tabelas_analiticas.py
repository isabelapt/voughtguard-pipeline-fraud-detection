import pandas as pd
from src.tabelas_analiticas import (
    ranking_paises_fraude,
    top_merchant_risco,
    salvar_tabelas_analiticas,
)

def test_ranking_paises_fraude():
    df = pd.DataFrame({
        "country": ["BR", "BR", "US", "US", "US"],
        "is_fraud": [1, 0, 1, 0, 0],
    })

    resultado = ranking_paises_fraude(df)

    assert list(resultado.columns) == [
        "country",
        "total_transacoes",
        "total_fraudes",
        "taxa_fraude",
    ]
    assert resultado.iloc[0]["country"] == "BR"
    assert resultado.iloc[0]["total_transacoes"] == 2
    assert resultado.iloc[0]["total_fraudes"] == 1
    assert resultado.iloc[0]["taxa_fraude"] == 0.5

def test_top_merchant_risco():
    df = pd.DataFrame({
        "merchant_category": ["A", "A", "B"],
        "combined_risk": [10, 20, 5],
    })

    resultado = top_merchant_risco(df)

    assert list(resultado.columns) == ["merchant_category", "combined_risk_medio"]
    assert resultado.iloc[0]["merchant_category"] == "A"
    assert resultado.iloc[0]["combined_risk_medio"] == 15.0