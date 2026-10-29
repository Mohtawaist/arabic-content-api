"""عميل بسيط بـ urllib فقط — لا تبعيات، يعمل في أي بيئة."""
from __future__ import annotations

import json
import urllib.error
import urllib.request

BASE = "https://mohtawaist.com"


class Client:
    def __init__(self, api_key: str, base: str = BASE, timeout: int = 20):
        self.api_key = api_key
        self.base = base.rstrip("/")
        self.timeout = timeout

    def _call(self, path: str, payload: dict | None = None) -> dict:
        data = json.dumps(payload).encode() if payload is not None else None
        req = urllib.request.Request(self.base + path, data=data, method="POST" if data else "GET")
        req.add_header("X-API-Key", self.api_key)
        req.add_header("Accept", "application/json")
        req.add_header("User-Agent", "mohtawaist-python/1.0")
        if data:
            req.add_header("Content-Type", "application/json")
        try:
            with urllib.request.urlopen(req, timeout=self.timeout) as r:
                out = json.loads(r.read().decode("utf-8"))
                out["quota"] = {
                    "limit": r.headers.get("x-quota-limit"),
                    "remaining": r.headers.get("x-quota-remaining"),
                    "reset": r.headers.get("x-quota-reset"),
                }
                return out
        except urllib.error.HTTPError as e:
            body = {}
            try:
                body = json.loads(e.read().decode("utf-8"))
            except Exception:  # noqa: BLE001
                pass
            raise RuntimeError(body.get("error") or f"HTTP {e.code}") from None

    def analyze(self, text: str, keyword: str = "", **kw) -> dict:
        return self._call("/api/v1/analyze", {"text": text, "keyword": keyword, **kw})

    def slug(self, text: str) -> dict:
        return self._call("/api/v1/slug", {"text": text})

    def keywords(self, text: str, top: int = 10) -> dict:
        return self._call("/api/v1/keywords", {"text": text, "top": top})

    def readability(self, text: str) -> dict:
        return self._call("/api/v1/readability", {"text": text})

    def health(self) -> dict:
        return self._call("/api/v1/health")


def analyze(text: str, api_key: str, keyword: str = "") -> dict:
    """دالة مختصرة: analyze(text, api_key, keyword)."""
    return Client(api_key).analyze(text, keyword)
