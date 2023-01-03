In this step, you have to host your images and metadata to IPFS network, so that they can be used in the DApp. As a gateway for IPFS, you can use service like [Pinata](https://www.pinata.cloud/), that will help you to pin files on the IPFS. Assume it like Google Drive or Dropbox, with the difference that it puts your all files on IPFS network, with peer to peer distribution.

In order to upload all your files to Pinata IPFS, follow these steps:

1. Upload entire `nfts` folder, which is present under `src/assets` folder to IPFS network. After uploading, you will get a Content ID. 

2. You can then reference your files using this URL scheme: https://gateway.pinata.cloud/ipfs/{content_id}/{file_name}.{file_type}. For example, if your Content ID is xxxxxxxyyyyyyyyzzzzzz and file is 1.png, then your URL would be: https://gateway.pinata.cloud/ipfs/xxxxxxxyyyyyyyyzzzzzz/1.png

You can now use hosted images as NFTs and their metadata in the DApp.