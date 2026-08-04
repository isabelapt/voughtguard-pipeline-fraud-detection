"""Tabelas analíticas - ranking de fraude por país e merchant"""
import pandas as pd

def ranking_paises_fraude(df: pd.DataFrame) -> pd.DataFrame:
    """ Gera um ranking de países com base na quantidade de transações fraudulentas."""
    ranking = (
        df.groupby("country", as_index=False)
        .agg(
            total_transacoes=("is_fraud", "size"),
            total_fraudes=("is_fraud", "sum"),
        )
    )
    ranking["taxa_fraude"] = ranking["total_fraudes"] / ranking["total_transacoes"]
    return ranking.sort_values("taxa_fraude", ascending=False).reset_index(drop=True)

def top_merchant_risco(df: pd.DataFrame) -> pd.DataFrame:
    """Gera o top de categorias de merchant por combined_risk médio.""" 
    ranking = (
        df.groupby("merchant_category", as_index=False)
        .agg(combined_risk_medio=("combined_risk", "mean"))
    )
    return ranking.sort_values("combined_risk_medio", ascending=False).reset_index(drop=True)

def salvar_tabelas_analiticas(
    ranking_paises: pd.DataFrame,
    top_merchant: pd.DataFrame,
    diretorio_saida: str = "data/processed",
) -> None:
    """Salva as tabelas analíticas no diretório de saída."""

    ranking_paises.to_csv(f"{diretorio_saida}/ranking_paises_fraude.csv", index=False)
    top_merchant.to_csv(f"{diretorio_saida}/top_merchant_risco.csv", index=False)       
    
    