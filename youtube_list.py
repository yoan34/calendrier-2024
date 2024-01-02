import requests
import html


api_key = "AIzaSyCNAXe0T9uNW0E69rAlMcp-k5nu-fOjczo"

def get_latest_videos(channel_id, api_key, max_results=4):
    url = "https://www.googleapis.com/youtube/v3/search"
    params = {
        'part': 'snippet',
        'channelId': channel_id,
        'order': 'date',
        'type': 'video',
        'maxResults': max_results,
        'key': api_key
    }
    response = requests.get(url, params=params)
    return response.json()


def decode_html_entities(text):
    return html.unescape(text)


# Liste des identifiants de chaînes
channel_ids = {
    'UCsBPtU4hJkWNQ4kA-IsxgKw': "Idriss Aberkane",
    "UCaNlbnghtwlsGF-KzAFThqA": "Science étonnante",
    "UCsz9DiwPtgDvxJ-njWnieZw": "Passe-science",
    "UCrmjX43WdTRI8RwVuRUACCw": "Sadghuru",
    "UCSHZKyawb77ixDdsGog4iWA": "Lex fridman",
    "UCX0p0BGwCfJoz7oB-TSJ57Q": "Jean-Pierre petit",
    
}


# Récupération des vidéos pour chaque chaîne
for channel_id in channel_ids:
    videos = get_latest_videos(channel_id, api_key)
    channel = channel_ids[channel_id]
    print(f"{channel:-^110}")
    for video in videos['items']:
        date = video['snippet']['publishedAt'][:10]
        title = decode_html_entities(video['snippet']['title'])
        print(f"{date} - {title}")
    print("\n")