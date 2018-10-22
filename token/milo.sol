pragma solidity ^0.4.0;
contract Milo{
    address owner;
    mapping (address => uint64) public balances;
    string name;
    uint256 supply;
    
    constructor() public{
        name = "Milo";
        owner = msg.sender;
        balances[owner] = 1000000;
        supply = 1000000;
    }
    
    function totalSupply() public constant returns (uint256 a){
        a = supply;
        return a;
    }
    
    function transfer(address to, address from, uint64 quantity) public{
        require(0x0 != to, "You do not want to send to 0 address!");
        require(balances[from] >= quantity, "Not enough MILO");
        
        balances[from] = balances[from] - quantity;
        balances[to] = balances[to] + quantity;
    }
    
    function balance(address account) public view returns (uint64 accountBalance){
        accountBalance = balances[account];
        return accountBalance;
    }
}
