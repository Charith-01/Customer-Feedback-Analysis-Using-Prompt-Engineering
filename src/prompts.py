# ============================================================
# Prompt Engineering Functions
# Customer Feedback Analysis Using Prompt Engineering
# ============================================================


# ------------------------------------------------------------
# V1 - Baseline Prompts
# ------------------------------------------------------------

def analysis_prompt_v1(ticket_data):
    """Baseline prompt for customer support data analysis."""

    return f"""
Analyze the following customer support ticket data and describe the main patterns.

Data:
{ticket_data}
"""


def summarization_prompt_v1(subject, body):
    """Baseline prompt for customer support ticket summarization."""

    return f"""
Summarize the following customer support ticket.

Subject:
{subject}

Ticket:
{body}
"""


def classification_prompt_v1(subject, body):
    """Baseline prompt for customer support ticket classification."""

    return f"""
Classify the following customer support ticket into one of these types:
Incident, Request, Problem, Change.

Subject:
{subject}

Ticket:
{body}
"""


def generation_prompt_v1(subject, body):
    """Baseline prompt for customer support response generation."""

    return f"""
Write a response to the following customer support ticket.

Subject:
{subject}

Ticket:
{body}
"""


# ------------------------------------------------------------
# V2 - Improved Prompts
# ------------------------------------------------------------

def analysis_prompt_v2(ticket_data):
    """Improved prompt for structured customer support analysis."""

    return f"""
You are a customer support data analyst.

Analyze only the customer support ticket data provided below.

Identify:

1. The main ticket types present.
2. Patterns in ticket priority.
3. Common or recurring customer issues.
4. Any noticeable relationship between ticket type and priority.
5. Three key insights from the supplied records.

Present the response using exactly these headings:

Ticket Type Patterns:
Priority Patterns:
Common Issues:
Type-Priority Relationship:
Key Insights:

Do not invent statistics, trends, or information that cannot be supported
by the provided data.

Customer Support Data:
{ticket_data}
"""


def summarization_prompt_v2(subject, body):
    """Improved prompt for concise and factual ticket summarization."""

    return f"""
You are a customer support analyst.

Summarize the customer support ticket below in no more than 2 sentences.

Requirements:

- Clearly state the main problem or request.
- Preserve important details needed to understand the issue.
- Be concise and factual.
- Use only information contained in the ticket.
- Do not add assumptions or unsupported information.

Subject:
{subject}

Ticket:
{body}
"""


def classification_prompt_v2(subject, body):
    """Improved prompt for consistent ticket classification."""

    return f"""
You are a customer support ticket classification system.

Classify the ticket into exactly ONE of these categories:

Incident - An unplanned interruption, failure, or reduction in service.

Request - A request for information, access, assistance,
or a standard service.

Problem - An underlying, recurring, or root-cause issue
requiring investigation.

Change - A request to modify, update, configure,
or change a system or service.

Return ONLY one of these exact labels:

Incident
Request
Problem
Change

Do not provide explanations, punctuation, or additional text.

Subject:
{subject}

Ticket:
{body}
"""


def generation_prompt_v2(subject, body):
    """Improved prompt for professional support response generation."""

    return f"""
You are a professional customer support agent.

Write a concise response to the customer ticket below.

Requirements:

- Acknowledge the customer's issue or request.
- Use a polite and professional tone.
- Clearly state the next reasonable step.
- Do not invent technical details.
- Do not make unsupported promises.
- Do not promise a resolution, refund, deadline, or action
  unless supported by the provided information.
- Keep the response under 120 words.

Subject:
{subject}

Ticket:
{body}
"""


# ------------------------------------------------------------
# V3 - Refined Classification Prompt
# ------------------------------------------------------------

def classification_prompt_v3(subject, body):
    """
    Refined classification prompt with clearer decision rules
    for distinguishing Incident and Problem.
    """

    return f"""
You are a customer support ticket classification system.

Classify the ticket into exactly ONE category.

Definitions:

Incident:
A specific unplanned interruption, outage, failure, degradation,
or malfunction affecting a service or system.

Request:
A request for information, access, assistance,
a standard service, or something the customer wants provided.

Problem:
A recurring issue or an underlying root-cause issue
that requires investigation.

Change:
A request to modify, update, configure, replace,
or change an existing system or service.

Important decision rules:

- A current or one-time service failure or outage
  should normally be classified as Incident.

- Use Problem when the ticket focuses on a recurring issue,
  repeated failures, or investigation of an underlying root cause.

- Do NOT classify a single service failure as Problem
  only because the customer mentions a possible cause.

- Use Change when the customer explicitly asks
  for a modification or configuration change.

- Use Request for normal information, access,
  assistance, or service requests.

Return ONLY one exact label:

Incident
Request
Problem
Change

Do not include explanations, punctuation, or additional text.

Subject:
{subject}

Ticket:
{body}
"""