class OpenRouterPricingTrackerClient:
    def estimate_cost(self, model_name: str, input_tokens: int, output_tokens: int) -> dict:
        rate = 0.000015 if "claude" in model_name else 0.000002
        cost = (input_tokens + output_tokens) * rate
        return {"estimated_cost_usd": round(cost, 6)}