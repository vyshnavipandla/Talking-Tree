import openai
openai.api_key = "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"
#text="what is meant by frequency"
def intel(text):
  response = openai.Completion.create(
    engine="text-davinci-003",
    prompt=text,
    temperature=0,
    max_tokens=50,
    
    
  top_p=1.0,
  frequency_penalty=0.0,
  presence_penalty=0.0,
  stop=["###"]
  )
  data_1=(response.choices[0].text)
  print(data_1)
  return data_1
