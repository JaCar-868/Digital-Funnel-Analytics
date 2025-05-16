# Digital-Funnel-Analytics
Full-cycle analytics pipeline to ingest raw clickstream data, stitch user sessions, quantify drop-offs in key flows (public site → account opening → mobile/online banking), and surface actionable insights via an interactive Python dashboard.

# Digital Funnel & Adoption Analytics

A full-cycle Python pipeline to ingest clickstream data (Adobe Analytics), model multi-step conversion funnels, monitor instrumentation health, and surface insights in an interactive Plotly Dash dashboard.

## Features

- **Data Ingestion & Cleansing**  
  Fetches Adobe Analytics events, standardizes naming, dedupes sessions.

- **Funnel Modeling**  
  Computes step-by-step conversion rates, time-to-convert, cohort retention.

- **Instrumentation Health Checks**  
  Automates daily monitoring of event volumes; alerts on anomalies.

- **Interactive Dashboard**  
  Drill-down funnel, cohort heatmaps, real-time “heartbeat” charts.

## Setup

1. Clone repository  
   ```bash
   git clone https://github.com/<you>/digital-funnel-analytics.git
   cd digital-funnel-analytics

2. Install dependencies

python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt

3. Create .env with your Adobe Analytics creds:

ADOBE_API_KEY=xxx
ADOBE_API_SECRET=yyy

4. Run

python main.py
