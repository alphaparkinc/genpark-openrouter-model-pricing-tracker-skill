from client import OpenRouterPricingTrackerClient
client = OpenRouterPricingTrackerClient()
print(client.estimate_cost("anthropic/claude-3", 1000, 500))