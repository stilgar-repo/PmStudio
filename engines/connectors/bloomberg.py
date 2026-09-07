"""Bloomberg Desktop API connector leveraging xbbg and Polars.

Provides typed reference, historical, BQL, and chain data queries with
automatic conversion to Polars DataFrames.
"""

from __future__ import annotations

import socket
from collections.abc import Sequence
from datetime import date
from typing import Any

import polars as pl
from xbbg import blp


class BloombergConnectionError(ConnectionError):
    """Raised when unable to communicate with the local Bloomberg Desktop API."""


def check_terminal_connection(
    host: str = "127.0.0.1",
    port: int = 8194,
    timeout: float = 2.0,
) -> bool:
    """Verify that the Bloomberg Desktop API (bbcomm/terminal) is actively listening."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(timeout)
        try:
            sock.connect((host, port))
            return True
        except (OSError, TimeoutError):
            return False


def get_reference_data(
    tickers: str | Sequence[str],
    fields: str | Sequence[str],
    **kwargs: Any,
) -> pl.DataFrame:
    """Fetch reference/static Bloomberg data (BDP) formatted as a Polars DataFrame.

    Parameters
    ----------
    tickers : str | Sequence[str]
        One or more Bloomberg tickers (e.g. 'SPY US Equity', ['AAPL US Equity', 'MSFT US Equity']).
    fields : str | Sequence[str]
        One or more Bloomberg field mnemonics (e.g. 'PX_LAST', 'SECURITY_NAME').
    kwargs : Any
        Additional overrides or keyword arguments forwarded to xbbg.blp.bdp.

    Returns
    -------
    pl.DataFrame
        Polars DataFrame containing ticker, field, and value columns.
    """
    res = blp.bdp(tickers=tickers, flds=fields, **kwargs)
    df = pl.from_arrow(res.to_native())
    if isinstance(df, pl.Series):
        return df.to_frame()
    return df


def get_historical_data(
    tickers: str | Sequence[str],
    fields: str | Sequence[str],
    start_date: str | date,
    end_date: str | date | None = None,
    **kwargs: Any,
) -> pl.DataFrame:
    """Fetch historical daily Bloomberg data (BDH) formatted as a Polars DataFrame.

    Parameters
    ----------
    tickers : str | Sequence[str]
        One or more Bloomberg tickers.
    fields : str | Sequence[str]
        One or more Bloomberg field mnemonics (e.g. ['PX_LAST', 'VOLUME']).
    start_date : str | date
        Start date in 'YYYY-MM-DD' format or date object.
    end_date : str | date | None
        End date in 'YYYY-MM-DD' format or date object. Defaults to latest available.
    kwargs : Any
        Additional overrides (e.g. Fill='P', Days='A') forwarded to xbbg.blp.bdh.

    Returns
    -------
    pl.DataFrame
        Polars DataFrame containing ticker, date, field, and value columns.
    """
    res = blp.bdh(
        tickers=tickers,
        flds=fields,
        start_date=str(start_date),
        end_date=str(end_date) if end_date is not None else None,
        **kwargs,
    )
    df = pl.from_arrow(res.to_native())
    if isinstance(df, pl.Series):
        return df.to_frame()
    return df


def query_bql(expression: str) -> pl.DataFrame:
    """Execute a Bloomberg Query Language (BQL) query and return a Polars DataFrame.

    Parameters
    ----------
    expression : str
        Bloomberg Query Language expression string.
        Examples:
            "get(px_last) for(['AAPL US Equity'])"
            "get(px_last, pe_ratio) for(members('SPX Index')) with(pe_ratio > 25)"
            "get(id_isin, weights) for(holdings('SPY US Equity'))"

    Returns
    -------
    pl.DataFrame
        Polars DataFrame containing the resulting BQL dataset.
    """
    res = blp.bql(expression)
    df = pl.from_arrow(res.to_native())
    if isinstance(df, pl.Series):
        return df.to_frame()
    return df
