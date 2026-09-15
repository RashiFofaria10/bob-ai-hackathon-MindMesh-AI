# ChainGuard AI — AI/ML Module

## Overview

The AI/ML module of ChainGuard AI analyzes supply-chain conditions and produces explainable risk scores and operational recommendations.

The module contains five main capabilities:

1. Shipment Risk Prediction
2. Route Recommendation
3. Carrier Recommendation
4. Fleet Matching
5. Cold-Chain Anomaly Detection and Severity Classification

The current implementation uses explainable scoring and rule-based decision models with Python. These models are designed to be connected to the application backend.

---

## Technology

* Python 3.12
* NumPy
* pandas
* scikit-learn
* Python standard library
* JSON-compatible input/output

---

## 1. Shipment Risk Prediction

### File

`ml/risk/shipment_risk.py`

### Purpose

Calculates the risk level of a shipment based on operational factors.

### Inputs

* Shipment information
* Disruption severity
* Predicted delay
* Cargo temperature sensitivity
* Route risk
* Deadline pressure

### Risk components

| Component         | Maximum Score |
| ----------------- | ------------: |
| Disruption Risk   |            40 |
| Delay Risk        |            20 |
| Cargo Sensitivity |            15 |
| Route Risk        |            15 |
| Deadline Pressure |            10 |
| Total             |           100 |

### Risk levels

* 0–39: Low
* 40–59: Medium
* 60–79: High
* 80–100: Critical

### Example

For shipment `SH1024`:

* Critical disruption
* 8.2 hour predicted delay
* Temperature-sensitive cargo
* High route risk
* High deadline pressure

Result:

`96/100 — CRITICAL`

The model also generates human-readable reasons explaining why the shipment received its score.

---

## 2. Route Recommendation

### File

`ml/routing/route_recommendation.py`

### Purpose

Selects the best alternative route by balancing:

* Route risk
* Predicted delay
* Cost

### Default weights

| Factor | Weight |
| ------ | -----: |
| Risk   |    50% |
| Delay  |    30% |
| Cost   |    20% |

The route with the lowest combined score is selected.

### Example

For the Mumbai → Frankfurt scenario:

`R-ALT-1`

was selected because it provides the best balance between risk, delay, and cost.

---

## 3. Carrier Recommendation

### File

`ml/carrier/carrier_recommendation.py`

### Purpose

Ranks available carriers according to operational suitability.

### Factors

* Reliability
* Predicted delay
* Cost difference
* Availability

### Default weights

| Factor       | Weight |
| ------------ | -----: |
| Reliability  |    40% |
| Delay        |    30% |
| Cost         |    15% |
| Availability |    15% |

### Example

The test scenario selected:

`CMA CGM`

with a carrier score of `84.1`.

---

## 4. Fleet Matching

### File

`ml/fleet/fleet_matching.py`

### Purpose

Matches an available vehicle with a shipment.

### Factors

* Cold-chain compatibility
* Vehicle capacity
* Reliability
* Current utilization
* Availability

Vehicles that are not available are automatically excluded.

### Example

For a temperature-sensitive shipment requiring 10 tons:

`VH-021`

was selected.

Its properties include:

* Refrigerated vehicle
* 14 ton capacity
* 96% reliability
* 12% utilization
* Available

This makes it a strong candidate for urgent cold-chain redeployment.

---

## 5. Cold-Chain Anomaly Detection

### File

`ml/cold_chain/anomaly_detection.py`

### Purpose

Detects temperature readings outside the allowed range.

Example safe range:

`2°C – 8°C`

For the test readings:

`3.8, 4.1, 4.0, 5.4, 7.9, 9.7, 8.4, 6.1`

the system detected:

* 2 anomalous readings
* 25% anomaly rate
* WARNING status

The abnormal readings were:

* 9.7°C
* 8.4°C

---

## 6. Temperature Severity Classification

### File

`ml/cold_chain/severity.py`

### Purpose

Determines how serious a temperature excursion is.

The classification considers:

* Temperature deviation from the safe range
* Duration of the excursion

Possible results:

* NORMAL
* MEDIUM
* HIGH
* CRITICAL

Example:

Current temperature: `9.7°C`

Safe maximum: `8°C`

Deviation: `1.7°C`

Duration: `18 minutes`

Result:

`HIGH`

---

## 7. Integrated AI Pipeline

### File

`ml/pipeline.py`

The pipeline combines all AI components.

```text
Shipment Data
      +
Disruption Data
      +
Route Data
      +
Carrier Data
      +
Fleet Data
      +
Temperature Data
      ↓
AI PIPELINE
      ↓
Shipment Risk
      ↓
Route Recommendation
      ↓
Carrier Recommendation
      ↓
Fleet Matching
      ↓
Temperature Anomaly Detection
      ↓
Temperature Severity
      ↓
Final AI Decision
```

The complete pipeline can be executed using:

```powershell
python ml\pipeline.py
```

---

## 8. Multi-Scenario Testing

### File

`ml/test_pipeline.py`

Four scenarios were tested.

| Scenario                                    | Risk Score | Risk Level | Temperature | Vehicle |
| ------------------------------------------- | ---------: | ---------- | ----------- | ------- |
| Critical disruption + temperature excursion |         96 | CRITICAL   | HIGH        | VH-021  |
| Low-risk shipment + normal temperature      |         37 | LOW        | NORMAL      | VH-021  |
| High delay + high disruption                |         68 | HIGH       | CRITICAL    | VH-301  |
| Cold-chain temperature warning              |         64 | HIGH       | MEDIUM      | VH-021  |

All four scenarios completed successfully.

Run the test suite with:

```powershell
python ml\test_pipeline.py
```

---

## 9. Explainable AI

A major feature of the AI module is explainability.

Instead of returning only:

```text
Risk = 96
```

the system explains the contributing factors:

```text
- Critical disruption affects the shipment route
- Predicted delay is high
- Shipment contains temperature-sensitive cargo
- Current route has elevated disruption exposure
- Delivery deadline is approaching
```

This allows logistics operators to understand why the AI recommends an action.

---

## 10. Example AI Decision

For a high-risk shipment affected by a critical disruption:

```text
Shipment Risk:
96/100 — CRITICAL

Recommended Route:
R-ALT-1

Recommended Carrier:
CMA CGM

Recommended Vehicle:
VH-021

Cold-Chain Severity:
HIGH
```

This produces an operational decision rather than only a prediction.

---

## 11. Important Note

The current risk, route, carrier, fleet, and temperature modules are explainable scoring/decision models.

They are not presented as trained machine-learning models with real-world accuracy metrics.

The architecture is designed so that trained ML models can be introduced later when sufficient historical shipment and sensor data becomes available.

---

## 12. Running the AI Module

From the project root:

```powershell
cd E:\chain-guard-ai
```

Activate the environment if required:

```powershell
.venv\Scripts\Activate.ps1
```

Run the integrated pipeline:

```powershell
python ml\pipeline.py
```

Run multi-scenario testing:

```powershell
python ml\test_pipeline.py
```

---

## AI/ML Contribution Summary

Person 3 implemented:

* Explainable shipment risk scoring
* Route optimization/recommendation
* Carrier recommendation
* Idle fleet matching
* Cold-chain temperature anomaly detection
* Temperature severity classification
* Integrated AI pipeline
* Multi-scenario testing
* Explainable AI reasoning

These outputs can be consumed by the backend and displayed by the ChainGuard AI control tower.
