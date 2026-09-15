# 🚀 ChainGuard AI

> **AI-Powered Supply Chain Disruption Assistant & Fleet Utilisation Optimizer**

---

## 👥 Team

| Field         | Value                                          |
| ------------- | ---------------------------------------------- |
| **Team Name** | MindMesh AI                                    |
| **Track**     | Logistics & Ports                              |
| **Team Lead** | Rashi Fofaria - d25dce154@charusat.edu.in      |
| **Members**   | Yesha Chauhan, Fagun Mataria, Priya Pathak     |

---

## 🎯 Problem Statement

Supply chain disruptions — weather events, port strikes, geopolitical crises — cascade across hundreds of active shipments in ways that are impossible to track manually. Fleet assets (trucks, containers, vessels) sit idle while other routes are overloaded. Cold chain shipments (vaccines, perishables) are especially vulnerable — a single temperature excursion across any leg can spoil a $500K+ cargo, but breaches are only discovered at delivery when it is too late.

---

## 💡 Solution

**ChainGuard AI** is an AI-powered supply-chain control tower that identifies disruption-affected shipments, evaluates shipment risk and recommends alternative routes and carriers. It also matches idle fleet vehicles to urgent shipments and monitors cold-chain temperature data to detect excursions and classify their severity, with **IBM Bob** providing a conversational AI interface for supply-chain decision support.

---

## ✨ Key Features

* **Disruption Impact Analysis:** Identifies shipments affected by active disruptions and determines their level of risk.
* **AI Shipment Risk Assessment:** Calculates shipment risk using factors such as disruption severity, route exposure, delay, cargo sensitivity and delivery urgency.
* **Route & Carrier Recommendations:** Recommends safer alternative routes and suitable carriers by comparing risk, cost and estimated travel time.
* **Idle Fleet Redeployment:** Identifies available idle vehicles and matches them with affected shipments based on location, capacity, vehicle type and cargo requirements.
* **Cold-Chain Monitoring:** Analyzes temperature logs for temperature-sensitive shipments and detects abnormal temperature excursions.
* **Severity Classification:** Classifies detected cold-chain excursions according to the severity rules implemented in the system.
* **AI Recommendations:** Converts detected risks and available resources into actionable operational recommendations.
* **IBM Bob Assistant:** Allows users to ask natural-language questions about disruptions, shipment risks, fleet availability, recommendations and cold-chain alerts.

---

## 🛠️ Tech Stack

| Category               | Technologies                                                            |
| ---------------------- | ----------------------------------------------------------------------- |
| **Languages**          | TypeScript, JavaScript                                                  |
| **Frontend Framework** | Next.js, React                                                          |
| **Frontend Styling**   | Tailwind CSS, PostCSS                                                   |
| **UI Components**      | shadcn/ui, Base UI React                                                |
| **Visualization**      | Recharts                                                                |
| **Icons**              | Lucide React                                                            |
| **Package Manager**    | pnpm                                                                    |
| **Analytics**          | Vercel Analytics                                                        |
| **Backend**            | Node.js, Express.js                                                     |
| **AI / ML**            | Machine Learning, Risk Scoring, Anomaly Detection, Recommendation Logic |
| **IBM Technologies**   | IBM Bob                                                                 |
| **Database**           | MongoDB                                                                 |
| **Database ODM**       | Mongoose                                                                |
| **API Communication**  | REST APIs                                                               |
| **Version Control**    | Git, GitHub                                                             |
| **Other**              | Environment Variables                                                   |

---


## 📁 Repository Structure

```text
├── src/
│   ├── frontend/             # Frontend application
│   │   ├── app/
│   │   ├── components/
│   │   ├── lib/
│   │   └── public/
│   │
│   ├── backend/              # Backend application
│   │   ├── config/
│   │   ├── controllers/
│   │   ├── models/
│   │   ├── routes/
│   │   ├── services/
│   │   └── server.js
│   │
│   ├── ml/                   # AI/ML and recommendation modules
│   └── data/                 # Project datasets
│
├── docs/                     # Written documentation
│   ├── problem-statement.md
│   ├── solution-overview.md
│   ├── architecture.md
│   └── setup-guide.md
│
├── demo/                     # Demo artifacts
│   ├── screenshots/
│   ├── demo-video-link.txt
│   └── live-demo-url.txt
│
├── presentation/             # Slide deck
│   └── slides.pdf
│
└── submission.yaml            # Structured submission metadata
```

---

## ⚡ How to Run

> **Copy these exact steps from your [`docs/setup-guide.md`](docs/setup-guide.md) after finalising the environment configuration.**

```bash
# 1. Clone the repo
git clone https://github.com/[your-repo].git
cd [your-repo]

# 2. Install frontend dependencies
cd src/frontend
npm install

# 3. Install backend dependencies
cd ../backend
npm install

# 4. Configure environment
# Create the required .env file using .env.example
# Add the MongoDB connection string and required API/configuration values

# 5. Start the backend
npm start

# 6. Start the frontend
# Open another terminal
cd src/frontend
npm run dev
```

> **Note:** Replace the commands above with the exact commands used by the final repository before submission.

---

## 🖥️ Demo

| Artifact        | Link                                                     |
| --------------- | -------------------------------------------------------- |
| 📹 Demo Video   | [See demo/demo-video-link.txt](demo/demo-video-link.txt) |
| 🌐 Live Demo    | [See demo/live-demo-url.txt](demo/live-demo-url.txt)     |
| 🖼️ Screenshots | [See demo/screenshots/](demo/screenshots/)               |
| 📊 Presentation | [See presentation/slides.pdf](presentation/)             |

---

## ⚠️ Known Limitations

* The prototype uses simulated/synthetic supply-chain, fleet, disruption and temperature data rather than live enterprise logistics data.
* Real-world IoT hardware integration is represented through temperature-log data in the prototype.
* Route and fleet recommendations are designed as a prototype decision-support mechanism and may require additional constraints and optimization for production deployment.
* Cold-chain severity classification depends on the rules and thresholds configured for the prototype.
* Authentication and enterprise-level access control may require further implementation for production use.
* The system has been developed and tested within the supported project environment and may require additional deployment configuration for other environments.

---

## 🏅 What We're Most Proud Of

We are most proud of bringing **multiple supply-chain intelligence capabilities into one integrated decision-support platform**. ChainGuard AI connects disruption impact analysis, shipment risk assessment, route and carrier recommendations, idle fleet redeployment and cold-chain monitoring into a single workflow, while **IBM Bob** provides a natural-language interface through which users can understand risks and obtain actionable recommendations.
