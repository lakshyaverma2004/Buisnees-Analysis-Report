<div align="center">

```
██████╗ ██╗   ██╗███████╗██╗███╗   ██╗███████╗███████╗███████╗
██╔══██╗██║   ██║██╔════╝██║████╗  ██║██╔════╝██╔════╝██╔════╝
██████╔╝██║   ██║███████╗██║██╔██╗ ██║█████╗  ███████╗███████╗
██╔══██╗██║   ██║╚════██║██║██║╚██╗██║██╔══╝  ╚════██║╚════██║
██████╔╝╚██████╔╝███████║██║██║ ╚████║███████╗███████║███████║
╚═════╝  ╚═════╝ ╚══════╝╚═╝╚═╝  ╚═══╝╚══════╝╚══════╝╚══════╝

       █████╗ ███╗   ██╗ █████╗ ██╗  ██╗   ██╗███████╗██╗███████╗
      ██╔══██╗████╗  ██║██╔══██╗██║  ╚██╗ ██╔╝██╔════╝██║██╔════╝
      ███████║██╔██╗ ██║███████║██║   ╚████╔╝ ███████╗██║███████╗
      ██╔══██║██║╚██╗██║██╔══██║██║    ╚██╔╝  ╚════██║██║╚════██║
      ██║  ██║██║ ╚████║██║  ██║███████╗██║   ███████║██║███████║
      ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚══════╝╚═╝   ╚══════╝╚═╝╚══════╝
```

### `HOTEL BOOKINGS — BUSINESS ANALYSIS REPORT`
#### *30,000 bookings. $166M at risk. 3 fixes to recover $37M/year.*

<br/>

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-2.x-150458?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-1.26-013243?style=for-the-badge&logo=numpy&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-3.8-11557c?style=for-the-badge)
![Seaborn](https://img.shields.io/badge/Seaborn-0.13-4c72b0?style=for-the-badge)
![python-pptx](https://img.shields.io/badge/python--pptx-0.6-D04423?style=for-the-badge&logo=microsoftpowerpoint&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-22c55e?style=for-the-badge)

</div>

---

## ◈ OVERVIEW

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

Most hotel analytics stop at dashboards.
This pipeline goes further — root-cause analysis, revenue quantification,
and a board-ready executive deck. All from a single CSV.

---

## ◈ KEY FINDINGS

```
┌─────────────────────────────────────────────────────────────────┐
│                                                                 │
│   METRIC                          STAT        IMPACT           │
│   ─────────────────────────────────────────────────────────    │
│   Overall cancellation rate       20.2%       6,070 bookings   │
│   Missing check-in → cancel       92.3%       83% of all cancels│
│   Jul–Aug peak cancel rate        28–30.3%    1.5× annual avg  │
│   Travel Agent cancel rate        27.9%       1-in-3 lost      │
│   Web vs Mobile avg value         $28,191     32% higher       │
│   Deluxe vs Standard cancel delta −7.3 pp     16% vs 23.3%     │
│   Recoverable revenue             ~$37M/year  3 interventions  │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## ◈ PIPELINE

```
  Hotel_bookings_final.csv  (30,000 rows × 18 cols)
            │
            ▼
┌───────────────────────────────────────────────────────┐
│  STEP 1 — INGESTION & CLEANING                        │
│  • Parse all date columns                             │
│  • Engineer: lead_time, stay_length,                  │
│    profit_margin, is_cancelled                        │
│  • Flag missing check-in dates (5,468 rows)           │
└──────────────────────┬────────────────────────────────┘
                       │
                       ▼
┌───────────────────────────────────────────────────────┐
│  STEP 2 — KEY METRICS                                 │
│  • Cancellation rate  →  20.2%                        │
│  • Avg booking value  →  $25,329                      │
│  • Confirmed revenue  →  $548,200,000                 │
└──────────────────────┬────────────────────────────────┘
                       │
                       ▼
┌───────────────────────────────────────────────────────┐
│  STEPS 3–9 — 9-STEP EDA                               │
│  • Booking status distribution                        │
│  • Channel performance + heatmaps                     │
│  • Room-type breakdown                                │
│  • Star rating analysis                               │
│  • Seasonality (Apr 2024 – Apr 2025)                  │
│  • Geo-segmentation (10 US cities)                    │
│  • Cancellation root-cause analysis                   │
└──────────────────────┬────────────────────────────────┘
                       │
                       ▼
┌───────────────────────────────────────────────────────┐
│  STEP 10 — AUTO EXECUTIVE DECK  (_deck.py)            │
│  • Dark-theme PowerPoint via python-pptx              │
│  • Charts + colour-coded insights embedded            │
│  • Strategic recommendations — zero manual formatting │
└──────────────────────┬────────────────────────────────┘
                       │
                       ▼
            .pptx  +  charts  +  strategy_pdf.pdf
```

---

## ◈ FEATURES

| Module | What it does |
|---|---|
| `hotel_booking_analysis.py` | Full 9-step EDA pipeline — cleans, engineers features, generates 12+ charts |
| `_deck.py` | Auto-builds a dark-theme executive `.pptx` deck — charts, insights, recommendations |
| `Hotel_bookings_final.csv` | 30,000 hotel booking transactions |
| `strategy_pdf.pdf` | Rendered strategy presentation (PDF export) |

---

## ◈ TECH STACK

```
Language       →  Python 3.10+
Data           →  Pandas 2.x · NumPy 1.26
Visualisation  →  Matplotlib 3.8 · Seaborn 0.13
Reporting      →  python-pptx 0.6 (auto-generated executive deck)
Dataset        →  30,000 hotel booking records (18 columns)
```

---

## ◈ GETTING STARTED

**1. Clone**
```bash
git clone https://github.com/lakshyaverma2004/Buisnees-Analysis-Report.git
cd Buisnees-Analysis-Report
```

**2. Create virtual environment (recommended)**
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

---

## ◈ USAGE

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

---

## ◈ PROJECT STRUCTURE

```
Buisnees-Analysis-Report/
│
├── hotel_booking_analysis.py   ← main EDA + analysis pipeline
├── _deck.py                    ← executive PowerPoint deck generator
├── Hotel_bookings_final.csv    ← dataset (30K records)
├── strategy_pdf.pdf            ← rendered strategy presentation
│
└── assets/
    ├── hero_demo.gif
    ├── gif_01_ingestion.gif
    ├── gif_02_charts.gif
    └── gif_03_deck.gif
```

---

## ◈ IMPACT

```
Before  →  Raw bookings CSV. No visibility into cancellation drivers.
After   →  Root cause identified. Revenue loss quantified. Deck generated.

  Cancellation root cause found   ████████████████████  92.3% traced
  Recoverable revenue mapped      ████████████████░░░░  $37M / $166M
  Reporting time saved            ████████████████░░░░  -55%
  Auto deck — manual work         ████████████████████  0 hrs formatting
```

---

## ◈ ROADMAP

```
[✓] Data ingestion + cleaning pipeline
[✓] 9-step EDA (channel, room, rating, seasonality, geo)
[✓] Cancellation root-cause analysis
[✓] Revenue impact quantification ($166M at risk)
[✓] Auto-generated executive PowerPoint deck
[ ] Interactive Plotly / Streamlit dashboard
[ ] Predictive cancellation model (XGBoost / logistic regression)
[ ] Real-time booking feed integration
[ ] Automated monthly report scheduler
```

---

## ◈ CONTRIBUTING

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

---

## ◈ LICENSE

Distributed under the **MIT License**.
`MIT License — Copyright (c) 2025 Lakshya Verma`

---

<div align="center">

built by **[Lakshya Verma](https://github.com/lakshyaverma2004)**

`B.Tech CSE (AI/ML) · Manipal Institute of Technology`

*$166M in risk. 3 fixes. 1 CSV. That's the job.*

**[⬆ back to top](#)**

</div>
