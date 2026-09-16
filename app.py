import streamlit as st
import random
from datetime import datetime

# ============================================================
# PAYGUARD AI
# AI-ASSISTED TRANSACTION RISK & FRAUD DETECTION
# ============================================================

st.set_page_config(
    page_title="PayGuard AI",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================
# SESSION STATE
# ============================================================

if "transactions" not in st.session_state:
    st.session_state.transactions = []

if "page" not in st.session_state:
    st.session_state.page = "Dashboard"


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown("""
<style>

.main {
    background-color: #0b1120;
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 3rem;
}

h1, h2, h3 {
    color: white;
}

p {
    color: #aeb8c7;
}

.section-title {
    font-size: 24px;
    font-weight: 700;
    color: white;
    margin-top: 25px;
    margin-bottom: 15px;
}

.card {
    background: #111827;
    border: 1px solid #263244;
    border-radius: 14px;
    padding: 22px;
    margin-bottom: 15px;
}

.metric-card {
    background: #111827;
    border: 1px solid #263244;
    border-radius: 14px;
    padding: 20px;
    text-align: center;
}

.metric-number {
    font-size: 30px;
    font-weight: 700;
    color: white;
}

.metric-label {
    font-size: 14px;
    color: #9ca3af;
}

.tech-card {
    background: #111827;
    border: 1px solid #263244;
    border-radius: 14px;
    padding: 20px;
    min-height: 150px;
}

.risk-high {
    background: #3b1118;
    border: 1px solid #ef4444;
    padding: 15px;
    border-radius: 10px;
}

.risk-medium {
    background: #3b2a0b;
    border: 1px solid #f59e0b;
    padding: 15px;
    border-radius: 10px;
}

.risk-low {
    background: #0b3323;
    border: 1px solid #22c55e;
    padding: 15px;
    border-radius: 10px;
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.markdown("# 🛡️ PayGuard AI")

    st.caption("AI-Assisted Transaction Risk Detection")

    st.divider()

    page = st.radio(
        "Navigation",
        [
            "Dashboard",
            "Analyze Transaction",
            "Transaction History",
            "Analytics",
            "About"
        ]
    )

    st.session_state.page = page

    st.divider()

    st.markdown("### System Status")

    st.success("Risk Engine Online")

    st.caption("PayGuard AI v1.0")


# ============================================================
# RISK ENGINE
# ============================================================

def calculate_risk(
    amount,
    transaction_count,
    failed_attempts,
    new_device,
    unusual_location,
    unusual_time,
    velocity
):

    score = 0
    signals = []

    # Amount
    if amount >= 100000:
        score += 25
        signals.append("Very high transaction amount")

    elif amount >= 50000:
        score += 18
        signals.append("High transaction amount")

    elif amount >= 20000:
        score += 10
        signals.append("Elevated transaction amount")

    # Failed attempts
    if failed_attempts >= 5:
        score += 25
        signals.append("Multiple failed attempts")

    elif failed_attempts >= 3:
        score += 15
        signals.append("Repeated failed attempts")

    elif failed_attempts >= 1:
        score += 5
        signals.append("Previous failed attempt")

    # Device
    if new_device:
        score += 15
        signals.append("New or unrecognized device")

    # Location
    if unusual_location:
        score += 15
        signals.append("Unusual transaction location")

    # Time
    if unusual_time:
        score += 10
        signals.append("Unusual transaction time")

    # Velocity
    if velocity >= 10:
        score += 20
        signals.append("High transaction velocity")

    elif velocity >= 5:
        score += 10
        signals.append("Elevated transaction velocity")

    # Transaction count
    if transaction_count >= 20:
        score += 10
        signals.append("High transaction frequency")

    score = min(score, 100)

    if score >= 70:
        level = "HIGH"
        action = "Block or manually review transaction."

    elif score >= 40:
        level = "MEDIUM"
        action = "Request additional verification."

    else:
        level = "LOW"
        action = "Allow transaction with normal monitoring."

    return score, level, signals, action


# ============================================================
# DASHBOARD
# ============================================================

if page == "Dashboard":

    st.title("🛡️ PayGuard AI")

    st.markdown(
        "### AI-Assisted Transaction Risk & Fraud Detection"
    )

    st.write(
        "PayGuard AI evaluates multiple transaction signals "
        "and converts them into an interpretable risk score."
    )

    transactions = st.session_state.transactions

    total = len(transactions)

    high = sum(
        1 for t in transactions
        if t["level"] == "HIGH"
    )

    medium = sum(
        1 for t in transactions
        if t["level"] == "MEDIUM"
    )

    low = sum(
        1 for t in transactions
        if t["level"] == "LOW"
    )

    st.markdown(
        '<div class="section-title">Risk Overview</div>',
        unsafe_allow_html=True
    )

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.markdown(
            f"""
            <div class="metric-card">
                <div class="metric-number">{total}</div>
                <div class="metric-label">Transactions</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with c2:
        st.markdown(
            f"""
            <div class="metric-card">
                <div class="metric-number">{high}</div>
                <div class="metric-label">High Risk</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with c3:
        st.markdown(
            f"""
            <div class="metric-card">
                <div class="metric-number">{medium}</div>
                <div class="metric-label">Medium Risk</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with c4:
        st.markdown(
            f"""
            <div class="metric-card">
                <div class="metric-number">{low}</div>
                <div class="metric-label">Low Risk</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown(
        '<div class="section-title">How PayGuard AI Works</div>',
        unsafe_allow_html=True
    )

    st.markdown("""
    <div class="card">

    <p>
    PayGuard AI uses multiple transaction signals instead of
    relying on a single indicator.
    </p>

    <p>
    The system evaluates transaction amount, failed attempts,
    device information, location, transaction time and velocity.
    </p>

    <p>
    These signals are combined into a risk score from 0 to 100.
    The score is then converted into a risk classification and
    recommended action.
    </p>

    </div>
    """, unsafe_allow_html=True)

    st.markdown(
        '<div class="section-title">Detection Architecture</div>',
        unsafe_allow_html=True
    )

    st.code("""
Transaction
     ↓
Risk Signals
     ↓
Multi-Factor Risk Engine
     ↓
Risk Score (0–100)
     ↓
Risk Classification
     ↓
AI-Assisted Explanation
     ↓
Recommended Action
""")

    st.markdown(
        '<div class="section-title">Recent Transactions</div>',
        unsafe_allow_html=True
    )

    if transactions:

        for transaction in transactions[-5:][::-1]:

            if transaction["level"] == "HIGH":
                st.error(
                    f"🔴 HIGH | ₹{transaction['amount']:,.2f} | "
                    f"Risk Score: {transaction['score']}"
                )

            elif transaction["level"] == "MEDIUM":
                st.warning(
                    f"🟠 MEDIUM | ₹{transaction['amount']:,.2f} | "
                    f"Risk Score: {transaction['score']}"
                )

            else:
                st.success(
                    f"🟢 LOW | ₹{transaction['amount']:,.2f} | "
                    f"Risk Score: {transaction['score']}"
                )

    else:

        st.info(
            "No transactions analyzed yet. "
            "Go to 'Analyze Transaction' to test PayGuard AI."
        )


# ============================================================
# ANALYZE TRANSACTION
# ============================================================

elif page == "Analyze Transaction":

    st.title("🔍 Analyze Transaction")

    st.write(
        "Enter transaction characteristics to evaluate fraud risk."
    )

    st.markdown(
        '<div class="section-title">Transaction Details</div>',
        unsafe_allow_html=True
    )

    c1, c2 = st.columns(2)

    with c1:

        amount = st.number_input(
            "Transaction Amount (₹)",
            min_value=1.0,
            value=5000.0,
            step=500.0
        )

        transaction_count = st.number_input(
            "Transactions in Recent Period",
            min_value=1,
            value=2,
            step=1
        )

        failed_attempts = st.number_input(
            "Failed Attempts",
            min_value=0,
            value=0,
            step=1
        )

        velocity = st.number_input(
            "Transactions in Last Hour",
            min_value=1,
            value=1,
            step=1
        )

    with c2:

        new_device = st.checkbox(
            "New / Unrecognized Device"
        )

        unusual_location = st.checkbox(
            "Unusual Location"
        )

        unusual_time = st.checkbox(
            "Unusual Transaction Time"
        )

    st.divider()

    if st.button(
        "🛡️ Analyze Transaction",
        use_container_width=True
    ):

        score, level, signals, action = calculate_risk(
            amount,
            transaction_count,
            failed_attempts,
            new_device,
            unusual_location,
            unusual_time,
            velocity
        )

        transaction = {
            "id": f"TXN-{random.randint(100000, 999999)}",
            "amount": amount,
            "score": score,
            "level": level,
            "signals": signals,
            "action": action,
            "time": datetime.now().strftime(
                "%d-%m-%Y %H:%M:%S"
            )
        }

        st.session_state.transactions.append(transaction)

        st.markdown(
            '<div class="section-title">Risk Assessment</div>',
            unsafe_allow_html=True
        )

        c1, c2, c3 = st.columns(3)

        with c1:
            st.metric(
                "Risk Score",
                f"{score}/100"
            )

        with c2:
            st.metric(
                "Classification",
                level
            )

        with c3:
            st.metric(
                "Transaction",
                transaction["id"]
            )

        if level == "HIGH":

            st.error(
                "🔴 HIGH RISK — Immediate attention recommended."
            )

        elif level == "MEDIUM":

            st.warning(
                "🟠 MEDIUM RISK — Additional verification recommended."
            )

        else:

            st.success(
                "🟢 LOW RISK — Transaction can proceed normally."
            )

        st.markdown(
            '<div class="section-title">Risk Signals</div>',
            unsafe_allow_html=True
        )

        if signals:

            for signal in signals:
                st.write(f"⚠️ {signal}")

        else:

            st.write(
                "No significant risk signals detected."
            )

        st.markdown(
            '<div class="section-title">AI-Assisted Explanation</div>',
            unsafe_allow_html=True
        )

        if level == "HIGH":

            explanation = (
                "The transaction contains multiple risk indicators. "
                "The combination of elevated risk signals has pushed "
                "the overall risk score into the high-risk range."
            )

        elif level == "MEDIUM":

            explanation = (
                "The transaction contains some potentially unusual "
                "characteristics. Additional verification can reduce "
                "the possibility of unauthorized activity."
            )

        else:

            explanation = (
                "The transaction does not currently show significant "
                "risk indicators based on the supplied signals."
            )

        st.info(explanation)

        st.markdown(
            '<div class="section-title">Recommended Action</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            f"""
            <div class="card">
                <h3>{action}</h3>
            </div>
            """,
            unsafe_allow_html=True
        )


# ============================================================
# TRANSACTION HISTORY
# ============================================================

elif page == "Transaction History":

    st.title("📋 Transaction History")

    transactions = st.session_state.transactions

    if not transactions:

        st.info(
            "No transactions available yet."
        )

    else:

        for transaction in transactions[::-1]:

            with st.expander(
                f"{transaction['id']} — "
                f"₹{transaction['amount']:,.2f} — "
                f"{transaction['level']}"
            ):

                st.write(
                    f"**Risk Score:** "
                    f"{transaction['score']}/100"
                )

                st.write(
                    f"**Time:** "
                    f"{transaction['time']}"
                )

                st.write(
                    f"**Recommended Action:** "
                    f"{transaction['action']}"
                )

                if transaction["signals"]:

                    st.write("**Risk Signals:**")

                    for signal in transaction["signals"]:
                        st.write(f"- {signal}")

                else:

                    st.write(
                        "No significant risk signals."
                    )


# ============================================================
# ANALYTICS
# ============================================================

elif page == "Analytics":

    st.title("📊 Risk Analytics")

    transactions = st.session_state.transactions

    if not transactions:

        st.info(
            "Analyze some transactions first to view analytics."
        )

    else:

        total = len(transactions)

        high = sum(
            1 for t in transactions
            if t["level"] == "HIGH"
        )

        medium = sum(
            1 for t in transactions
            if t["level"] == "MEDIUM"
        )

        low = sum(
            1 for t in transactions
            if t["level"] == "LOW"
        )

        average_score = sum(
            t["score"] for t in transactions
        ) / total

        total_value = sum(
            t["amount"] for t in transactions
        )

        c1, c2, c3, c4 = st.columns(4)

        with c1:
            st.metric(
                "Total Transactions",
                total
            )

        with c2:
            st.metric(
                "Average Risk Score",
                f"{average_score:.1f}"
            )

        with c3:
            st.metric(
                "High Risk %",
                f"{(high / total) * 100:.1f}%"
            )

        with c4:
            st.metric(
                "Transaction Value",
                f"₹{total_value:,.0f}"
            )

        st.markdown(
            '<div class="section-title">Risk Distribution</div>',
            unsafe_allow_html=True
        )

        chart_data = {
            "HIGH": high,
            "MEDIUM": medium,
            "LOW": low
        }

        st.bar_chart(chart_data)


# ============================================================
# ABOUT
# ============================================================

elif page == "About":

    st.title("ℹ️ About PayGuard AI")

    st.markdown("""
    <div class="card">

    <h2>What is PayGuard AI?</h2>

    <p>
    PayGuard AI is an AI-assisted transaction risk detection
    prototype designed to identify potentially suspicious
    transactions.
    </p>

    <p>
    Instead of presenting only a numerical score, the system
    explains which signals contributed to the assessment and
    recommends an appropriate next action.
    </p>

    </div>
    """, unsafe_allow_html=True)

    st.markdown(
        '<div class="section-title">Detection Architecture</div>',
        unsafe_allow_html=True
    )

    st.code("""
Transaction
     ↓
Risk Signals
     ↓
Multi-Factor Risk Engine
     ↓
Risk Score (0–100)
     ↓
Risk Classification
     ↓
AI-Assisted Explanation
     ↓
Recommended Action
""")

    st.markdown(
        '<div class="section-title">Technology</div>',
        unsafe_allow_html=True
    )

    c1, c2, c3 = st.columns(3)

    with c1:

        st.markdown("""
        <div class="tech-card">

        <h3>Python</h3>

        <p>
        Core application and transaction-risk logic.
        </p>

        </div>
        """, unsafe_allow_html=True)

    with c2:

        st.markdown("""
        <div class="tech-card">

        <h3>Streamlit</h3>

        <p>
        Interactive dashboard and application interface.
        </p>

        </div>
        """, unsafe_allow_html=True)

    with c3:

        st.markdown("""
        <div class="tech-card">

        <h3>Risk Engine</h3>

        <p>
        Multi-factor transaction risk evaluation.
        </p>

        </div>
        """, unsafe_allow_html=True)

    st.markdown(
        '<div class="section-title">Project Objective</div>',
        unsafe_allow_html=True
    )

    st.write(
        "The objective of PayGuard AI is to make transaction "
        "risk easier to understand by combining multiple "
        "signals into an interpretable risk assessment."
    )

    st.caption(
        "PayGuard AI — Prototype for demonstration purposes."
    )
