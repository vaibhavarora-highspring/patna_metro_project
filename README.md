🚇 Patna Metro Data Crawling & Route Analysis Project
📌 Project Overview

This project is a hands-on data crawling, extraction, transformation, and analysis system built using Python and SQL.
The objective is to crawl metro-related website data, process and transform it, compute journey-level information (routes, fares, distance, etc.), store it in a database, and generate a final sheet output.

The project demonstrates real-world data engineering practices, including handling incomplete web data using logical computation and documented assumptions.

🎯 Objectives

Crawl metro website data

Clean and transform extracted data

Compute route-based metrics such as:

Stations in between

Distance

Duration

Interchanges

Fare

First & last train timings

Store processed data in a SQL database

Generate a summary output and export it as a sheet (CSV)

Follow modular coding, logging, and error handling practices

🛠️ Technologies Used

Python 3

Requests – website crawling

BeautifulSoup – HTML parsing

SQLite – relational database

CSV – sheet export

Virtual Environment (venv) – dependency isolation

📂 Project Structure
patna_metro_project/
│
├── craawler/
│   └── crawler.py          # Crawls website and saves raw HTML
│
├── parser/
│   └── parser.py           # Parses HTML to inspect available data
│
├── logic/
│   └── route_fare.py       # Core route, distance, fare logic
│
├── database/
│   ├── db.py               # Database creation & insertion
│   └── export_csv.py       # Export SQL data to CSV
│
├── data/
│   └── patna_metro_raw.html
│
├── logs/
│   └── app.log
│
├── main.py                 # Runs full computation & DB insertion
├── requirements.txt
└── README.md

🔄 Data Flow Architecture
Metro Website
      ↓
crawler.py (raw HTML)
      ↓
parser.py (data understanding)
      ↓
route_fare.py (compute routes & fares)
      ↓
SQLite Database
      ↓
CSV Sheet Output

🌐 Website Crawling

The official metro website is crawled using Python.

Raw HTML is stored locally to preserve original data.

This ensures reproducibility and allows offline processing.

File involved:
craawler/crawler.py

🧹 Data Cleaning & Transformation

The website does not provide structured station-to-station fare or route tables.
Hence, the project:

Extracts what is available

Defines official station order based on public route plans

Computes missing journey data logically

This approach reflects real-world data engineering practices.

🧠 Route, Distance & Fare Logic

The core logic computes:

Stations in between – from ordered station list

Distance – calculated using distance per station

Duration – calculated using time per station

Fare – calculated using fare per station

Interchanges – identified when changing lines

First / Last Train – fixed operational timings

Assumptions (Documented)
Parameter	Value
Fare per station	₹10
Distance per station	1.2 km
Time per station	3 minutes
First train	06:00 AM
Last train	10:30 PM

These assumptions are clearly documented and can be replaced with official data when available.

File involved:
logic/route_fare.py

🗄️ Database (Python + SQL)

The project uses SQLite to store computed route summaries.

Tables Created

stations – station master data

routes – basic route data

route_summary – final analytics-ready data

Example SQL Query
SELECT start_station, end_station, fare
FROM route_summary
WHERE start_station = 'Patna Junction'
  AND end_station = 'PMCH';


This returns the computed fare between two stations.