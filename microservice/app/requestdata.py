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
    return "0x2Cd8938a50AC96d4e8967f83905Bb94902073AB1", "0x8a5587F2A4B130eCf7A3c3bc1578cd6C88a51cf2"
