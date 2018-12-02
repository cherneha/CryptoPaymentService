from app.routes import current_web3
from app.bdmanager import ordermanager
import json

class OrderManager:

    contract_abi = '''[
	{
		"constant": true,
		"inputs": [],
		"name": "seller",
		"outputs": [
			{
				"name": "",
				"type": "address"
			}
		],
		"payable": false,
		"stateMutability": "view",
		"type": "function"
	},
	{
		"constant": false,
		"inputs": [],
		"name": "confirmRecieved",
		"outputs": [],
		"payable": false,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"constant": true,
		"inputs": [],
		"name": "value",
		"outputs": [
			{
				"name": "",
				"type": "uint256"
			}
		],
		"payable": false,
		"stateMutability": "view",
		"type": "function"
	},
	{
		"constant": false,
		"inputs": [],
		"name": "refund",
		"outputs": [],
		"payable": false,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"constant": false,
		"inputs": [],
		"name": "cancelOrder",
		"outputs": [],
		"payable": false,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"constant": true,
		"inputs": [],
		"name": "mediator",
		"outputs": [
			{
				"name": "",
				"type": "address"
			}
		],
		"payable": false,
		"stateMutability": "view",
		"type": "function"
	},
	{
		"constant": true,
		"inputs": [],
		"name": "buyer",
		"outputs": [
			{
				"name": "",
				"type": "address"
			}
		],
		"payable": false,
		"stateMutability": "view",
		"type": "function"
	},
	{
		"constant": false,
		"inputs": [],
		"name": "confirmSupplied",
		"outputs": [],
		"payable": false,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"constant": true,
		"inputs": [],
		"name": "state",
		"outputs": [
			{
				"name": "",
				"type": "uint8"
			}
		],
		"payable": false,
		"stateMutability": "view",
		"type": "function"
	},
	{
		"constant": false,
		"inputs": [],
		"name": "freezeTokens",
		"outputs": [],
		"payable": false,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"name": "price",
				"type": "uint256"
			},
			{
				"name": "miloAdress",
				"type": "address"
			},
			{
				"name": "sellerAddress",
				"type": "address"
			},
			{
				"name": "mediatorAddress",
				"type": "address"
			}
		],
		"payable": false,
		"stateMutability": "nonpayable",
		"type": "constructor"
	}
]'''

    compiled = '''608060405234801561001057600080fd5b50604051608080610e298339810180604052608081101561003057600080fd5b81019080805190602001909291908051906020019092919080519060200190929190805190602001909291905050506000600460146101000a81548160ff0219169083600281111561007e57fe5b021790555033600260006101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff16021790555081600160006101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff16021790555080600360006101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff1602179055508360008190555082600460006101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff16021790555050505050610c88806101a16000396000f3fe6080604052600436106100a4576000357c0100000000000000000000000000000000000000000000000000000000900463ffffffff16806308551a53146100a957806334f013b1146101005780633fa4f24514610117578063590e1ae3146101425780636a816548146101595780636d0501f6146101705780637150d8ae146101c75780637700985b1461021e578063c19d93fb14610235578063da9f48751461026e575b600080fd5b3480156100b557600080fd5b506100be610285565b604051808273ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200191505060405180910390f35b34801561010c57600080fd5b506101156102ab565b005b34801561012357600080fd5b5061012c6104b9565b6040518082815260200191505060405180910390f35b34801561014e57600080fd5b506101576104bf565b005b34801561016557600080fd5b5061016e61076a565b005b34801561017c57600080fd5b506101856108f4565b604051808273ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200191505060405180910390f35b3480156101d357600080fd5b506101dc61091a565b604051808273ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200191505060405180910390f35b34801561022a57600080fd5b50610233610940565b005b34801561024157600080fd5b5061024a610a2b565b6040518082600281111561025a57fe5b60ff16815260200191505060405180910390f35b34801561027a57600080fd5b50610283610a3e565b005b600160009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1681565b600260009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff163373ffffffffffffffffffffffffffffffffffffffff16141515610370576040517f08c379a000000000000000000000000000000000000000000000000000000000815260040180806020018281038252601c8152602001807f4f6e6c792062757965722063616e20667265657a6520746f6b656e730000000081525060200191505060405180910390fd5b6002600460146101000a81548160ff0219169083600281111561038f57fe5b0217905550600460009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1663a9059cbb600160009054906101000a900473ffffffffffffffffffffffffffffffffffffffff166000546040518363ffffffff167c0100000000000000000000000000000000000000000000000000000000028152600401808373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020018281526020019250505060206040518083038186803b15801561047b57600080fd5b505afa15801561048f573d6000803e3d6000fd5b505050506040513d60208110156104a557600080fd5b810190808051906020019092919050505050565b60005481565b600360009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff163373ffffffffffffffffffffffffffffffffffffffff16141515610584576040517f08c379a00000000000000000000000000000000000000000000000000000000081526004018080602001828103825260188152602001807f4f6e6c79206d65646961746f722063616e20726566756e64000000000000000081525060200191505060405180910390fd5b60028081111561059057fe5b600460149054906101000a900460ff1660028111156105ab57fe5b14151515610621576040517f08c379a00000000000000000000000000000000000000000000000000000000081526004018080602001828103825260198152602001807f43616e6e6f7420726566756264206f6e20696e6163746976650000000000000081525060200191505060405180910390fd5b600460009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1663a9059cbb600260009054906101000a900473ffffffffffffffffffffffffffffffffffffffff166000546040518363ffffffff167c0100000000000000000000000000000000000000000000000000000000028152600401808373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020018281526020019250505060206040518083038186803b15801561070857600080fd5b505afa15801561071c573d6000803e3d6000fd5b505050506040513d602081101561073257600080fd5b8101908080519060200190929190505050506002600460146101000a81548160ff0219169083600281111561076357fe5b0217905550565b600160009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff163373ffffffffffffffffffffffffffffffffffffffff1614151561082f576040517f08c379a00000000000000000000000000000000000000000000000000000000081526004018080602001828103825260168152602001807f4f6e6c792073656c6c65722063616e2063616e63656c0000000000000000000081525060200191505060405180910390fd5b600080600281111561083d57fe5b600460149054906101000a900460ff16600281111561085857fe5b1415156108cd576040517f08c379a000000000000000000000000000000000000000000000000000000000815260040180806020018281038252600e8152602001807f496e76616c69642073746174652e00000000000000000000000000000000000081525060200191505060405180910390fd5b6002600460146101000a81548160ff021916908360028111156108ec57fe5b021790555050565b600360009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1681565b600260009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1681565b600160009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff163373ffffffffffffffffffffffffffffffffffffffff16141515610a05576040517f08c379a00000000000000000000000000000000000000000000000000000000081526004018080602001828103825260168152602001807f4f6e6c792073656c6c65722063616e2063616e63656c0000000000000000000081525060200191505060405180910390fd5b6001600460146101000a81548160ff02191690836002811115610a2457fe5b0217905550565b600460149054906101000a900460ff1681565b600260009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff163373ffffffffffffffffffffffffffffffffffffffff16141515610b03576040517f08c379a000000000000000000000000000000000000000000000000000000000815260040180806020018281038252601c8152602001807f4f6e6c792062757965722063616e20667265657a6520746f6b656e730000000081525060200191505060405180910390fd5b600460009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff166323b872dd600260009054906101000a900473ffffffffffffffffffffffffffffffffffffffff16306000546040518463ffffffff167c0100000000000000000000000000000000000000000000000000000000028152600401808473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020018373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff168152602001828152602001935050505060206040518083038186803b158015610c1e57600080fd5b505afa158015610c32573d6000803e3d6000fd5b505050506040513d6020811015610c4857600080fd5b81019080805190602001909291905050505056fea165627a7a72305820c7c745243087adc4bd539db244e32c343457daed5fd9359cf5daf7fa120cab790029'''

    def deploy(self, buyer, seller, mediator, value):

        current_web3.eth.defaultAccount = buyer
        order_contract = current_web3.eth.contract(abi=self.contract_abi, bytecode=self.compiled)

        transaction = order_contract.constructor(price=value, miloAdress="0xfa8b724558412CD5f2E07cAF2337885dA13864D5",
                                            sellerAddress=seller, mediatorAddress=mediator).\
            buildTransaction({
            'from': buyer,  # Only 'from' address, don't insert 'to' address
            'value': 0,  # Add how many ethers you'll transfer during the deploy
            'gas': 6903259,  # Trying to make it dynamic ..
            'gasPrice': current_web3.eth.gasPrice * 30,  # Get Gas Price
            'nonce': current_web3.eth.getTransactionCount(buyer),  # Get Nonce
        })

        signed = current_web3.eth.account.signTransaction(transaction,'d0eaed9b1a4633b358208793a96aba7fd42547472682a2e6fe73cf3ababef3fc')
        tx_hash = current_web3.eth.sendRawTransaction(signed.rawTransaction)
        print("contract deploy")
        print(tx_hash.hex())
        tx_reciept = current_web3.eth.waitForTransactionReceipt(tx_hash)
        print(tx_reciept)
        print(tx_reciept.contractAddress)
        return tx_reciept.contractAddress


    def freezeTokens(self, buyer, contract_address):
        contract = current_web3.eth.contract(abi=self.contract_abi, address=contract_address)
        tx = contract.functions.freezeTokens().buildTransaction({
            'from': buyer,  # Only 'from' address, don't insert 'to' address
            'value': 0,  # Add how many ethers you'll transfer during the deploy
            'gas': 5903259,  # Trying to make it dynamic ..
            'gasPrice': current_web3.eth.gasPrice * 30,  # Get Gas Price
            'nonce': current_web3.eth.getTransactionCount(buyer),
        })
        signed = current_web3.eth.account.signTransaction(tx, 'd0eaed9b1a4633b358208793a96aba7fd42547472682a2e6fe73cf3ababef3fc')
        tx_hash = current_web3.eth.sendRawTransaction(signed.rawTransaction)
        print("freeze tokens")
        print(tx_hash.hex())
        tx_reciept = current_web3.eth.waitForTransactionReceipt(tx_hash)
        print(tx_reciept)


    def confirmRecieved(self, current_order_state, buyer_private_key, contract_address, buyer):
        if current_order_state == 2:
            print("already confirmed recieving")
            return 2
        else:
            buyer_private_key = 'd0eaed9b1a4633b358208793a96aba7fd42547472682a2e6fe73cf3ababef3fc'
            contract = current_web3.eth.contract(abi=self.contract_abi, address=contract_address)
            tx = contract.functions.confirmRecieved().buildTransaction({
                'from': buyer,  # Only 'from' address, don't insert 'to' address
                'value': 0,  # Add how many ethers you'll transfer during the deploy
                'gas': 5903259,  # Trying to make it dynamic ..
                'gasPrice': current_web3.eth.gasPrice * 30,  # Get Gas Price
                'nonce': current_web3.eth.getTransactionCount(buyer),
            })
            signed = current_web3.eth.account.signTransaction(tx, buyer_private_key)
            tx_hash = current_web3.eth.sendRawTransaction(signed.rawTransaction)
            print("confirm recieved")
            print(tx_hash.hex())
            tx_reciept = current_web3.eth.waitForTransactionReceipt(tx_hash)
            print(tx_reciept)
            if current_order_state == 1:
                return 3
            elif current_order_state == 0:
                return 2


    def confirmSupplied(self, current_order_state, seller, seller_private_key, contract_address):
        if current_order_state == 1:
            print("already confirmed supplying")
            return 1
        elif current_order_state == 2:
            seller_private_key = '28c6015bea8a8c6eec5b8d7cd9b4e6b58a5a63ccaa6ab9af398c9fa362094d76'
            contract = current_web3.eth.contract(abi=self.contract_abi, address=contract_address)
            tx = contract.functions.confirmSupplied().buildTransaction({
                'from': seller,  # Only 'from' address, don't insert 'to' address
                'value': 0,  # Add how many ethers you'll transfer during the deploy
                'gas': 5903259,  # Trying to make it dynamic ..
                'gasPrice': current_web3.eth.gasPrice * 30,  # Get Gas Price
                'nonce': current_web3.eth.getTransactionCount(seller),
            })
            signed = current_web3.eth.account.signTransaction(tx, seller_private_key)
            tx_hash = current_web3.eth.sendRawTransaction(signed.rawTransaction)
            print("confirm supplied")
            print(tx_hash.hex())
            tx_reciept = current_web3.eth.waitForTransactionReceipt(tx_hash)
            print(tx_reciept)
            if current_order_state == 0:
                return 1
            elif current_order_state == 2:
                return 3











