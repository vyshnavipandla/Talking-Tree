"""In this "openai_1.py" file import "openai" module and set the access key used for authentication.
define a function "intel" and argument is "text".
"response" send a request to the openai follows the parameters.
"data_1" extracts the generated text from the response object returned by the API.
and returns the data."""


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
