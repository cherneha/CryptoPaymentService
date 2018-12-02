import requests

def get_user_address(user_id):
    r = requests.get("http://35.244.240.101/profiles/get", params={"id": user_id})
    res_json = r.json()
    user_address = res_json['walletAddress']
    return user_address


# "0x2Cd8938a50AC96d4e8967f83905Bb94902073AB1"
# "0x8a5587F2A4B130eCf7A3c3bc1578cd6C88a51cf2"
