import pandas as pd

def run_instrumentation_checks(df: pd.DataFrame):
    """
    Verify expected events volume; alert on missing/duplicate.
    """
    # Example threshold check
    count = df[df.event == "form_submit"].shape[0]
    if count < 1000:
        print(f"⚠️ Low form_submit volume: {count}")
    # TODO: integrate Slack/email alerts
