# Micro-SaaS Starter Backend: Serverless FastAPI & AWS SAM

This blueprint provides a production-ready, serverless backend foundation using modern, type-safe Python. It is designed for maximum scalability, cost-efficiency, and developer experience.

## 🚀 Key Features

* **Serverless-Native:** Deploys as a lightweight AWS Lambda function using **Mangum** and **AWS API Gateway**.
* **Clean Architecture:** Strict separation of concerns (Routers, Services, Schemas) for easy maintenance and testing.
* **Type-Safe Python:** Built with **FastAPI** and **Pydantic** for automatic data validation, documentation (`/docs`), and robust type-hinting.
* **Automated Deployment:** Includes a full **GitHub Actions** CI/CD pipeline definition using **AWS SAM** (Serverless Application Model) for reliable, single-command cloud deployment.
* **Configuration:** Uses `pydantic-settings` for clean loading of environment variables via `.env`.

## 💻 Local Development

1.  **Environment:** Ensure you have Python 3.11+ installed.
2.  **Setup:**
    ```bash
    # Create and activate virtual environment
    python -m venv .venv
    source .venv/bin/activate  # Windows: .venv\Scripts\activate
    
    # Install dependencies
    pip install -r requirements.txt
    
    # Copy and configure environment variables
    cp .env.template .env
    # (Edit .env variables as needed)
    ```

3.  **Run API Server:**
    ```bash
    # Start the API with Uvicorn (local development server)
    uvicorn app.main:app --reload
    # Access the API documentation (Swagger UI) at [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
    ```

## ☁️ Deployment (AWS)

This project is configured to deploy via the **AWS Serverless Application Model (SAM)**, which manages the necessary Lambda, API Gateway, and IAM resources defined in [`serverless.yaml`](serverless.yaml).

1.  **Prerequisites:** You must have the AWS CLI and AWS SAM CLI installed and configured locally.
2.  **Manual Deployment (Test):**
    ```bash
    # Build the application package
    sam build
    
    # Deploy to AWS CloudFormation (creates Lambda/API Gateway)
    sam deploy --guided
    ```
3.  **CI/CD Automation:** The included [`./github/workflows/deploy.yml`](.github/workflows/deploy.yml) defines a pipeline that automatically runs the SAM build and deploy steps upon code push to `main`. Requires configuring AWS credentials as GitHub Secrets.

## ⚙️ Project Structure

| File / Folder | Purpose |
| :--- | :--- |
| `app/main.py` | FastAPI application entry point, wraps app with `Mangum` handler. |
| `app/schemas/` | **Pydantic Models** (`Zone`, `ZoneCreate`) for request/response validation. |
| `app/services/` | **Business Logic** (`ZoneService`) layer. |
| `app/api/endpoints/`| **API Routers** (FastAPI) defining URL paths. |
| `serverless.yaml` | AWS SAM template defining Lambda, API Gateway, and CloudFormation resources. |
| `.github/workflows/`| GitHub Actions CI/CD pipeline for automated deployment. |

