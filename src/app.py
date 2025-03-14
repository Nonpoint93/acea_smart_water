# your code here
from pmdarima import auto_arima
import pandas as pd


dataframe = pd.read_csv("./data/processed/processed_temperature_data.csv")

if dataframe is not None and not dataframe.empty:
    arima_model = auto_arima(dataframe['Representative_Temperature'], seasonal=True, trace=True, m=12)
    print(arima_model)
else:
    print("[ ERROR ] DataFrame is None or Empty.")