In this step, we will be working on frontend of DApp using React. Now that you have a smart contract deployed and NFT images along with their metadata hosted on IPFS, it is time to design our frontend and use web3 functionalities to carry out transactions.

In order to make the frontend for the DApp, follow these instructions:

1. First of all, check if any Ethereum wallet is found by DApp. If it finds one, render the UI. If it doesn't, redirect the user to Metamask's installation page. 

2. Prepare the UI for DApp by taking reference from the provided UI Reference. You can use Material UI or any other UI library to help you get the desired UI easily, or you can choose to design the UI from scratch, whatever suits you the best.

3. Use `window.ethereum` object to request connection with a Ethereum Wallet. You can also use this object to check what is current balance of user's wallet, and display the connected wallet address along with its balance in the DApp.

4. Create an instance of the deployed contract, which can be used to call functions created by you in the smart contract. You need to use the address of the deployed smart contract, the ABI of deployed smart contract and the Signer, which is the account interacting with smart contract, to achieve this functionality.

5. Now, make use of `map()` of JavaScript in order to map over all NFT minted along with NFT which is next to be minted (as shown in UI Reference). Make a card that will have the NFT Image along with its Token ID. If the NFT is already minted, show a disabled button of `Already Minted`, else show an enabled `Mint` button.

6. On the `Mint` button, add an onClick listener, that will call `payToMint()` function of smart contract to make the transaction. The Token ID for each minted NFT can be obtained from `count()` function of smart contract. The ownership status of each NFT can be obtained from `isContentOwned()` of smart contract.

7. Display the NFT Image after user has successfully made the transaction. Use the IPFS address of image to render the NFT Image. Also, display a question mark logo (which can be obtained from `src/assets`) on NFT which will be minted next.