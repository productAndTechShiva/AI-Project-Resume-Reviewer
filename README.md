# AI Resume Reviewer

## Project Overview

AI Resume Reviewer is an AI-powered application that helps job seekers evaluate and improve their resumes through automated analysis and actionable feedback.

The system analyzes an uploaded resume and generates a structured review, including an overall resume score, strengths, weaknesses, improvement suggestions, and an enhanced professional summary. The objective is to provide users with quick, personalized feedback that can help improve resume quality before applying for jobs.

This project demonstrates how Large Language Models (LLMs) can be integrated into business applications to automate document review workflows and provide decision-support recommendations.


# Business Problem

Recruiters often spend only a few seconds reviewing a resume before deciding whether to continue evaluating a candidate.

Many job seekers struggle with:

* Identifying weaknesses in their resumes
* Writing compelling professional summaries
* Understanding how their resumes are perceived by recruiters
* Receiving objective feedback before applying for jobs
* Improving resume quality without professional consulting services

Manual resume reviews are time-consuming and often expensive. This project explores how AI can streamline the resume review process and provide instant feedback at scale.


# Product Vision

To build an AI-powered career assistance platform that helps job seekers improve their resumes, increase interview opportunities, and prepare more effectively for job applications.

The current version focuses on resume evaluation and personalized improvement recommendations.

Future versions can expand into:

* ATS Compatibility Analysis
* Job Description Matching
* Resume Optimization
* Cover Letter Generation
* Interview Question Preparation
* Career Coaching Assistance


# Target Users

## Primary Users

* Job Seekers
* Students
* Fresh Graduates
* Career Switchers
* Software Professionals

## Secondary Users

* Recruitment Agencies
* Career Coaches
* Resume Writing Services
* HR Consultants


# Product Objectives

The solution aims to:

* Automate resume review workflows
* Provide structured and actionable feedback
* Improve resume quality
* Reduce manual review effort
* Demonstrate practical use of Generative AI in document analysis


# Key Features

## Screenshots

<img width="4141" height="2245" alt="combined_img" src="https://github.com/user-attachments/assets/675a93fc-40b0-4add-bbe8-d4d0a0174ae0" />


## Resume Upload
Users can upload resumes in:

* PDF format
* DOCX format


## Resume Parsing

The system extracts text content from uploaded documents and converts it into a format suitable for AI analysis.


## AI-Powered Resume Analysis

The application evaluates:

* Resume quality
* Professional presentation
* Content clarity
* Skills representation
* Overall effectiveness


## Resume Score

Generates an overall resume quality score ranging from:

* 0 to 100

This provides a quick assessment of resume quality.


## Strength Analysis

Identifies the strongest aspects of the resume, including:

* Technical skills
* Experience
* Accomplishments
* Professional presentation


## Weakness Analysis

Highlights areas that require improvement, such as:

* Missing information
* Formatting concerns
* Weak descriptions
* Lack of measurable achievements


## Improvement Suggestions

Provides actionable recommendations that can help improve the effectiveness of the resume.


## Enhanced Professional Summary

Generates an improved professional summary that can potentially replace the existing resume summary section.


# Functional Requirements

## Resume Management

### FR-01

User shall be able to upload a PDF resume.

### FR-02

User shall be able to upload a DOCX resume.

### FR-03

System shall validate supported file formats.


## Resume Processing

### FR-04

System shall extract text from uploaded resumes.

### FR-05

System shall convert extracted content into an AI-compatible prompt.

### FR-06

System shall submit the prompt to the LLM for analysis.


## Resume Evaluation

### FR-07

System shall generate a resume quality score.

### FR-08

System shall identify strengths.

### FR-09

System shall identify weaknesses.

### FR-10

System shall provide improvement recommendations.

### FR-11

System shall generate an improved professional summary.


# Non-Functional Requirements

## Performance

* Resume analysis should complete within a reasonable response time.

## Usability

* Simple and intuitive user interface.
* Minimal user actions required.

## Scalability

* Architecture should support future AI features.

## Maintainability

* Modular backend services.
* Separation of concerns across components.


# User Workflow

## Step 1

User uploads a resume.

↓

## Step 2

System validates the file.

↓

## Step 3

Resume content is extracted.

↓

## Step 4

AI prompt is generated.

↓

## Step 5

Llama 3 analyzes the resume.

↓

## Step 6

Structured feedback is generated.

↓

## Step 7

Results are displayed to the user.


# Solution Architecture

## Frontend

Responsible for:

* Resume upload
* User interaction
* Displaying AI feedback

### Technology

* React
* TypeScript
* Vite


## Backend

Responsible for:

* API management
* File handling
* Resume parsing
* AI orchestration
* Response validation

### Technology

* FastAPI
* Python


## AI Layer

Responsible for:

* Resume evaluation
* Recommendation generation
* Professional summary enhancement

### Technology

* Llama 3
* Ollama


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


# Technology Stack

## Frontend

* React
* TypeScript
* Vite
* Axios

## Backend

* Python
* FastAPI
* Uvicorn
* Pydantic

## AI & NLP

* Llama 3
* Ollama

## Document Processing

* PyPDF2
* python-docx


# My Contribution

As the Product Manager and Business Analyst for this project, I was responsible for:

## Product Discovery

* Defining the business problem
* Identifying user pain points
* Defining product objectives

## Product Design

* Designing user workflow
* Defining feature scope
* Creating functional requirements
* Designing AI interaction flow

## Business Analysis

* Requirement analysis
* Feature prioritization
* User journey mapping
* Solution architecture planning

## AI Solution Design

* Prompt engineering strategy
* Structured AI response design
* Output validation approach
* AI workflow orchestration

## Technical Implementation

* Frontend development
* Backend API development
* Resume parsing integration
* LLM integration using Llama 3 and Ollama


# Future Enhancements

## Version 2

* ATS Score Analysis
* Job Description Matching
* Missing Skills Detection
* Resume Keyword Analysis

## Version 3

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
