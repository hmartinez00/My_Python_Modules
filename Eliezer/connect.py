import openai

openai.api_key = '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'

completion = openai.Completion.create(
    engine='text-davinci-003',
    prompt='Que es ChatGPT',
    max_token=2048
)

ans = completion.choice[0].text

print(ans)