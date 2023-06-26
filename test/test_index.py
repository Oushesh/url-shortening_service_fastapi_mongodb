import pytest
import json, requests
import os,sys
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from src.msg.data import data
from src.index import encode_url, decode_url

"""
@pytest.mark.asyncio
async def test_encode_url():
    URL = "https://url-shortening-service-ol9j.vercel.app/encode_url"
    params = {"url_input": "https://www.google.com"}
    response = requests.get(URL, params=params)
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data["short_url"], str)
    #assert data["short_url"] == "8ffdef1"  # Update the expected short_url value


@pytest.mark.asyncio
async def test_decode_url():
    # Test cases for decoding URLs
    pass  # Placeholder for the test cases
    URL = "https://url-shortening-service-ol9j.vercel.app/decode_url"
    params = {"url_input": "https://www.google.com"}
    response = requests.get(URL, params=params)
    assert response.status_code == 200
    data = response.json()
    #assert isinstance(data["long_url"], str )
    assert isinstance(data,dict)
    #assert isinstance(data["error"], str)
    params = {"url_input": "https://www.google.com"}
"""

##OK. we will write pair test cases to see if the recover works.
## We test with pairs from the

## Pairwise testing for N examples and see 
## what and why thing fails.

"""
@pytest.mark.asyncio
async def test_encode_decode_recover():
    encoded_URL = "https://url-shortening-service-ol9j.vercel.app/encode_url"
    decoded_URL = "https://url-shortening-service-ol9j.vercel.app/decode_url"
    
    input_url = "https://www.google.com"
    encoded_params = {"url_input": input_url}
    encoded_response = requests.get(encoded_URL,params=encoded_params) 
    assert encoded_response.status_code ==200

    data = encoded_response.json()
    encoded_data = data["short_url"]

    decoded_params = {"short_url":encoded_data}
    decoded_response = requests.get(decoded_URL,params=decoded_params)

    original_url = decoded_response.json()["long_url"]
    #Check that the decoded reponse is the original url.
    assert (input_url==original_url)
"""


class TestURLShortener:

    encoded_URL = "https://url-shortening-service-ol9j.vercel.app/encode_url"
    decoded_URL = "https://url-shortening-service-ol9j.vercel.app/decode_url"

    @pytest.mark.asyncio
    async def test_encode_decode_recover(self):
        input_urls = [
            "https://www.google.com",
            "https://www.example.com",
            "https://www.github.com",
            "https://www.openai.com"
        ]
        errors = []
        
        for url in input_urls:
            try:
                encoded_params = {"url_input": url}
                encoded_response = requests.get(self.encoded_URL, params=encoded_params)
                assert encoded_response.status_code == 200

                data = encoded_response.json()
                encoded_data = data["short_url"]

                decoded_params = {"short_url": encoded_data}
                decoded_response = requests.get(self.decoded_URL, params=decoded_params)

                original_url = decoded_response.json()["long_url"]
                assert url == original_url

            except AssertionError:
                errors.append(f"Assertion failed for URL: {url}")

        if errors:
            pytest.fail("\n".join(errors))


import pytest
import requests

class TestURLShortenerFail:

    encoded_URL = "https://url-shortening-service-ol9j.vercel.app/encode_url"
    decoded_URL = "https://url-shortening-service-ol9j.vercel.app/decode_url"

    @pytest.mark.asyncio
    async def test_encode_decode_recover(self):
        input_urls = [
            "https://www.google.com",
            "https://www.example.com",
            "https://www.github.com",
            "https://www.openai.com",
            "https://www.invalidurl.com",  # Invalid URL intentionally added
            "https://www.example.com/page?param1=value1&param2=value2&param3=value3",
            "https://www.google.com/search?q=python+programming&num=10",
            "https://www.github.com/repo/issues?state=open&labels=bug",
            "https://www.openai.com/blog/the-future-of-artificial-intelligence",
        ]
        errors = []
        
        for url in input_urls:
            try:
                encoded_params = {"url_input": url}
                encoded_response = requests.get(self.encoded_URL, params=encoded_params)
                assert encoded_response.status_code == 200

                data = encoded_response.json()
                encoded_data = data["short_url"]

                decoded_params = {"short_url": encoded_data}
                decoded_response = requests.get(self.decoded_URL, params=decoded_params)

                original_url = decoded_response.json()["long_url"]
                assert url == original_url+"url"

            except AssertionError:
                errors.append(f"Assertion failed for URL: {url}")

        if errors:
            pytest.fail("\n".join(errors))










