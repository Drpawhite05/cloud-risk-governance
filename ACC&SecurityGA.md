```python
import pandas as pd

# 1. Resource Inventory Data
inventory_data = {
    'Resource_ID': ['i-08a1b2c3d4e5f6g7h', 's3-cust-data-prod-99', 'rds-cluster-auth-02', 'k8s-cluster-core-01', 'i-09f8e7d6c5b4a3210'],
    'Resource_Type': ['EC2 Instance', 'S3 Bucket', 'RDS Database', 'Kubernetes Cluster', 'EC2 Instance'],
    'Service_Vertical': ['Payments API', 'Data Engineering', 'User Authentication', 'Core Infrastructure', 'Marketing Analytics'],
    'Owner_Email': ['dev-lead-payments@enterprise.com', 'data-eng-team@enterprise.com', 'sec-ops-admin@enterprise.com', 'platform-eng@enterprise.com', 'marketing-tech@enterprise.com'],
    'Budget_Allocation': [1200.00, 500.00, 2500.00, 5000.00, 800.00]
}
df_inventory = pd.DataFrame(inventory_data)

# 2. Weekly Cost Telemetry Data
telemetry_data = {
    'Resource_ID': ['i-08a1b2c3d4e5f6g7h', 's3-cust-data-prod-99', 'rds-cluster-auth-02', 'k8s-cluster-core-01', 'i-09f8e7d6c5b4a3210'],
    'Week_Ending_Date': ['2026-10-10', '2026-10-10', '2026-10-10', '2026-10-10', '2026-10-10'],
    'Current_Weekly_Cost': [1150.00, 850.00, 2400.00, 4900.00, 1450.00],
    'Previous_Weekly_Cost': [1100.00, 450.00, 2450.00, 4800.00, 750.00]
}
df_telemetry = pd.DataFrame(telemetry_data)

# 3. Security Posture Data
security_data = {
    'Resource_ID': ['i-08a1b2c3d4e5f6g7h', 's3-cust-data-prod-99', 'rds-cluster-auth-02', 'k8s-cluster-core-01', 'i-09f8e7d6c5b4a3210'],
    'Encryption_Status': ['Encrypted', 'Unencrypted', 'Encrypted', 'Encrypted', 'Unencrypted'],
    'Public_Access_Flag': [False, True, False, False, True],
    'Days_Since_Last_Audit': [12, 45, 5, 8, 90],
    'Orphaned_Status': ['Active', 'Active', 'Active', 'Active', 'Orphaned/Idle']
}
df_security = pd.DataFrame(security_data)

# 4. Empty Agent Audit Log Template
audit_log_data = {
    'Log_ID': [None],
    'Resource_ID': [None],
    'Timestamp': [None],
    'Calculated_Risk_Score': [None],
    'Risk_Tier': [None],
    'Agent_Action_Taken': [None],
    'Resolution_Status': [None]
}
df_audit = pd.DataFrame(audit_log_data)

# Write all four dataframes to separate sheets in a single Excel workbook
with pd.ExcelWriter('Cloud_Risk_Governance_Model.xlsx', engine='openpyxl') as writer:
    df_inventory.to_excel(writer, sheet_name='Resource_Inventory', index=False)
    df_telemetry.to_excel(writer, sheet_name='Weekly_Cost_Telemetry', index=False)
    df_security.to_excel(writer, sheet_name='Security_Posture', index=False)
    df_audit.to_excel(writer, sheet_name='Agent_Audit_Log', index=False)

print("Excel workbook 'Cloud_Risk_Governance_Model.xlsx' created successfully!")
```

    Excel workbook 'Cloud_Risk_Governance_Model.xlsx' created successfully!
    


```python
import pandas as pd
from datetime import datetime

# 1. Load the data from your workbook
file_path = 'Cloud_Risk_Governance_Model.xlsx'
df_inventory = pd.read_excel(file_path, sheet_name='Resource_Inventory')
df_telemetry = pd.read_excel(file_path, sheet_name='Weekly_Cost_Telemetry')
df_security = pd.read_excel(file_path, sheet_name='Security_Posture')

# 2. Merge data into a unified dataframe for evaluation
df_merged = df_inventory.merge(df_telemetry, on='Resource_ID').merge(df_security, on='Resource_ID')

# 3. Define the Agentic Evaluation Logic
audit_logs = []
timestamp_str = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
log_counter = 1

for index, row in df_merged.iterrows():
    # Calculate Cost Variance Percentage
    cost_diff = row['Current_Weekly_Cost'] - row['Previous_Weekly_Cost']
    variance_pct = (cost_diff / row['Previous_Weekly_Cost']) * 100
    
    # Initialize risk score calculation (0 to 100 scale)
    risk_score = 0
    
    # Rule 1: Financial Anomaly (Cost spike > 30%)
    if variance_pct > 30:
        risk_score += 40
        
    # Rule 2: Security & Posture Vulnerabilities
    if row['Encryption_Status'] == 'Unencrypted':
        risk_score += 30
    if row['Public_Access_Flag'] == True:
        risk_score += 20
    if row['Orphaned_Status'] == 'Orphaned/Idle':
        risk_score += 10
        
    # Determine Risk Tier and Action based on Score
    if risk_score >= 60:
        risk_tier = 'High'
        action_taken = 'Automated Slack Alert Sent + Compliance Flag Logged'
        resolution_status = 'Open - Pending Review'
    elif risk_score >= 30:
        risk_tier = 'Medium'
        action_taken = 'Weekly Cost Variance Flagged for Owner'
        resolution_status = 'Under Review'
    else:
        risk_tier = 'Low'
        action_taken = 'Routine Audit Cleared'
        resolution_status = 'Resolved'
        
    # Append to our audit log structure
    audit_logs.append({
        'Log_ID': f'LOG-2026-{log_counter:03d}',
        'Resource_ID': row['Resource_ID'],
        'Timestamp': timestamp_str,
        'Calculated_Risk_Score': risk_score,
        'Risk_Tier': risk_tier,
        'Agent_Action_Taken': action_taken,
        'Resolution_Status': resolution_status
    })
    log_counter += 1

df_new_audit = pd.DataFrame(audit_logs)

# 4. Write back to the Excel file while preserving all 4 sheets
with pd.ExcelWriter(file_path, engine='openpyxl', mode='w') as writer:
    df_inventory.to_excel(writer, sheet_name='Resource_Inventory', index=False)
    df_telemetry.to_excel(writer, sheet_name='Weekly_Cost_Telemetry', index=False)
    df_security.to_excel(writer, sheet_name='Security_Posture', index=False)
    df_new_audit.to_excel(writer, sheet_name='Agent_Audit_Log', index=False)

print("Agentic audit cycle completed! 'Agent_Audit_Log' sheet has been updated.")
```

    Agentic audit cycle completed! 'Agent_Audit_Log' sheet has been updated.
    


```python
import os

print(
    "Actual saved location:",
    os.path.abspath("Cloud_Risk_Governance_Model.xlsx"),
)
```

    Actual saved location: C:\Users\dpawe\Cloud_Risk_Governance_Model.xlsx
    


```python
import pandas as pd
import streamlit as st

st.title("🛡️ Autonomous Cloud Cost & Security Risk Agent")
st.write(
    "This dashboard monitors cloud telemetry, evaluates risk rules, and logs"
    " automated remediation."
)

# Load data from your local Excel file
file_path = "Cloud_Risk_Governance_Model.xlsx"

try:
  df_inventory = pd.read_excel(file_path, sheet_name="Resource_Inventory")
  df_telemetry = pd.read_excel(file_path, sheet_name="Weekly_Cost_Telemetry")
  df_security = pd.read_excel(file_path, sheet_name="Security_Posture")
  df_audit = pd.read_excel(file_path, sheet_name="Agent_Audit_Log")

  # Sidebar configuration
  st.sidebar.header("Agent Controls")
  if st.sidebar.button("Run Autonomous Risk Audit"):
    st.success("Audit executed successfully! Logs updated.")
    # (Your agent loop script would trigger here)

  # Main Dashboard Tabs
  tab1, tab2, tab3 = st.tabs(
      ["Executive Audit Log", "Resource Inventory", "Cost & Security Telemetry"]
  )

  with tab1:
    st.subheader("Live Agent Audit & Remediation Log")
    st.dataframe(df_audit, use_container_width=True)

  with tab2:
    st.subheader("Cloud Resource Inventory")
    st.dataframe(df_inventory, use_container_width=True)

  with tab3:
    st.subheader("Telemetry & Security Posture")
    col1, col2 = st.columns(2)
    with col1:
      st.write("**Cost Telemetry**")
      st.dataframe(df_telemetry, use_container_width=True)
    with col2:
      st.write("**Security Posture**")
      st.dataframe(df_security, use_container_width=True)

except Exception as e:
  st.error(f"Could not load the Excel file. Error: {e}")
```

    2026-10-10 12:14:52.127 
      [33m[1mWarning:[0m to view this Streamlit app on a browser, run it with the following
      command:
    
        streamlit run C:\Users\dpawe\anaconda3\Lib\site-packages\ipykernel_launcher.py [ARGUMENTS]
    


```python
file_path = r"C:\Users\dpawe\Cloud_Risk_Governance_Model.xlsx"
```


```python
import pandas as pd

excel_path = r"C:\Users\dpawe\Cloud_Risk_Governance_Model.xlsx"

# Load sheets
resource_inventory = pd.read_excel(excel_path, sheet_name="Resource_Inventory")
weekly_cost = pd.read_excel(excel_path, sheet_name="Weekly_Cost_Telemetry")
security_posture = pd.read_excel(excel_path, sheet_name="Security_Posture")
audit_log = pd.read_excel(excel_path, sheet_name="Agent_Audit_Log")

# --- Risk scoring logic ---
weekly_cost["Variance"] = weekly_cost["Current_Weekly_Cost"] - weekly_cost["Previous_Weekly_Cost"]
weekly_cost["RiskScore"] = weekly_cost["Variance"].abs()

def assign_tier(score):
    if score >= 80:
        return "High"
    elif score >= 40:
        return "Medium"
    return "Low"

weekly_cost["Risk_Tier"] = weekly_cost["RiskScore"].apply(assign_tier)

# --- Create new audit log entry for each resource ---
new_entries = []

for idx, row in weekly_cost.iterrows():
    resource_id_value = row["Resource_ID"]
    risk_score_value = row["RiskScore"]
    risk_tier_value = row["Risk_Tier"]

    # Generate correct Log_ID format
    next_id = len(audit_log) + len(new_entries) + 1
    log_id_value = f"LOG-2026-{next_id:03d}"

    # Determine agent action
    if risk_tier_value == "High":
        agent_action = "Automated Slack Alert Sent + Compliance Flag Logged"
        resolution_status = "Open - Pending Review"
    else:
        agent_action = "Routine Audit Cleared"
        resolution_status = "Resolved"

    new_entry = {
        "Log_ID": log_id_value,
        "Resource_ID": resource_id_value,
        "Timestamp": pd.Timestamp.now(),
        "Calculated_Risk_Score": risk_score_value,
        "Risk_Tier": risk_tier_value,
        "Agent_Action_Taken": agent_action,
        "Resolution_Status": resolution_status
    }

    new_entries.append(new_entry)

# Append new entries using concat (append removed in pandas 2.0+)
audit_log = pd.concat([audit_log, pd.DataFrame(new_entries)], ignore_index=True)

# --- Write updated sheets back to Excel ---
with pd.ExcelWriter(excel_path, mode="a", if_sheet_exists="replace") as writer:
    weekly_cost.to_excel(writer, sheet_name="Weekly_Cost_Telemetry", index=False)
    audit_log.to_excel(writer, sheet_name="Agent_Audit_Log", index=False)

print("Risk scoring complete. Excel updated.")


```

    Risk scoring complete. Excel updated.
    


```python
import os
print(os.access(r"C:\Users\dpawe\Cloud_Risk_Governance_Model.xlsx", os.W_OK))

```

    True
    


```python
st.title("Cloud Governance Risk Dashboard")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Risk Scores")
    st.bar_chart(weekly_cost.set_index("Resource_ID")["RiskScore"])

with col2:
    st.subheader("Risk Tier Distribution")
    st.write(weekly_cost["Risk_Tier"].value_counts())

```


```python
import altair as alt
import pandas as pd
import streamlit as st

excel_path = r"C:\Users\dpawe\Cloud_Risk_Governance_Model.xlsx"

weekly_cost = pd.read_excel(excel_path, sheet_name="Weekly_Cost_Telemetry")

st.header("📊 Risk Score by Resource (Color‑Coded)")

risk_chart = alt.Chart(weekly_cost).mark_bar().encode(
    x=alt.X("Resource_ID:N", title="Resource"),
    y=alt.Y("RiskScore:Q", title="Risk Score"),
    color=alt.Color(
        "Risk_Tier:N",
        scale=alt.Scale(
            domain=["High", "Medium", "Low"],
            range=["red", "orange", "green"]
        ),
        title="Risk Tier"
    ),
    tooltip=["Resource_ID", "RiskScore", "Risk_Tier"]
)

st.altair_chart(risk_chart, use_container_width=True)

```




    DeltaGenerator()




```python
security_posture = pd.read_excel(excel_path, sheet_name="Security_Posture")

# Identify violations
security_posture["Violation"] = (
    (security_posture["Encryption_Status"] == "Unencrypted") |
    (security_posture["Public_Access_Flag"] == True) |
    (security_posture["Orphaned_Status"] != "Active")
)

violations = security_posture[security_posture["Violation"] == True]

st.header("🔐 Security Posture Violations")

sec_chart = alt.Chart(violations).mark_bar(color="red").encode(
    x=alt.X("Resource_ID:N", title="Resource"),
    y=alt.Y("Days_Since_Last_Audit:Q", title="Days Since Last Audit"),
    tooltip=[
        "Resource_ID",
        "Encryption_Status",
        "Public_Access_Flag",
        "Orphaned_Status",
        "Days_Since_Last_Audit"
    ]
)

st.altair_chart(sec_chart, use_container_width=True)

```




    DeltaGenerator()




```python
%matplotlib inline
import matplotlib.pyplot as plt
import pandas as pd

# 1. Load your Audit Log sheet where the risk scores were calculated
file_path = r"C:\Users\dpawe\Cloud_Risk_Governance_Model.xlsx"
df_audit = pd.read_excel(file_path, sheet_name="Agent_Audit_Log")

# 2. Set up the figure size
plt.figure(figsize=(10, 5))

# 3. Create a bar chart for Risk Scores by Resource ID
colors = [
    "red" if tier == "High" else "orange" if tier == "Medium" else "green"
    for tier in df_audit["Risk_Tier"]
]
plt.bar(
    df_audit["Resource_ID"],
    df_audit["Calculated_Risk_Score"],
    color=colors,
    width=0.6,
)

# 4. Add titles and labels
plt.title(
    "Autonomous Risk Agent: Calculated Risk Scores by Resource",
    fontsize=14,
    fontweight="bold",
)
plt.xlabel("Resource ID", fontsize=11)
plt.ylabel("Risk Score (0-100)", fontsize=11)
plt.ylim(0, 100)
plt.xticks(rotation=15, ha="right")
plt.grid(axis="y", linestyle="--", alpha=0.7)

# 5. Display the chart right below your cell
plt.tight_layout()
plt.show()
```


    
![png](output_10_0.png)
    



    
![png](output_10_1.png)
    



```python
%matplotlib inline
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Load telemetry data
file_path = r"C:\Users\dpawe\Cloud_Risk_Governance_Model.xlsx"
df_telemetry = pd.read_excel(file_path, sheet_name="Weekly_Cost_Telemetry")

x = np.arange(len(df_telemetry["Resource_ID"]))
width = 0.35

plt.figure(figsize=(10, 5))
plt.bar(
    x - width / 2,
    df_telemetry["Previous_Weekly_Cost"],
    width,
    label="Previous Week",
    color="skyblue",
)
plt.bar(
    x + width / 2,
    df_telemetry["Current_Weekly_Cost"],
    width,
    label="Current Week",
    color="salmon",
)

plt.title(
    "Week-over-Week Cloud Cost Comparison by Resource",
    fontsize=14,
    fontweight="bold",
)
plt.xlabel("Resource ID", fontsize=11)
plt.ylabel("Cost ($)", fontsize=11)
plt.xticks(x, df_telemetry["Resource_ID"], rotation=15, ha="right")
plt.legend()
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.tight_layout()
plt.show()
```


    
![png](output_11_0.png)
    



```python
%matplotlib inline
import matplotlib.pyplot as plt
import pandas as pd

file_path = r"C:\Users\dpawe\Cloud_Risk_Governance_Model.xlsx"
df_audit = pd.read_excel(file_path, sheet_name="Agent_Audit_Log")

# Count occurrences of each risk tier
tier_counts = df_audit["Risk_Tier"].value_counts()

colors = {"High": "red", "Medium": "orange", "Low": "green"}
chart_colors = [
    colors.get(tier, "blue") for tier in tier_counts.index
]  # Matches colors safely

plt.figure(figsize=(6, 6))
plt.pie(
    tier_counts,
    labels=tier_counts.index,
    autopct="%1.1f%%",
    colors=chart_colors,
    startangle=140,
    wedgeprops={"edgecolor": "black"},
)
plt.title(
    "Proportion of Resources by Risk Tier", fontsize=14, fontweight="bold"
)
plt.tight_layout()
plt.show()
```


    
![png](output_12_0.png)
    



```python
%matplotlib inline
import matplotlib.pyplot as plt
import pandas as pd

file_path = r"C:\Users\dpawe\Cloud_Risk_Governance_Model.xlsx"
df_merged = pd.read_excel(file_path, sheet_name="Resource_Inventory").merge(
    pd.read_excel(file_path, sheet_name="Security_Posture"), on="Resource_ID"
).merge(pd.read_excel(file_path, sheet_name="Agent_Audit_Log"), on="Resource_ID")

plt.figure(figsize=(9, 5))
plt.scatter(
    df_merged["Days_Since_Last_Audit"],
    df_merged["Calculated_Risk_Score"],
    color="purple",
    s=100,
    edgecolors="black",
)

for i, row in df_merged.iterrows():
  plt.annotate(
      row["Resource_ID"],
      (row["Days_Since_Last_Audit"], row["Calculated_Risk_Score"]),
      textcoords="offset points",
      xytext=(0, 10),
      ha="center",
      fontsize=9,
  )

plt.title(
    "Risk Score vs. Days Since Last Security Audit",
    fontsize=14,
    fontweight="bold",
)
plt.xlabel("Days Since Last Audit", fontsize=11)
plt.ylabel("Calculated Risk Score", fontsize=11)
plt.grid(True, linestyle="--", alpha=0.7)
plt.tight_layout()
plt.show()
```


    
![png](output_13_0.png)
    



```python

```
