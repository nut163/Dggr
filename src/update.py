```python
import os
import requests

def check_for_updates():
    response = requests.get('https://api.dogmeetdog.com/updates')
    if response.status_code == 200:
        return response.json()
    else:
        return None

def download_update(update_url):
    response = requests.get(update_url, stream=True)
    if response.status_code == 200:
        with open('update.zip', 'wb') as f:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)
        return True
    else:
        return False

def install_update():
    os.system('unzip update.zip -d /')
    os.remove('update.zip')
    return True

def update():
    updates = check_for_updates()
    if updates:
        for update in updates:
            if download_update(update['url']):
                install_update()
                print('update_installed')
    else:
        print('No updates available')
```