# PC Performance Lab

A Windows 11-friendly Python and Streamlit application for **actual read-only laptop monitoring** and **safe Operating Systems demonstrations**.

## Two clearly separated modes

### Live System Mode
The Performance Dashboard and Live System Monitor collect actual system telemetry using `psutil`: CPU utilization and frequency (when available), RAM usage and availability, swap, disk capacity, disk I/O counters, network counters, CPU-core utilization, and accessible process information. The views refresh automatically every 3 seconds.

Live monitoring is read-only. It does not terminate processes, change Windows settings, allocate real memory, or deliberately create CPU load. Laptop temperature sensors are not guaranteed to be available through `psutil`; unsupported readings are not fabricated.

### Learning Mode
The Performance Dashboard displays the project's simulated memory state and learning-lab progress. Memory allocation, paging, CPU scheduling, and disk scheduling use controlled mathematical models. They do not consume real laptop RAM or CPU for the purpose of simulation.

The **Live System Monitor** always displays real telemetry, regardless of the dashboard mode selector. Other laboratory pages are educational simulations.

## Run locally on Windows 11

Requires Python 3.11 or later.

```powershell
python -m venv .venv
.venv\Scripts\activate
python -m pip install --upgrade pip
pip install -r requirements.txt
python -m streamlit run app.py
```

Open the local URL shown in the terminal (usually `http://localhost:8501`).

## Main modules

- `modules/dashboard.py` — separate Live System and Learning dashboards.
- `modules/live_monitor.py` — detailed live laptop telemetry.
- `modules/memory_lab.py` — simulated memory allocation and deallocation.
- `modules/allocation_lab.py` — First Fit, Best Fit and Worst Fit.
- `modules/paging_lab.py` — FIFO, LRU, MRU and Optimal page replacement.
- `modules/process_manager.py` — CPU scheduling algorithms.
- `modules/storage_lab.py` — disk scheduling demonstrations.
- `modules/analytics.py` — charts and comparisons from session data.
- `core/` — simulation engines.
- `utils/system_monitor.py` — safe, read-only `psutil` telemetry collection.

## Suggested teacher demonstration

1. Open **Live System Monitor** and explain that the displayed CPU, RAM and process readings come from the actual laptop.
2. Switch the dashboard to **Learning Mode**.
3. Open Memory Management Lab and allocate/deallocate sample processes.
4. Demonstrate First Fit, Best Fit and Worst Fit.
5. Demonstrate FIFO, LRU, MRU and Optimal page replacement.
6. Run CPU scheduling and explain the Gantt chart.
7. Compare disk scheduling algorithms.

## Important distinction

Do not describe simulated lab values as actual Windows memory usage. Live telemetry and educational simulations are deliberately separated and labelled throughout the application.
