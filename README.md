# SafeStreet IP Analyzer

Welcome to the SafeStreet IP Analyzer - your go-to open-source tool for checking the safety and integrity of IP addresses. Our easy-to-use platform provides detailed insights into potentially malicious activities associated with IP addresses and helps in enhancing the cybersecurity posture of individuals and communities alike.

<img width="779" alt="Screenshot 2024-04-22 at 00 32 57" src="https://github.com/DeepNandre/SafeStreet-IP-Analyzer/assets/81618576/08e0f31e-f65e-495b-8abd-e45f1da3744a">

## Features

- **IP Information Retrieval**: Get detailed information about an IP address, including its geolocation, ISP, and associated domain information.
- **Threat Intelligence**: Determine if an IP address has been flagged for suspicious activities by integrating with threat intelligence databases.
- **Anomaly Detection**: Utilize machine learning to score and identify unusual behavior or anomalies associated with an IP address.
- **User-Friendly Interface**: Analyze IP addresses through a simple and intuitive web interface.
- **Real-Time Alerts**: Receive instant notifications for any identified threats or unusual activities.
- **Community Contribution**: As an open-source project, we welcome contributions to make the internet a safer place for everyone.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- flask: 1.1.2
- requests: 2.25.1
- scikit-learn: 0.24.1
- waitress: 2.0.0
- numpy: 1.20.1
- pytest: 6.2.2
- gunicorn: 20.0.4


### Installing

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/SafeStreet-IP-Analyzer.git
   cd SafeStreet-IP-Analyzer
   ```

2. **Set Up a Virtual Environment** (optional but recommended)

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Required Packages**

   ```bash
   pip3 install -r requirements.txt
   ```

4. **Environment Variables**

   Set up the necessary environment variables. For security reasons, never hardcode sensitive information like API tokens within your application code.

   ```bash
   export IPINFO_API_TOKEN='your_ipinfo_api_token'
   export THREAT_INTELLIGENCE_API_TOKEN='your_threat_intelligence_api_token'
   ```

5. **Run the Application**

   ```bash
   python3 app.py
   ```

## How to Use

1. **Enter the IP Address**: Simply type the IP address you wish to analyze into the input field.
2. **Analyze**: Click the 'Analyze' button to retrieve information about the IP address.
3. **Review the Results**: The analysis results will provide detailed information and a security assessment.

## Contributing

We welcome contributions from the community. Whether it's improving the codebase, refining the user interface, or extending the feature set - your contributions are valuable to us.

1. Fork the repository.
2. Create your feature branch (`git checkout -b feature/AmazingFeature`).
3. Commit your changes (`git commit -am 'Add some AmazingFeature'`).
4. Push to the branch (`git push origin feature/AmazingFeature`).
5. Open a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE) file for details.

## Acknowledgments

- To all contributors and the community for their ideas and support.
- Threat intelligence data provided by [Threat Intelligence API](#).
- Geolocation data by [IPinfo](https://ipinfo.io/).

Join us in our mission to make the digital streets safer!

---

Remember to replace placeholders like `yourusername`, `your_ipinfo_api_token`, `your_threat_intelligence_api_token`, and others with actual data. Also, make sure to include the actual links to the APIs or other services you're using. A LICENSE.md file should also be included if you're mentioning it in the README.
