
# CNG Configurator App

This is a dynamic CNG system configurator built using [Streamlit](https://streamlit.io/). It allows users to filter and select configuration options for commercial and industrial chassis systems, and view the corresponding system components and pricing information.

## 🔧 Features

- Filter by Application, Body Manufacturer, Chassis Type, System Type, and more
- Dynamic output including:
  - Part Numbers
  - System Cost
  - FET (Federal Excise Tax)
  - Install Cost
  - Total Pricing
- Powered by a real dataset (`RSG_CONFIGURATOR_CLEANED.xlsx`)

## 📁 Files

- `app.py` — the Streamlit app
- `RSG_CONFIGURATOR_CLEANED.xlsx` — dataset for configuration options
- `requirements.txt` — dependencies

## 🚀 How to Run

1. **Install dependencies**:

```bash
pip install -r requirements.txt
```

2. **Run the app**:

```bash
streamlit run app.py
```

3. Open your browser and go to `http://localhost:8501`

## ☁️ Deploy on Streamlit Cloud

1. Push these files to a GitHub repository.
2. Go to [https://streamlit.io/cloud](https://streamlit.io/cloud)
3. Click “New App” and connect your GitHub repo.
4. Set the path to `app.py` and click “Deploy”.

## 🧰 Requirements

- Python 3.7 or higher
- Streamlit
- pandas
- openpyxl

---

Maintained by: [Your Name or Team]
