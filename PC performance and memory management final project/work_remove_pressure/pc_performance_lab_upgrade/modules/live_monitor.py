import streamlit as st
import pandas as pd
import plotly.express as px
from utils.system_monitor import snapshot, partitions, top_processes
from components.metric_cards import metrics

def _render_live_measurements():
    d = snapshot()
    st.success("LIVE SYSTEM MONITOR — actual read-only measurements from this laptop.")
    metrics([
        ("CPU utilization", f'{d["cpu"]:.1f}%', f'{d["frequency_mhz"]:.0f} MHz' if d.get("frequency_mhz") else "Frequency unavailable"),
        ("RAM utilization", f'{d["ram_percent"]:.1f}%', f'{d["ram_used_mb"]:.0f} MB used'),
        ("Available RAM", f'{d["ram_available_mb"]:.0f} MB', f'{d["ram_total_mb"]:.0f} MB total'),
        ("Swap utilization", f'{d["swap_percent"]:.1f}%', f'{d["swap_used_mb"]:.0f} MB used'),
        ("Running processes", d["process_count"], "Processes detected by psutil"),
    ])
    st.caption(f'Last updated: {d["timestamp"]} · Refreshes automatically every 3 seconds')
    left, right = st.columns(2)
    with left:
        st.subheader("CPU usage per core")
        cpu_df = pd.DataFrame({"CPU core": [f"Core {i+1}" for i in range(len(d["per_cpu"]))], "Usage (%)": d["per_cpu"]})
        st.plotly_chart(px.bar(cpu_df, x="CPU core", y="Usage (%)", template="plotly_dark", color_discrete_sequence=["#25c7d9"]).update_layout(height=300, paper_bgcolor="#101827"), use_container_width=True)
    with right:
        st.subheader("Disk partitions")
        parts = pd.DataFrame(partitions())
        if not parts.empty:
            st.dataframe(parts, use_container_width=True, hide_index=True)
        else:
            st.info("No accessible disk partitions were returned by the operating system.")
    st.subheader("Disk and network I/O counters")
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Disk read", f'{d["disk_read_mb"]:.1f} MB' if d.get("disk_read_mb") is not None else "Unavailable")
    c2.metric("Disk written", f'{d["disk_write_mb"]:.1f} MB' if d.get("disk_write_mb") is not None else "Unavailable")
    c3.metric("Network sent", f'{d["net_sent_mb"]:.1f} MB' if d.get("net_sent_mb") is not None else "Unavailable")
    c4.metric("Network received", f'{d["net_recv_mb"]:.1f} MB' if d.get("net_recv_mb") is not None else "Unavailable")
    left, right = st.columns(2)
    with left:
        st.subheader("Top processes by CPU")
        st.dataframe(pd.DataFrame(top_processes("cpu", 10)), use_container_width=True, hide_index=True)
    with right:
        st.subheader("Top processes by memory")
        st.dataframe(pd.DataFrame(top_processes("memory", 10)), use_container_width=True, hide_index=True)
    st.caption("Read-only monitoring: this page never ends processes or changes Windows settings. CPU temperature is shown only if a supported sensor source is available; psutil alone does not reliably expose laptop temperatures on Windows.")

@st.fragment(run_every="3s")
def _live_monitor_fragment():
    _render_live_measurements()

def render(state):
    _live_monitor_fragment()
