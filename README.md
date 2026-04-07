# 🚀 AI Resume Analyzer (CI/CD + AWS + Bedrock)

## 📌 Overview

This project demonstrates a **full end-to-end CI/CD pipeline** integrated with AWS and AI capabilities using **Amazon Bedrock**.

The application allows users to upload a resume and receive AI-generated feedback including:

* Strengths
* Weaknesses
* Suggested improvements
* Missing skills for IT roles

This lab showcases real-world DevOps and cloud engineering practices including:

* CI/CD automation
* Serverless deployment
* API exposure
* AI integration

---

## 🧱 Architecture

```
                ┌──────────────┐
                │   GitHub     │
                │ (Source Code)│
                └──────┬───────┘
                       │
                       ▼
            ┌────────────────────┐
            │ GitHub Actions CI  │
            │  - Install deps    │
            │  - Run tests       │
            └──────┬─────────────┘
                   │
                   ▼
        ┌──────────────────────────┐
        │ AWS Lambda (FastAPI App) │
        │  - Mangum Adapter        │
        └──────┬───────────────────┘
               │
               ▼
     ┌───────────────────────┐
     │ Amazon API Gateway    │
     │  - Public Endpoint    │
     └──────┬────────────────┘
            │
            ▼
   ┌────────────────────────────┐
   │ Amazon Bedrock (Claude AI) │
   │  - Resume Analysis         │
   └────────────────────────────┘
```

---

## 🔄 CI/CD Pipeline

### Pipeline Stages

1. **Source**

   * Code pushed to GitHub triggers pipeline

2. **Test**

   * Dependencies installed
   * Unit tests executed with `pytest`

3. **Deploy**

   * Application packaged using Docker (Linux-compatible)
   * Deployed to AWS Lambda

---

## 🛠️ Tech Stack

* **Backend:** FastAPI (Python)
* **CI/CD:** GitHub Actions
* **Cloud:** AWS Lambda, API Gateway
* **AI:** Amazon Bedrock (Claude model)
* **Packaging:** Docker (Amazon Linux)
* **Adapter:** Mangum (FastAPI → Lambda)

---

## 📂 Project Structure

```
ai-resume-analyzer/
│
├── backend/
│   └── main.py
│
├── tests/
│   └── test_basic.py
│
├── .github/workflows/
│   └── cicd.yml
│
├── requirements.txt
└── README.md
```

---

## ⚙️ How It Works

1. User uploads a resume via API
2. API Gateway routes request to Lambda
3. Lambda runs FastAPI app via Mangum
4. Resume text is extracted
5. Request is sent to Amazon Bedrock
6. AI generates structured feedback
7. Response returned to user

---

## 🚀 Deployment Steps

### 1. Clone Repository

```bash
git clone https://github.com/your-username/ai-resume-analyzer-cicd.git
cd ai-resume-analyzer-cicd
```

---

### 2. Build Lambda Package (Docker)

```bash
docker run --rm -v "$PWD":/app -w /app amazonlinux:2 \
bash -c "yum install -y python3 zip && \
mkdir -p package && \
pip3 install fastapi mangum boto3 python-multipart -t package && \
cp -r backend package/ && \
cd package && zip -r ../app.zip ."
```

---

### 3. Deploy to Lambda

```bash
aws lambda update-function-code \
  --function-name resume-analyzer \
  --zip-file fileb://app.zip
```

---

### 4. Test API

```bash
curl -X POST \
https://7usnrpkkr1.execute-api.us-east-2.amazonaws.com/prod/analyze \
-F "file=@test_resume.txt"
```

---

## 🔐 Authentication Strategy

* **Local Development:** Environment variables / AWS CLI
* **CI/CD:** GitHub Secrets
* **Production:** IAM Roles

---

## 🧠 Key Learnings

* Handling **dependency compatibility issues** between macOS and AWS Lambda
* Building **CI/CD pipelines with GitHub Actions**
* Deploying **serverless applications**
* Integrating **AI services (Amazon Bedrock)**
* Debugging real-world issues like:

  * Module import errors
  * Packaging issues
  * API routing errors

---

## 🧪 Example Output

```json
{
  "analysis": {
    "strengths": "...",
    "weaknesses": "...",
    "improvements": "...",
    "missing_skills": "..."
  }
}
```

---

## 💼 Resume Bullet (Use This)

> Built and deployed an AI-powered resume analysis application using FastAPI, AWS Lambda, and Amazon Bedrock, with a CI/CD pipeline (GitHub Actions) enabling automated testing and serverless deployment.

---

## 🔥 Future Improvements

* Add frontend UI (React)
* Store results in DynamoDB
* Add authentication (Cognito)
* Implement logging/monitoring dashboards
* Use AWS CodePipeline for native CI/CD

---

## 📬 Contact

If you have questions or want to collaborate, feel free to connect!

---
