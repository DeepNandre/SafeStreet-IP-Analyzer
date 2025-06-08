from flask import Flask, request, render_template
import requests
from sklearn.cluster import KMeans
import numpy as np
import os

app = Flask(__name__)

# Securely set the API token using environment variables
ipinfo_api_token = os.getenv("IPINFO_API_TOKEN", "your_ipinfo_api_token")
threat_intelligence_api_token = os.getenv("THREAT_INTELLIGENCE_API_TOKEN", "your_threat_intelligence_api_token")

# Define the function for threat intelligence check outside of the route
def fetch_threat_info(ip_address, api_token):
    # Make sure to use the actual threat intelligence API endpoint
    url = f"https://api.abuseipdb.com/ip/{ip_address}"
    headers = {'Authorization': f'Bearer {api_token}'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        threat_info = response.json()  # Assuming JSON response
        # Process the response and extract the necessary information
        # ...
    else:
        threat_info = None  # Handle error or no threat found
    return threat_info

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/result", methods=["POST"])
def result():
    try:
        ip_address = request.form["ip_address"]
        
        # Retrieve the IP address information from ipinfo
        response = requests.get(f"https://ipinfo.io/{ip_address}?token={ipinfo_api_token}")
        if response.status_code == 200:
            data = response.json()
            region = data.get("region", "Not Available")
            city = data.get("city", "Not Available")
            country = data.get("country", "Not Available")
            
            # Check IP against threat intelligence API
            threat_info = fetch_threat_info(ip_address, threat_intelligence_api_token)
            
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
            return f"Error fetching data: {response.status_code}", 500
    except Exception as e:
        return str(e), 500

if __name__ == "__main__":
    app.run(debug=True)
