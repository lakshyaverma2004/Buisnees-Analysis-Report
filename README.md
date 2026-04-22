<div align="center">

<!--
  ╔══════════════════════════════════════════════════════════════╗
  ║  HERO GIF PLACEHOLDER                                        ║
  ║  Replace the src below with a screen-recording of your       ║
  ║  analysis running end-to-end (e.g. recorded with LICEcap     ║
  ║  or Kap). Recommended size: 900×500px.                       ║
  ╚══════════════════════════════════════════════════════════════╝
-->
<img src="assets/hero_demo.gif" alt="Hotel Bookings Analysis — Live Demo" width="90%" style="border-radius:12px"/>

<br/><br/>

# 🏨 Hotel Bookings Analysis

### *What the data tells us. Why guests cancel. What to do about it.*

<br/>

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Pandas](https://img.shields.io/badge/Pandas-2.x-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org)
[![NumPy](https://img.shields.io/badge/NumPy-1.26-013243?style=for-the-badge&logo=numpy&logoColor=white)](https://numpy.org)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-3.8-11557c?style=for-the-badge)](https://matplotlib.org)
[![Seaborn](https://img.shields.io/badge/Seaborn-0.13-4c72b0?style=for-the-badge)](https://seaborn.pydata.org)
[![PowerPoint](https://img.shields.io/badge/python--pptx-0.6-D04423?style=for-the-badge&logo=microsoftpowerpoint&logoColor=white)](https://python-pptx.readthedocs.io)
[![License: MIT](https://img.shields.io/badge/License-MIT-22c55e?style=for-the-badge)](LICENSE)

<br/>

## ✨ Features

- 🧹 **Automated Data Cleaning** — Parses and coerces all date columns, engineers `lead_time`, `stay_length`, `profit_margin`, and `is_cancelled` flags in one pass
- 📊 **End-to-End EDA Pipeline** — 9-step modular analysis covering status distribution, channel performance, room-type breakdown, seasonal trends, star ratings, and geo-segmentation
- 💡 **Cancellation Root-Cause Analysis** — Pinpoints that 83% of all cancellations share a single trait: missing check-in date — the highest-ROI fix in the dataset
- 📈 **Revenue Intelligence** — Quantifies $166M in potential lost revenue and maps a path to recover ~$37M/year through three targeted interventions
- 🗺 **Channel & Room-Type Heatmaps** — Cross-tab visualisations of cancellation rate by booking channel × star rating and average booking value by channel × room type
- 🌍 **Geo-Segmentation** — City-level cancellation rate ranking across 10 major US cities
- 📅 **Seasonality Modelling** — Monthly cancellation rate trend from Apr-2024 through Apr-2025, identifying summer spikes and the November sweet-spot
- 📑 **Auto-Generated Executive Deck** — `_deck.py` builds a pixel-perfect dark-theme PowerPoint presentation (`python-pptx`) with charts, colour-coded insights, and strategic recommendations, zero manual formatting
- 🔁 **Fully Reproducible** — Single CSV in → cleaned data, all charts, and a `.pptx` board-ready deck out

---

## 🕹 Key Workflows in Action

### 1 · Data Ingestion, Cleaning & KPI Calculation

<!--
  Replace src with a GIF showing the script loading the CSV,
  printing the cleaning summary, and outputting key metrics.
  Recommended tool: asciinema, LICEcap, or Kap.
-->
<div align="center">
  <img src="assets/gif_01_ingestion.gif" alt="Data Ingestion & Cleaning Workflow" width="82%" style="border-radius:8px"/>
  <p><em>CSV loads → date columns parsed → engineered features computed → KPIs printed to console</em></p>
</div>

---

### 2 · EDA Visualisation Suite

<!--
  Replace src with a GIF scrolling through the generated charts:
  booking status pie, monthly cancel trend, channel heatmap, etc.
-->
<div align="center">
  <img src="assets/gif_02_charts.gif" alt="EDA Chart Generation" width="82%" style="border-radius:8px"/>
  <p><em>9-step analysis generates 12+ charts — cancellation anatomy, channel heatmaps, geo maps, and seasonality curves</em></p>
</div>

---

### 3 · Executive Deck Auto-Generation

<!--
  Replace src with a GIF of _deck.py running and the resulting
  .pptx opening in PowerPoint or LibreOffice.
-->
<div align="center">
  <img src="assets/gif_03_deck.gif" alt="PowerPoint Deck Generation" width="82%" style="border-radius:8px"/>
  <p><em><code>python _deck.py</code> → fully formatted dark-theme executive presentation in seconds</em></p>
</div>

---

## 🛠 Tech Stack

<div align="center">

| Layer | Technology | Purpose |
|---|---|---|
| **Language** | [![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)](https://python.org) | Core runtime |
| **Data** | [![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat-square&logo=pandas&logoColor=white)](https://pandas.pydata.org) [![NumPy](https://img.shields.io/badge/NumPy-013243?style=flat-square&logo=numpy&logoColor=white)](https://numpy.org) | Ingestion, cleaning, feature engineering |
| **Visualisation** | [![Matplotlib](https://img.shields.io/badge/Matplotlib-11557c?style=flat-square)](https://matplotlib.org) [![Seaborn](https://img.shields.io/badge/Seaborn-4c72b0?style=flat-square)](https://seaborn.pydata.org) | EDA charts, heatmaps, trend lines |
| **Reporting** | [![python-pptx](https://img.shields.io/badge/python--pptx-D04423?style=flat-square&logo=microsoftpowerpoint&logoColor=white)](https://python-pptx.readthedocs.io) | Auto-generated executive deck |
| **Dataset** | `Hotel_bookings_final.csv` | 30,000 hotel booking transactions |

</div>

---

## 🚀 Getting Started

### Prerequisites

Ensure you have the following installed:

- Python **3.10+**
- `pip` (comes with Python)

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/lakshyaverma2004/Buisnees-Analysis-Report.git
cd Buisnees-Analysis-Report

# 2. (Recommended) Create and activate a virtual environment
python -m venv .venv
source .venv/bin/activate        # macOS / Linux
.venv\Scripts\activate           # Windows

# 3. Install dependencies
pip install pandas numpy matplotlib seaborn python-pptx
```

Make sure `Hotel_bookings_final.csv` is in the project root before running any scripts.

---

## 💻 Usage

### Run the full EDA pipeline

```bash
python hotel_booking_analysis.py
```

This will:
1. Load and clean `Hotel_bookings_final.csv` (30,000 rows)
2. Engineer features: `lead_time`, `stay_length`, `profit_margin`, `is_cancelled`
3. Print key metrics to the console — cancellation rate, avg booking value, total confirmed revenue
4. Run 9-step cross-tab analysis (channel, room type, star rating, seasonality, city)
5. Generate and save all charts to the working directory

### Generate the executive PowerPoint deck

```bash
python _deck.py
```

Outputs a dark-theme `.pptx` file with all slides, charts, and strategic recommendations — ready to present.

### Sample console output

```
══════════════════════════════════════════════════════════════════════
STEP 1: DATA INGESTION & CLEANING
══════════════════════════════════════════════════════════════════════
Dataset loaded: 30,000 rows x 18 columns

Rows with missing check-in date :  5,468
  -> Of those, cancelled         :  5,047
  -> Of those, failed            :    396

══════════════════════════════════════════════════════════════════════
STEP 2: KEY METRICS
══════════════════════════════════════════════════════════════════════
Total Bookings       : 30,000
Confirmed            : 21,660  (72.2%)
Cancelled            :  6,070  (20.2%)
Failed               :  2,260  ( 7.5%)
Avg Booking Value    : $25,329
Total Confirmed Rev  : $548,200,000
```

---

## 📂 Project Structure

```
Buisnees-Analysis-Report/
│
├── hotel_booking_analysis.py   # Main EDA & analysis pipeline
├── _deck.py                    # Executive PowerPoint deck generator
├── Hotel_bookings_final.csv    # Dataset — 30K hotel booking records
├── strategy_pdf.pdf            # Rendered strategy presentation (PDF)
│
└── assets/                     # Charts, GIFs, and 3D model go here
    ├── hero_demo.gif           # ← Replace with your hero GIF
    ├── gif_01_ingestion.gif    # ← Replace with workflow GIF 1
    ├── gif_02_charts.gif       # ← Replace with workflow GIF 2
    ├── gif_03_deck.gif         # ← Replace with workflow GIF 3
    └── dashboard_3d.glb        # ← Optional: 3D model for GitHub viewer
```

---

## 🔑 Key Findings at a Glance

| Finding | Stat | Impact |
|---|---|---|
| Overall cancellation rate | **20.2%** | 6,070 lost bookings |
| Missing check-in → cancellation | **92.3%** | Drives 83% of all cancellations |
| Jul–Aug peak cancel rate | **28.8–30.3%** | 1.5× the annual average |
| Travel Agent cancel rate | **27.9%** | Nearly 1-in-3 bookings lost |
| Web channel avg booking value | **$28,191** | 32% higher than Mobile App |
| Deluxe vs Standard cancel delta | **−7.3 pp** | 16.0% vs 23.3% |
| Estimated recoverable revenue | **~$37M/year** | With 3 targeted interventions |

---

## 🤝 Contributing

Contributions are what make the open-source community such a great place to learn and grow. Any contributions you make are **genuinely appreciated**.

1. **Fork** the repository
2. Create your feature branch: `git checkout -b feature/your-feature-name`
3. Commit your changes: `git commit -m 'Add: brief description of your change'`
4. Push to the branch: `git push origin feature/your-feature-name`
5. Open a **Pull Request** — describe what you changed and why

Please make sure your code follows the existing style and that any new analysis is accompanied by a short explanation of the business insight it surfaces.

---

## 📜 License

Distributed under the **MIT License**. See [`LICENSE`](LICENSE) for full details.

```
MIT License — Copyright (c) 2025 Lakshya Verma
```

---

<div align="center">

Made with 🖤 and a lot of cancelled bookings.

**[⬆ Back to top](#-hotel-bookings-analysis)**

</div>
