import json
import pandas as pd

file_path = r"C:\Users\Laurent\Desktop\recuperation\Data analyse\Twitch project\twitch_Data\raw\twitch_history.jsonl"

data = []
with open(file_path, "r", encoding="utf-8") as f:
    for line in f:
        data.append(json.loads(line))


rows = []
for snapshot in data:
    for stream in snapshot["data"]:
        rows.append({
            "snapshot_time": snapshot["timestamp"],
            "streamer": stream["user_name"],
            "game": stream["game_name"],
            "viewers": stream["viewer_count"],
            "started_at": stream["started_at"]
        })

df = pd.DataFrame(rows)


df["snapshot_time"] = pd.to_datetime(df["snapshot_time"], utc=True)
df["started_at"] = pd.to_datetime(df["started_at"], utc=True)
df["hour_start"] = df["started_at"].dt.hour
df["hour_snapshot"] = df["snapshot_time"].dt.hour
delta = df["snapshot_time"] - df["started_at"]
df["stream_age_seconds"] = delta.dt.total_seconds().round(0)
df["stream_age_minutes"] = df["stream_age_seconds"] / 60
df["stream_age_hours"] = df["stream_age_seconds"] / 3600
df["stream_age_minutes"] = df["stream_age_minutes"].round(2)
df["stream_age_hours"] = df["stream_age_hours"].round(2)


output_path = r"C:\Users\Laurent\Desktop\recuperation\Data analyse\Twitch project\twitch_Data\exports\twitch_dataset_clean.csv"
df.to_csv(output_path, index=False)
print(f"\n--- Dataset exporté --- {output_path}")