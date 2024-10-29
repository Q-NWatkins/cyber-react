# api_integrations.py

import requests
from config import VT_API_KEY, ABUSEIPDB_API_KEY

def virus_total_scan(url):
    api_url = f"https://www.virustotal.com/api/v3/urls"
    headers = {
        "x-apikey": VT_API_KEY,
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {"url": url}
    response = requests.post(api_url, headers=headers, data=data)
    return response.json()

def abuse_ipdb_check(ip):
    api_url = f"https://api.abuseipdb.com/api/v2/check"
    headers = {
        "Accept": "application/json",
        "Key": ABUSEIPDB_API_KEY
    }
    params = {"ipAddress": ip}
    response = requests.get(api_url, headers=headers, params=params)
    return response.json()