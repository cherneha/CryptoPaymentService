import requests

def get_buyer_seller_address(buyer_id, seller_id):
    buyer_id = 1
    seller_id = 1
    r = requests.get("http://35.244.240.101/profiles/get", params={"id": buyer_id})
    res_json = r.json()
    buyer_address = res_json['walletAddress']

    r = requests.get("http://35.244.240.101/profiles/get", params={"id": seller_id})
    res_json = r.json()
    seller_address = res_json['walletAddress']
    # return buyer_address, seller_address
    return "0x554e1F37Bb03903Dd1eA7eFe9DC1dD9a160C6Ba5", "0x2Cd8938a50AC96d4e8967f83905Bb94902073AB1"
