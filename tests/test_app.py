import os
import sys
import pytest

# Ensure the app module can be imported
sys.path.insert(0, os.path.abspath(os.path.dirname(os.path.dirname(__file__))))
from app import app

class DummyResponse:
    status_code = 200
    def json(self):
        return {}

def test_home_route():
    with app.test_client() as client:
        resp = client.get('/')
        assert resp.status_code == 200

def test_result_invalid_ip(monkeypatch):
    monkeypatch.setattr(app.requests, 'get', lambda *args, **kwargs: DummyResponse())
    monkeypatch.setattr(app, 'threat_intelligence_api_token', lambda ip, token: {'is_malicious': False})
    with app.test_client() as client:
        resp = client.post('/result', data={'ip_address': 'invalid'})
        assert resp.status_code == 500
