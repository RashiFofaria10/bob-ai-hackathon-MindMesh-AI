from typing import Dict, List


def match_fleet(
    shipment: Dict,
    vehicles: List[Dict],
) -> Dict:

    candidates = []

    shipment_requires_cold_chain = shipment.get(
        "coldChainCapable",
        False,
    )

    shipment_capacity = float(
        shipment.get("requiredCapacity", 0)
    )

    for vehicle in vehicles:

        # Only available vehicles can be assigned
        if vehicle.get("status") != "available":
            continue

        score = 0
        reasons = []

        # -----------------------------
        # 1. Cold-chain compatibility
        # -----------------------------

        if shipment_requires_cold_chain:

            if vehicle.get("coldChainCapable", False):
                score += 35
                reasons.append(
                    "Vehicle supports cold-chain transportation"
                )
            else:
                score -= 40
                reasons.append(
                    "Vehicle does not support cold-chain transportation"
                )

        # -----------------------------
        # 2. Capacity
        # -----------------------------

        capacity_text = str(
            vehicle.get("capacity", "0")
        )

        capacity_value = float(
            capacity_text.split()[0]
        )

        if capacity_value >= shipment_capacity:
            score += 25
            reasons.append(
                "Vehicle has sufficient capacity"
            )
        else:
            score -= 30
            reasons.append(
                "Vehicle capacity is insufficient"
            )

        # -----------------------------
        # 3. Reliability
        # -----------------------------

        reliability = float(
            vehicle.get("reliability", 0)
        )

        reliability_score = reliability * 0.25

        score += reliability_score

        if reliability >= 90:
            reasons.append(
                f"High reliability ({reliability:.0f}%)"
            )

        # -----------------------------
        # 4. Utilization
        # -----------------------------

        utilization = float(
            vehicle.get("utilization", 100)
        )

        if utilization <= 30:
            score += 15
            reasons.append(
                "Vehicle has low utilization and is available"
            )

        # -----------------------------
        # Final candidate
        # -----------------------------

        candidates.append({
            "vehicleId": vehicle.get("id"),
            "type": vehicle.get("type"),
            "location": vehicle.get("location"),
            "capacity": vehicle.get("capacity"),
            "reliability": reliability,
            "score": round(score, 2),
            "reasons": reasons,
        })

    if not candidates:
        return {
            "recommendedVehicle": None,
            "alternatives": [],
            "reason": "No suitable available vehicle found.",
        }

    candidates.sort(
        key=lambda x: x["score"],
        reverse=True,
    )

    best_vehicle = candidates[0]

    return {
        "recommendedVehicle": best_vehicle,
        "alternatives": candidates,
        "reason": (
            f"Vehicle {best_vehicle['vehicleId']} "
            f"is the best available match based on "
            f"capacity, compatibility, reliability, and utilization."
        ),
    }


if __name__ == "__main__":

    shipment = {
        "id": "SH1024",
        "cargo": "Electronics",
        "coldChainCapable": True,
        "requiredCapacity": 10,
    }

    vehicles = [
        {
            "id": "VH-021",
            "type": "Refrigerated Truck",
            "location": "Mundra Hub",
            "capacity": "14 tons",
            "status": "available",
            "utilization": 12,
            "coldChainCapable": True,
            "reliability": 96,
        },
        {
            "id": "VH-087",
            "type": "Reefer Truck",
            "location": "Pune",
            "capacity": "12 tons",
            "status": "available",
            "utilization": 28,
            "coldChainCapable": True,
            "reliability": 94,
        },
        {
            "id": "VH-114",
            "type": "Dry Van",
            "location": "Mumbai",
            "capacity": "18 tons",
            "status": "assigned",
            "utilization": 80,
            "coldChainCapable": False,
            "reliability": 88,
        },
        {
            "id": "VH-208",
            "type": "Volvo FH16",
            "location": "Rotterdam",
            "capacity": "22 tons",
            "status": "maintenance",
            "utilization": 0,
            "coldChainCapable": False,
            "reliability": 91,
        },
    ]

    result = match_fleet(
        shipment,
        vehicles,
    )

    print("ChainGuard AI - Fleet Matching")
    print("=" * 60)

    if result["recommendedVehicle"]:

        vehicle = result["recommendedVehicle"]

        print(
            f"Recommended Vehicle: "
            f"{vehicle['vehicleId']}"
        )

        print(
            f"Type: {vehicle['type']}"
        )

        print(
            f"Location: {vehicle['location']}"
        )

        print(
            f"Capacity: {vehicle['capacity']}"
        )

        print(
            f"Reliability: {vehicle['reliability']:.0f}%"
        )

        print(
            f"Match Score: {vehicle['score']}"
        )

        print("\nReasons:")

        for reason in vehicle["reasons"]:
            print(f"  - {reason}")

    print("\nAll Available Candidates:")

    for vehicle in result["alternatives"]:
        print(
            f"  {vehicle['vehicleId']} | "
            f"Score: {vehicle['score']} | "
            f"Reliability: {vehicle['reliability']:.0f}%"
        )