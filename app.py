import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st

st.title("Cloud Risk Governance Model")

file_path = r"C:\Users\dpawe\Cloud_Risk_Governance_Model.xlsx"

try:
  # Load the correct sheet where the risk scores and tiers are logged
  df = pd.read_excel(file_path, sheet_name="Agent_Audit_Log")

  st.subheader("Data Preview: Agent_Audit_Log")
  st.dataframe(df, use_container_width=True)

  # Refresh Button
  if st.button("🔄 Refresh Data from Excel"):
    st.rerun()

  # Chart Section
  if "Resource_ID" in df.columns and "Calculated_Risk_Score" in df.columns:
    st.subheader("📊 Risk Score Distribution Chart")

    fig, ax = plt.subplots(figsize=(8, 4))

    # Color mapping based on risk tier
    colors = [
        "red" if str(tier).lower() == "high" else "orange" if str(tier).lower() == "medium" else "green"
        for tier in df.get("Risk_Tier", ["Low"] * len(df))
    ]

    ax.bar(
        df["Resource_ID"],
        df["Calculated_Risk_Score"],
        color=colors,
        width=0.6,
    )
    ax.set_title("Calculated Risk Scores by Resource", fontweight="bold")
    ax.set_xlabel("Resource ID")
    ax.set_ylabel("Risk Score (0-100)")
    ax.set_ylim(0, 100)
    plt.xticks(rotation=15, ha="right")
    ax.grid(axis="y", linestyle="--", alpha=0.7)

    st.pyplot(fig)
  else:
    st.warning(
        "Could not generate chart: 'Resource_ID' or 'Calculated_Risk_Score'"
        " columns not found."
    )

except Exception as e:
  st.error(f"Error loading data: {e}")