import streamlit as st
import pandas as pd
from datetime import datetime
from data import generate_events, SPORTS

# ── Page config ───────────────────────────────────────────
st.set_page_config(
    page_title="BetPro Sportsbook",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── Custom CSS ────────────────────────────────────────────
st.markdown("""
<style>
    /* Base */
    .stApp { background-color: #f0f4f8; color: #1a1a2e; }
    section[data-testid="stSidebar"] { background-color: #1a1a2e; }
    section[data-testid="stSidebar"] * { color: #e0e0e0 !important; }

    /* Event card */
    .event-card {
        background: #ffffff;
        border: 1px solid #dde3ec;
        border-radius: 12px;
        padding: 14px 18px;
        margin-bottom: 12px;
        box-shadow: 0 2px 6px rgba(0,0,0,0.06);
    }

    /* Live badge */
    .live-badge {
        background: #e53935;
        color: white;
        padding: 3px 9px;
        border-radius: 5px;
        font-size: 11px;
        font-weight: bold;
    }

    /* Score */
    .score-box {
        background: #1a1a2e;
        border-radius: 8px;
        padding: 4px 16px;
        font-size: 20px;
        font-weight: bold;
        color: #ffffff;
        text-align: center;
    }

    /* League tag */
    .league-tag {
        color: #1565c0;
        font-size: 12px;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }

    /* Team name */
    .team-name {
        font-size: 15px;
        font-weight: 700;
        color: #1a1a2e;
    }

    /* Odds buttons */
    div[data-testid="stButton"] button {
        background: #e8f0fe;
        border: 1.5px solid #1565c0;
        border-radius: 8px;
        color: #1565c0;
        font-weight: 700;
        font-size: 14px;
        transition: all 0.15s;
    }
    div[data-testid="stButton"] button:hover {
        background: #1565c0;
        color: #ffffff;
    }

    /* Primary button (Place Bets) */
    div[data-testid="stButton"] button[kind="primary"] {
        background: #1565c0;
        color: #ffffff;
        border: none;
        font-size: 15px;
    }

    /* Metrics */
    div[data-testid="stMetricValue"] { color: #1565c0; font-weight: 700; }
    div[data-testid="stMetricLabel"] { color: #555; }

    /* Bet slip container */
    .slip-empty {
        background: #ffffff;
        border: 2px dashed #c5cae9;
        border-radius: 12px;
        padding: 24px;
        text-align: center;
        color: #9e9e9e;
        font-size: 14px;
    }

    /* Divider */
    hr { border-color: #dde3ec; }

    /* Tabs */
    button[data-baseweb="tab"] { color: #1a1a2e !important; font-weight: 600; }
    button[data-baseweb="tab"][aria-selected="true"] {
        border-bottom: 3px solid #1565c0 !important;
        color: #1565c0 !important;
    }

    .profit-positive { color: #2e7d32; font-weight: bold; }
    .profit-negative { color: #c62828; font-weight: bold; }
</style>
""", unsafe_allow_html=True)

# ── Session state ─────────────────────────────────────────
if "betslip" not in st.session_state:
    st.session_state.betslip = []          # list of bet dicts
if "balance" not in st.session_state:
    st.session_state.balance = 1000.0
if "history" not in st.session_state:
    st.session_state.history = []
if "events" not in st.session_state:
    st.session_state.events = generate_events()


def add_to_slip(event_id, market, selection, odds):
    # Remove duplicate selection for same event
    st.session_state.betslip = [
        b for b in st.session_state.betslip if b["event_id"] != event_id
    ]
    st.session_state.betslip.append({
        "event_id": event_id,
        "market": market,
        "selection": selection,
        "odds": odds,
        "stake": 10.0,
    })


def remove_from_slip(event_id):
    st.session_state.betslip = [
        b for b in st.session_state.betslip if b["event_id"] != event_id
    ]


def place_bets():
    total_stake = sum(b["stake"] for b in st.session_state.betslip)
    if total_stake > st.session_state.balance:
        st.error("Insufficient balance!")
        return
    for bet in st.session_state.betslip:
        st.session_state.history.append({
            "time": datetime.now().strftime("%H:%M:%S"),
            "selection": bet["selection"],
            "odds": bet["odds"],
            "stake": bet["stake"],
            "status": "Pending",
            "return": round(bet["stake"] * bet["odds"], 2),
        })
    st.session_state.balance -= total_stake
    st.session_state.betslip = []
    st.success(f"✅ {len(st.session_state.history)} bet(s) placed! Stake: HK${total_stake:.2f}")


# ── Layout ────────────────────────────────────────────────
# Header
col_logo, col_bal, col_dep = st.columns([3, 1, 1])
with col_logo:
    st.markdown("## 🎯 BetPro Sportsbook")
with col_bal:
    st.metric("Balance", f"HK${st.session_state.balance:,.2f}")
with col_dep:
    if st.button("💳 Deposit HK$500"):
        st.session_state.balance += 500
        st.rerun()

st.divider()

# Main columns
main_col, slip_col = st.columns([3, 1])

# ── Sidebar filters ───────────────────────────────────────
with st.sidebar:
    st.markdown("### 🔍 Filter Events")
    sport_filter = st.selectbox("Sport", SPORTS)
    status_filter = st.radio("Status", ["All", "🔴 Live", "Upcoming"])
    st.divider()
    st.markdown("### 📊 Quick Stats")
    live_count = sum(1 for e in st.session_state.events if e["status"] == "live")
    st.metric("Live Events", live_count)
    st.metric("Total Events", len(st.session_state.events))
    if st.button("🔄 Refresh Odds"):
        st.session_state.events = generate_events()
        st.rerun()

# ── Events ────────────────────────────────────────────────
with main_col:
    tabs = st.tabs(["🏟️ Events", "📋 My Bets", "📈 Stats"])

    # ── Tab 1: Events ──
    with tabs[0]:
        events = st.session_state.events

        # Filter
        if sport_filter != "All":
            events = [e for e in events if e["sport"] == sport_filter]
        if status_filter == "🔴 Live":
            events = [e for e in events if e["status"] == "live"]
        elif status_filter == "Upcoming":
            events = [e for e in events if e["status"] == "upcoming"]

        # Group by sport
        sports_in_view = list(dict.fromkeys(e["sport"] for e in events))

        for sport in sports_in_view:
            sport_events = [e for e in events if e["sport"] == sport]
            st.markdown(f"### {sport}")

            for ev in sport_events:
                is_live = ev["status"] == "live"
                live_html = '<span class="live-badge">● LIVE</span>' if is_live else ""
                score_html = ""
                if is_live and "score" in ev:
                    s = ev["score"]
                    if isinstance(s["home"], int):
                        score_html = f'<span class="score-box">{s["home"]} — {s["away"]}</span>'
                    else:
                        score_html = f'<span class="score-box">{s["home"]} | {s["away"]}</span>'

                minute_html = f'<span style="color:#ff9800;font-size:12px">⏱ {ev.get("minute","")}</span>' if is_live else f'<span style="color:#888;font-size:12px">🕐 {ev["date"]} {ev["time"]}</span>'

                st.markdown(f"""
                <div class="event-card">
                    <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:8px">
                        <span class="league-tag">{ev["league"]}</span>
                        <span>{live_html} {minute_html}</span>
                    </div>
                    <div style="display:flex;justify-content:space-between;align-items:center">
                        <span class="team-name">{ev["home"]}</span>
                        {score_html}
                        <span class="team-name">{ev["away"]}</span>
                    </div>
                </div>
                """, unsafe_allow_html=True)

                # Odds buttons
                odds = ev["odds"]
                if "draw" in odds and odds["draw"]:
                    c1, c2, c3 = st.columns(3)
                    cols_map = [
                        (c1, "1 Home", ev["home"], odds["home"]),
                        (c2, "X Draw", "Draw", odds["draw"]),
                        (c3, "2 Away", ev["away"], odds["away"]),
                    ]
                elif "Win" in odds:
                    c1, c2, c3 = st.columns(3)
                    cols_map = [
                        (c1, "Win", "Win", odds["Win"]),
                        (c2, "Place", "Place", odds["Place"]),
                        (c3, "Each Way", "Each Way", odds["Each Way"]),
                    ]
                else:
                    c1, c2 = st.columns(2)
                    cols_map = [
                        (c1, "1 Home", ev["home"], odds["home"]),
                        (c2, "2 Away", ev["away"], odds["away"]),
                    ]

                for col, label, selection, odd in cols_map:
                    with col:
                        in_slip = any(b["event_id"] == ev["id"] and b["selection"] == selection
                                      for b in st.session_state.betslip)
                        btn_label = f"{'✓ ' if in_slip else ''}{label}\n**{odd}**"
                        if st.button(btn_label, key=f"{ev['id']}_{label}", use_container_width=True):
                            add_to_slip(ev["id"], label, selection, odd)
                            st.rerun()

                st.markdown("---")

    # ── Tab 2: My Bets ──
    with tabs[1]:
        if not st.session_state.history:
            st.info("No bets placed yet. Add selections from the Events tab.")
        else:
            df = pd.DataFrame(st.session_state.history)
            # Simulate some results
            import random
            def result_color(status):
                if status == "Won": return "profit-positive"
                if status == "Lost": return "profit-negative"
                return ""

            st.dataframe(df, use_container_width=True, hide_index=True)

            total_staked = df["stake"].sum()
            pending = df[df["status"] == "Pending"]
            st.metric("Total Staked", f"HK${total_staked:.2f}")
            st.metric("Pending Bets", len(pending))

            col1, col2 = st.columns(2)
            with col1:
                if st.button("🎲 Settle All (Random)", use_container_width=True):
                    for i, bet in enumerate(st.session_state.history):
                        if bet["status"] == "Pending":
                            won = random.random() < (1 / bet["odds"])
                            st.session_state.history[i]["status"] = "Won" if won else "Lost"
                            if won:
                                st.session_state.balance += bet["return"]
                    st.rerun()
            with col2:
                if st.button("🗑️ Clear History", use_container_width=True):
                    st.session_state.history = []
                    st.rerun()

    # ── Tab 3: Stats ──
    with tabs[2]:
        if not st.session_state.history:
            st.info("Place some bets to see your stats.")
        else:
            df = pd.DataFrame(st.session_state.history)
            won = df[df["status"] == "Won"]
            lost = df[df["status"] == "Lost"]
            pending = df[df["status"] == "Pending"]

            c1, c2, c3, c4 = st.columns(4)
            c1.metric("Total Bets", len(df))
            c2.metric("Won", len(won), delta=f"+HK${won['return'].sum():.0f}" if len(won) else None)
            c3.metric("Lost", len(lost), delta=f"-HK${lost['stake'].sum():.0f}" if len(lost) else None)
            c4.metric("Pending", len(pending))

            if len(won) + len(lost) > 0:
                win_rate = len(won) / (len(won) + len(lost)) * 100
                profit = won["return"].sum() - df[df["status"] != "Pending"]["stake"].sum()
                st.metric("Win Rate", f"{win_rate:.1f}%")
                st.metric("Net P&L", f"HK${profit:+.2f}",
                          delta="Profit" if profit >= 0 else "Loss")

            if len(df) > 0:
                st.subheader("Bet History Chart")
                chart_data = df[["stake", "return"]].copy()
                chart_data.index = range(1, len(chart_data) + 1)
                st.bar_chart(chart_data)


# ── Bet Slip ──────────────────────────────────────────────
with slip_col:
    slip_count = len(st.session_state.betslip)
    st.markdown(f"### 🎟️ Bet Slip ({slip_count})")

    if not st.session_state.betslip:
        st.markdown("""
        <div class="slip-empty">
            Click any odds button<br>to add to your slip
        </div>
        """, unsafe_allow_html=True)
    else:
        total_stake = 0.0
        total_return = 0.0

        for i, bet in enumerate(st.session_state.betslip):
            with st.container():
                st.markdown(f"**{bet['selection']}**")
                st.markdown(f"<span style='color:#4fc3f7'>Odds: {bet['odds']}</span>", unsafe_allow_html=True)
                stake = st.number_input(
                    "Stake (HK$)", min_value=1.0, max_value=float(st.session_state.balance),
                    value=bet["stake"], step=5.0,
                    key=f"stake_{bet['event_id']}"
                )
                st.session_state.betslip[i]["stake"] = stake
                ret = round(stake * bet["odds"], 2)
                st.markdown(f"<span style='color:#4caf50'>Return: HK${ret:.2f}</span>", unsafe_allow_html=True)
                if st.button("✕ Remove", key=f"rm_{bet['event_id']}", use_container_width=True):
                    remove_from_slip(bet["event_id"])
                    st.rerun()
                total_stake += stake
                total_return += ret
                st.markdown("---")

        st.markdown(f"**Total Stake:** HK${total_stake:.2f}")
        st.markdown(f"**Est. Return:** HK${total_return:.2f}")
        st.markdown(f"**Est. Profit:** HK${total_return - total_stake:.2f}")

        if st.button("✅ Place Bets", use_container_width=True, type="primary"):
            place_bets()
            st.rerun()

        if st.button("🗑️ Clear Slip", use_container_width=True):
            st.session_state.betslip = []
            st.rerun()
