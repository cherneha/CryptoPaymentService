from app.routes import current_web3

class TokenManager:
    def __init__(self):
        self.token_adress = '0xfa8b724558412CD5f2E07cAF2337885dA13864D5'
        self.abi = '[{"constant":true,"inputs":[],"name":"supply","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},' \
              '{"constant":true,"inputs":[],"name":"name","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},' \
              '{"constant":false,"inputs":[{"name":"spender","type":"address"},{"name":"tokens","type":"uint256"}],"name":"approve",' \
              '"outputs":[{"name":"success","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},' \
              '{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"name":"a","type":"uint256"}],"payable":false,' \
              '"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"from","type":"address"},' \
              '{"name":"to","type":"address"},{"name":"tokens","type":"uint256"}],"name":"transferFrom","outputs":' \
              '[{"name":"success","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,' \
              '"inputs":[{"name":"","type":"address"}],"name":"balances","outputs":[{"name":"","type":"uint256"}],"payable":false,' \
              '"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"name":"",' \
              '"type":"uint8"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"to",' \
              '"type":"address"},{"name":"tokens","type":"uint256"}],"name":"transfer","outputs":[{"name":"success","type":"bool"}],' \
              '"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"tokenOwner",' \
              '"type":"address"},{"name":"spender","type":"address"}],"name":"allowance","outputs":[{"name":"remaining","type":"uint256"}],' \
              '"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"account","type":"address"}],' \
              '"name":"balance","outputs":[{"name":"accountBalance","type":"uint256"}],"payable":false,"stateMutability":"view",' \
              '"type":"function"},{"inputs":[],"payable":false,"stateMutability":"nonpayable","type":"constructor"}]'

        self.token =  current_web3.eth.contract(abi=self.abi, address=self.token_adress)

    def approve(self, sender, spender, value):
        tx = self.token.functions.approve(spender=spender, tokens=value).buildTransaction(
        {
            'from': sender,
            'gas': 1100000,
            'value': 0,
            'gasPrice': current_web3.eth.gasPrice * 30,  # Get Gas Price
            'nonce': current_web3.eth.getTransactionCount(sender)
        })

        signed = current_web3.eth.account.signTransaction(tx,
                                                          'd0eaed9b1a4633b358208793a96aba7fd42547472682a2e6fe73cf3ababef3fc')
        tx_hash = current_web3.eth.sendRawTransaction(signed.rawTransaction)
        print ("approve spending")
        print(tx_hash.hex())
        tx_reciept = current_web3.eth.waitForTransactionReceipt(tx_hash)
        print(tx_reciept)


