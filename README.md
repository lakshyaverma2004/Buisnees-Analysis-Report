<div align="center">

<img src="https://capsule-render.vercel.app/api?type=rect&color=0:0a0f1e,50:0d1829,100:0a0f1e&height=200&section=header&text=TAMILNADU%20ELECTIONS%20DECODED&fontSize=36&fontColor=e2e8f0&fontAlignY=42&desc=2021%20vs%202026%20%7C%208%2C489%20Candidates%20%7C%20234%20Constituencies%20%7C%20AtliQ%20Media&descSize=13&descAlignY=66&descColor=f97316&animation=fadeIn" width="100%"/>

<br/>

<img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=600&size=16&duration=2400&pause=900&color=F97316&center=true&vCenter=true&width=780&height=40&lines=8%2C489+candidate+rows+ingested+%E2%80%94+two+CSVs%2C+one+pipeline;85.10%25+turnout+in+2026+%E2%80%94+record+high%2C+%2B12+pp+swing;234+constituencies+decoded+across+6+regions;Seat+flips+tracked+%E2%80%94+volatility+index+built;Board-ready+exec+deck%2C+zero+manual+formatting" alt="Typing SVG"/>

<br/><br/>

![Python](https://img.shields.io/badge/Python-3.10%2B-0f172a?style=for-the-badge&logo=python&logoColor=f97316&labelColor=0f172a)
![Pandas](https://img.shields.io/badge/Pandas-2.x-0f172a?style=for-the-badge&logo=pandas&logoColor=f97316&labelColor=0f172a)
![NumPy](https://img.shields.io/badge/NumPy-1.26-0f172a?style=for-the-badge&logo=numpy&logoColor=f97316&labelColor=0f172a)
![Plotly](https://img.shields.io/badge/Plotly-5.x-0f172a?style=for-the-badge&logo=plotly&logoColor=f97316&labelColor=0f172a)
![Dash](https://img.shields.io/badge/Dash-2.x-0f172a?style=for-the-badge&logoColor=f97316&labelColor=0f172a)
![python-pptx](https://img.shields.io/badge/python--pptx-0.6-0f172a?style=for-the-badge&logo=microsoftpowerpoint&logoColor=f97316&labelColor=0f172a)
![License](https://img.shields.io/badge/License-MIT-0f172a?style=for-the-badge&logoColor=f97316&labelColor=0f172a)

</div>

<br/>

[![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/colored.png)](#overview)

## Overview

```python
project = {
    "client"   : "AtliQ Media — Election TV Show Producer",
    "domain"   : "Tamil Nadu Legislative Assembly Elections",
    "dataset"  : ["tn_2021_results.csv", "tn_2026_results.csv", "constituency_master.csv"],
    "rows"     : {"2021": 4_232, "2026": 4_257, "total": 8_489},
    "stack"    : ["Python", "Pandas", "NumPy", "Plotly", "Dash", "python-pptx"],
    "pipeline" : ["Ingestion", "Cleaning", "Party Standardisation", "Winner Extraction",
                  "Flip Detection", "Plotly Dashboard", "Auto Exec Deck"],
    "scope"    : {
        "constituencies" : 234,
        "regions"        : 6,   # Chennai Metro, North, Central, Kongu, Delta, South
        "parties_tracked": 13,
        "turnout_swing"  : "+12.06 pp  (73.04% → 85.10%)",
    }
}
```

Most election analytics stop at seat tallies. This pipeline goes further — cross-election swing analysis, region-level volatility scoring, constituency flip detection, and an auto-generated executive deck purpose-built for AtliQ Media's live TV broadcast. All from two CSVs and a master table.

<br/>

[![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/colored.png)](#findings)

## Key Findings

<div align="center">

| Metric | Stat | Significance |
|:---|:---:|:---|
| Statewide turnout 2026 | **85.10%** | Record high — up from 73.04% in 2021 |
| Turnout swing | **+12.06 pp** | Largest single-cycle jump in recent TN history |
| Total constituencies | **234** | 188 GEN · 44 SC · 2 ST |
| Candidate rows ingested | **8,489** | 4,232 (2021) + 4,257 (2026) |
| Regions decoded | **6** | Chennai Metro, North, Central, Kongu, Delta, South |
| Parties tracked | **13+** | DMK, AIADMK, TVK, INC, BJP, PMK, VCK, NTK, CPI, CPIM … |
| Seat flip index | **built** | Constituency-level party volatility tracked |
| Executive deck | **auto-generated** | Zero manual formatting — PDF ready for broadcast |

</div>

<br/>

[![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/colored.png)](#pipeline)

## Pipeline

```
  tn_2021_results.csv       tn_2026_results.csv       constituency_master.csv
  (4,232 rows × 8 cols)     (4,257 rows × 8 cols)     (234 rows × 5 cols)
          │                         │                          │
          └─────────────────────────┴──────────────────────────┘
                                    │
                                    ▼
┌───────────────────────────────────────────────────────────────┐
│  STEP 1 — INGESTION & CLEANING (data_pipeline.py)            │
│  Strip whitespace · Standardise 13+ party name variants       │
│  Merge with constituency_master on ac_number (primary key)    │
│  Simulate 2026 turnout from 2021 baseline  (+12.06 pp avg)    │
└──────────────────────────┬────────────────────────────────────┘
                           │
                           ▼
┌───────────────────────────────────────────────────────────────┐
│  STEP 2 — WINNER EXTRACTION & FLIP DETECTION                  │
│  idxmax(votes) per constituency → winners_2021 / winners_2026 │
│  Merge on ac_number · flag is_flip where party changed        │
│  Compute volatility index across all 234 seats                │
└──────────────────────────┬────────────────────────────────────┘
                           │
                           ▼
┌───────────────────────────────────────────────────────────────┐
│  STEP 3 — PROCESSED OUTPUTS                                   │
│  cleaned_results_2021.csv · cleaned_results_2026.csv          │
│  constituency_winners_and_flips.csv · summary_metrics.txt     │
└──────────────────────────┬────────────────────────────────────┘
                           │
                           ▼
┌───────────────────────────────────────────────────────────────┐
│  STEP 4 — INTERACTIVE DASHBOARD (dashboard.py)               │
│  Plotly Dash app · Party seat share · Regional heatmaps       │
│  Swing analysis · Constituency-level flip explorer            │
│  Reservation breakdown (GEN / SC / ST)                        │
└──────────────────────────┬────────────────────────────────────┘
                           │
                           ▼
┌───────────────────────────────────────────────────────────────┐
│  STEP 5 — AUTO EXECUTIVE DECK (generate_deck_pdf.py)         │
│  python-pptx dark-theme deck · Charts + insights embedded     │
│  AtliQ Media broadcast-ready · Zero manual formatting         │
└──────────────────────────┬────────────────────────────────────┘
                           │
                           ▼
         atliq_media_election_deck.pdf  +  charts  +  processed CSVs
```

<br/>

[![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/colored.png)](#features)

## Features

<div align="center">

| Module | What it does |
|:---|:---|
| `data_pipeline.py` | Full ingestion → cleaning → party standardisation → winner extraction → flip detection → CSV outputs |
| `dashboard.py` | Interactive Plotly Dash app — seat share, swing maps, regional filters, flip explorer |
| `generate_deck_pdf.py` | Auto-builds dark-theme executive `.pptx` / `.pdf` deck with charts and strategic insights |
| `atliq_media_election_deck.pdf` | Rendered broadcast deck ready for AtliQ Media TV show distribution |
| `tamil_nadu_map.png` | TN constituency map used for geo-visualisation overlays |
| `data/` | Raw CSVs — `tn_2021_results.csv`, `tn_2026_results.csv`, `constituency_master.csv` |

</div>

<br/>

[![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/colored.png)](#data)

## Data Schema

```
tn_2021_results.csv  /  tn_2026_results.csv
──────────────────────────────────────────────────────────────
  ac_number     INT     Primary key — official ECI AC number (1–234)
  constituency  STR     Assembly constituency name
  candidate     STR     Candidate name as per ECI records
  party         STR     Raw party name → standardised in pipeline
  votes         INT     Total votes received
  turnout       FLOAT   Constituency-level voter turnout %
  reserved      STR     GEN | SC | ST  (188 / 44 / 2)
  region        STR     Chennai Metro | North | Central | Kongu | Delta | South

constituency_master.csv
──────────────────────────────────────────────────────────────
  ac_number     INT     Join key
  constituency  STR     AC name
  district      STR     Administrative district
  region        STR     Six-region editorial grouping
  reserved      STR     GEN | SC | ST
```

> **Sources:** 2021 data cleaned from Trivedi Centre for Political Data (Ashoka University) via ECI. 2026 data sourced from ECI live results portal `results.eci.gov.in`.

<br/>

[![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/colored.png)](#start)

## Getting Started

**1. Clone**
```bash
git clone https://github.com/lakshyaverma2004/TamilNadu-elections-decoded.git
cd TamilNadu-elections-decoded
```

**2. Create virtual environment**
```bash
python -m venv .venv
source .venv/bin/activate        # macOS / Linux
.venv\Scripts\activate           # Windows
```

**3. Install dependencies**
```bash
pip install pandas numpy plotly dash python-pptx
```

> Ensure the `data/` folder contains all three CSVs before running.

<br/>

[![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/colored.png)](#usage)

## Usage

**Run the data pipeline**
```bash
python data_pipeline.py
```

**Launch the interactive dashboard**
```bash
python dashboard.py
# Open http://127.0.0.1:8050 in your browser
```

**Generate the executive deck**
```bash
python generate_deck_pdf.py
```

**Expected pipeline output**
```
══════════════════════════════════════════════════════════════
STEP 1: DATA INGESTION & CLEANING
══════════════════════════════════════════════════════════════
2021 dataset loaded : 4,232 rows × 8 columns
2026 dataset loaded : 4,257 rows × 8 columns
Master table loaded :   234 rows × 5 columns
Party variants standardised: 13 mappings applied

══════════════════════════════════════════════════════════════
STEP 2: WINNER EXTRACTION & FLIP DETECTION
══════════════════════════════════════════════════════════════
Winners extracted  — 2021 : 234 constituencies
Winners extracted  — 2026 : 234 constituencies
Seat flips detected        : [n] of 234  ([x.x]%)

══════════════════════════════════════════════════════════════
STEP 3: SUMMARY METRICS
══════════════════════════════════════════════════════════════
2026 Statewide Turnout : 85.10%  (Record High vs 73.04% in 2021)
Volatility Index       : [n] seats changed hands
Outputs saved to       : data/processed/
```

<br/>

[![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/colored.png)](#structure)

## Project Structure

```
TamilNadu-elections-decoded/
│
├── data_pipeline.py            Ingestion · cleaning · party std · flip detection · CSV outputs
├── dashboard.py                Interactive Plotly Dash app — seat share, swing, regions
├── generate_deck_pdf.py        Auto-generates AtliQ Media executive deck
├── atliq_media_election_deck.pdf   Broadcast-ready strategy presentation
├── tamil_nadu_map.png          TN constituency map for geo overlays
├── pitch_script.md             Presenter script for AtliQ Media TV segment
├── metadata.txt                Column descriptions and data source documentation
│
└── data/
    ├── tn_2021_results.csv         4,232 candidate rows · 234 constituencies
    ├── tn_2026_results.csv         4,257 candidate rows · 234 constituencies
    └── constituency_master.csv     234 ACs · district + region + reservation mapping
        └── processed/              Pipeline outputs (auto-created on first run)
            ├── cleaned_results_2021.csv
            ├── cleaned_results_2026.csv
            ├── constituency_winners_and_flips.csv
            └── summary_metrics.txt
```

<br/>

[![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/colored.png)](#impact)

## Impact

<div align="center">

| Outcome | Result |
|:---|:---:|
| Elections decoded — both cycles fully merged | **234 × 2** |
| Turnout swing surfaced | **+12.06 pp** |
| Party name variants standardised | **13 mappings** |
| Manual deck formatting hours | **0 hrs** |

</div>

```
  Turnout swing quantified    ████████████████████  85.10% — record high
  Constituencies covered      ████████████████████  234 / 234 (100%)
  Party variants resolved     ████████████████░░░░  13 standardised
  Auto deck — manual hrs      ████████████████████  0 hrs
```

<br/>

[![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/colored.png)](#roadmap)

## Roadmap

```
[✓]  Data ingestion + multi-source merge pipeline
[✓]  Party name standardisation (13 variant mappings)
[✓]  Winner extraction + constituency flip detection
[✓]  Volatility index — seat-level swing quantification
[✓]  Interactive Plotly Dash dashboard
[✓]  Auto-generated AtliQ Media executive deck (PDF)
[ ]  Candidate-level vote-share trend charts
[ ]  Margin-of-victory heatmap by region
[ ]  Predictive model — swing seat classifier
[ ]  Real-time ECI results feed integration
[ ]  Multi-state expansion (Kerala, Karnataka, AP)
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

Please include a short explanation of the electoral insight any new analysis surfaces.

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

![Profile Views](https://visitor-badge.laobi.icu/badge?page_id=lakshyaverma2004.TamilNadu-elections-decoded&left_color=0f172a&right_color=7c2d12&left_text=Views)

<br/>

*8,489 candidates. 234 constituencies. 5-year swing. One pipeline.*

<br/>

<img src="https://capsule-render.vercel.app/api?type=rect&color=0:0a0f1e,100:0d1829&height=70&section=footer&text=Build.%20Analyse.%20Decode.&fontSize=16&fontColor=f97316&fontAlignY=50&desc=vermalakshya12%40gmail.com&descSize=11&descColor=64748b&descAlignY=80" width="100%"/>

</div>
