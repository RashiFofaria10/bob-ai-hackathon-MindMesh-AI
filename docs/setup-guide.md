# Setup Guide

> **This file is read by the automated evaluation pipeline. Be precise and complete.**

## Prerequisites

Before you begin, ensure you have the following installed:

- Node.js 18+
- npm
- Git
- MongoDB or MongoDB Atlas
- A modern web browser such as Chrome, Edge, or Firefox

## Environment Variables

Create a `.env` file in the backend directory and add the required environment variables for MongoDB and IBM Bob/AI services.

Copy `.env.example` to `.env` using the command `cp .env.example .env`.

API keys, database credentials, and other sensitive information must be stored in environment variables and must not be committed to Git.

| Variable | Description | Required |
|---|---|---|
| `MONGODB_URI` | MongoDB database connection string | Yes |
| `IBM_BOB_API_KEY` | IBM Bob / AI service API key | Yes |
| `IBM_BOB_URL` | IBM Bob / AI service endpoint | Yes |

## Installation

Clone the repository using `git clone https://github.com/RashiFofaria10/bob-ai-hackathon-MindMesh-AI.git` and enter the project directory using `cd bob-ai-hackathon-MindMesh-AI`.

Install backend dependencies by entering the `backend` directory and running `npm install`.

Install frontend dependencies by entering the `frontend` directory and running `npm install`.

The installation sequence is:

1. Clone the repository.
2. Enter the project directory.
3. Enter the backend directory and run `npm install`.
4. Create the backend `.env` file and configure the required environment variables.
5. Enter the frontend directory and run `npm install`.

## Running the Application

The backend and frontend should be started in separate terminals.

### Backend

From the project root, enter the backend directory and run `npm start`.

The Node.js/Express backend will start on its configured port.

### Frontend

Open a second terminal, enter the frontend directory, and run `npm run dev`.

The React frontend will normally be available at `http://localhost:5173`.

Open the displayed local URL in a web browser to use ChainGuard AI.

## Running Tests

Run the available project tests using `npm test`.

For backend tests, enter the `backend` directory and run `npm test`.

Before submission, verify that the frontend builds successfully and that the backend starts without errors.

## Quick Demo

To demonstrate ChainGuard AI quickly:

1. Start the backend using `npm start`.
2. Start the frontend using `npm run dev`.
3. Open `http://localhost:5173` or the URL displayed by Vite.
4. Explore the supply-chain dashboard.
5. Review shipment and disruption information.
6. Check shipment risk scores and severity levels.
7. Review route and carrier recommendations.
8. Review fleet availability and redeployment recommendations.
9. Review cold-chain temperature monitoring and alerts.
10. Use the IBM Bob conversational assistant for supply-chain questions and decision support.

## Troubleshooting

| Issue | Solution |
|---|---|
| `npm install` fails | Verify that Node.js 18+ and npm are installed, then run `npm install` again. |
| Backend does not start | Verify backend dependencies are installed and the required `.env` variables are configured correctly. |
| Frontend does not start | Enter the `frontend` directory, run `npm install`, and then run `npm run dev`. |
| MongoDB connection fails | Check the MongoDB connection string, credentials, database availability, and network access. |
| Frontend cannot connect to backend | Make sure the backend is running and the frontend is configured with the correct backend API URL. |
| Port already in use | Stop the process using the port or change the configured application port. |
| Environment variable is missing | Verify that the `.env` file exists in the backend directory and contains all required values. |
| IBM Bob assistant does not respond | Verify the IBM Bob/AI credentials, endpoint configuration, and backend server status. |
| Browser cannot open the application | Make sure the frontend development server is running and open the URL displayed in the terminal. |
