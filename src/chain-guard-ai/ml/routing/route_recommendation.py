from typing import Dict, List


def recommend_route(
    routes: List[Dict],
    risk_weight: float = 0.5,
    delay_weight: float = 0.3,
    cost_weight: float = 0.2,
) -> Dict:

    recommendations = []

    for route in routes:

        # Risk score
        risk_values = {
            "low": 20,
            "medium": 50,
            "high": 75,
            "critical": 100,
        }

        risk_score = risk_values.get(
            route.get("riskLevel", "medium").lower(),
            50,
        )

        # Normalize delay to 0-100
        delay = float(route.get("predictedDelay", 0))
        delay_score = min(delay * 10, 100)

        # Normalize cost relative to 50,000
        cost = float(route.get("cost", 0))
        cost_score = min((cost / 50000) * 100, 100)

        # Lower is better
        total_score = (
            risk_score * risk_weight
            + delay_score * delay_weight
            + cost_score * cost_weight
        )

        recommendations.append({
            "routeId": route.get("id"),
            "origin": route.get("origin"),
            "destination": route.get("destination"),
            "riskLevel": route.get("riskLevel"),
            "predictedDelay": delay,
            "cost": cost,
            "score": round(total_score, 2),
        })

    # Lowest score = best route
    recommendations.sort(key=lambda x: x["score"])

    best_route = recommendations[0]

    return {
        "recommendedRoute": best_route,
        "alternatives": recommendations,
        "reason": (
            f"Route {best_route['routeId']} provides the best "
            f"balance of risk, delay, and cost."
        ),
    }


if __name__ == "__main__":

    routes = [
        {
            "id": "R-ALT-1",
            "origin": "Mumbai",
            "destination": "Frankfurt",
            "predictedDelay": 2.1,
            "cost": 48000,
            "riskLevel": "low",
        },
        {
            "id": "R-ALT-2",
            "origin": "Mumbai",
            "destination": "Frankfurt",
            "predictedDelay": 4.2,
            "cost": 52000,
            "riskLevel": "medium",
        },
        {
            "id": "R-ALT-3",
            "origin": "Mumbai",
            "destination": "Frankfurt",
            "predictedDelay": 6.8,
            "cost": 45000,
            "riskLevel": "high",
        },
    ]

    result = recommend_route(routes)

    print("ChainGuard AI - Route Recommendation")
    print("=" * 60)

    print(
        f"Recommended Route: "
        f"{result['recommendedRoute']['routeId']}"
    )

    print(
        f"Route Score: "
        f"{result['recommendedRoute']['score']}"
    )

    print(
        f"Risk Level: "
        f"{result['recommendedRoute']['riskLevel'].upper()}"
    )

    print(
        f"Predicted Delay: "
        f"{result['recommendedRoute']['predictedDelay']} hours"
    )

    print(
        f"Cost: "
        f"${result['recommendedRoute']['cost']:,.0f}"
    )

    print(f"\nReason:")
    print(f"  {result['reason']}")

    print("\nAll Routes:")

    for route in result["alternatives"]:
        print(
            f"  {route['routeId']} | "
            f"Score: {route['score']} | "
            f"Risk: {route['riskLevel']} | "
            f"Delay: {route['predictedDelay']}h | "
            f"Cost: ${route['cost']:,.0f}"
        )