from jira_client import JiraClient
from version_manager import VersionManager

if __name__ == "__main__":
    jira_client = JiraClient()
    if jira_client.authenticate():
        project_key = input("Podaj klucz projektu: ")
        versions_response = jira_client.get_project_versions(project_key)
        if versions_response and "values" in versions_response:
            versions = versions_response["values"]
            version_manager = VersionManager(versions)

            formatted_versions = version_manager.format_versions()
            for formatted_version in formatted_versions:
                print(formatted_version)

            fixversion = version_manager.get_version_jql()
            print(f"fixversion IN ({fixversion})")
        else:
            print("Brak wersji projektu.")
    else:
        print("Autentykacja nieudana.")
