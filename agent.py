import os
from openai import OpenAI

# Initialize client using GitHub's unified inference endpoint
client = OpenAI(
    base_url="https://models.inference.ai.azure.com",
    api_key=os.environ["GITHUB_TOKEN"]
)

# A raw Playwright timeout error for the AI to analyze
playwright_log = """
TimeoutError: locator.click: Timeout 30000ms exceeded.
Call log:
  - waiting for locator("button#log-in-submit")
  - locator resolved to <button id="log-in-submit" disabled>Login</button>
  - attempting click action
  - element is disabled - retrying...
"""

# Request chat completion from the model (e.g., gpt-4o, DeepSeek-R1)
response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "You are a QA expert. Keep answers concise."},
        {"role": "user", "content": f"Analyze this failed Playwright test log:\n\n{playwright_log}"}
    ]
)

print("\n--- AI Analysis ---")
print(response.choices[0].message.content)
