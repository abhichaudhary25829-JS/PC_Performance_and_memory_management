import streamlit as st
import pandas as pd
import plotly.express as px
from components.metric_cards import metrics
from components.charts import line_chart
from components.memory_visualizer import render_memory
from core.performance_engine import health_status
from utils.system_monitor import snapshot, top_processes

def _render_live_dashboard(state):
    data = snapshot()
    history = state.setdefault("history", [])
    history.append({
        "cpu": data["cpu"], "ram": data["ram_percent"],
        "swap": data["swap_percent"], "disk": data.get("disk_percent") or 0,
        "mode": "live", "timestamp": data["timestamp"]
    })
    state["history"] = history[-120:]
    health, reason = health_status(data["cpu"], data["ram_percent"], data["swap_percent"])

    st.success("LIVE TELEMETRY — readings are collected from this laptop using psutil. No simulated values are used in this view.")
    metrics([
        ("CPU utilization", f'{data["cpu"]:.1f}%', f'{data["frequency_mhz"]:.0f} MHz' if data.get("frequency_mhz") else "Frequency unavailable"),
        ("RAM utilization", f'{data["ram_percent"]:.1f}%', f'{data["ram_used_mb"]:.0f} MB used'),
        ("Available RAM", f'{data["ram_available_mb"]:.0f} MB', f'{data["ram_total_mb"]:.0f} MB total'),
        ("Disk usage", f'{data["disk_percent"]:.1f}%' if data.get("disk_percent") is not None else "Unavailable", "System drive"),
        ("System health", health, reason),
    ])
    st.caption(f'Last sample: {data["timestamp"]} · Auto-refresh every 3 seconds · {data["process_count"]} running processes detected')

    left, right = st.columns([1.55, 1])
    with left:
        st.subheader("Live resource history")
        st.plotly_chart(line_chart(state["history"], ["cpu", "ram", "swap"], "CPU, RAM and swap utilization (%)"), use_container_width=True)
    with right:
        st.subheader("RAM composition")
        ram_df = pd.DataFrame({"Memory": ["Used", "Available"], "MB": [data["ram_used_mb"], data["ram_available_mb"]]})
        fig = px.pie(ram_df, names="Memory", values="MB", hole=0.62, template="plotly_dark")
        fig.update_layout(height=310, margin=dict(l=5, r=5, t=25, b=5), paper_bgcolor="#101827")
        st.plotly_chart(fig, use_container_width=True)

    st.subheader("CPU core utilization")
    core_df = pd.DataFrame({"Core": [f"Core {i+1}" for i in range(len(data["per_cpu"]))], "Usage (%)": data["per_cpu"]})
    st.plotly_chart(px.bar(core_df, x="Core", y="Usage (%)", template="plotly_dark", color_discrete_sequence=["#25c7d9"]).update_layout(height=260, margin=dict(l=5,r=5,t=20,b=5), paper_bgcolor="#101827"), use_container_width=True)

    st.subheader("Top memory-consuming processes")
    proc_df = pd.DataFrame(top_processes("memory", 10))
    if not proc_df.empty:
        st.dataframe(proc_df[["PID", "Name", "Status", "Memory %", "CPU %"]], use_container_width=True, hide_index=True)
    else:
        st.info("Process details are unavailable on this system.")
    st.caption("All measurements are read-only. The application does not terminate processes, change system settings, or allocate real memory.")

@st.fragment(run_every="3s")
def _live_dashboard_fragment(state):
    _render_live_dashboard(state)

def _render_learning_dashboard(state):
    mem = state["memory"]
    snap = mem.snapshot()
    processes = state.get("processes", [])
    st.info("LEARNING MODE — all values on this page come from the project's educational simulation engines, not from your laptop hardware.")
    metrics([
        ("Simulated memory", f'{snap["total"]:,} KB', "Configured lab capacity"),
        ("Allocated memory", f'{snap["used"]:,} KB', f'{snap["utilization"]:.1f}% simulated utilization'),
        ("Free memory", f'{snap["free"]:,} KB', "Available in the model"),
        ("External fragmentation", f'{snap["external_fragmentation"]:,} KB', "Free space outside largest block"),
        ("Simulated processes", len(processes), "Created in Process and CPU Lab"),
    ])
    st.subheader("Simulated memory layout")
    render_memory(snap["blocks"], snap["total"])
    a, b = st.columns(2)
    with a:
        st.subheader("Memory allocation status")
        st.progress(snap["utilization"] / 100)
        st.caption(f'{snap["used"]:,} KB allocated out of {snap["total"]:,} KB')
        st.metric("Internal fragmentation", f'{snap["internal_fragmentation"]:,} KB')
    with b:
        st.subheader("Learning laboratories")
        labs = [
            ("Memory Management Lab", "Allocate, release and compact simulated memory."),
            ("Allocation Algorithms", "Compare First Fit, Best Fit and Worst Fit."),
            ("Paging Simulator", "Step through FIFO, LRU, MRU and Optimal."),
            ("Process and CPU Lab", "Run FCFS, SJF, Priority and Round Robin."),
            ("Storage and I/O Lab", "Compare disk scheduling algorithms."),
        ]
        for name, description in labs:
            st.markdown(f"**{name}**")
            st.caption(description)
    st.subheader("How to demonstrate this mode")
    st.markdown("1. Open **Memory Management Lab** and allocate memory to sample processes.\n2. Show free space, fragmentation and compaction.\n3. Compare allocation algorithms using the same workload.\n4. Demonstrate page replacement and CPU scheduling step by step.")
    st.caption("Switch to Live System Mode to display actual CPU, RAM, disk and process telemetry from your laptop.")

def render(state, mode):
    st.subheader("System Command Center")
    if mode == "Live System Mode":
        _live_dashboard_fragment(state)
    else:
        _render_learning_dashboard(state)
