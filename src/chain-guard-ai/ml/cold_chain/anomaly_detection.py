from typing import Dict, List


def detect_temperature_anomalies(
    temperatures: List[float],
    safe_min: float,
    safe_max: float,
) -> Dict:

    anomalies = []

    for index, temperature in enumerate(temperatures):

        if temperature < safe_min:
            anomalies.append({
                "index": index,
                "temperature": temperature,
                "type": "below_range",
            })

        elif temperature > safe_max:
            anomalies.append({
                "index": index,
                "temperature": temperature,
                "type": "above_range",
            })

    total_readings = len(temperatures)

    anomaly_count = len(anomalies)

    if anomaly_count == 0:
        status = "normal"

    elif anomaly_count <= 2:
        status = "warning"

    else:
        status = "critical"

    anomaly_percentage = 0

    if total_readings > 0:
        anomaly_percentage = (
            anomaly_count / total_readings
        ) * 100

    return {
        "status": status,
        "totalReadings": total_readings,
        "anomalyCount": anomaly_count,
        "anomalyPercentage": round(
            anomaly_percentage,
            2,
        ),
        "anomalies": anomalies,
    }


if __name__ == "__main__":

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

    safe_min = 2.0
    safe_max = 8.0

    result = detect_temperature_anomalies(
        temperatures,
        safe_min,
        safe_max,
    )

    print("ChainGuard AI - Cold Chain Anomaly Detection")
    print("=" * 60)

    print(
        f"Status: {result['status'].upper()}"
    )

    print(
        f"Total Readings: "
        f"{result['totalReadings']}"
    )

    print(
        f"Anomalies Detected: "
        f"{result['anomalyCount']}"
    )

    print(
        f"Anomaly Percentage: "
        f"{result['anomalyPercentage']}%"
    )

    print("\nDetected Anomalies:")

    if result["anomalies"]:

        for anomaly in result["anomalies"]:

            print(
                f"  Reading {anomaly['index'] + 1}: "
                f"{anomaly['temperature']}°C "
                f"({anomaly['type']})"
            )

    else:
        print("  No temperature anomalies detected.")