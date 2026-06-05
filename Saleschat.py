import webbrowser
from urllib.parse import quote_plus

FAST_BASE = "https://saleschat.dell.com/chat?chatAgent=FAST&message="
ADV_BASE = "https://saleschat.dell.com/chat?chatAgent=ADVANCED&message="
SOURCE_SUFFIX = "&source=chat-user-bubble-copy-link"

FAST_QUERIES = [
    "show me a summary of the top 3 news articles from the last week that mention Red Hat",
    "show me a summary of the top 3 news articles from the last week that mention Azure",
    "show me a summary of the top 3 news articles from the last week that mention Pure Storage",
    "show me a summary of the top 3 news articles from the last week that mention VMware",
    "show me a summary of the top 5 news articles from the last week that mention Dell",
    "show me a summary of the top 5 news articles from the last week that mention IBM",
    "show me a summary of the top 5 news articles from the last week that mention HPE",
    "show me a summary of the top 5 news articles from the last week that mention Google",
    "show me a summary of the top 5 news articles from the last week that mention Microsoft",
    "show me a summary of the top 5 news articles from the last week that mention Nvidia",
    "show me a summary of the top 5 news articles from the last week that mention OpenAI",
    "show me a summary of the top 5 news articles from the last week that mention Anthropic",
    "show me a summary of the top 5 news articles from the last week that mention Meta",
    "show me a summary of the top 5 news articles from the last week that mention AWS",
    "show me a summary of the top 5 news articles from the last week that mention Grok",
    "show me a summary of the top 5 news articles from the last week that mention Snowflake",
    "show me a summary of the top 5 news articles from the last week that mention Databricks",
    "show me a summary of the top 5 news articles from the last week that mention VAST Data",
    "show me a summary of the top 5 news articles from the last week that mention NetApp",
    "show me a summary of the top 5 news articles from the last week that mention CNCF",
    "show me a summary of the top 5 news articles from the last week that mention Kubernetes",
    "show me a summary of the top 5 news articles from the last week that mention Perplexity",
    "show me a summary of the top 5 news articles from the last week that mention IonQ",
    "show me a summary of the top 5 news articles from the last week that mention D-Wave",
    "show me a summary of the top 5 news articles from the last week that mention Quantum",
]

ADVANCED_MESSAGE = """
Act as an intelligence analyst specializing in Dell Technologies Enterprise Compute, Storage, Edge, AI, HPC and Cloud Platform solutions. Your task is to find the most recent collateral developed in the last week for the following platforms: "PowerEdge" "PowerMax", "PowerStore", "PowerFlex", "PowerScale", "OneFS", "Lightening File System", "ObjectScale", "ECS", "Dell Distributed Private Cloud", "Dell Automation Platform", "Dell Private Cloud", "Dell AI Factory", "Dell AI Data Platform".

**Primary Objective:** Prioritize any content that explicitly discusses: "What's New" recent software/hardware updates (e.g., new PowerMaxOS, PowerStoreOS, or PowerFlex releases), new reference architectures, or validated designs related to these platforms.

**Constraints:**
Timeframe: Focus *only* on content published or updated within the last week.
Source Type: Search for official Dell-produced content (internal or external) or content from major vendor partners (e.g., VMware, Red Hat, Microsoft, Intel, Nutanix).
Content Type: Include solution briefs, white papers, reference architectures, validated designs, official presentations (e.g., from Dell events, internal sales kickoffs), technical specifications sheets, and detailed official blog posts.

**Output Format:** Deliver the findings in a markdown table with the following columns. Make sure the table is complete:
Content Title: The official name of the document or presentation.
Summary: A concise summary (2-3 sentences or bullet points) detailing the content's key objectives and, most importantly, any specific "What's New" features, hardware, software versions, or partner integrations mentioned.
Content Type: (e.g., White Paper, Reference Architecture, Presentation)
Date: The publication or "last modified" date.
Source/Link: A direct link to the content or its internal repository location.

**Executive Summary:** In addition to the tabular output, provide a concise executive summary of all the items.
""".strip()

def open_fast_queries():
    for query in FAST_QUERIES:
        url = FAST_BASE + quote_plus(query) + SOURCE_SUFFIX
        webbrowser.open(url)

def open_advanced_query():
    url = ADV_BASE + quote_plus(ADVANCED_MESSAGE) + SOURCE_SUFFIX
    webbrowser.open(url)

if __name__ == "__main__":
    open_fast_queries()
    open_advanced_query()