# Cloud Risk Governance & Automated Telemetry Model

An automated cloud risk governance framework and interactive web dashboard designed to evaluate infrastructure inventory, monitor cost telemetry, assess security postures, and calculate dynamic risk tiers.

##  Overview
Managing cloud environments requires continuous auditing of resource inventory, financial trends, and security compliance. This project integrates Python-based risk analytics with a multi-sheet Excel backend and a live Streamlit web interface to automate risk scoring and provide real-time operational visibility.

---

##  Architecture & Workbook Structure
The underlying data model (`Cloud_Risk_Governance_Model.xlsx`) is structured across four dedicated relational sheets:
1. **`Resource_Inventory`**: Catalogs active cloud resources and metadata.
2. **`weekly_cost-telemetry`**: Tracks week-over-week financial metrics and cost variances.
3. **`security_posture`**: Evaluates security compliance, vulnerability markers, and audit recency.
4. **`agen_sudit_log`**: Houses autonomous agent risk scores, assigned tiers, and remediation logs.

---

##  Key Features
* **Automated Risk Scoring Engine:** Evaluates infrastructure and security metrics in Jupyter Notebooks to compute quantitative risk scores (0–100) and qualitative tiers (*High*, *Medium*, *Low*).
* **Interactive Streamlit Dashboard (`app.py`):** Renders live data tables and dynamic, color-coded risk distribution charts directly on `localhost`.
* **One-Click Refresh:** Built-in UI action hooks allowing instantaneous ingestion of newly calculated Excel telemetry without restarting the server.

---

##  Tech Stack
* **Language:** Python 3.x
* **Data Processing:** Pandas, NumPy
* **Visualization:** Matplotlib, Streamlit native UI components
* **Data Store:** Excel (`.xlsx`)
* **Environment:** Jupyter Notebook & Anaconda Prompt

---

##  Getting Started & Local Execution

### 1. Clone the Repository
```bash
git clone [https://github.com/Drpawhite05/cloud-risk-governance.git](https://github.com/Drpawhite05/cloud-risk-governance.git)
cd cloud-risk-governance