import evaluate
from openai import OpenAI

api_key = "sk-proj-UeiL7KrdPp5gGML8bAlkT3BlbkFJWk0ZR9TY54s6TVcgiuOq"
client = OpenAI(api_key=api_key)

completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system",
         "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
        {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
    ]
)

print(completion.choices[0].message)

# rouge = evaluate.load('rouge')
# predictions = ["hello goodbye", "ankh morpork"]
# references = ["goodbye", "general kenobi"]
# results = rouge.compute(predictions=predictions,
#                         references=references,
#                         rouge_types=['rouge_1'],
#                         use_aggregator=True)
# print(list(results.keys()))
# print(results["rouge1"])
