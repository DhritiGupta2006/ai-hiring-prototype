import requests

# Free Judge0 CE endpoint (no RapidAPI, no key required)
JUDGE0_URL = "https://ce.judge0.com/submissions?base64_encoded=false&wait=true"

def run_code(source_code: str, language_id: int = 71):  # 71 = Python 3
    payload = {
        "source_code": source_code,
        "language_id": language_id
    }
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.post(JUDGE0_URL, json=payload, headers=headers)
    return response.json()

