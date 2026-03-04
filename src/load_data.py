from pathlib import Path
import pandas as pd

def carregar_dados():
    base_dir = Path(__file__).parent.parent.resolve()
    data_path = base_dir / 'data' / 'income.csv'
    df = pd.read_csv(data_path)
    return df