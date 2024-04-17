import requests
import os
import json
from os.path import join, dirname
from dotenv import load_dotenv


class JiraClient:
    def __init__(self):
        dotenv_path = join(dirname(__file__), '.env')
        load_dotenv(dotenv_path)
        self.email = os.environ.get('JIRA_EMAIL')
        self.api_token = os.environ.get('JIRA_API_TOKEN')
        self.base_url = os.environ.get('JIRA_BASE_URL')

    def authenticate(self):
        if not self.email or not self.api_token or not self.base_url:
            print("Brak wymaganych danych uwierzytelniających.")
            return False
        try:
            response = requests.get(f'{self.base_url}/rest/api/3/myself', auth=(self.email, self.api_token))
            if response.status_code == 200:
                print("Autentykacja udana!")
                return True
            else:
                print("Błąd autentykacji. Sprawdź dane uwierzytelniające.")
                return False
        except Exception as e:
            print(f"Wystąpił błąd podczas autentykacji: {e}")
            return False

    def get_project_versions(self, key: str):
        try:
            headers = {
                "Accept": "application/json"
            }

            params = {
                "expand": "description, approvers",
                "orderBy": "-releaseDate",
                "maxResults": 1000
            }

            url = f'{self.base_url}/rest/api/3/project/{key}/version'
            response = requests.get(
                url,
                headers=headers,
                auth=(self.email, self.api_token),
                params=params
            )

            if response.status_code == 200:
                data = response.json()
                print(json.dumps(data, indent=4))
                return data
            else:
                print(f"Błąd pobierania wersji projektu: {response.status_code} - {response.text}")
                return None

        except Exception as e:
            print(f"Wystąpił błąd podczas pobierania wersji projektu: {e}")
            return None
