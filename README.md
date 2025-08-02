# Healthcare Data Management Platform

A secure healthcare data management platform utilizing blockchain technology for data storage and AI for treatment recommendations.

## Features

- Secure patient data storage using blockchain
- Role-based access control
- HIPAA-compliant data handling
- RESTful API for data access
- Web interface for healthcare providers

## Tech Stack

- Backend: FastAPI, Python
- Blockchain: Hyperledger Fabric
- Database: MongoDB
- Security: JWT, Bcrypt
- Frontend: React.js, Material-UI

## Project Structure

```
healthcare-platform/
├── backend/
│   ├── app/
│   │   ├── api/
│   │   ├── blockchain/
│   │   ├── core/
│   │   ├── db/
│   │   └── models/
│   └── tests/
├── frontend/
│   ├── public/
│   └── src/
├── blockchain/
│   └── contracts/
└── docker/
```

## Setup Instructions

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up environment variables:
   ```bash
   cp .env.example .env
   ```
4. Start the development server:
   ```bash
   uvicorn app.main:app --reload
   ```

## Environment Variables

Create a `.env` file with the following variables:

```
MONGODB_URL=your_mongodb_url
JWT_SECRET=your_jwt_secret
BLOCKCHAIN_NODE_URL=your_blockchain_node_url
```

## API Documentation

Once the server is running, visit:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Security

This platform implements several security measures:
- End-to-end encryption
- Role-based access control
- Audit logging
- HIPAA compliance measures

## License

MIT 