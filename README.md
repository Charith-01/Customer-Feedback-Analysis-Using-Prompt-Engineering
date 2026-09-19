# Customer Feedback Analysis Using Prompt Engineering

## Project Overview

This project explores how prompt engineering can improve the quality,
consistency, and usefulness of Large Language Model (LLM) outputs for
customer support ticket analysis.

The project focuses on four prompt engineering tasks:

1. Data Analysis
2. Summarization
3. Classification
4. Content Generation

Different prompt versions were designed, tested, and improved based on
observed output quality.

---

## Objective

The main objective of this project is to evaluate how prompt design affects
LLM output quality.

The project compares simple baseline prompts with more structured prompts
that include:

- Role instructions
- Clear task definitions
- Output constraints
- Category definitions
- Decision rules
- Response formatting requirements

---

## Dataset

The project uses a multilingual customer support ticket dataset.

The original dataset contained:

- 20,000 customer support tickets
- English and German records
- Ticket subject
- Ticket body
- Support response
- Ticket type
- Queue
- Priority
- Language
- Tags

For this project, only English records were used.

After cleaning, approximately 11,919 English tickets remained.

The main columns used were:

- `subject`
- `body`
- `answer`
- `type`
- `queue`
- `priority`
- `language`

A balanced experiment dataset of 120 records was created using:

- 30 Incident tickets
- 30 Request tickets
- 30 Problem tickets
- 30 Change tickets

---

## Data Preparation

The data preparation process included:

- Filtering English-language tickets
- Removing records with missing ticket body or answer
- Replacing missing subjects with `No subject`
- Removing leading and trailing whitespace
- Checking duplicate records
- Resetting the dataframe index
- Creating a balanced prompt experiment dataset

The original raw dataset was kept unchanged.

---

## LLM Model

The prompt experiments were performed using:

**Google Gemini 2.5 Flash**

The Gemini API was accessed through the Google GenAI Python SDK.

The API key was stored securely in a `.env` file and excluded from Git
using `.gitignore`.

---

## Prompt Engineering Approach

### Version 1 - Baseline Prompts

V1 prompts were intentionally simple.

Examples included:

- "Summarize the following customer support ticket."
- "Classify the following customer support ticket."
- "Write a response to the following customer support ticket."

These prompts were used to establish a baseline.

### Version 2 - Improved Prompts

V2 prompts introduced:

- Defined model roles
- Clear instructions
- Structured output formats
- Category definitions
- Length constraints
- Factuality requirements
- Restrictions against unsupported information

### Version 3 - Classification Refinement

A third classification prompt was created to improve the distinction between:

- Incident
- Problem

Additional decision rules were introduced to separate one-time failures
from recurring or root-cause issues.

---

## Prompt Tasks

### 1. Data Analysis

The data analysis prompts were designed to identify:

- Ticket type patterns
- Priority patterns
- Common customer issues
- Relationships between ticket type and priority
- Key observations

### 2. Summarization

The summarization prompts were designed to produce concise summaries while
preserving important information and avoiding unsupported assumptions.

### 3. Classification

Tickets were classified into:

- Incident
- Request
- Problem
- Change

Prompt versions were compared based on classification behavior and output
consistency.

### 4. Content Generation

The content generation prompts produced professional customer support
responses.

Improved prompts included requirements for:

- Professional tone
- Relevance
- Conciseness
- Clear next steps
- Avoiding unsupported promises

---

## Evaluation

A pilot evaluation was performed to compare prompt versions.

### Classification Findings

V1:
- Produced correct classifications in the initial small test sample.
- Frequently returned additional explanations.
- Output format was inconsistent.

V2:
- Produced cleaner, machine-readable labels.
- Improved output consistency.
- One ticket differed from the dataset label.

V3:
- Added clearer Incident vs Problem decision rules.
- The ambiguous ticket remained classified as `Problem`.

The ambiguous ticket described repeated security breaches caused by outdated
software.

Although the dataset label was `Incident`, the prompt definitions supported
a possible `Problem` interpretation because the ticket explicitly described
an underlying cause.

This demonstrates that disagreements between an LLM prediction and dataset
label may sometimes result from label ambiguity rather than only poor model
performance.

---

## Limitations

This project has several limitations:

- The evaluation sample was small.
- Gemini free-tier API request limits restricted large-scale testing.
- Generative outputs such as summaries and customer responses require
  qualitative evaluation.
- Some ticket labels may be ambiguous.
- Results from the pilot evaluation should not be treated as a full model
  benchmark.

Future work could evaluate a larger test set and use multiple LLM models.

---

## Project Structure

```text
Customer-Feedback-Analysis-Using-Prompt-Engineering/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│   ├── 01_data_exploration.ipynb
│   ├── 02_data_cleaning.ipynb
│   └── 03_prompt_experiments.ipynb
│
├── src/
│   ├── llm_client.py
│   ├── prompts.py
│   └── test_model.py
│
├── outputs/
│   ├── classification_v1_v2_comparison.csv
│   └── prompt_evaluation_summary.csv
│
├── dashboard/
│
├── .env.example
├── .gitignore
├── README.md
└── requirements.txt
```

