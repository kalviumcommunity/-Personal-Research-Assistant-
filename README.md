Personal Research Assistant
An AI-powered research companion that helps users search, summarize, and organize knowledge with source-backed answers using LLMs, RAG (Retrieval-Augmented Generation), and Tool Integration.

🚀 Features
Smart Research: Ask any question and get AI-generated, fact-grounded summaries.

Source Citations: Each response includes links or references to the sources used.

Structured Output: Generates organized research reports in JSON, Markdown, or PDF.

Multi-Format Export: Save research results as PDF, Markdown, or Word.

RAG-Powered Accuracy: Retrieves information from verified sources to reduce hallucination.

Web Search & API Integration: Optionally fetches live data from the web.

🛠️ Tech Stack
Frontend: React.js / Next.js (for interactive dashboard)

Backend: Node.js / Express.js or Python FastAPI

LLM: OpenAI GPT / Llama 3 / Claude

RAG:

Vector DB: Pinecone / ChromaDB / Weaviate

Embedding Model: OpenAI Embeddings / Sentence Transformers

Tools & Libraries:

LangChain or LlamaIndex for RAG pipeline

pdfkit / python-docx for exporting reports

axios or requests for API calls [web search, news API, etc.]



## ONE-SHOT Prompting
<!-- One-shot prompting is a technique in prompt engineering where you show the AI one example of the task you want it to perform. Unlike zero-shot prompting, where you just ask without examples, one-shot provides a single sample so the AI better understands the format and style you expect." -->

You are an assistant that generates concise summaries of news articles.  
Here’s an example:  

[Example Article]:  
"OpenAI has released a new AI model that improves reasoning abilities and reduces hallucinations."  

[Example Summary]:  
"OpenAI launched a new AI model with stronger reasoning and fewer errors."  

Now, summarize this article in the same style:  

[Article]:  
"Researchers at MIT have developed a solar-powered desalination system that can provide clean drinking water at low cost to rural communities."  

<!-- "In this example, I gave the model one example article and its summary. That’s the one shot. Then I asked it to summarize a new article in the same way. By doing this, I guided the model’s output style and reduced the chances of vague or inconsistent responses. This makes one-shot prompting super useful when you want AI to follow a specific pattern without writing long instructions." -->



## ZERO-SHOT Prompting
<!-- "Zero-shot prompting is when you ask an AI to perform a task without giving it any examples. You rely only on clear instructions in your prompt. Unlike one-shot or few-shot prompting, the model doesn’t see any sample output — it has to figure out the task directly from your instructions." -->

Summarize the following article in one concise sentence:  

"Researchers at MIT have developed a solar-powered desalination system that can provide clean drinking water at low cost to rural communities."

<!-- "In this case, I didn’t provide the AI with any sample summaries. I just gave a clear instruction — ‘Summarize in one concise sentence.’ That’s why it’s called zero-shot prompting. The model uses its general knowledge to complete the task without needing examples." -->

## MULTI-SHOT Prompting

You are an assistant that translates English sentences into French.  
Here are some examples:  

[Example 1]  
English: "Good morning, how are you?"  
French: "Bonjour, comment ça va ?"  

[Example 2]  
English: "I would like a cup of coffee, please."  
French: "Je voudrais une tasse de café, s'il vous plaît."  

[Example 3]  
English: "Where is the nearest train station?"  
French: "Où est la gare la plus proche ?"  

Now, translate the following sentence into French:  

English: "Can you help me find a good restaurant nearby?"  


## Dynamic Prompting

You are a fitness coach. Create a 15-minute workout plan for a user.  
User details:  
- Name: Sarah  
- Age: 28  
- Fitness Level: Beginner  
- Goal: Weight loss  

Generate a step-by-step plan with warm-up, main exercises, and cooldown.  

## Chain of thought Prompting

SYSTEM
You are a careful reasoner. Use internal step-by-step reasoning to solve problems,
but do NOT reveal that internal reasoning. Only output the requested fields.

USER
Task: Solve the problem below using private chain-of-thought. 
Output MUST be valid JSON with these keys:
{
  "answer": string,                      // final result only
  "key_steps": [string, string, string], // max 3 bullets, each ≤ 12 words
  "check": string                        // one-sentence sanity check
}

Rules:
- Think step-by-step internally.
- Do NOT reveal or narrate your internal chain-of-thought.
- "key_steps" must be high-level and concise (not detailed reasoning).
- If math is involved, ensure calculations are correct before responding.

Problem:
{problem_text}
