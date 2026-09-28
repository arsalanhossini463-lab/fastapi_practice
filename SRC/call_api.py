import requests


def get_all_item():
    url = "http://127.0.0.1:8000/getitem/"
    response = requests.get(url)

    if response.status_code != 200:
        return "EROR"

    else:
        return response.json()
# =================================
def add_item(item):
    url = f"http://127.0.0.1:8000/add/{item}"
    response = requests.post(url)

    if response.status_code != 200:
        return "EROR"
    
    else:
        return response.json()
# =================================
def delete_item(item):
    url = f"http://127.0.0.1:8000/deleteitem/?item={item}"
    response = requests.delete(url)
    
    if response.status_code != 200:
        return "EROR"
            
    else:
        return response.json()

# =================================
def delete_item_by_index(index=-1):
    url = f"http://127.0.0.1:8000/deleteindex/?index={index}"
    response = requests.delete(url)
    
    if response.status_code != 200:
        return "EROR"
            
    else:
        return response.json()
# =================================
def update_item(old_item, new_item):
    url = f"http://127.0.0.1:8000/update/?old_item={old_item}&new_item={new_item}"
    response = requests.put(url)

    if response.status_code != 200:
        return "EROR"
        
    else:
        return response.json()

# =================================

def update_item_by_index(index, new_item):
    url = f"http://127.0.0.1:8000/updateindex/?index={index}&new_item={new_item}"
    response = requests.put(url)


    url2 = "http://127.0.0.1:8000/updateindex/"
    params = {
        "index":index,
        "new_item":new_item
    }
    response = requests.put(url, params=params)


    if response.status_code != 200:
        return "EROR"
        
    else:
        return response.json()




if __name__ == "__main__":
    print('=' * 20)
    print(get_all_item())
    print('~' * 10)
    print(delete_item_by_index())
    print('~' * 10)
    print(get_all_item())
    print('=' * 20)
    
