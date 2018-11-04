pragma solidity ^0.4.0;
contract Milo{
    address owner;
    mapping (address => uint) public balances;
    mapping(address => mapping (address => uint)) allowed;
    
    string public constant name = "Milo";
    uint public constant supply = 1000000;
    uint8 public constant decimals = 0;
    
    constructor() public{
        owner = msg.sender;
        balances[owner] = 1000000;
    }
    
    function totalSupply() public view returns (uint a){
        return supply;
    }
    
    function transferFrom(address from, address to, uint tokens) public returns (bool success){
        success = false;
        require(0x0 != to, "You do not want to send to 0 address!");
        require(balances[from] >= tokens, "Not enough MILO");
        require(allowed[from][to] >= tokens, "Not allowed to transfer this amount");
        allowed[from][to] = allowed[from][to] - tokens;
        balances[from] = balances[from] - tokens;
        balances[to] = balances[to] + tokens;
        return true;
    }
    
    function balance(address account) public view returns (uint accountBalance){
        accountBalance = balances[account];
        return accountBalance;
    }
    
    function transfer(address to, uint tokens) public returns (bool success){
        success = false;
        require(0x0 != to, "You do not want to send to 0 address!");
        require(balances[msg.sender] >= tokens, "Not enough MILO");
        balances[msg.sender] = balances[msg.sender] - tokens;
        balances[to] = balances[to] + tokens;
        return true;
    }
    function approve(address spender, uint tokens) public returns (bool success){
        success = false;
        allowed[msg.sender][spender] = allowed[msg.sender][spender] + tokens;
        return true;
    }
    function allowance(address tokenOwner, address spender) public constant returns (uint remaining){
        return allowed[tokenOwner][spender];
    }
}
