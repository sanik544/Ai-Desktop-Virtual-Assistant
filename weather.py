from requests_html import HTMLSession

def get_weather(city):
    session = HTMLSession()
    url = f'https://www.google.com/search?q=weather+{city}'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                      '(KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36 Edg/136.0.0.0'
    }

    response = session.get(url, headers=headers)

    # Render the page to execute JavaScript (requires pyppeteer)
    response.html.render(timeout=20)

    snippet = response.html.find('div#wob_wc', first=True)
    if snippet:
        print("Weather widget found!")
        print(snippet.html[:1000])
    else:
        print("Weather widget NOT found.")

    temperature = response.html.find('span#wob_tm', first=True)
    condition = response.html.find('span#wob_dc', first=True)

    if temperature and condition:
        return f"Current temperature in {city}: {temperature.text}°C, {condition.text}"
    else:
        return "Could not retrieve weather data."

city_name = "Patan"
print(get_weather(city_name))
