# Solution Overview

## What We Built

ChainGuard AI is an AI-powered supply-chain control tower designed to help businesses monitor shipments, identify risks, detect disruptions, and make faster logistics decisions from a single platform.

The system brings together shipment information, disruption events, fleet availability, cold-chain temperature data, risk analysis, recommendations, and conversational AI. Instead of manually checking different sources and analysing supply-chain problems, users can view important information through one dashboard and use the IBM Bob assistant to ask supply-chain related questions in natural language.

ChainGuard AI helps users understand which shipments or operations require attention, why a risk exists, and what actions can be considered, such as alternative routes, carrier changes, or fleet redeployment.

## How It Works

1. The user opens the ChainGuard AI web application and interacts with the React-based dashboard.
2. The frontend sends requests to the Node.js and Express backend through REST APIs.
3. The backend retrieves and manages supply-chain information stored in MongoDB.
4. Shipment, disruption, fleet, and cold-chain information is processed by the AI/ML layer.
5. The AI/ML layer evaluates supply-chain conditions and generates risk scores, severity levels, disruption analysis, and recommendations.
6. The processed information is returned to the frontend and displayed through dashboards, charts, alerts, and recommendation cards.
7. For conversational queries, the user interacts with IBM Bob through the application.
8. The backend sends the relevant user request and supply-chain context to IBM Bob.
9. IBM Bob generates a natural-language response that helps the user understand the situation and make supply-chain decisions.
10. The final information is displayed to the user through the ChainGuard AI interface.

## Architecture Diagram

> See [`architecture.md`](architecture.md) for the detailed architecture diagram.

```text
[User / Browser]
        |
        v
[React Frontend]
        |
        | REST API
        v
[Node.js / Express Backend]
        |
        +--------------------+
        |                    |
        v                    v
   [MongoDB]           [AI / ML Engine]
                             |
                             v
                      [Risk Analysis &
                       Recommendations]
        |
        v
    [IBM Bob]
        |
        v
[AI Decision Support]
        |
        v
[React Dashboard]
