import yfinance as yf
class Fetching:
    def fetch_data(symbol):
        data = {}
        for s in symbol:
            comp = yf.Ticker(s)
            hist = comp.history(period = "2y")
            if not hist.empty:
                company_name = comp.info.get('shortName')
                data[company_name] = hist
        return data
    symbols = ["MSFT", "AAPL", "NVDA", "AMZN", "META", "GOOG", "LLY", "AVGO","TSLA", "JPM", "UNH", "V", "XOM", "MA", "JNJ", "PG", "HD", "MRK", "COST", "ABBV",
    "CRM", "ADBE", "AMD", "CVX", "NFLX", "WMT", "PEP", "KO", "ACN", "BAC", "TMO", "MCD",
    "CSCO", "DIS", "LIN", "ABT", "ORCL", "INTU", "INTC", "WFC", "IBM", "VZ", "CMCSA",
    "QCOM", "CAT", "NOW", "DHR", "AMGN", "PFE", "UNP", "GE", "UBER", "TXN", "AMAT", "SPGI",
    "PM", "ISRG", "COP", "BKNG", "RTX", "HON", "LOW", "NKE", "GS", "PLD", "AXP", "T",
    "BA", "ELV", "NEE", "MDT", "SYK", "PANW", "LRCX", "TJX", "BLK", "SBUX", "ETN", "VRTX",
    "MS", "PGR", "UPS", "C", "DE", "ADP", "MDLZ", "REGN", "CB", "BMY", "CI", "MMC", "ADI",
    "CVS", "BSX", "LMT", "MU", "SCHW", "GILD", "BX", "AMT", "ZTS", "SNPS", "FI", "KLAC",
    "CDNS", "TMUS", "EQIX", "ICE", "SHW", "CME", "CSX", "SO", "CMG", "DUK", "MO", "BDX",
    "ITW", "WM", "CL", "ANET", "SLB", "TGT", "PH", "EOG", "MCK", "ABNB", "PSX", "MPC",
    "NOC", "USB", "MCO", "APH", "TDG", "TT", "MAR", "AON", "GD", "PYPL", "HCA", "ORLY",
    "PNC", "NXPI", "EMR", "ROP", "NSC", "FDX", "ADSK", "PCAR"]
    main_data = fetch_data(symbols)





