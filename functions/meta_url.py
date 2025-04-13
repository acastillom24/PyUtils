from urllib.parse import urlparse

class MetaUrl:
    def __init__(self, url):
        self.parsed_url = urlparse(url)
    
    def get_parts_url(self):
        url_parts = {
            "protocol": self.parsed_url.scheme,
            "host": self.parsed_url.netloc,
            "path": self.parsed_url.path,
            "query": self.parsed_url.query,
            "fragment": self.parsed_url.fragment,
        }
        return url_parts
    
# Example usage:
url = "https://example.com/onboarding?type=student#section1"
meta_url = MetaUrl(url)
print(meta_url.get_parts_url())