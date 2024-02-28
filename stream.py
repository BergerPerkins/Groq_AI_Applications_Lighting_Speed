import os
from groq import Groq

client=Groq(
    api_key=os.environ.get('GROQ_API_KEY'),
)

stream = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Explain the importance of low latency LLms"
        }
    ],
    model="mixtral-8x7b-32768",
    stream=True,
    temperature=0.5,
    max_tokens=1024,
    top_p=1,
    stop=None,
)
for chunk in stream:
    print(chunk.choices[0].delta.content,end="")