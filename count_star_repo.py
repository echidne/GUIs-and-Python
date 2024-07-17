import requests

def search_github_repos(repo_name):
    search_url = f"https://api.github.com/search/repositories?q={repo_name}+in:name"
    response = requests.get(search_url)
    
    if response.status_code == 200:
        data = response.json()
        if data['total_count'] > 0:
            return data['items'][0]  # Return the first repository found
        else:
            print("No repositories found with that name.")
            return None
    else:
        print(f"Failed to retrieve data: {response.status_code}")
        return None

def get_github_stars(repo_info):
    return repo_info.get('stargazers_count', 0)

# Example usage
repo_name = "Hello-World"  # replace with the repository name you are searching for
repo_info = search_github_repos(repo_name)
if repo_info:
    stars = get_github_stars(repo_info)
    full_name = repo_info['full_name']
    print(f"The repository '{full_name}' has {stars} stars.")
