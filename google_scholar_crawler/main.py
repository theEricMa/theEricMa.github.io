from scholarly import scholarly
import jsonpickle
import json
from datetime import datetime
import os
import requests

os.environ['GOOGLE_SCHOLAR_ID'] = 'F15mLDYAAAAJ'

# Fetch Google Scholar Data
author: dict = scholarly.search_author_id(os.environ['GOOGLE_SCHOLAR_ID'])
scholarly.fill(author, sections=['basics', 'indices', 'counts', 'publications'])
name = author['name']
author['updated'] = str(datetime.now())
author['publications'] = {v['author_pub_id']:v for v in author['publications']}

# Add GitHub repository data
github_repos = {
    "OTAvatar": "theEricMa/OTAvatar",
    "DiffSpeaker": "theEricMa/DiffSpeaker",
    "ScaleDreamer": "theEricMa/ScaleDreamer",
    "TriplaneTurbo": "theEricMa/TriplaneTurbo",
    # Add more repositories as needed
}

author['github_repos'] = {}
for repo_name, repo_path in github_repos.items():
    try:
        headers = {}
        if 'GITHUB_TOKEN' in os.environ:
            headers['Authorization'] = f"token {os.environ['GITHUB_TOKEN']}"
            
        response = requests.get(f"https://api.github.com/repos/{repo_path}", headers=headers)
        if response.status_code == 200:
            repo_data = response.json()
            author['github_repos'][repo_name] = {
                'stars': repo_data['stargazers_count'],
                'forks': repo_data['forks_count'],
                'url': repo_data['html_url']
            }
    except Exception as e:
        print(f"Error fetching data for {repo_name}: {e}")

print(json.dumps(author, indent=2))
os.makedirs('results', exist_ok=True)
with open(f'results/gs_data.json', 'w') as outfile:
    json.dump(author, outfile, ensure_ascii=False)

shieldio_data = {
  "schemaVersion": 1,
  "label": "citations",
  "message": f"{author['citedby']}",
}
with open(f'results/gs_data_shieldsio.json', 'w') as outfile:
    json.dump(shieldio_data, outfile, ensure_ascii=False)
