import os
import sys
import pytest

sys.path.insert(0, os.path.abspath(os.path.dirname(os.path.dirname(__file__))))
from app import app


async def dummy_fetch(*args, **kwargs):
    return {}


def test_home_route():
    with app.test_client() as client:
        resp = client.get("/")
        assert resp.status_code == 200


def test_result_invalid_ip(monkeypatch):
    monkeypatch.setattr(app, "fetch_ipinfo", dummy_fetch)
    monkeypatch.setattr(app, "fetch_threat_intelligence", dummy_fetch)
    with app.test_client() as client:
        resp = client.post("/result", data={"ip_address": "invalid"})
        assert resp.status_code == 500
