import requests
import json


def question():
  a = input("Deine Frage: ")
  headers = {
    'Content-Type':
    'application/json',
    'Authorization':
    'Bearer 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',
  }

  json_data = {
    'model': 'text-davinci-003',
    'prompt': a,
    'max_tokens': 4000,
    'temperature': 1.0,
  }

  response = requests.post('https://api.openai.com/v1/completions',
                           headers=headers,
                           json=json_data)
  r = response.json()
  print(r["choices"][0]["text"])
  return question()


question()