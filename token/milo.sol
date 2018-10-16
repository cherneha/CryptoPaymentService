pragma solidity ^0.4.0;
contract Milo {
    address owner;
    mapping (address => uint64) public balances;
    string name;
    
    constructor(uint64 initialSupply){
        name = "Milo";
        owner = msg.sender;
        balances[owner] = initialSupply;
    }
    
    function transfer(address to, address from, uint64 quantity){
        require(0x0 != to, "You do not want to send to 0 address!");
        require(balances[from] >= quantity, "Not enough MILO");
        
        balances[from] = balances[from] - quantity;
        balances[to] = balances[to] + quantity;
    }
    
    function balance(address account) returns (uint64 accountBalance){
        return balances[account];
    }
}
