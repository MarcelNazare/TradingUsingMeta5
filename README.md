
# 📈 MetaTrader5 Data Collector & Analyzer
This project is a Python-based tool that connects to the MetaTrader5 trading platform to retrieve historical financial data, perform basic technical analysis using the ADX (Average Directional Index) indicator, and save the results in a CSV file. It allows users to select trading symbols and timeframes interactively and is designed for traders and analysts looking to automate market data collection and analysis.

This Python script connects to MetaTrader5 using API credentials stored in a `.env` file, allows the user to select a trading symbol and timeframe, pulls historical data, analyzes it using the ADX (Average Directional Index) indicator, and saves the results to a CSV file.

---

## 🔧 Features

- Connects securely to MetaTrader5 using environment variables
- Supports interactive selection of trading pairs and timeframes
- Fetches and stores historical trading data
- Converts raw data to a clean `pandas` DataFrame
- Performs ADX analysis using a custom module (`calculate_adx`)
- Saves results to a CSV file

---

## 📁 Project Structure

```
project/
│
├── analysis.py         # Custom module with calculate_adx function
├── main.py             # Main script (the code you provided)
├── .env                # Stores login credentials
├── /csv/               # Output directory for CSV files
├── eurusd_rates.csv    # Example output file
├── README.md           # You're here
```

---

## 📦 Requirements

Install dependencies using:

```bash
pip install -r requirements.txt
```

**`requirements.txt` (example):**
```
MetaTrader5
python-dotenv
pandas
```

---

## 🔑 .env File

Create a `.env` file in the project root with the following content:

```env
LOGIN_KEY=your_login_id
PASS_KEY=your_password
SERVER_KEY=your_server_name
```

> ⚠️ Keep this file secret and **never** commit it to version control.

---

## 🚀 How to Use

### Run the script:

```bash
python main.py
```


### Interactive Flow:

1. Log in to your MetaTrader5 account using `.env` credentials.
2. Select a trading pair (e.g., `EURUSD`, `XAUUSD`).
3. Select a timeframe (e.g., 1-minute, 1-hour, daily).
4. Data is retrieved from MT5 and converted into a DataFrame.
5. ADX analysis is performed using the custom period you input.
6. Data is saved to a CSV file (e.g., `eurusd_rates.csv`).

---

## 📊 ADX Analysis

The script uses a custom `calculate_adx` function from the `analysis.py` module to compute the **Average Directional Index**, a technical indicator that quantifies trend strength.

Ensure `analysis.py` contains the following function or equivalent:

```python
def calculate_adx(data, period):
    # Your implementation here
    return adx_series
```

---

## 📝 Notes

- Ensure MetaTrader5 is installed and the platform is accessible.
- Your MetaTrader5 terminal must be running and connected.
- Some symbols like `XAUUSD` might require special permissions or account types.

---

## 🐛 Troubleshooting

- **Login failed**: Check your credentials and `.env` file.
- **Connection issues**: Make sure you are connected to the Internet and MetaTrader5 is properly configured.
- **Symbol not found**: Check if the selected trading pair is available on your broker account.

---

## 📬 Contact

For issues or feature requests, feel free to open an issue or contact the developer.
