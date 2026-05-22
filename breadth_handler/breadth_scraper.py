from datetime import datetime, timedelta, timezone
import urllib.parse
import requests
from payload_config import DASHBOARD_URL, WIDGET_URL, QUERY


def _merge_results(results: list) -> dict:
    merged = {}
    for fragment in results:
        merged.update(fragment)
    return merged


def get_data():
    with requests.Session() as s:
        s.headers.update({"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"})
        s.get(DASHBOARD_URL).raise_for_status()

        xsrf = urllib.parse.unquote(s.cookies.get("XSRF-TOKEN") or "")
        if not xsrf:
            raise SystemExit("Missing XSRF-TOKEN cookie")

        s.headers.update({
            "accept": "*/*",
            "content-type": "application/x-www-form-urlencoded",
            "x-requested-with": "XMLHttpRequest",
            "x-xsrf-token": xsrf,
        })

        params = {
            "query": QUERY,
            "use_live": "1",
            "limit": "6",
            "size": "375",
            "widget_id": "2723959"
        }

        body = urllib.parse.urlencode(params)
        r = s.post(WIDGET_URL, data=body)
        r.raise_for_status()
        return r.json()


def _format_line(ts: int, tz: timezone, merged: dict, idx: int) -> str:
    date = datetime.fromtimestamp(ts / 1000, tz=tz).strftime("%Y-%m-%d")
    return (
        f"date={date}, e20={merged['e20'][idx]}%, u4={merged['u4'][idx]}, "
        f"d4={merged['d4'][idx]}, w20={merged['w20'][idx]}, universe={merged['universe'][idx]}\n"
    )

    
if __name__ == "__main__":
    data = get_data()
    results = data["groupData"][0]["results"]
    timestamps = data["metaData"][0]["tradeTimes"]

    merged = _merge_results(results)
    tz = timezone(timedelta(hours=5, minutes=30))

    with open("Output/breadth.txt", "w") as f:
        for i in reversed(range(len(merged["e20"]))):
            f.write(_format_line(timestamps[i], tz, merged, i))