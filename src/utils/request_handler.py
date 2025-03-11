import httpx

def handle_request(url, method, headers, body):
    """Sends an HTTP request and returns response details."""
    try:
        with httpx.Client() as client:
            response = client.request(
                method=method,
                url=url,
                headers=headers,
                json=body if isinstance(body, dict) else None,
                data=body if isinstance(body, str) else None,
            )
            return {
                "status_code": response.status_code,
                "headers": dict(response.headers),
                "body": response.text
            }
    except httpx.RequestError as e:
        return {
            "status_code": 0,
            "headers": {},
            "body": str(e)
        }
