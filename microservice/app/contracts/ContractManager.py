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
        transact_params = {
            'from': sender,
            'gas': 21000,
            'gas_price': 1,
        }
        self.token.functions.approve(spender=spender, tokens=value).transact(transact_params)
