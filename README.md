# Munch Catering Backend ÌΩΩÔ∏è

A robust **FastAPI** backend designed for the Munch Catering mobile application. This API handles user authentication, catering searches, and booking management using **MongoDB** as the primary data store.

## Ì∫Ä Getting Started

### 1. Prerequisites
* Python 3.10+
* A MongoDB Atlas Cluster (or local MongoDB instance)

### 2. Installation
Clone the repository and set up your environment:
```bash
# Clone the project
git clone https://github.com
cd munch_catering_backend

# Create and activate virtual environment
python -m venv venv
# On Windows use:
.\venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 3. Environment Configuration
Create a `.env` file in the root directory and add your credentials:
```text
MONGO_URI=mongodb+srv://<username>:<password>@cluster.mongodb.net/munch_db
SECRET_KEY=your_super_secret_jwt_key
```

### 4. Running the API
Start the development server:
```bash
uvicorn main:app --reload
```

## Ìª†Ô∏è Tech Stack
- **Framework:** [FastAPI](https://fastapi.tiangolo.com)
- **Database:** [MongoDB](https://www.mongodb.com)
- **Frontend (Mobile):** [BeeWare Toga](https://beeware.org)

---
**Team Members:**
- **Derick** (@rico-del) - Backend & DevOps Lead
