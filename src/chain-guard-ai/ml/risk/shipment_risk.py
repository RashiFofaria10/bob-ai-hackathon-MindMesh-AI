from typing import Dict, List


def calculate_shipment_risk(
    shipment: Dict,
    disruption: Dict | None = None,
    route_risk: float = 0,
    deadline_pressure: float = 0,
) -> Dict:

    reasons: List[str] = []

    # -----------------------------
    # 1. Disruption risk
    # -----------------------------

    disruption_score = 0

    if disruption:
        severity = disruption.get("severity", "low").lower()

        severity_scores = {
            "low": 10,
            "medium": 20,
            "high": 30,
            "critical": 40,
        }

        disruption_score = severity_scores.get(severity, 0)

        if severity in {"high", "critical"}:
            reasons.append(
                f"{severity.capitalize()} disruption affects the shipment route"
            )

    # -----------------------------
    # 2. Delay risk
    # -----------------------------

    predicted_delay = float(
        shipment.get("predictedDelay", 0)
    )

    delay_score = min(predicted_delay * 2, 20)

    if predicted_delay >= 6:
        reasons.append(
            f"Predicted delay is high ({predicted_delay:.1f} hours)"
        )
    elif predicted_delay >= 3:
        reasons.append(
            f"Predicted delay is moderate ({predicted_delay:.1f} hours)"
        )

    # -----------------------------
    # 3. Cargo sensitivity
    # -----------------------------

    cargo_score = 0

    cold_chain = shipment.get(
        "coldChainCapable",
        False
    )

    if cold_chain:
        cargo_score = 15
        reasons.append(
            "Shipment contains temperature-sensitive cargo"
        )

    # -----------------------------
    # 4. Route risk
    # -----------------------------

    route_score = min(
        max(float(route_risk), 0),
        15
    )

    if route_score >= 10:
        reasons.append(
            "Current route has elevated disruption exposure"
        )

    # -----------------------------
    # 5. Deadline pressure
    # -----------------------------

    deadline_score = min(
        max(float(deadline_pressure), 0),
        10
    )

    if deadline_score >= 7:
        reasons.append(
            "Delivery deadline is approaching"
        )

    # -----------------------------
    # Final score
    # -----------------------------

    raw_score = (
        disruption_score
        + delay_score
        + cargo_score
        + route_score
        + deadline_score
    )

    risk_score = round(
        min(raw_score, 100)
    )

    # -----------------------------
    # Risk classification
    # -----------------------------

    if risk_score >= 80:
        risk_level = "critical"

    elif risk_score >= 60:
        risk_level = "high"

    elif risk_score >= 40:
        risk_level = "medium"

    else:
        risk_level = "low"

    return {
        "shipmentId": shipment.get("id"),
        "riskScore": risk_score,
        "riskLevel": risk_level,
        "reasons": reasons,
        "components": {
            "disruptionRisk": disruption_score,
            "delayRisk": round(delay_score, 2),
            "cargoSensitivity": cargo_score,
            "routeRisk": round(route_score, 2),
            "deadlinePressure": round(deadline_score, 2),
        },
    }


if __name__ == "__main__":

    example_shipment = {
        "id": "SH1024",
        "predictedDelay": 8.2,
        "coldChainCapable": True,
    }

    example_disruption = {
        "severity": "critical",
    }

    result = calculate_shipment_risk(
        shipment=example_shipment,
        disruption=example_disruption,
        route_risk=15,
        deadline_pressure=10,
    )

    print("ChainGuard AI - Shipment Risk")
    print("=" * 50)

    print(f"Shipment: {result['shipmentId']}")
    print(f"Risk Score: {result['riskScore']}/100")
    print(f"Risk Level: {result['riskLevel'].upper()}")

    print("\nRisk Components:")

    for key, value in result["components"].items():
        print(f"  {key}: {value}")

    print("\nReasons:")

    for reason in result["reasons"]:
        print(f"  - {reason}")