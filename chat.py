from openai import OpenAI

client = OpenAI()

response=client.responses.create(
    input="In sentence,what is CS50?",
    model="gpt-3.5-turbo"
)

print(responnse.output_text)