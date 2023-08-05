import requests
from bs4 import BeautifulSoup
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import json
import os


def main(args):
    url = "https://dexscreener.com"

    flareSolverrAPI = args.get("flareSolverrAPI", None)
    mongoURI = args.get("mongoURI", None)
    msgBotAPI = args.get("msgBotAPI", None)
    print(flareSolverrAPI, msgBotAPI, mongoURI)

    try:
        if flareSolverrAPI is None or mongoURI is None or msgBotAPI is None:
            raise Exception("flareSolverrAPI or mongoURI or msgBotAPI is None")

        client = MongoClient(mongoURI, server_api=ServerApi('1'))
        db = client['dexscreener']
        collection = db['chains']

        print('get html...')
        payload = json.dumps({
            "cmd": "request.get",
            "url": url,
            "maxTimeout": 30000
        })
        headers = {
            'Content-Type': 'application/json'
        }
        response = requests.post(flareSolverrAPI, headers=headers, data=payload)
        code = response.json()['status']
        message = response.json()['message']
        print(code, message)
        if code != 'ok':
            raise Exception(message)

        html = response.json()['solution']['response']
        bs = BeautifulSoup(html, 'html.parser')
        chain_list = bs.find_all(name='ul', attrs={'class': 'ds-nav-main-list'})[1]
        chains = chain_list.find_all(name='li', attrs={'class': 'ds-nav-main-list-item'})
        result = []
        for chain in chains:
            chain_name = chain.find(name='a').text
            chain_url = chain.find(name='a')['href']
            chain_url = url + chain_url
            chain_img = chain.find(name='img')['src']
            chain_img = url + chain_img
            chain_dict = {
                "chain_name": chain_name,
                "chain_url": chain_url,
                "chain_img": chain_img
            }
            result.append(chain_dict)
        print('n_result:', len(result))
        tg_message = "Dexscreener new chain listed: \n"  # telegram message
        tg_message_bak = tg_message
        for chain in result:
            r = collection.find_one({"chain_name": chain['chain_name']})
            if r is None:
                _ = collection.insert_one(chain)
                tg_message += f"{chain['chain_name']}: {chain['chain_url']}\n"
        print(tg_message)
        if tg_message != tg_message_bak:
            rsp = requests.post(msgBotAPI, data={
                "message": tg_message
            })
            print(rsp.status_code)

        return {
            "body": {
                "functionCode": 0,
                "message": "success",
                "data": []
            }
        }
    except Exception as e:
        print(e)
        return {
            "body": {
                "functionCode": -1,
                "message": str(e)
            }
        }


