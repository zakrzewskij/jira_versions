from jira_client import JiraClient
from version_manager import VersionManager, format_versions, get_versions_jql

if __name__ == "__main__":
    jira_client = JiraClient()
    if jira_client.authenticate():
        project_key = input("Podaj klucz projektu: ")
        version_manager = VersionManager(jira_client)

        versions_response = version_manager.get_project_versions(project_key)

        if versions_response and "values" in versions_response:
            versions = versions_response["values"]

            formatted_versions = format_versions(versions)
            for formatted_version in formatted_versions:
                print(formatted_version)

            fixversion = get_versions_jql(versions)
            print(f"fixversion IN ({fixversion})")
        else:
            print("Brak wersji projektu.")
    else:
        print("Autentykacja nieudana.")
