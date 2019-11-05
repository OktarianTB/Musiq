import requests
from bs4 import BeautifulSoup

url = "https://www.billboard.com/charts/hot-100"


def get_ranking():
    response = requests.get(url).text
    soup = BeautifulSoup(response, "html.parser")
    date = soup.find("button", class_="date-selector__button").get_text().replace("  ", "").replace("\n", "")
    items = soup.find_all("li", class_="chart-list__element")

    ranking = [date]
    for item in items[:20]:
        artist_span = item.find("span", class_="chart-element__information__artist")
        song_span = item.find("span", class_="chart-element__information__song")
        if artist_span and song_span:
            artist = artist_span.get_text()
            song = song_span.get_text()
            ranking.append((song, artist))

    if len(ranking) > 10:
        return ranking

    return None
