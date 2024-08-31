import requests

def fetch_data():
    url = ('https://api.freeapi.app/api/v1/public/randomjokes/joke/random')
    response=requests.get(url)
    data = response.json()

    if data['success'] and 'data' in data:
        user_data = data['data']
        content = user_data['content']
        return content

    else:
        raise Exception('failed to fetch')  


def main():
    try:
        content = fetch_data()
        print(f'content:{content}')
    except Exception as e:
        print(str(e))

if __name__ == '__main__':
  main()
