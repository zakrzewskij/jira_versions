def get_version_names(versions):
    return [version['name'] for version in versions]


def get_versions_jql(versions):
    version_names = get_version_names(versions)
    return ", ".join(version_names)


def format_versions(versions):
    formatted_versions = []
    for version in versions:
        name = version['name']
        release_date = version.get('releaseDate', 'No release date')
        formatted_versions.append(f"{name:<10} | {release_date}")
    return formatted_versions


class VersionManager:
    def __init__(self, jira_client) -> None:
        self.jira_client = jira_client

    def get_project_versions(self, key: str):
        url = f'{self.jira_client.base_url}/rest/api/3/project/{key}/version'
        params = {
            "expand": "description, approvers",
            "orderBy": "-releaseDate",
            "maxResults": 100
        }
        return self.jira_client.get(url, params)
