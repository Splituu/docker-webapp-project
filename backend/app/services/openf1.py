import requests

def get_top10_results(race_name: str):
    races = requests.get("https://api.openf1.org/v1/meetings?year=2025").json()

    meeting_key = None
    for race in races:
        if race["meeting_name"] == race_name:
            meeting_key = race["meeting_key"]
            break
    
    if not meeting_key:
        return [] 

    sessions = requests.get(f"https://api.openf1.org/v1/sessions?meeting_key={meeting_key}").json()
    session_key = None
    for session in sessions:
        if session["session_name"] == "Race":
            session_key = session["session_key"]
            break
    if not session_key:
        return []

    results = requests.get(
        f"https://api.openf1.org/v1/session_result?session_key={session_key}&position<=10"
    ).json()

    top10 = []
    for r in results:
        driver_number = r["driver_number"]
        driver_info = requests.get(
            f"https://api.openf1.org/v1/drivers?driver_number={driver_number}&session_key={session_key}"
        ).json()
        if driver_info and len(driver_info) > 0:
            full_name = driver_info[0].get("full_name", "Unknown")
        else:
            full_name = "Unknown"

        top10.append({
            "position": r["position"],
            "driver": full_name,
            "points": r["points"]
        })

    return top10
