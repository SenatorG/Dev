import webbrowser
from urllib.parse import quote_plus

FAST_BASE = "https://saleschat.dell.com/chat?chatAgent=FAST&message="
ADV_BASE = "https://saleschat.dell.com/chat?chatAgent=ADVANCED&message="
SOURCE_SUFFIX = "&source=chat-user-bubble-copy-link"

QUERY_TEMPLATE = (
    "show me a summary of the top news articles from the last week that mention {company}. "
    "For each article, provide a clickable hyperlink to the source. At the end, create a bibliography "
    "of all articles formatted per Chicago Manual of Style 17th Edition (author, title, publication, date, URL). "
    "Fetch all necessary metadata from the source articles."
)

# Original targets are retained; landscape companies are appended and deduplicated.
TRACKED_COMPANIES = [
    'Red Hat',
    'Azure',
    'VMware',
    'Dell',
    'IBM',
    'HPE',
    'Nvidia',
    'Google',
    'Google DeepMind',
    'Google Cloud',
    'Microsoft',
    'Microsoft Azure',
    'OpenAI',
    'Anthropic',
    'AWS',
    'Amazon Web Services',
    'Grok',
    'xAI',
    'Snowflake',
    'Databricks',
    'NetApp',
    'CNCF',
    'Kubernetes',
    'Perplexity',
    'Palantir',
    'Meta AI',
    'Mistral AI',
    'DeepSeek',
    'Alibaba / Qwen',
    'Cohere',
    'AI21 Labs',
    'Z.AI (Zhipu AI)',
    'Alibaba Cloud',
    'Moonshot AI',
    'Together AI',
    'Fireworks AI',
    'Groq',
    'Palantir Technologies',
    'C3 AI',
    'unsloth.ai',
    'UiPath',
    'Dataiku',
    'Scale AI',
    'Glean',
    'ServiceNow',
    'Salesforce',
    'SAP',
    'Stability AI',
    'Hugging Face',
    'Aleph Alpha',
    'DataRobot',
    'Celonis',
    'Quantum',
    'IonQ',
    'D-Wave Quantum',
    'Rigetti Computing',
    'Quantinuum',
    'Xanadu',
    'IQM Quantum Computers',
    'PASQAL',
    'PsiQuantum',
    'QuEra Computing',
    'Oxford Quantum Circuits',
    'Alice & Bob',
    'Q-CTRL',
    'Quantum Brilliance',
    'SEEQC',
    'Classiq',
]

FAST_QUERIES = [
    QUERY_TEMPLATE.format(company=company)
    for company in TRACKED_COMPANIES
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
Source/Link: A direct link to the content or its internal repository location. Ensure each link is clickable.

**Bibliography:** At the end of the response, create a bibliography of all discovered content formatted per Chicago Manual of Style 17th Edition (author, title, publication, date, URL). Fetch all necessary metadata from the source content to format the citations correctly.

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
