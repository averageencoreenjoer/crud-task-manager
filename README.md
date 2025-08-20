# CRUD TASK MANAGER

<p align="center"> 
<img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi" alt="FastAPI"> 
<img src="https://img.shields.io/badge/Gauge-E3583A?style=for-the-badge&logo=gauge&logoColor=white" alt="Gauge"> 
<img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white" alt="Docker"> 
<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
</p>

<p align="center">
Professional implementation of REST API for task management.
<br />
Completed as a test task with a focus on <strong>clean architecture</strong> and <strong>BDD testing</strong>.
</p>

---

## Compliance with Technical Task

- **Backend**: **FastAPI** (3 out of 3 points).
- **Testing**: **Gauge** (3 out of 3 points). BDD tests are written in the form of human-readable specifications that serve as "living" documentation.
- **Code Quality**: Clean architecture with separation of layers (`api`, `crud`, `core`, `db`) is used. The code is formatted with `black` according to the PEP8 standard.
- **Test Coverage**: All CRUD operations (`create`, `get`, `get_list`, `update`, `delete`) and error handling scenarios are covered by tests.
- **API Documentation**: Automatically generated interactive documentation **Swagger UI** and **ReDoc**.
- **Containerization**: The project is fully wrapped in **Docker** and contains `docker-compose.yml` for easy launch with one command.
- **Manual**: This `README.md` file contains comprehensive instructions on how to launch and test the project.

---

## Architectural solutions

- **Clean architecture**: The project is divided into logical layers, which ensures low coupling of components, high maintainability and easy scalability of the solution.
- **BDD approach (Behavior-Driven Development)**: Tests are written in the "Specification-Scenario-Step" format in natural language. This makes them understandable not only for developers, but also for the entire team.
- **Containerization**: Using Docker and Docker Compose ensures that the application will work the same in any environment and simplifies the deployment and local development process as much as possible.

---

## Tech stack

| Direction | Technology / Tool |
| --------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Backend Framework** | <img src="https://img.shields.io/badge/FastAPI-009688?style=flat&logo=fastapi" alt="FastAPI"> |
| **Testing (BDD)** | <img src="https://img.shields.io/badge/Gauge-E3583A?style=flat&logo=gauge&logoColor=white" alt="Gauge"> |
| **Web Server (ASGI)** | <img src="https://img.shields.io/badge/Uvicorn-29AEB2?style=flat&logo=python&logoColor=white" alt="Uvicorn"> |
| **Containerization** | <img src="https://img.shields.io/badge/Docker-2496ED?style=flat&logo=docker&logoColor=white" alt="Docker"> & <img src="https://img.shields.io/badge/Docker_Compose-3B74B8?style=flat&logo=docker&logoColor=white" alt="Docker Compose"> |
| **Code Formatting** | <img src="https://img.shields.io/badge/Black-000000?style=flat&logo=python&logoColor=white" alt="Black"> |

---

## Install and Run

### Method 1: Run Locally (Recommended for Development)

1. **Clone the repository**
```bash
git clone https://github.com/averageencoreenjoer/crud-task-manager.git
cd crud-task-manager
```

2. **Create and activate the virtual environment**
```bash
python3 -m venv venv
source venv/bin/activate
```
*(For Windows: `venv\Scripts\activate`)*

3. **Install dependencies**
*(First create `requirements.txt` file if it does not exist: `pip freeze > requirements.txt`)*
```bash
pip install -r requirements.txt
```

4. **Run the application**
```bash
uvicorn src.task_manager.main:app --reload
```
The application will be available at `http://127.0.0.1:8000`.

### Method 2: Launch via Docker Compose (Recommended for a quick start)

1. **Build and run the application with one command:**
From the root folder of the project, run:
```
bash
docker-compose up --build -d
```
- `--build` — rebuild the image if there were changes in the code.
- `-d` — run in the background.

2. **To stop the application:**
```bash
docker-compose down
```
The application will be available at `http://localhost:8000`.

---

## Testing

To run BDD tests:
1. Make sure the application is **running** (locally or via Docker).
2. In a **new** terminal window, with the virtual environment activated (`source venv/bin/activate`), run the command:
```bash
gauge run specs
```
You will see a report on the execution of all scenarios in the console. A detailed HTML report will be automatically generated in the `reports` folder.

---

## API Documentation

After launching the application, the interactive documentation of **Swagger UI** and **ReDoc** will be available at the following addresses:

- **Swagger UI**: `http://127.0.0.1:8000/docs`
- **ReDoc**: `http://127.0.0.1:8000/redoc`
