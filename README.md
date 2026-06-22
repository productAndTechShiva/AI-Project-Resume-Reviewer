# AI Resume Reviewer

# Project Overview

AI Resume Reviewer is an AI-powered application that analyzes uploaded resumes and generates structured feedback. The system evaluates resume quality, identifies strengths and weaknesses, provides improvement recommendations, generates an overall resume score and suggests an enhanced professional summary. The project demonstrates the practical application of Generative AI and LLMs for document analysis and review automation.

# Problem Statement

Many job seekers struggle to evaluate the quality of their resumes before applying for jobs. Professional resume reviews can be time-consuming and expensive, while objective feedback is often difficult to obtain. This project explores how AI can automate resume analysis and provide instant, actionable feedback to help candidates improve their resumes.

# Business Impact
* Automates the resume review process and reduces manual effort.
* Provides instant, structured and personalized feedback to job seekers.
* Helps users improve resume quality and professional presentation.
* Demonstrates the use of Generative AI for document analysis and decision-support applications.
* Serves as a foundation for future career-assistance solutions such as ATS analysis, job matching and interview preparation.


# Target Users

* Primary Users - Job Seekers, Students
* Secondary Users - Recruitment Agencies, Career Coaches, Resume Writing Services, HR Consultants


# Key Features

* Upload resumes in PDF and DOCX formats.
* Extract and process resume content for AI analysis.
* Analyze resume quality, content clarity, skills presentation and overall effectiveness.
* Generate an overall resume score (0–100).
* Identify key strengths across skills, experience, achievements and professional presentation.
* Highlight weaknesses such as missing information, weak descriptions, formatting issues and skill gaps.
* Provide actionable recommendations to improve resume quality and impact.
* Generate an enhanced professional summary tailored to the candidate's profile.

### Screenshot
<img width="4141" height="2245" alt="combined_img" src="https://github.com/user-attachments/assets/675a93fc-40b0-4add-bbe8-d4d0a0174ae0" />

# Functional Requirements

### Resume Management
* FR-01: User shall be able to upload a PDF resume.
* FR-02: User shall be able to upload a DOCX resume.
* FR-03: System shall validate supported file formats.

### Resume Processing
* FR-04: System shall extract text from uploaded resumes.
* FR-05: System shall convert extracted content into an AI-compatible prompt.
* FR-06: System shall submit the prompt to the LLM for analysis.

### Resume Evaluation
* FR-07: System shall generate a resume quality score.
* FR-08: System shall identify strengths.
* FR-09 System shall identify weaknesses.
* FR-10: System shall provide improvement recommendations.
* FR-11: System shall generate an improved professional summary.

# Non-Functional Requirements

* Performance: Resume analysis should complete within a reasonable response time.
* Usability: 1. Simple and intuitive user interface. 2. Minimal user actions required.
* Scalability: Architecture should support future AI features.
* Maintainability: 1. Modular backend services. 2. Separation of concerns across components.


# User Workflow

```text
User Uploads Resume
        │
        ▼
Validate File Format & Content
        │
        ▼
Extract Resume Text
        │
        ▼
Generate AI Analysis Prompt
        │
        ▼
Llama 3 Processes Resume
        │
        ▼
Generate Structured Feedback
        │
        ├── ATS Score
        ├── Strengths
        ├── Weaknesses
        ├── Missing Skills
        └── Recommendations
        │
        ▼
Display Results to User
```

# Technology Stack
* Backend - Python, FastAPI, Uvicorn, Pydantic
* Frontend - React, TypeScript, Vite, Axios
* AI & NLP - Llama 3, Ollama
* Document Processing - PyPDF2, python-docx

# Project Structure

```text
frontend/
│
├── src/
│   ├── api/
│   ├── components/
│   ├── styles/
│   └── types/

backend/
│
├── app/
│   ├── routes/
│   ├── services/
│   ├── schemas/
│   └── utils/
│
└── main.py
```

# My Contribution
* Defined the business problem, user pain points and product objectives.
* Gathered and analyzed requirements, prioritized features and designed user workflows.
* Created functional specifications, user journeys and solution architecture.
* Designed the AI workflow, prompt engineering strategy and structured response framework.
* Developed the frontend, backend APIs and resume parsing integration.
* Integrated Llama 3 (via Ollama) and implemented the end-to-end AI-powered resume review process.

# Future Enhancements

### Version 2

* ATS Score Analysis
* Job Description Matching
* Missing Skills Detection
* Resume Keyword Analysis

### Version 3

* Cover Letter Generator
* Interview Question Generator
* AI Career Coach
* Resume Optimization Assistant


# Key Learnings

This project demonstrates practical implementation of:

* Generative AI Applications
* Prompt Engineering
* LLM Integration
* Document Intelligence
* AI-Powered Workflow Automation
* Product Management
* Business Analysis
* Full-Stack Application Development


# Disclaimer

This project is intended for educational, learning, and portfolio purposes. AI-generated feedback should be reviewed by users and may not fully replace professional career consulting services.
