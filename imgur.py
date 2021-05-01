import requests


async def upload():
    url = "https://api.imgur.com/3/upload"

    files = [
        ('video', open('temp/output.mp4', 'rb'))
    ]

    response = requests.request("POST", url, headers={}, data={}, files=files)

    return response.json()['data']['link']
