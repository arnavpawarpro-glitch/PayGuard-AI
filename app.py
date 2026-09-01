import streamlit as st
from datetime import datetime

st.set_page_config(
    page_title="PayGuard AI",
    page_icon="🛡️",
    layout="wide"
)

if "transactions" not in st.session_state:
    st.session_state.transactions = []


def generate_ai_explanation(
    amount,
    new_device,
    high_velocity,
    international,
    failed_attempts,
    account_age,
    risk_score
):
    factors = []

    if amount >= 50000:
        factors.append(
            "The transaction amount is significantly high, increasing "
            "the potential financial impact of fraud."
        )

    if new_device:
        factors.append(
            "The payment originated from a new device, which can indicate "
            "an account takeover or unfamiliar access pattern."
        )

    if high_velocity:
        factors.append(
            "A high transaction frequency was detected. Rapid transactions "
            "can be associated with automated or fraudulent activity."
        )

    if international:
        factors.append(
            "The transaction is international, adding geographical risk "
            "to the assessment."
        )

    if failed_attempts >= 3:
        factors.append(
            "Multiple failed payment attempts were recorded before the "
            "transaction, which increases the risk profile."
        )

    if account_age <= 30:
        factors.append(
            "The account is relatively new, providing limited historical "
            "behavior for comparison."
        )

    if risk_score >= 70:
        summary = (
            "AI assessment: Multiple risk indicators are present. "
            "The transaction should undergo additional verification "
            "before completion."
        )
    elif risk_score >= 40:
        summary = (
            "AI assessment: Some unusual indicators are present. "
            "The transaction may be legitimate but should receive "
            "additional monitoring."
        )
    else:
        summary = (
            "AI assessment: The available indicators do not show "
            "significant signs of suspicious activity."
        )

    return summary, factors


# HEADER
st.title("🛡️ PayGuard AI")
st.markdown("### Intelligent Payment Risk Manager")

st.write(
    "Analyze payment transactions using a multi-factor risk engine "
    "and generate an AI-assisted risk explanation."
)

st.divider()


# SIDEBAR
with st.sidebar:
    st.header("🛡️ PayGuard AI")

    st.write("Payment Risk Intelligence")

    st.divider()

    st.write("### Detection Signals")

    st.write("• Transaction amount")
    st.write("• Device behavior")
    st.write("• Transaction velocity")
    st.write("• Geographic risk")
    st.write("• Failed payment attempts")
    st.write("• Account age")

    st.divider()

    st.caption(
        "Prototype for demonstration purposes."
    )


# INPUTS
st.header("💳 Transaction Analysis")

col1, col2 = st.columns(2)

with col1:

    amount = st.number_input(
        "Transaction Amount (₹)",
        min_value=1.0,
        value=5000.0,
        step=500.0
    )

    account_age = st.number_input(
        "Account Age (days)",
        min_value=1,
        value=365
    )

    failed_attempts = st.number_input(
        "Previous Failed Payment Attempts",
        min_value=0,
        max_value=20,
        value=0
    )


with col2:

    new_device = st.checkbox(
        "📱 New Device"
    )

    high_velocity = st.checkbox(
        "⚡ High Transaction Frequency"
    )

    international = st.checkbox(
        "🌍 International Transaction"
    )


st.divider()


# ANALYSIS
if st.button(
    "🔍 Analyze Transaction",
    use_container_width=True
):

    risk_score = 0
    reasons = []

    # Amount
    if amount >= 50000:
        risk_score += 30
        reasons.append("Very high transaction amount")

    elif amount >= 20000:
        risk_score += 15
        reasons.append("Higher-than-normal transaction amount")

    # New device
    if new_device:
        risk_score += 20
        reasons.append("New device detected")

    # Velocity
    if high_velocity:
        risk_score += 25
        reasons.append("High transaction frequency")

    # International
    if international:
        risk_score += 10
        reasons.append("International transaction")

    # Failed payments
    if failed_attempts >= 3:
        risk_score += 15
        reasons.append("Multiple failed payment attempts")

    elif failed_attempts >= 1:
        risk_score += 5
        reasons.append("Previous failed payment attempt")

    # Account age
    if account_age <= 30:
        risk_score += 15
        reasons.append("Very new account")

    risk_score = min(risk_score, 100)


    # RISK LEVEL
    if risk_score >= 70:

        risk_level = "HIGH RISK"

        recommendation = (
            "Temporarily hold the transaction and request "
            "additional verification."
        )

    elif risk_score >= 40:

        risk_level = "MEDIUM RISK"

        recommendation = (
            "Allow the transaction with additional monitoring "
            "and verification."
        )

    else:

        risk_level = "LOW RISK"

        recommendation = (
            "Proceed with standard monitoring."
        )


    # AI EXPLANATION
    ai_summary, ai_factors = generate_ai_explanation(
        amount,
        new_device,
        high_velocity,
        international,
        failed_attempts,
        account_age,
        risk_score
    )


    # SAVE TRANSACTION
    transaction = {
        "time": datetime.now().strftime("%H:%M:%S"),
        "amount": amount,
        "score": risk_score,
        "risk": risk_level
    }

    st.session_state.transactions.insert(
        0,
        transaction
    )

    st.session_state.transactions = (
        st.session_state.transactions[:10]
    )


    # RESULTS
    st.divider()

    st.header("📊 Risk Assessment")

    metric1, metric2, metric3 = st.columns(3)

    with metric1:
        st.metric(
            "Risk Score",
            f"{risk_score}/100"
        )

    with metric2:
        st.metric(
            "Risk Level",
            risk_level
        )

    with metric3:
        st.metric(
            "Transaction",
            f"₹{amount:,.0f}"
        )


    st.progress(
        risk_score / 100
    )


    if risk_score >= 70:
        st.error(
            "🚨 HIGH RISK TRANSACTION DETECTED"
        )

    elif risk_score >= 40:
        st.warning(
            "⚠️ MEDIUM RISK TRANSACTION"
        )

    else:
        st.success(
            "✅ LOW RISK TRANSACTION"
        )


    # AI EXPLANATION
    st.header("🤖 AI Risk Explanation")

    st.info(ai_summary)


    if ai_factors:

        st.subheader(
            "Why was this transaction flagged?"
        )

        for factor in ai_factors:
            st.write(
                f"🔹 {factor}"
            )

    else:

        st.success(
            "No significant suspicious indicators were detected."
        )


    # RISK SIGNALS
    st.subheader("⚠️ Risk Signals")

    if reasons:

        for reason in reasons:
            st.write(
                f"• {reason}"
            )

    else:

        st.write(
            "No major risk signals detected."
        )


    # RECOMMENDATION
    st.subheader(
        "💡 Recommended Action"
    )

    st.info(
        recommendation
    )


# HISTORY
st.divider()

st.header(
    "📜 Recent Transaction Analysis"
)

if st.session_state.transactions:

    for tx in st.session_state.transactions:

        if tx["risk"] == "HIGH RISK":
            icon = "🔴"

        elif tx["risk"] == "MEDIUM RISK":
            icon = "🟡"

        else:
            icon = "🟢"

        st.write(
            f"{icon} **{tx['time']}** — "
            f"₹{tx['amount']:,.0f} — "
            f"Risk Score: **{tx['score']}/100** — "
            f"{tx['risk']}"
        )

else:

    st.caption(
        "No transactions analyzed yet."
    )


st.divider()

st.caption(
    "PayGuard AI • AI-assisted payment risk assessment prototype"
)