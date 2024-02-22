// Install ethers.js using: npm install ethers

import { ethers } from 'ethers';

// Ethereum mainnet provider
const provider = new ethers.providers.JsonRpcProvider('https://mainnet.infura.io/v3/your-infura-api-key');

// USDT contract address and ABI
const usdtAddress = '0xdac17f958d2ee523a2206206994597c13d831ec7';
const usdtAbi = [
  'function balanceOf(address) view returns (uint256)',
];

// Ethereum address to check USDT balance
const userAddress = '0x1234567890123456789012345678901234567890';

// Function to get the last block number of Ethereum mainnet
async function getLastBlockNumber() {
  const blockNumber = await provider.getBlockNumber();
  console.log('Last Block Number:', blockNumber);
}

// Function to get USDT balance of a provided address
async function getUsdtBalance() {
  const usdtContract = new ethers.Contract(usdtAddress, usdtAbi, provider);
  const balance = await usdtContract.balanceOf(userAddress);
  console.log('USDT Balance:', ethers.utils.formatUnits(balance, 6));
}

// Unit test using Jest
describe('Ethereum Webpage', () => {
  test('Get Last Block Number', async () => {
    await getLastBlockNumber();
  });

  test('Get USDT Balance', async () => {
    await getUsdtBalance();
  });
});
