class VersionManager:
    def __init__(self, versions):
        self.versions = versions

    def format_versions(self):
        formatted_versions = []
        for version in self.versions:
            name = version['name']
            release_date = version.get('releaseDate', 'No release date')
            formatted_versions.append(f"{name:<20} | {release_date}")
        return formatted_versions

    def get_version_names(self):
        return [version['name'] for version in self.versions]

    def get_version_jql(self):
        version_names = self.get_version_names()
        return ", ".join(version_names)
