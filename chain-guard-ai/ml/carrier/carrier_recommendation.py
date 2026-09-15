from typing import Dict, List


def recommend_carrier(
    carriers: List[Dict],
    reliability_weight: float = 0.4,
    delay_weight: float = 0.3,
    cost_weight: float = 0.15,
    availability_weight: float = 0.15,
) -> Dict:

    recommendations = []

    for carrier in carriers:

        # --------------------------------
        # Reliability Score
        # --------------------------------

        reliability = float(
            carrier.get("reliability", 0)
        )

        reliability_score = reliability

        # --------------------------------
        # Delay Score
        # Lower delay = better score
        # --------------------------------

        predicted_delay = float(
            carrier.get("predictedDelay", 0)
        )

        delay_score = max(
            100 - (predicted_delay * 10),
            0
        )

        # --------------------------------
        # Cost Score
        # Lower cost = better score
        # --------------------------------

        cost_delta = float(
            carrier.get("costDelta", 0)
        )

        # Convert cost difference into a
        # simple 0-100 score.
        cost_score = max(
            100 - (cost_delta * 10),
            0
        )

        # --------------------------------
        # Availability Score
        # --------------------------------

        availability = str(
            carrier.get("availability", "limited")
        ).lower()

        if availability == "available":
            availability_score = 100
        elif availability == "limited":
            availability_score = 50
        else:
            availability_score = 0

        # --------------------------------
        # Final Carrier Score
        # --------------------------------

        total_score = (
            reliability_score * reliability_weight
            + delay_score * delay_weight
            + cost_score * cost_weight
            + availability_score * availability_weight
        )

        # --------------------------------
        # Explainable Reasons
        # --------------------------------

        reasons = []

        if reliability >= 90:
            reasons.append(
                f"High reliability ({reliability:.0f}%)"
            )
        elif reliability >= 80:
            reasons.append(
                f"Good reliability ({reliability:.0f}%)"
            )
        else:
            reasons.append(
                f"Lower reliability ({reliability:.0f}%)"
            )

        if predicted_delay <= 3:
            reasons.append(
                f"Low predicted delay ({predicted_delay:.1f} hours)"
            )
        elif predicted_delay <= 6:
            reasons.append(
                f"Moderate predicted delay ({predicted_delay:.1f} hours)"
            )
        else:
            reasons.append(
                f"High predicted delay ({predicted_delay:.1f} hours)"
            )

        if availability == "available":
            reasons.append(
                "Carrier is currently available"
            )
        elif availability == "limited":
            reasons.append(
                "Carrier has limited availability"
            )
        else:
            reasons.append(
                "Carrier is currently unavailable"
            )

        recommendations.append({
            "carrier": carrier.get("carrier"),
            "reliability": reliability,
            "predictedDelay": predicted_delay,
            "costDelta": cost_delta,
            "availability": availability,
            "score": round(total_score, 2),
            "reasons": reasons,
        })

    # --------------------------------
    # Sort by best score
    # --------------------------------

    recommendations.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    if not recommendations:
        return {
            "recommendedCarrier": None,
            "alternatives": [],
            "reason": "No carrier data available.",
        }

    best_carrier = recommendations[0]

    return {
        "recommendedCarrier": best_carrier,
        "alternatives": recommendations,
        "reason": (
            f"Carrier {best_carrier['carrier']} provides "
            f"the best balance of reliability, delay, "
            f"cost, and availability."
        ),
    }


if __name__ == "__main__":

    carriers = [
        {
            "carrier": "Maersk Line",
            "reliability": 94,
            "availability": "available",
            "costDelta": 0,
            "predictedDelay": 8.2,
        },
        {
            "carrier": "CMA CGM",
            "reliability": 91,
            "availability": "available",
            "costDelta": 4,
            "predictedDelay": 2.1,
        },
        {
            "carrier": "Hapag-Lloyd",
            "reliability": 87,
            "availability": "limited",
            "costDelta": -2,
            "predictedDelay": 4.3,
        },
    ]

    result = recommend_carrier(carriers)

    print("ChainGuard AI - Carrier Recommendation")
    print("=" * 60)

    carrier = result["recommendedCarrier"]

    if carrier:

        print(
            f"Recommended Carrier: "
            f"{carrier['carrier']}"
        )

        print(
            f"Reliability: "
            f"{carrier['reliability']:.0f}%"
        )

        print(
            f"Predicted Delay: "
            f"{carrier['predictedDelay']} hours"
        )

        print(
            f"Cost Delta: "
            f"{carrier['costDelta']:+.0f}%"
        )

        print(
            f"Availability: "
            f"{carrier['availability'].upper()}"
        )

        print(
            f"Carrier Score: "
            f"{carrier['score']}"
        )

        print("\nReasons:")

        for reason in carrier["reasons"]:
            print(f"  - {reason}")

    print("\nAll Carriers:")

    for carrier in result["alternatives"]:

        print(
            f"  {carrier['carrier']} | "
            f"Score: {carrier['score']} | "
            f"Reliability: "
            f"{carrier['reliability']:.0f}% | "
            f"Delay: "
            f"{carrier['predictedDelay']}h"
        )