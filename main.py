#!/usr/bin/env python3
"""
Entry point for Digital Funnel & Adoption Analytics
"""
import os
from dotenv import load_dotenv
from modules.ingestion import fetch_and_store_events
from modules.funnel import compute_funnel_metrics
from modules.health_checks import run_instrumentation_checks
from modules.dashboard import launch_dashboard

def main():
    load_dotenv()
    # 1. Ingest & cleanse data
    df = fetch_and_store_events(
        api_key=os.getenv("ADOBE_API_KEY"),
        api_secret=os.getenv("ADOBE_API_SECRET")
    )

    # 2. Compute funnel metrics
    funnel_stats = compute_funnel_metrics(df)

    # 3. Run instrumentation health checks
    run_instrumentation_checks(df)

    # 4. Launch interactive dashboard
    launch_dashboard(df, funnel_stats)

if __name__ == "__main__":
    main()
