import httpx

def get(url, **kwargs):
    return httpx.get(url, timeout=10, **kwargs)

def post(url, data=None, json=None, **kwargs):
    return httpx.post(url, data=data, json=json, timeout=10, **kwargs)