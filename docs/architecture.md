# Architecture

## System Architecture

ChainGuard AI is an AI-powered supply-chain control tower that connects the frontend, backend, database, AI/ML processing, and IBM Bob conversational assistant. Users interact with the React frontend, which communicates with the Node.js/Express backend through REST APIs. The backend manages supply-chain data, performs AI/ML analysis, communicates with MongoDB, and integrates IBM Bob for conversational decision support.

```mermaid
graph TD
    A[User / Browser] -->|HTTP / HTTPS| B[Frontend - React]
    B -->|REST API| C[Backend - Node.js / Express]
    C -->|Query / Update| D[MongoDB]
    C -->|Analyze Supply Chain Data| E[AI / ML]
    E -->|Risk Scores / Recommendations| C
    C -->|AI Request| F[IBM Bob]
    F -->|AI Response| C
    C -->|JSON Response| B
    B -->|Dashboard / Alerts / Analytics| A

## Components

| Component    | Technology                                        | Responsibility                                                                                                     |
| ------------ | ------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------ |
| Frontend     | React, TypeScript, Tailwind CSS, shadcn/ui        | Dashboard UI, user interaction, supply-chain monitoring, analytics, and visualization                              |
| Backend API  | Node.js, Express.js                               | Business logic, REST APIs, data processing, and orchestration                                                      |
| AI / ML      | Machine Learning, Risk Scoring, Anomaly Detection | Shipment risk assessment, disruption analysis, cold-chain monitoring, severity classification, and recommendations |
| Database     | MongoDB, Mongoose                                 | Storing shipment, fleet, disruption, temperature, and supply-chain data                                            |
| AI Assistant | IBM Bob                                           | Conversational AI and natural-language supply-chain decision support                                               |


## Data Flow
ChainGuard AI receives user requests through the React frontend and sends them to the Node.js/Express backend through REST APIs.

The user interacts with the ChainGuard AI dashboard through the React frontend.
The frontend sends requests to the backend through REST APIs.
The backend retrieves relevant supply-chain data from MongoDB.
Shipment, disruption, fleet, and cold-chain data are processed by the AI/ML layer.
The AI/ML layer generates risk scores, disruption analysis, severity levels, and recommendations.
For conversational queries, the backend sends the request and relevant context to IBM Bob.
IBM Bob returns an AI-generated response to the backend.
The backend sends the processed results to the React frontend.
The frontend displays risks, alerts, analytics, charts, and recommendations to the user.

## Security Considerations

API keys and sensitive credentials are stored in environment variables and are never committed to Git.
Database credentials are stored securely through environment configuration.
Environment files containing sensitive information are excluded using .gitignore.
AI and database credentials are not exposed directly in the frontend.
Backend APIs act as the controlled communication layer between the frontend, database, and AI services.
User input and API data should be validated before processing or storage.
HTTPS should be used for secure communication in production.

## Scalability Notes

The Node.js/Express backend can be horizontally scaled to handle increased user traffic and API requests. MongoDB can be scaled using indexing, replication, and appropriate database optimization. AI/ML processing can be moved to dedicated services or background workers for larger workloads. The system can also be extended with real-time GPS tracking, IoT temperature sensors, weather APIs, port-status data, and live logistics feeds. Caching, message queues, asynchronous processing, and load balancing could be introduced for enterprise-scale supply-chain operations.
