# Crypto Monitor

[![License](https://img.shields.io/badge/license-MIT-2EE89A)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.9+-2EE89A)](https://python.org)
[![VEROQ](https://img.shields.io/badge/powered%20by-VEROQ-2EE89A)](https://veroq.ai)

Live crypto monitoring -- prices, DeFi TVL, sentiment, and claim verification. Powered by [VEROQ](https://veroq.ai).

## Quick Start

```bash
pip install veroq
export VEROQ_API_KEY=vq_live_xxx
python monitor.py
```

## Example Output

```
Crypto Market Overview

Token      Price         24h     Market Cap
----------------------------------------------
BTC      $ 66,605.00  +0.96%        $1.3T
ETH      $  3,412.00  -1.20%      $410.5B
USDT     $      1.00  +0.01%      $144.2B
BNB      $    608.50  +2.10%       $88.7B
XRP      $      0.52  -0.85%       $28.9B
SOL      $    147.30  +3.40%       $68.2B
...

Fact check:
  SUPPORTED (78% confidence)
```

## Features

- Real-time crypto prices (200+ tokens)
- DeFi TVL overview
- 24h change tracking with market cap
- Claim verification for crypto headlines
- Multi-provider data (Binance, CoinGecko, Coinbase)

## Links

- [VEROQ](https://veroq.ai) | [Python SDK](https://github.com/Veroq-api/veroq-python) | [Cookbook](https://github.com/Veroq-api/veroq-cookbook)