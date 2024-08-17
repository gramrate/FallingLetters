from openai import OpenAI

client = OpenAI(
api_key = "LA-9622c672a05f43fc9cc74ed79f7edd87f6a271b586734f40a46b7b4df86ef0e1",
base_url = "https://api.llama-api.com"
)

response = client.chat.completions.create(
    model="llama-13b-chat",
    messages=[
        {"role": "system", "content": "Assistant is a large language model trained by OpenAI."},
        {"role": "user", "content": "Who were the founders of Microsoft?"}
    ]

)

#print(response)
print(response.model_dump_json(indent=2))
print(response.choices[0].message.content)
