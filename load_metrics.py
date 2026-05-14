import requests
import pandas as pd

TOKEN = "y0__wgBEJay_bMHGPfMQSD6-_mzFxX2oNzkD2S9CoqJBVHH9XybVRHm"
COUNTER_ID = "100770844"

url = "https://api-metrika.yandex.net/stat/v1/data"

headers = {
    "Authorization": f"OAuth {TOKEN}"
}

params = {

    "ids": COUNTER_ID,

    "metrics": ",".join([

        "ym:s:visits",
        "ym:s:users",
        "ym:s:avgVisitDurationSeconds",
        "ym:s:bounceRate",

        # Конверсия цели
        "ym:s:goal395964629conversionRate"

    ]),

    "dimensions": ",".join([

    "ym:s:date",
    "ym:s:lastTrafficSource",
    "ym:s:lastSearchEngine",
    "ym:s:lastAdvEngine"

    ]),

    "date1": "2025-04-01",
    "date2": "today",

    "limit": 100000
}

response = requests.get(
    url,
    headers=headers,
    params=params
)

data = response.json()

rows = []

for item in data["data"]:

    rows.append({

    "date":
        item["dimensions"][0]["name"],

    "traffic_source":
        item["dimensions"][1]["name"],

    "search_engine":
        item["dimensions"][2]["name"],

    "adv_engine":
        item["dimensions"][3]["name"],

    "visits":
        item["metrics"][0],

    "users":
        item["metrics"][1],

    "avg_visit_duration_sec":
        item["metrics"][2],

    "bounce_rate":
        item["metrics"][3],

    "goal_conversion_rate":
        item["metrics"][4]
    })

df = pd.DataFrame(rows)

print(df.head())

df.to_csv(
    "metrika_dataset.csv",
    index=False
)

print("Dataset сохранен")