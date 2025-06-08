from flask import Flask, request, render_template
import httpx
import asyncio
from sklearn.cluster import KMeans
import numpy as np
import os

app = Flask(__name__)

# Securely set the API token using environment variables
ipinfo_api_token = os.getenv("IPINFO_API_TOKEN", "your_ipinfo_api_token")
threat_intelligence_api_token = os.getenv(
    "THREAT_INTELLIGENCE_API_TOKEN", "your_threat_intelligence_api_token"
)


async def fetch_threat_intelligence(ip_address: str, api_token: str):
    """Query the threat intelligence API for an IP address."""
    url = f"https://api.abuseipdb.com/ip/{ip_address}"
    headers = {"Authorization": f"Bearer {api_token}"}
    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()  # Assuming JSON response
    return None


async def fetch_ipinfo(ip_address: str, api_token: str):
    """Retrieve IP address information from IPinfo."""
    url = f"https://ipinfo.io/{ip_address}?token={api_token}"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
    if response.status_code == 200:
        return response.json()
    return None

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/result", methods=["POST"])
async def result():
    try:
        ip_address = request.form["ip_address"]

        ipinfo_task = fetch_ipinfo(ip_address, ipinfo_api_token)
        threat_task = fetch_threat_intelligence(ip_address, threat_intelligence_api_token)
        data, threat_info = await asyncio.gather(ipinfo_task, threat_task)
        if data:
            region = data.get("region", "Not Available")
            city = data.get("city", "Not Available")
            country = data.get("country", "Not Available")

            # Assuming the threat info contains a key "is_malicious" for simplicity
            is_malicious = threat_info.get("is_malicious") if threat_info else False

            # Convert the IP address to a numerical format for the machine learning model
            ip_parts = ip_address.split('.')
            ip_array = np.array([int(x) for x in ip_parts])
            kmeans = KMeans(n_clusters=2, random_state=0)
            kmeans.fit(ip_array.reshape(-1, 1))
            anomaly_score = abs(kmeans.score(ip_array.reshape(-1, 1)))
            
            return render_template(
                "result.html", 
                ip_address=ip_address, 
                region=region, 
                city=city, 
                country=country, 
                anomaly_score=anomaly_score,
                is_malicious=is_malicious
            )
        else:
            return "Error fetching data from IPinfo", 500
    except Exception as e:
        return str(e), 500

if __name__ == "__main__":
    app.run(debug=True)
