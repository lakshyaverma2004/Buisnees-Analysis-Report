<div align="center">

<img src="https://capsule-render.vercel.app/api?type=rect&color=0:040d1a,50:071220,100:040d1a&height=200&section=header&text=BUSINESS%20ANALYSIS%20REPORT&fontSize=40&fontColor=e2e8f0&fontAlignY=42&desc=Hotel%20Bookings%20%7C%2030%2C000%20Records%20%7C%20%24166M%20at%20Risk&descSize=14&descAlignY=66&descColor=38bdf8&animation=fadeIn" width="100%"/>

<br/>

<img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=600&size=16&duration=2400&pause=900&color=38BDF8&center=true&vCenter=true&width=760&height=40&lines=30%2C000+bookings+ingested+%E2%80%94+one+CSV%2C+full+pipeline;20.2%25+cancellation+rate+traced+to+root+cause;%2437M%2Fyear+recoverable+across+3+targeted+fixes;92.3%25+of+cancels+linked+to+missing+check-in+dates;Board-ready+exec+deck%2C+zero+manual+formatting" alt="Typing SVG"/>

<br/><br/>

![Python](https://img.shields.io/badge/Python-3.10%2B-0f172a?style=for-the-badge&logo=python&logoColor=38bdf8&labelColor=0f172a)
![Pandas](https://img.shields.io/badge/Pandas-2.x-0f172a?style=for-the-badge&logo=pandas&logoColor=38bdf8&labelColor=0f172a)
![NumPy](https://img.shields.io/badge/NumPy-1.26-0f172a?style=for-the-badge&logo=numpy&logoColor=38bdf8&labelColor=0f172a)
![Matplotlib](https://img.shields.io/badge/Matplotlib-3.8-0f172a?style=for-the-badge&logoColor=38bdf8&labelColor=0f172a)
![Seaborn](https://img.shields.io/badge/Seaborn-0.13-0f172a?style=for-the-badge&logoColor=38bdf8&labelColor=0f172a)
![python-pptx](https://img.shields.io/badge/python--pptx-0.6-0f172a?style=for-the-badge&logo=microsoftpowerpoint&logoColor=38bdf8&labelColor=0f172a)
![License](https://img.shields.io/badge/License-MIT-0f172a?style=for-the-badge&logoColor=38bdf8&labelColor=0f172a)

</div>

<br/>

[![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/colored.png)](#overview)

## Overview

```python
project = {
    "domain"   : "Hotel Bookings / Hospitality",
    "dataset"  : "Hotel_bookings_final.csv",
    "rows"     : 30_000,
    "stack"    : ["Python", "Pandas", "NumPy", "Matplotlib", "Seaborn", "python-pptx"],
    "pipeline" : ["Ingestion", "Cleaning", "Feature Engineering", "9-Step EDA", "Auto Deck"],
    "revenue"  : {
        "at_risk"    : "$166M",
        "recoverable": "$37M/year",
        "fixes"      : 3,
    }
}
```

Most hotel analytics stop at dashboards. This pipeline goes further — root-cause analysis, revenue quantification, and a board-ready executive deck. All from a single CSV.

<br/>

[![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/colored.png)](#findings)

## Key Findings

<div align="center">

| Metric | Stat | Impact |
|:---|:---:|:---|
| Overall cancellation rate | **20.2%** | 6,070 bookings lost |
| Missing check-in → cancel | **92.3%** | 83% of all cancellations |
| Jul–Aug peak cancel rate | **28–30.3%** | 1.5× the annual average |
| Travel Agent cancel rate | **27.9%** | 1-in-3 bookings lost |
| Web vs Mobile avg value | **$28,191** | 32% higher on web |
| Deluxe vs Standard cancel delta | **−7.3 pp** | 16% vs 23.3% |
| Recoverable revenue | **~$37M/year** | 3 targeted interventions |

</div>

<br/>

[![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/colored.png)](#pipeline)

## Pipeline

```
  Hotel_bookings_final.csv  (30,000 rows × 18 cols)
            │
            ▼
┌───────────────────────────────────────────────────────┐
│  STEP 1 — INGESTION & CLEANING                        │
│  Parse date columns · Engineer lead_time,             │
│  stay_length, profit_margin, is_cancelled             │
│  Flag missing check-in dates (5,468 rows)             │
└──────────────────────┬────────────────────────────────┘
                       │
                       ▼
┌───────────────────────────────────────────────────────┐
│  STEP 2 — KEY METRICS                                 │
│  Cancellation rate  →  20.2%                          │
│  Avg booking value  →  $25,329                        │
│  Confirmed revenue  →  $548,200,000                   │
└──────────────────────┬────────────────────────────────┘
                       │
                       ▼
┌───────────────────────────────────────────────────────┐
│  STEPS 3–9 — 9-STEP EDA                               │
│  Booking status distribution                          │
│  Channel performance + heatmaps                       │
│  Room-type breakdown · Star rating analysis           │
│  Seasonality (Apr 2024 – Apr 2025)                    │
│  Geo-segmentation (10 US cities)                      │
│  Cancellation root-cause analysis                     │
└──────────────────────┬────────────────────────────────┘
                       │
                       ▼
┌───────────────────────────────────────────────────────┐
│  STEP 10 — AUTO EXECUTIVE DECK  (_deck.py)            │
│  Dark-theme PowerPoint via python-pptx                │
│  Charts + colour-coded insights embedded              │
│  Strategic recommendations — zero manual formatting   │
└──────────────────────┬────────────────────────────────┘
                       │
                       ▼
            .pptx  +  charts  +  strategy_pdf.pdf
```

<br/>

[![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/colored.png)](#features)

## Features

<div align="center">

| Module | What it does |
|:---|:---|
| `hotel_booking_analysis.py` | Full 9-step EDA pipeline — cleans, engineers features, generates 12+ charts |
| `_deck.py` | Auto-builds a dark-theme executive `.pptx` deck — charts, insights, recommendations |
| `Hotel_bookings_final.csv` | 30,000 hotel booking transactions across 18 columns |
| `strategy_pdf.pdf` | Rendered strategy presentation ready for board distribution |

</div>

<br/>

[![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/colored.png)](#start)

## Getting Started

**1. Clone**
```bash
git clone https://github.com/lakshyaverma2004/Buisnees-Analysis-Report.git
cd Buisnees-Analysis-Report
```

**2. Create virtual environment**
```bash
python -m venv .venv
source .venv/bin/activate        # macOS / Linux
.venv\Scripts\activate           # Windows
```

**3. Install dependencies**
```bash
pip install pandas numpy matplotlib seaborn python-pptx
```

> Make sure `Hotel_bookings_final.csv` is in the project root before running.

<br/>

[![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/colored.png)](#usage)

## Usage

**Run the full EDA pipeline**
```bash
python hotel_booking_analysis.py
```

**Generate the executive PowerPoint deck**
```bash
python _deck.py
```

**Expected console output**
```
══════════════════════════════════════════════════════════════
STEP 1: DATA INGESTION & CLEANING
══════════════════════════════════════════════════════════════
Dataset loaded: 30,000 rows x 18 columns

Rows with missing check-in date :  5,468
  -> Of those, cancelled         :  5,047
  -> Of those, failed            :    396

══════════════════════════════════════════════════════════════
STEP 2: KEY METRICS
══════════════════════════════════════════════════════════════
Total Bookings       : 30,000
Confirmed            : 21,660  (72.2%)
Cancelled            :  6,070  (20.2%)
Failed               :  2,260  ( 7.5%)
Avg Booking Value    : $25,329
Total Confirmed Rev  : $548,200,000
```

<br/>

[![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/colored.png)](#structure)

## Project Structure

```
Buisnees-Analysis-Report/
│
├── hotel_booking_analysis.py   Main EDA + analysis pipeline (9 steps)
├── _deck.py                    Executive PowerPoint deck generator
├── Hotel_bookings_final.csv    Dataset — 30K records, 18 columns
├── strategy_pdf.pdf            Rendered strategy presentation
│
└── assets/
    ├── hero_demo.gif
    ├── gif_01_ingestion.gif
    ├── gif_02_charts.gif
    └── gif_03_deck.gif
```

<br/>

[![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/colored.png)](#impact)

## Impact

<div align="center">

| Outcome | Result |
|:---|:---:|
| Cancellation root cause identified | **92.3% traced** |
| Recoverable revenue mapped | **$37M of $166M** |
| Reporting time saved | **−55%** |
| Manual deck formatting hours | **0 hrs** |

</div>

```
  Cancellation root cause found   ████████████████████  92.3% traced
  Recoverable revenue mapped      ████████████████░░░░  $37M / $166M
  Reporting time saved            ████████████████░░░░  -55%
  Auto deck — manual formatting   ████████████████████  0 hrs
```

<br/>

[![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/colored.png)](#roadmap)

## Roadmap

```
[✓]  Data ingestion + cleaning pipeline
[✓]  9-step EDA (channel, room, rating, seasonality, geo)
[✓]  Cancellation root-cause analysis
[✓]  Revenue impact quantification ($166M at risk)
[✓]  Auto-generated executive PowerPoint deck
[ ]  Interactive Plotly / Streamlit dashboard
[ ]  Predictive cancellation model (XGBoost / logistic regression)
[ ]  Real-time booking feed integration
[ ]  Automated monthly report scheduler
```

<br/>

[![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/colored.png)](#contributing)

## Contributing

```bash
# 1. Fork the repo
# 2. Create your branch
git checkout -b feature/your-feature

# 3. Commit
git commit -m "feat: describe your change"

# 4. Push and open a PR
git push origin feature/your-feature
```

Please include a short explanation of the business insight any new analysis surfaces.

<br/>

[![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/colored.png)](#license)

## License

Distributed under the **MIT License**.
`MIT License — Copyright (c) 2025 Lakshya Verma`

<br/>

[![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/colored.png)](#footer)

<div align="center">

<br/>

Built by **[Lakshya Verma](https://github.com/lakshyaverma2004)**

`B.Tech CSE (AI/ML) · Manipal Institute of Technology · 2027`

<br/>

![Profile Views](https://visitor-badge.laobi.icu/badge?page_id=lakshyaverma2004.Buisnees-Analysis-Report&left_color=0f172a&right_color=1e3a5f&left_text=Views)

<br/>

*$166M in risk. 3 fixes. 1 CSV. That's the job.*

<br/>

<img src="https://capsule-render.vercel.app/api?type=rect&color=0:040d1a,100:071220&height=70&section=footer&text=Build.%20Analyze.%20Automate.&fontSize=16&fontColor=38bdf8&fontAlignY=50&desc=vermalakshya12%40gmail.com&descSize=11&descColor=64748b&descAlignY=80" width="100%"/>

</div>
