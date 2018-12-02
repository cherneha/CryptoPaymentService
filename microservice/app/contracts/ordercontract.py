from flask_web3 import current_web3

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

    compiled = '''608060405234801561001057600080fd5b50604051608080611146833981018060405281019080805190602001909291908051906020019092919080519060200190929190805190602001909291905050506000600460146101000a81548160ff0219169083600281111561007057fe5b021790555033600260006101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff16021790555081600160006101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff16021790555080600360006101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff1602179055508360008190555082600460006101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff16021790555050505050610fb3806101936000396000f3006080604052600436106100af576000357c0100000000000000000000000000000000000000000000000000000000900463ffffffff16806308551a53146100b457806334f013b11461010b5780633fa4f24514610122578063590e1ae31461014d5780636a816548146101645780636d0501f61461017b5780637150d8ae146101d25780637700985b146102295780638aeb870714610240578063c19d93fb14610297578063da9f4875146102d0575b600080fd5b3480156100c057600080fd5b506100c96102ff565b604051808273ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200191505060405180910390f35b34801561011757600080fd5b50610120610325565b005b34801561012e57600080fd5b50610137610535565b6040518082815260200191505060405180910390f35b34801561015957600080fd5b5061016261053b565b005b34801561017057600080fd5b506101796107e8565b005b34801561018757600080fd5b50610190610972565b604051808273ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200191505060405180910390f35b3480156101de57600080fd5b506101e7610998565b604051808273ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200191505060405180910390f35b34801561023557600080fd5b5061023e6109be565b005b34801561024c57600080fd5b50610281600480360381019080803573ffffffffffffffffffffffffffffffffffffffff169060200190929190505050610aa9565b6040518082815260200191505060405180910390f35b3480156102a357600080fd5b506102ac610c6f565b604051808260028111156102bc57fe5b60ff16815260200191505060405180910390f35b3480156102dc57600080fd5b506102e5610c82565b604051808215151515815260200191505060405180910390f35b600160009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1681565b600260009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff163373ffffffffffffffffffffffffffffffffffffffff161415156103ea576040517f08c379a000000000000000000000000000000000000000000000000000000000815260040180806020018281038252601c8152602001807f4f6e6c792062757965722063616e20667265657a6520746f6b656e730000000081525060200191505060405180910390fd5b6002600460146101000a81548160ff0219169083600281111561040957fe5b0217905550600460009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1663a9059cbb600160009054906101000a900473ffffffffffffffffffffffffffffffffffffffff166000546040518363ffffffff167c0100000000000000000000000000000000000000000000000000000000028152600401808373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200182815260200192505050602060405180830381600087803b1580156104f757600080fd5b505af115801561050b573d6000803e3d6000fd5b505050506040513d602081101561052157600080fd5b810190808051906020019092919050505050565b60005481565b600360009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff163373ffffffffffffffffffffffffffffffffffffffff16141515610600576040517f08c379a00000000000000000000000000000000000000000000000000000000081526004018080602001828103825260188152602001807f4f6e6c79206d65646961746f722063616e20726566756e64000000000000000081525060200191505060405180910390fd5b60028081111561060c57fe5b600460149054906101000a900460ff16600281111561062757fe5b1415151561069d576040517f08c379a00000000000000000000000000000000000000000000000000000000081526004018080602001828103825260198152602001807f43616e6e6f7420726566756264206f6e20696e6163746976650000000000000081525060200191505060405180910390fd5b600460009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1663a9059cbb600260009054906101000a900473ffffffffffffffffffffffffffffffffffffffff166000546040518363ffffffff167c0100000000000000000000000000000000000000000000000000000000028152600401808373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200182815260200192505050602060405180830381600087803b15801561078657600080fd5b505af115801561079a573d6000803e3d6000fd5b505050506040513d60208110156107b057600080fd5b8101908080519060200190929190505050506002600460146101000a81548160ff021916908360028111156107e157fe5b0217905550565b600160009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff163373ffffffffffffffffffffffffffffffffffffffff161415156108ad576040517f08c379a00000000000000000000000000000000000000000000000000000000081526004018080602001828103825260168152602001807f4f6e6c792073656c6c65722063616e2063616e63656c0000000000000000000081525060200191505060405180910390fd5b60008060028111156108bb57fe5b600460149054906101000a900460ff1660028111156108d657fe5b14151561094b576040517f08c379a000000000000000000000000000000000000000000000000000000000815260040180806020018281038252600e8152602001807f496e76616c69642073746174652e00000000000000000000000000000000000081525060200191505060405180910390fd5b6002600460146101000a81548160ff0219169083600281111561096a57fe5b021790555050565b600360009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1681565b600260009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1681565b600160009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff163373ffffffffffffffffffffffffffffffffffffffff16141515610a83576040517f08c379a00000000000000000000000000000000000000000000000000000000081526004018080602001828103825260168152602001807f4f6e6c792073656c6c65722063616e2063616e63656c0000000000000000000081525060200191505060405180910390fd5b6001600460146101000a81548160ff02191690836002811115610aa257fe5b0217905550565b6000600260009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff163373ffffffffffffffffffffffffffffffffffffffff16141515610b70576040517f08c379a000000000000000000000000000000000000000000000000000000000815260040180806020018281038252601c8152602001807f4f6e6c792062757965722063616e20667265657a6520746f6b656e730000000081525060200191505060405180910390fd5b600460009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1663e3d670d7836040518263ffffffff167c0100000000000000000000000000000000000000000000000000000000028152600401808273ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff168152602001915050602060405180830381600087803b158015610c2d57600080fd5b505af1158015610c41573d6000803e3d6000fd5b505050506040513d6020811015610c5757600080fd5b81019080805190602001909291905050509050919050565b600460149054906101000a900460ff1681565b600080600260009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff163373ffffffffffffffffffffffffffffffffffffffff16141515610d4a576040517f08c379a000000000000000000000000000000000000000000000000000000000815260040180806020018281038252601c8152602001807f4f6e6c792062757965722063616e20667265657a6520746f6b656e730000000081525060200191505060405180910390fd5b7f581c981ddd793bb7b396d073f80e214ab99fd327cc1b5d49c242d61fd6bbecce6040518080602001828103825260068152602001807f696e64697365000000000000000000000000000000000000000000000000000081525060200191505060405180910390a1600460009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff166323b872dd600260009054906101000a900473ffffffffffffffffffffffffffffffffffffffff16306000546040518463ffffffff167c0100000000000000000000000000000000000000000000000000000000028152600401808473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020018373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020018281526020019350505050602060405180830381600087803b158015610ecf57600080fd5b505af1158015610ee3573d6000803e3d6000fd5b505050506040513d6020811015610ef957600080fd5b810190808051906020019092919050505090507fa60d3dbb9f5af52b29a8900e86e50b1db063a3a5e423763dde35a03657417eb681604051808060200183151515158152602001828103825260058152602001807f656e6465640000000000000000000000000000000000000000000000000000008152506020019250505060405180910390a180915050905600a165627a7a72305820e7d5ca93814ff75a8b337d02dd78c294f03b3b5cef6ebf63bd4cff4f01bb33250029'''
    def deploy(self, buyer, seller, mediator, value, buyer_key):
        token_adress = current_web3.toChecksumAddress('0xf66b8916918daef2ed5678ff29b634c5e9229395')

        current_web3.eth.defaultAccount = buyer
        order_contract = current_web3.eth.contract(abi=self.contract_abi, bytecode=self.compiled)
        print(seller)
        transaction = order_contract.constructor(price=value, miloAdress=token_adress,
                                            sellerAddress=seller,
                                                 mediatorAddress=mediator).\
            buildTransaction({
            'from': buyer,  # Only 'from' address, don't insert 'to' address
            'value': 0,  # Add how many ethers you'll transfer during the deploy
            'gas': 6903259,  # Trying to make it dynamic ..
            'gasPrice': current_web3.eth.gasPrice * 30,  # Get Gas Price
            'nonce': current_web3.eth.getTransactionCount(buyer),  # Get Nonce
        })

        signed = current_web3.eth.account.signTransaction(transaction, buyer_key)
        tx_hash = current_web3.eth.sendRawTransaction(signed.rawTransaction)
        print("contract deploy")
        print(tx_hash.hex())
        tx_reciept = current_web3.eth.waitForTransactionReceipt(tx_hash)
        print(tx_reciept)
        print(tx_reciept.contractAddress)
        return tx_reciept.contractAddress


    def freezeTokens(self, buyer, contract_address, buyer_key):
        contract = current_web3.eth.contract(abi=self.contract_abi, address=contract_address)
        tx = contract.functions.freezeTokens().buildTransaction({
            'from': buyer,  # Only 'from' address, don't insert 'to' address
            'value': 0,  # Add how many ethers you'll transfer during the deploy
            'gas': 5903259,  # Trying to make it dynamic ..
            'gasPrice': current_web3.eth.gasPrice * 30,  # Get Gas Price
            'nonce': current_web3.eth.getTransactionCount(buyer),
        })
        signed = current_web3.eth.account.signTransaction(tx, buyer_key)
        tx_hash = current_web3.eth.sendRawTransaction(signed.rawTransaction)
        print("freeze tokens")
        print(tx_hash.hex())
        tx_reciept = current_web3.eth.waitForTransactionReceipt(tx_hash)
        print(tx_reciept)


    def confirmRecieved(self, current_order_state, buyer, buyer_private_key, contract_address):

        # current_web3.middleware_stack.inject(current_web3.middleware.geth_poa_middleware, layer=0)
        if current_order_state == 3:
            print("already confirmed recieving")
            return 3
        else:
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
            if current_order_state == 2:
                return 4
            elif current_order_state == 1:
                return 3


    def confirmSupplied(self, current_order_state, seller, seller_private_key, contract_address):
        if current_order_state == 2:
            print("already confirmed supplying")
            return 2
        else:
            contract = current_web3.eth.contract(abi=self.contract_abi, address=contract_address)
            print("after contract")
            tx = contract.functions.confirmSupplied().buildTransaction({
                'from': seller,  # Only 'from' address, don't insert 'to' address
                'value': 0,  # Add how many ethers you'll transfer during the deploy
                'gas': 5903259,  # Trying to make it dynamic ..
                'gasPrice': current_web3.eth.gasPrice * 30,  # Get Gas Price
                'nonce': current_web3.eth.getTransactionCount(seller),
            })
            print("after build")
            signed = current_web3.eth.account.signTransaction(tx, seller_private_key)
            tx_hash = current_web3.eth.sendRawTransaction(signed.rawTransaction)
            print("confirm supplied")
            print(tx_hash.hex())
            tx_reciept = current_web3.eth.waitForTransactionReceipt(tx_hash)
            print(tx_reciept)
            if current_order_state == 1:
                return 2
            elif current_order_state == 3:
                return 4

