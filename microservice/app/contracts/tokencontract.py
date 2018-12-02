from flask_web3 import current_web3

class TokenContract:

    def __init__(self):
        self.abi = '''[{"constant":true,"inputs":[],"name":"supply","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"name","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"spender","type":"address"},{"name":"tokens","type":"uint256"}],"name":"approve","outputs":[{"name":"success","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"name":"a","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"from","type":"address"},{"name":"to","type":"address"},{"name":"tokens","type":"uint256"}],"name":"transferFrom","outputs":[{"name":"success","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"","type":"address"}],"name":"balances","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"name":"","type":"uint8"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"to","type":"address"},{"name":"tokens","type":"uint256"}],"name":"transfer","outputs":[{"name":"success","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"tokenOwner","type":"address"},{"name":"spender","type":"address"}],"name":"allowance","outputs":[{"name":"remaining","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"account","type":"address"}],"name":"balance","outputs":[{"name":"accountBalance","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"inputs":[],"payable":false,"stateMutability":"nonpayable","type":"constructor"}]'''
        self.token_adress = current_web3.toChecksumAddress('0xf66b8916918daef2ed5678ff29b634c5e9229395')
        self.token = current_web3.eth.contract(abi=self.abi, address=self.token_adress)

    def approve(self, sender, spender, value, sender_key):

        tx = self.token.functions.approve(spender=spender, tokens=value).buildTransaction(
        {
            'from': sender,
            'gas': 1100000,
            'value': 0,
            'gasPrice': current_web3.eth.gasPrice * 30,  # Get Gas Price
            'nonce': current_web3.eth.getTransactionCount(sender)
        })

        signed = current_web3.eth.account.signTransaction(tx, sender_key)
        tx_hash = current_web3.eth.sendRawTransaction(signed.rawTransaction)
        print ("approve spending")
        print(tx_hash.hex())
        tx_reciept = current_web3.eth.waitForTransactionReceipt(tx_hash)
        print(tx_reciept)

    def balance(self, address):
        return self.token.functions.balance(address).call()



