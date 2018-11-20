import solc
from app.routes import current_web3

class OrderManager:

    contract_source_code = '''
        
        pragma solidity ^0.4.0;
        contract Milo{
            constructor() public{}
            function totalSupply() public view returns (uint a){}
            function transferFrom(address from, address to, uint tokens) public pure returns (bool success){}
            function balance(address account) public view returns (uint accountBalance){}
            function transfer(address to, uint tokens) public pure returns (bool success){}
            function approve(address spender, uint tokens) public pure returns (bool success){}
            function allowance(address tokenOwner, address spender) public constant returns (uint remaining){}
        }
        
        contract Order{
            uint public value;
            address public seller;
            address public buyer;
            address public mediator;
            Milo miloContract;
            
            enum State { Opened, SellerConfirmed, Inactive }
            State public state;
            
            constructor(uint price, address miloAddress, address sellerAddress, address mediatorAddress) public{
                state = State.Opened;
                buyer = msg.sender;
                seller = sellerAddress;
                mediator = mediatorAddress;
                value = price;
                miloContract = Milo(miloAddress);
            
            }
            modifier inState(State _state) {
                require(
                    state == _state,
                    "Invalid state."
                );
                _;
            }
            
            modifier onlySeller(){
                require(msg.sender == seller, "Only seller can cancel");
                _;
            }
            
            modifier onlyBuyer(){
                require(msg.sender == buyer, "Only buyer can freeze tokens");
                _;
            }
            
            modifier buyerOrMediator(){
                require((msg.sender == buyer) || (msg.sender == mediator), 
                "Only buyer and mediator can confirm recieved");
                _;
            }
            
            modifier onlyMediator(){
                require(msg.sender == mediator, "Only mediator can refund");
                _;
            }
            
            function cancelOrder() public onlySeller inState(State.Opened){
                state = State.Inactive;
            }
            
            function freezeTokens() onlyBuyer{
                miloContract.transferFrom(buyer, this, value);
            }
            
            function confirmRecieved() public onlyBuyer{
                state = State.Inactive;
                miloContract.transfer(seller, value);
            }
            
            function confirmSupplied() public onlySeller{
                state = State.SellerConfirmed;
            }
            
            function getPrice() public view returns (uint a){
                return value;
            }
            
            function refund() onlyMediator {
                require(state != State.Inactive,
                "Cannot refubd on inactive");
                miloContract.transfer(buyer, value);
                state = State.Inactive;
            }   
        }    
            '''

    def deploy(self, buyer, seller, mediator, value):
        compiled_sol = solc.compile_source(self.contract_source_code)  # Compiled source code
        contract_interface = compiled_sol['<stdin>:Order']
        current_web3.eth.defaultAccount = buyer
        Order = current_web3.eth.contract(abi=contract_interface['abi'], bytecode=contract_interface['bin'])
        tx_hash = Order.constructor(price=value, miloAddress="0xfa8b724558412CD5f2E07cAF2337885dA13864D5",
                                    sellerAddress=seller, mediatorAddress=mediator).transact()
        tx_receipt = current_web3.eth.waitForTransactionReceipt(tx_hash)
        self.order = current_web3.eth.contract(
            address=tx_receipt.contractAddress,
            abi=contract_interface['abi'],
        )

        print('Default contract greeting: {}'.format(
            self.order.functions.getPrice().call()
        ))

    def freezeTokens(self, buyer):
        tx_hash = self.order.functions.freezeTokens().transact({"from" : buyer})
        current_web3.eth.waitForTransactionReceipt(tx_hash)



