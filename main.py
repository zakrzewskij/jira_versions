from jira_client import JiraClient

if __name__ == "__main__":
    jira_client = JiraClient()
    if jira_client.authenticate():
        project_key = input("Podaj klucz projektu: ")
        versions = jira_client.get_project_versions(project_key)
