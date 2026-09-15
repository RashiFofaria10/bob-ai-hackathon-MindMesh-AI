from shipment_risk import calculate_shipment_risk


test_shipments = [
    {
        "id": "SH1021",
        "predictedDelay": 2.1,
        "coldChainCapable": True,
    },
    {
        "id": "SH1019",
        "predictedDelay": 1.2,
        "coldChainCapable": False,
    },
    {
        "id": "SH1013",
        "predictedDelay": 4.8,
        "coldChainCapable": False,
    },
    {
        "id": "SH1024",
        "predictedDelay": 8.2,
        "coldChainCapable": True,
    },
]


test_cases = [
    {
        "severity": "low",
        "route_risk": 2,
        "deadline_pressure": 1,
    },
    {
        "severity": "low",
        "route_risk": 3,
        "deadline_pressure": 2,
    },
    {
        "severity": "medium",
        "route_risk": 8,
        "deadline_pressure": 5,
    },
    {
        "severity": "critical",
        "route_risk": 15,
        "deadline_pressure": 10,
    },
]


print("ChainGuard AI - Risk Model Test")
print("=" * 60)

for shipment, case in zip(test_shipments, test_cases):

    result = calculate_shipment_risk(
        shipment=shipment,
        disruption=case,
        route_risk=case["route_risk"],
        deadline_pressure=case["deadline_pressure"],
    )

    print(
        f"{result['shipmentId']:8} | "
        f"Score: {result['riskScore']:3}/100 | "
        f"Level: {result['riskLevel'].upper()}"
    )