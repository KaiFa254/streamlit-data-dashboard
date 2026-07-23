# Bank Dashboard Training Package

Everything you need to practice going from raw data → analysis → charts →
a live web dashboard, using synthetic (fake) bank loan data.

## What's inside

```
bank_training_package/
├── data/
│   └── bank_loan_portfolio.csv     ← synthetic sample data (1,200 loans)
├── bank_dashboard_training.ipynb   ← Jupyter notebook, commented step by step
├── dashboard.py                    ← the live Streamlit dashboard app
├── requirements.txt                ← packages needed to run everything
└── README.md                       ← this file
```

**Important:** `data/bank_loan_portfolio.csv` is entirely randomly generated.
It does not contain real NCBA customers, balances, or figures — it's safe to
use for learning and to share for training purposes.

## Recommended order

1. **Start with the notebook** — `bank_dashboard_training.ipynb`. Open it in
   VS Code or Jupyter and run each cell in order. Every step has a markdown
   explanation above it describing what the code does and why.
2. **Then run the dashboard** — `dashboard.py`. It uses the exact same data
   and calculations from the notebook, just wrapped as an interactive web
   app instead of static cells.

## Step 1: Set up

1. Unzip this package into a folder, e.g.
   `C:\Users\Erastus.Kaiba\Projects\bank-dashboard-training`
2. Open that folder in VS Code: **File → Open Folder**.
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
   you installed enables).
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

## Step 3: Run the live dashboard

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
- You'll see KPI cards, sidebar filters, interactive charts, a branch
  performance table, and a CSV download button.
- Press `Ctrl + C` in the terminal to stop the app.

## What "sharing" a dashboard actually means

Running `streamlit run` only starts a server on **your own laptop** —
nothing is uploaded anywhere automatically. What sharing looks like depends
on the audience:

| Method | Who can see it | Good for |
|---|---|---|
| **Network URL** (`http://192.168.x.x:8501`) | Anyone on the same office Wi-Fi/LAN, while your laptop stays on and the app keeps running | Quick demo to a colleague sitting nearby |
| **Streamlit Community Cloud** (share.streamlit.io) | Anyone with the public link, anywhere, anytime | Public/demo data only — never real customer data |
| **Internal company server / VM** | Anyone on NCBA's internal network/VPN | The correct option once you're working with real banking data — needs IT to provision and host it |

For this training package, running it locally and viewing it yourself at
`localhost:8501` is the right way to learn the pattern before thinking about
deployment.

## Common issues

| Problem | Likely fix |
|---|---|
| `streamlit: command not found` | Re-run `pip install -r requirements.txt` in the terminal matching your selected VS Code interpreter |
| Notebook won't open in VS Code | Make sure the **Jupyter** extension is installed (Extensions panel) |
| `FileNotFoundError: data/bank_loan_portfolio.csv` | Make sure your terminal's current folder is the package root (where `dashboard.py` lives), not a subfolder |
| Browser doesn't auto-open | Manually visit `http://localhost:8501` |
