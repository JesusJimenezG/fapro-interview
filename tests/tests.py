import requests


class TestServer:
    def test_health_check(self):
        r = requests.get("http://localhost:8000/health-check")
        assert r.status_code == 200


class TestAPI:
    def test_get_uf(self):
        r = requests.get("http://localhost:8000/api/uf/17-04-2023")
        assert r.status_code == 200
        assert r.json() == {"uf": 35669.06, "date": "17-04-2023"}

    def test_get_ug_should_raise_http_exception(self):
        r = requests.get("http://localhost:8000/api/uf/01-01-2012")
        assert r.status_code == 400
        assert r.json() == {
            "detail": "La fecha mínima permitida es 01-01-2013",
        }
