# Bank Loan Portfolio Dashboard

An interactive Streamlit dashboard for exploring a bank loan portfolio —
built as a self-training project to learn the path from raw data to a live,
shareable web dashboard using Python.

**🔗 Live app:** [kaifa254-streamlit-data-dashboard-dashboard-gvia7p.streamlit.app](https://kaifa254-streamlit-data-dashboard-dashboard-gvia7p.streamlit.app/)

> **Note:** All data used in this project (`data/bank_loan_portfolio.csv`) is
> entirely synthetic/randomly generated for training purposes. It does not
> represent real NCBA customers, balances, or figures.

## What the dashboard does

The app takes a loan portfolio dataset (1,200 synthetic loan records across
branches, products, and customer segments) and turns it into an interactive
view with:

- **KPI cards** — total outstanding loan book, number of loans, default rate
  (>30 DPD), and NPL ratio, all recalculated live as filters change
- **Sidebar filters** — filter the entire dashboard by Branch, Product, and
  Customer Segment
- **Outstanding balance by product** — interactive bar chart
- **Portfolio mix by IFRS9 risk stage** — donut chart (Performing /
  Underperforming / Non-Performing)
- **Monthly disbursement trend** — line chart showing lending volume over
  time
- **Branch performance summary** — aggregated table (loan count, total
  balance, average DPD per branch)
- **Loan-level detail table** — full sortable/searchable record view
- **CSV export** — download whatever data is currently filtered

Everything on the page reacts live to the sidebar filters — no page reloads,
no separate "apply" button.

## What's inside this repo

```
bank_training_package/
├── data/
│   └── bank_loan_portfolio.csv     ← synthetic sample data (1,200 loans)
├── bank_dashboard_training.ipynb   ← Jupyter notebook, commented step by step
├── dashboard.py                    ← the live Streamlit dashboard app
├── requirements.txt                ← packages needed to run everything
└── README.md                       ← this file
```

## Recommended order

1. **Start with the notebook** — `bank_dashboard_training.ipynb`. Open it in
   VS Code or Jupyter and run each cell in order. Every step has a markdown
   explanation above it describing what the code does and why — this is
   where the KPI calculations and charts are built up piece by piece before
   they're wrapped into the dashboard.
2. **Then run the dashboard** — `dashboard.py`. It uses the exact same data
   and calculations from the notebook, just wrapped as an interactive web
   app instead of static cells. Or just visit the **live app link above** to
   see it without installing anything.

## Step 1: Set up (to run locally)

1. Clone or download this repo.
2. Open the folder in VS Code: **File → Open Folder**.
3. Select your Anaconda Python interpreter:
   `Ctrl+Shift+P` → `Python: Select Interpreter` → choose your `base` (or
   `ds`) environment.
4. Open a terminal (**Terminal → New Terminal**) and install packages:
   ```
   pip install -r requirements.txt
   ```

## Step 2: Open and run the notebook

**In VS Code:**
1. Click `bank_dashboard_training.ipynb` in the file explorer — it opens in
   VS Code's built-in notebook viewer (this is what the Jupyter extension
   enables).
2. Click **"Run All"** at the top, or click into each cell and press
   `Shift + Enter` to run them one at a time — recommended for learning, so
   you can read the markdown explanation before each code cell runs.
3. Charts render directly inside the notebook, below each code cell.

**Alternative — classic Jupyter in the browser:**
```
jupyter notebook
```
This opens a browser tab at `http://localhost:8888`. Click
`bank_dashboard_training.ipynb` to open it there instead.

## Step 3: Run the dashboard locally

In the same terminal:
```
streamlit run dashboard.py
```

**What to expect:**
- Terminal prints:
  ```
  Local URL: http://localhost:8501
  Network URL: http://192.168.x.x:8501
  ```
- Your browser opens automatically to `http://localhost:8501`.
- If it doesn't open on its own, copy the **Local URL** and paste it into
  your browser manually.
- Press `Ctrl + C` in the terminal to stop the app.

## How this is deployed

This dashboard is deployed on **Streamlit Community Cloud**, connected
directly to this GitHub repository — every push to the `main` branch
automatically updates the live app.

| Method | Who can see it | Used for |
|---|---|---|
| **Local (`streamlit run`)** | Only you, on your own machine | Development and testing |
| **Network URL** (`http://192.168.x.x:8501`) | Anyone on the same office Wi-Fi/LAN while the app is running | Quick demo to a colleague nearby |
| **Streamlit Community Cloud** (this app) | Anyone with the public link, anywhere, anytime | This project — public/demo data only |
| **Internal company server / VM** | Anyone on NCBA's internal network/VPN | The correct option for real banking data — needs IT to provision and host it |

## Common issues

| Problem | Likely fix |
|---|---|
| `streamlit: command not found` | Re-run `pip install -r requirements.txt` in the terminal matching your selected VS Code interpreter |
| Notebook won't open in VS Code | Make sure the **Jupyter** extension is installed (Extensions panel) |
| `FileNotFoundError: data/bank_loan_portfolio.csv` | Make sure your terminal's current folder is the package root (where `dashboard.py` lives), not a subfolder |
| Browser doesn't auto-open | Manually visit `http://localhost:8501` |
