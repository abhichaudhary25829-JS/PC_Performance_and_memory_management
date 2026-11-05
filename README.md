# PC Performance & Memory Management Lab

A Python-based desktop-style web application built with **Streamlit** for monitoring real PC performance and learning core Operating Systems concepts through interactive simulations.

The project combines a **read-only live system monitor** with separate educational labs for memory management, page replacement, CPU scheduling, and disk scheduling.

## Features

### 1. Performance Dashboard
- Dashboard view for system performance and learning-lab activity.
- Live System Mode and Learning Mode are kept clearly separate.
- Performance measurements and simulation results are presented through metric cards and charts.

### 2. Live System Monitor
Uses `psutil` to read available information from the computer, including:
- CPU utilization and frequency (when available).
- RAM usage, available memory, and total memory.
- Swap memory statistics.
- Disk capacity and disk I/O counters.
- Network I/O counters.
- CPU-core utilization.
- Process information and processes using the most memory.

**Safety:** Live monitoring is read-only. The application does not terminate processes, change Windows settings, or deliberately create CPU or memory load. Hardware temperature readings are not guaranteed to be available on every system.

### 3. Memory Management Lab
- Work with a configurable simulated memory space.
- Allocate and deallocate sample processes.
- View memory blocks and allocation status.
- Understand how memory is assigned and released.

### 4. Memory Allocation Algorithms
Compare the commonly taught fixed-block allocation strategies:
- **First Fit** – selects the first available block large enough for the process.
- **Best Fit** – selects the smallest available block that can satisfy the request.
- **Worst Fit** – selects the largest available block.

### 5. Paging Simulator
Experiment with page replacement algorithms:
- FIFO (First In, First Out)
- LRU (Least Recently Used)
- MRU (Most Recently Used)
- Optimal Page Replacement

Explore page references, frame contents, page hits, page faults, and address translation.

### 6. Process and CPU Scheduling Lab
Add simulated processes and compare scheduling behaviour, including:
- FCFS (First Come, First Served)
- SJF (Shortest Job First)
- Priority Scheduling
- Round Robin

View scheduling results, Gantt-chart information, and performance metrics such as waiting and turnaround time.

### 7. Storage and Disk I/O Lab
Simulate disk-head movement using:
- FCFS
- SSTF
- SCAN
- C-SCAN
- LOOK
- C-LOOK

Change the request queue, initial head position, disk size, and scan direction to compare the results.

### 8. Performance Analytics
- Visualize recorded system measurements.
- Compare allocation and paging experiment results.
- Review charts generated from the current application session.

## Technology Stack

| Technology | Purpose |
|---|---|
| Python 3.11+ | Main programming language |
| Streamlit | Interactive application interface |
| psutil | Read-only system and process monitoring |
| Plotly | Interactive charts and visualizations |
| Pandas | Tabular data handling |
| NumPy | Numerical operations |
| ReportLab | PDF/report generation support |

## Project Structure

```text
pc_performance_lab_upgrade/
│
├── app.py
├── asgi_app.py
├── config.py
├── requirements.txt
├── pyproject.toml
├── run.bat
│
├── assets/
│   └── styles.css
│
├── components/
│   ├── charts.py
│   ├── event_log.py
│   ├── header.py
│   ├── memory_visualizer.py
│   ├── metric_cards.py
│   └── sidebar.py
│
├── core/
│   ├── allocation_algorithms.py
│   ├── disk_scheduler.py
│   ├── memory_manager.py
│   ├── paging_engine.py
│   ├── performance_engine.py
│   └── process_scheduler.py
│
├── modules/
│   ├── allocation_lab.py
│   ├── analytics.py
│   ├── dashboard.py
│   ├── live_monitor.py
│   ├── memory_lab.py
│   ├── paging_lab.py
│   ├── process_manager.py
│   └── storage_lab.py
│
├── tests/
│   └── test_engines.py
│
└── utils/
    ├── formatting.py
    └── system_monitor.py
```

## Installation and Setup (Windows 11)

### Prerequisites
- Windows 10/11
- Python 3.11 or later
- pip
- VS Code or another Python IDE (optional)

### 1. Download or clone the repository

If using Git:

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd pc_performance_lab_upgrade
```

Alternatively, download the ZIP file from GitHub and extract it. Open the extracted project folder in VS Code.

### 2. Create a virtual environment

Open the VS Code terminal in the project folder and run:

```powershell
python -m venv .venv
```

### 3. Activate the virtual environment

```powershell
.venv\Scripts\activate
```

If PowerShell blocks activation, use Command Prompt:

```cmd
.venv\Scripts\activate.bat
```

### 4. Install dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 5. Run the application

```bash
python -m streamlit run app.py
```

Streamlit will display a local address in the terminal. Open it in your browser, usually:

```text
http://localhost:8501
```

### Alternative: use the batch file

The project includes `run.bat`. On Windows, you can double-click it or run it from the project terminal:

```cmd
run.bat
```

If the batch file does not work, use the manual installation and run commands above.

## How to Use the Application

1. Start the application and open the Performance Dashboard.
2. Select **Live System Mode** to view actual CPU, RAM, disk, network, and process information.
3. Open **Live System Monitor** for detailed read-only telemetry.
4. Switch to **Learning Mode** to explore the educational simulations.
5. Open the Memory Management Lab and try allocating and releasing sample processes.
6. Compare First Fit, Best Fit, and Worst Fit using the same block and process inputs.
7. Enter a page-reference string and compare FIFO, LRU, MRU, and Optimal page replacement.
8. Add sample processes to the CPU scheduling lab and inspect the scheduling results.
9. Enter disk cylinder requests and compare the disk scheduling algorithms.
10. Open Performance Analytics to review available session charts and comparisons.

## Important: Live Monitoring vs. Simulation

This application has two different kinds of data:

- **Live System Mode:** measurements collected from the actual computer using `psutil`.
- **Learning Mode:** simulated values calculated by the project's algorithms for educational demonstrations.

Simulated memory allocation, paging, CPU scheduling, and disk scheduling do **not** modify the real Windows operating system or consume real system resources to reproduce those algorithms. Do not present simulated values as actual PC measurements.

## Running Tests

The project includes tests for its algorithm engines. From the project root, run:

```bash
python -m pytest
```

If pytest is not installed:

```bash
pip install pytest
python -m pytest
```

## Troubleshooting

**`streamlit` is not recognized**
```bash
python -m pip install -r requirements.txt
python -m streamlit run app.py
```

**ModuleNotFoundError**
- Confirm that the terminal is opened in the folder containing `app.py`.
- Activate `.venv`.
- Install the dependencies again with `pip install -r requirements.txt`.

**Port 8501 is already in use**
```bash
python -m streamlit run app.py --server.port 8502
```
Then open `http://localhost:8502`.

**Live system information is unavailable**
- Some hardware or operating-system metrics may not be exposed by `psutil`.
- Run the application locally on the computer you want to monitor.
- Some process details may be restricted by Windows permissions.

## Project Purpose

The goal of this project is to make Operating Systems concepts easier to understand by combining real-time, read-only PC performance monitoring with hands-on algorithm demonstrations. It can be used as an academic project, a learning tool, and a practical demonstration of Python application development.

## Future Improvements

Possible extensions include:
- Exporting monitoring sessions and simulation results.
- Additional memory-allocation and scheduling strategies.
- More detailed historical performance analysis.
- Improved test coverage and automated validation.
- Optional system-specific hardware sensor integrations.

## Author

**Abhishek Chaudhary**

Computer Science and Engineering Student

---

If you find this project useful, consider giving the repository a ⭐ on GitHub.
