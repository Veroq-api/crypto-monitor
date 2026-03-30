"""Live crypto monitor — prices, DeFi, sentiment."""
from veroq import VeroqClient

client = VeroqClient()

print("Crypto Market Overview\n")
result = client.ask("Top crypto prices and DeFi overview")
data = result.get("data", {})

tokens = data.get("crypto", {}).get("tokens", [])
if tokens:
    print(f"{'Token':8s} {'Price':>12s} {'24h':>8s} {'Market Cap':>14s}")
    print("-" * 46)
    for t in tokens[:10]:
        sym = t.get("symbol", "?")
        price = t.get("price", 0)
        change = t.get("change_24h", 0)
        mcap = t.get("market_cap", 0)
        mcap_str = f"${mcap/1e9:.1f}B" if mcap > 1e9 else f"${mcap/1e6:.0f}M"
        print(f"{sym:8s} ${price:>11,.2f} {change:>+7.2f}% {mcap_str:>14s}")

# Verify a crypto claim
print("\nFact check:")
v = client.verify("Bitcoin is trading above $60,000")
print(f"  {v['verdict'].upper()} ({v['confidence']*100:.0f}% confidence)")
