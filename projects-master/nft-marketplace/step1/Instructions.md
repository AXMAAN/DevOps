In this step, you need to complete the smart contract by making three functions that will be actively used in the DApp.

1. A function that will check if an NFT is already owned. This can be achieved by making a mapping of existing URIs, and then checking if corresponding value of URI in the mapping is equal to 1.  

    ```solidity
    mapping(string => uint8) existingURIs;
    ```

    ```solidity
    function isContentOwned(string memory uri) public view returns (bool){
        return existingURIs[uri] == 1;
    }
    ```

2. A function that will transfer NFT to the account, if the amount paid by that account is equal to the price of NFT. You can hard code the amount of each NFT that you want user to pay in order to mint an NFT. This function should also ensure that NFT that is being minted should not be owned by someone else. Here is something you can do.

    ```solidity
        function payToMint(address recipient, string memory metadataURI) public payable returns (uint256){
            require(existingURIs[metadataURI] != 1, "NFT is already minted");
            require(msg.value >= 0.05 ether, "Price is too low");

            uint256 newItemId = _tokenIdCounter.current();
            _tokenIdCounter.increment();
            existingURIs[metadataURI] = 1;

            _mint(recipient, newItemId);
            _setTokenURI(newItemId, metadataURI);
            return newItemId;
        }
    ```

3. A function that will return you current token ID.

    ```solidity
        function count() public view returns (uint256){
            return _tokenIdCounter.current();
        }
    ```

These three functions will be used actively in the DApp. Now that you have added these functions, compile the Solidity code and deploy the smart contract on the local Hardhat blockchain using `scripts/deploy.js` script. You will receive the address of the contract after deployment is successful. You will also get the contract ABI in `src/artifacts` directory, which you can use in frontend code.