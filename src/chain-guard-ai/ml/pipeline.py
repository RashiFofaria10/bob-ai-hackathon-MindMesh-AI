import sys
import json
from pathlib import Path

# Allow imports from the ml directory
ML_DIR = Path(__file__).resolve().parent

if str(ML_DIR) not in sys.path:
    sys.path.insert(0, str(ML_DIR))

from risk.shipment_risk import calculate_shipment_risk
from routing.route_recommendation import recommend_route
from carrier.carrier_recommendation import recommend_carrier
from fleet.fleet_matching import match_fleet
from cold_chain.anomaly_detection import detect_temperature_anomalies
from cold_chain.severity import classify_temperature_severity


def run_chainguard_ai(
    shipment,
    disruption,
    routes,
    carriers,
    vehicles,
    temperatures,
    safe_min,
    safe_max,
    excursion_duration,
    route_risk=15,
    deadline_pressure=10,
):
    # --------------------------------
    # 1. Shipment Risk
    # --------------------------------

    risk_result = calculate_shipment_risk(
        shipment=shipment,
        disruption=disruption,
        route_risk=route_risk,
        deadline_pressure=deadline_pressure,
    )

    # --------------------------------
    # 2. Route Recommendation
    # --------------------------------

    route_result = recommend_route(
        routes=routes
    )

    # --------------------------------
    # 3. Carrier Recommendation
    # --------------------------------

    carrier_result = recommend_carrier(
        carriers=carriers
    )

    # --------------------------------
    # 4. Fleet Matching
    # --------------------------------

    fleet_result = match_fleet(
        shipment=shipment,
        vehicles=vehicles,
    )

    # --------------------------------
    # 5. Temperature Anomaly Detection
    # --------------------------------

    anomaly_result = detect_temperature_anomalies(
        temperatures=temperatures,
        safe_min=safe_min,
        safe_max=safe_max,
    )

    # --------------------------------
    # 6. Temperature Severity
    # --------------------------------

    if temperatures:
        current_temperature = max(temperatures)
    else:
        current_temperature = safe_min

    severity_result = classify_temperature_severity(
        current_temp=current_temperature,
        safe_min=safe_min,
        safe_max=safe_max,
        excursion_duration=excursion_duration,
    )

    # --------------------------------
    # Combined AI Result
    # --------------------------------

    return {
        "shipmentRisk": risk_result,
        "routeRecommendation": route_result,
        "carrierRecommendation": carrier_result,
        "fleetRecommendation": fleet_result,
        "temperatureAnomaly": anomaly_result,
        "temperatureSeverity": severity_result,
    }


def run_from_json():
    """
    Read JSON from stdin, run the ChainGuard AI pipeline,
    and return the result as JSON.
    """

    try:
        input_data = sys.stdin.read()

        if not input_data.strip():
            raise ValueError("No JSON input received.")

        data = json.loads(input_data)

        required_fields = [
            "shipment",
            "disruption",
            "routes",
            "carriers",
            "vehicles",
            "temperatures",
            "safe_min",
            "safe_max",
            "excursion_duration",
        ]

        missing_fields = [
            field
            for field in required_fields
            if field not in data
        ]

        if missing_fields:
            raise ValueError(
                f"Missing required fields: {', '.join(missing_fields)}"
            )

        result = run_chainguard_ai(
            shipment=data["shipment"],
            disruption=data["disruption"],
            routes=data["routes"],
            carriers=data["carriers"],
            vehicles=data["vehicles"],
            temperatures=data["temperatures"],
            safe_min=data["safe_min"],
            safe_max=data["safe_max"],
            excursion_duration=data["excursion_duration"],
            route_risk=data.get("route_risk", 15),
            deadline_pressure=data.get("deadline_pressure", 10),
        )

        response = {
            "success": True,
            "result": result,
        }

        print(json.dumps(response, indent=2))

    except Exception as error:
        response = {
            "success": False,
            "error": str(error),
        }

        print(json.dumps(response, indent=2))
        sys.exit(1)


# ============================================
# Manual AI/ML Test
# ============================================

def run_manual_test():

    shipment = {
        "id": "SH1024",
        "cargo": "Electronics",
        "predictedDelay": 8.2,
        "coldChainCapable": True,
        "requiredCapacity": 10,
    }

    disruption = {
        "severity": "critical",
    }

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
    ]

    temperatures = [
        3.8,
        4.1,
        4.0,
        5.4,
        7.9,
        9.7,
        8.4,
        6.1,
    ]

    result = run_chainguard_ai(
        shipment=shipment,
        disruption=disruption,
        routes=routes,
        carriers=carriers,
        vehicles=vehicles,
        temperatures=temperatures,
        safe_min=2.0,
        safe_max=8.0,
        excursion_duration=18,
        route_risk=15,
        deadline_pressure=10,
    )

    print()
    print("ChainGuard AI - Integrated Pipeline")
    print("=" * 70)

    risk = result["shipmentRisk"]

    print()
    print("SHIPMENT RISK")
    print("-" * 70)
    print(f"Shipment: {risk['shipmentId']}")
    print(f"Risk Score: {risk['riskScore']}/100")
    print(f"Risk Level: {risk['riskLevel'].upper()}")

    print()
    print("Risk Reasons:")

    for reason in risk["reasons"]:
        print(f"  - {reason}")

    route_result = result["routeRecommendation"]
    route = route_result["recommendedRoute"]

    print()
    print("ROUTE RECOMMENDATION")
    print("-" * 70)
    print(f"Recommended Route: {route['routeId']}")
    print(f"Route Score: {route['score']}")
    print(f"Risk: {route['riskLevel'].upper()}")
    print(f"Predicted Delay: {route['predictedDelay']} hours")
    print(f"Cost: ${route['cost']:,.0f}")

    print()
    print(f"Reason: {route_result['reason']}")

    carrier_result = result["carrierRecommendation"]
    carrier = carrier_result["recommendedCarrier"]

    print()
    print("CARRIER RECOMMENDATION")
    print("-" * 70)

    if carrier:
        print(f"Recommended Carrier: {carrier['carrier']}")
        print(f"Reliability: {carrier['reliability']:.0f}%")
        print(f"Predicted Delay: {carrier['predictedDelay']} hours")
        print(f"Cost Delta: {carrier['costDelta']:+.0f}%")
        print(f"Availability: {carrier['availability'].upper()}")
        print(f"Carrier Score: {carrier['score']}")

    fleet_result = result["fleetRecommendation"]
    vehicle = fleet_result["recommendedVehicle"]

    print()
    print("FLEET RECOMMENDATION")
    print("-" * 70)

    if vehicle:
        print(f"Recommended Vehicle: {vehicle['vehicleId']}")
        print(f"Type: {vehicle['type']}")
        print(f"Location: {vehicle['location']}")
        print(f"Capacity: {vehicle['capacity']}")
        print(f"Reliability: {vehicle['reliability']:.0f}%")
        print(f"Match Score: {vehicle['score']}")
    else:
        print("No suitable vehicle found.")

    anomaly = result["temperatureAnomaly"]

    print()
    print("COLD CHAIN ANOMALY DETECTION")
    print("-" * 70)
    print(f"Total Readings: {anomaly['totalReadings']}")
    print(f"Anomalies: {anomaly['anomalyCount']}")
    print(f"Anomaly Percentage: {anomaly['anomalyPercentage']}%")
    print(f"Status: {anomaly['status'].upper()}")

    severity = result["temperatureSeverity"]

    print()
    print("TEMPERATURE SEVERITY")
    print("-" * 70)
    print(f"Current Temperature: {severity['currentTemperature']}°C")
    print(
        f"Safe Range: "
        f"{severity['safeRange']['min']}°C - "
        f"{severity['safeRange']['max']}°C"
    )
    print(f"Deviation: {severity['deviation']}°C")
    print(
        f"Excursion Duration: "
        f"{severity['excursionDuration']} minutes"
    )
    print(f"Severity: {severity['severity'].upper()}")

    print()
    print("AI DECISION SUMMARY")
    print("-" * 70)

    print(
        f"1. {risk['shipmentId']} risk is "
        f"{risk['riskLevel'].upper()} "
        f"({risk['riskScore']}/100)"
    )

    print(f"2. Use route {route['routeId']}")

    if carrier:
        print(f"3. Use carrier {carrier['carrier']}")

    if vehicle:
        print(f"4. Deploy vehicle {vehicle['vehicleId']}")

    print(
        f"5. Cold-chain severity is "
        f"{severity['severity'].upper()}"
    )

    print()
    print("=" * 70)
    print("ChainGuard AI pipeline completed successfully.")


if __name__ == "__main__":

    # If JSON is provided through stdin, use JSON API mode.
    # Otherwise, run the normal manual demonstration.
    if not sys.stdin.isatty():
        run_from_json()
    else:
        run_manual_test()