import pandas as pd
import requests
import os
import time

def get_names_from_text(path: str | os.PathLike) -> list: 
    keys = []
    with open(path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            line = line.strip()
            if "/" in line:
                keys += line.split('/')
            else:
                keys.append(line)

    return list(set(keys))
#print(get_names_from_text(r"C:\Users\Philippe\Desktop\liste GUI python.txt"))

def get_info_from_git(repo_name: str, info_type: str) -> str | int | dict:
    
    search_url = f"https://api.github.com/search/repositories?q={repo_name}+in:name"
    print(search_url)
    response = requests.get(search_url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'}, timeout = 10)
    time.sleep(10)
    print(response.status_code)
    if response.status_code == 200:
        data = response.json()
        try :
            return data['items'][0][info_type]
        except IndexError:
            return f"{repo_name} has no {info_type} key"
        except KeyError:
            print(f"{info_type} is not a valid key")
    elif response.status_code == 429:
        print(response.headers["Retry-After"])
    else:
        print(f"{repo_name} is not a valid repository name")

# get names of repo
names = get_names_from_text(r"C:\Users\Philippe\Desktop\liste GUI python.txt")
print(names)
# get links of the repo
links = [get_info_from_git(name, "html_url") for name in names]
print(links)
# get the stars counts
stars = [get_info_from_git(name, "stargazers_count") for name in names]
print(stars)
df_info = pd.DataFrame(zip(names, links, stars), columns= ["Names", "Links", "Stars"])
print(df_info)
df_info.to_csv("GUI_repo_infos.csv", index= False)






