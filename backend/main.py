from fastapi import FastAPI, UploadFile, File
import boto3

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "API is running"}

@app.post("/analyze")
async def analyze_resume(file: UploadFile = File(...)):
    # Read uploaded file
    contents = await file.read()
    resume_text = contents.decode("utf-8", errors="ignore")

    # Call Bedrock (we'll define this next)
    result = analyze_with_bedrock(resume_text)

    return {"analysis": result}
    
def analyze_with_bedrock(resume_text):
    client = boto3.client("bedrock-runtime", region_name="us-east-1")

    prompt = f"""
    Analyze this resume and provide:
    1. Strengths
    2. Weaknesses
    3. Suggested improvements
    4. Missing skills for IT roles

    Resume:
    {resume_text}
    """

    body = {
        "anthropic_version": "bedrock-2023-05-31",
        "max_tokens": 500,
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ]
    }

    import json

    response = client.invoke_model(
        modelId="anthropic.claude-3-sonnet-20240229",
        body=json.dumps(body)
    )

    response_body = json.loads(response["body"].read())

    return response_body["content"][0]["text"]