from pipeline import run_chainguard_ai


def print_separator():
    print("-" * 70)


def run_scenario(name, shipment, disruption, temperatures, excursion_duration):
    print()
    print("=" * 70)
    print(f"SCENARIO: {name}")
    print("=" * 70)

    routes = [
        {
            "id": "R-ALT-1",
            "origin": shipment["origin"],
            "destination": shipment["destination"],
            "predictedDelay": 2.1,
            "cost": 48000,
            "riskLevel": "low",
        },
        {
            "id": "R-ALT-2",
            "origin": shipment["origin"],
            "destination": shipment["destination"],
            "predictedDelay": 4.2,
            "cost": 52000,
            "riskLevel": "medium",
        },
        {
            "id": "R-ALT-3",
            "origin": shipment["origin"],
            "destination": shipment["destination"],
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
        {
            "id": "VH-301",
            "type": "Dry Van",
            "location": "Mumbai",
            "capacity": "20 tons",
            "status": "available",
            "utilization": 20,
            "coldChainCapable": False,
            "reliability": 90,
        },
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
        excursion_duration=excursion_duration,
    )

    risk = result["shipmentRisk"]
    route = result["routeRecommendation"]["recommendedRoute"]
    carrier = result["carrierRecommendation"]["recommendedCarrier"]
    vehicle = result["fleetRecommendation"]["recommendedVehicle"]
    anomaly = result["temperatureAnomaly"]
    severity = result["temperatureSeverity"]

    print_separator()

    print(f"Shipment: {risk['shipmentId']}")
    print(f"Risk Score: {risk['riskScore']}/100")
    print(f"Risk Level: {risk['riskLevel'].upper()}")

    print()

    print(f"Recommended Route: {route['routeId']}")
    print(f"Recommended Carrier: {carrier['carrier']}")

    if vehicle:
        print(f"Recommended Vehicle: {vehicle['vehicleId']}")
    else:
        print("Recommended Vehicle: None")

    print()

    print(f"Temperature Anomalies: {anomaly['anomalyCount']}")
    print(f"Temperature Status: {anomaly['status'].upper()}")
    print(f"Temperature Severity: {severity['severity'].upper()}")

    print_separator()


# ============================================================
# Scenario 1: Critical disruption
# ============================================================

scenario_1_shipment = {
    "id": "TEST-001",
    "origin": "Mumbai",
    "destination": "Frankfurt",
    "cargo": "Temperature Sensitive Cargo",
    "predictedDelay": 8.2,
    "coldChainCapable": True,
    "requiredCapacity": 10,
}

scenario_1_disruption = {
    "severity": "critical",
}

scenario_1_temperatures = [
    3.8,
    4.1,
    4.0,
    5.4,
    7.9,
    9.7,
    8.4,
    6.1,
]


run_scenario(
    "Critical disruption + temperature excursion",
    scenario_1_shipment,
    scenario_1_disruption,
    scenario_1_temperatures,
    18,
)


# ============================================================
# Scenario 2: Low-risk shipment
# ============================================================

scenario_2_shipment = {
    "id": "TEST-002",
    "origin": "Singapore",
    "destination": "London",
    "cargo": "Textiles",
    "predictedDelay": 1.0,
    "coldChainCapable": False,
    "requiredCapacity": 8,
}

scenario_2_disruption = {
    "severity": "low",
}

scenario_2_temperatures = [
    4.0,
    4.2,
    4.1,
    4.3,
    4.2,
    4.1,
]


run_scenario(
    "Low-risk shipment + normal temperature",
    scenario_2_shipment,
    scenario_2_disruption,
    scenario_2_temperatures,
    0,
)


# ============================================================
# Scenario 3: High delay
# ============================================================

scenario_3_shipment = {
    "id": "TEST-003",
    "origin": "Busan",
    "destination": "Long Beach",
    "cargo": "Automotive Parts",
    "predictedDelay": 6.5,
    "coldChainCapable": False,
    "requiredCapacity": 15,
}

scenario_3_disruption = {
    "severity": "high",
}

scenario_3_temperatures = [
    20.0,
    21.0,
    20.5,
    21.2,
]


run_scenario(
    "High delay + high disruption",
    scenario_3_shipment,
    scenario_3_disruption,
    scenario_3_temperatures,
    0,
)


# ============================================================
# Scenario 4: Cold-chain warning
# ============================================================

scenario_4_shipment = {
    "id": "TEST-004",
    "origin": "Shenzhen",
    "destination": "Rotterdam",
    "cargo": "Pharmaceuticals",
    "predictedDelay": 2.1,
    "coldChainCapable": True,
    "requiredCapacity": 8,
}

scenario_4_disruption = {
    "severity": "medium",
}

scenario_4_temperatures = [
    3.5,
    4.0,
    4.5,
    8.9,
    7.5,
    6.0,
]


run_scenario(
    "Cold-chain temperature warning",
    scenario_4_shipment,
    scenario_4_disruption,
    scenario_4_temperatures,
    10,
)


print()
print("=" * 70)
print("ALL CHAINGUARD AI TEST SCENARIOS COMPLETED")
print("=" * 70)