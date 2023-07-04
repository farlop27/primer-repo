import requests

def get_categories():
    r= requests.get('https://api.escuelajs.co/api/v1/categories')
    print(r.status_code)#obtienes el estado
    print(r.text)#HAsta aquí se tiene un string, se debe transofrmar
    categories = r.json()
    for category in categories:
        print(category['name'])
    