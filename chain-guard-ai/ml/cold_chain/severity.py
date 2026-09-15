def classify_temperature_severity(
    current_temp: float,
    safe_min: float,
    safe_max: float,
    excursion_duration: float,
) -> dict:

    # Calculate how far the temperature is outside
    # the safe range.

    if current_temp > safe_max:
        deviation = current_temp - safe_max

    elif current_temp < safe_min:
        deviation = safe_min - current_temp

    else:
        deviation = 0

    # --------------------------------
    # Severity classification
    # --------------------------------

    if deviation == 0:

        severity = "normal"

    elif deviation >= 3 or excursion_duration >= 30:

        severity = "critical"

    elif deviation >= 1.5 or excursion_duration >= 15:

        severity = "high"

    else:

        severity = "medium"

    # --------------------------------
    # Generate explanation
    # --------------------------------

    reasons = []

    if deviation > 0:
        reasons.append(
            f"Temperature is {deviation:.1f}°C "
            f"outside the safe range"
        )

    if excursion_duration >= 15:
        reasons.append(
            f"Temperature excursion lasted "
            f"{excursion_duration:.0f} minutes"
        )

    if not reasons:
        reasons.append(
            "Temperature is within the safe range"
        )

    return {
        "severity": severity,
        "currentTemperature": current_temp,
        "safeRange": {
            "min": safe_min,
            "max": safe_max,
        },
        "deviation": round(deviation, 2),
        "excursionDuration": excursion_duration,
        "reasons": reasons,
    }


if __name__ == "__main__":

    current_temp = 9.7
    safe_min = 2.0
    safe_max = 8.0
    excursion_duration = 18

    result = classify_temperature_severity(
        current_temp=current_temp,
        safe_min=safe_min,
        safe_max=safe_max,
        excursion_duration=excursion_duration,
    )

    print("ChainGuard AI - Temperature Severity")
    print("=" * 60)

    print(
        f"Current Temperature: "
        f"{result['currentTemperature']}°C"
    )

    print(
        f"Safe Range: "
        f"{result['safeRange']['min']}°C - "
        f"{result['safeRange']['max']}°C"
    )

    print(
        f"Deviation: "
        f"{result['deviation']}°C"
    )

    print(
        f"Excursion Duration: "
        f"{result['excursionDuration']} minutes"
    )

    print(
        f"Severity: "
        f"{result['severity'].upper()}"
    )

    print("\nReasons:")

    for reason in result["reasons"]:
        print(f"  - {reason}")