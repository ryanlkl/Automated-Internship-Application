import openai
from decouple import config
from information import *

openai.organization = "org-QYjvQh3cb3VZlXOk0lWndUr1"
openai.api_key = config("API_KEY")

def choose_answer(question,answersMap):
  closest_match = None
  closest_score = 0

  for k in answersMap:
    response = openai.Completion.create(
      engine="davinci",
      prompt=f"What option is closest to '{question}' from the following options: {k}?",
      max_tokens = 50,
      n = 1,
      stop = None,
      temperature=0.7
    )

    score = response.choices[0].score

    if score > closest_score:
      closest_match = k
      closest_score = score

  return closest_match

def choose_option(answer,*options):
  closest_match = None
  closest_score = 0

  for option in options:
    response = openai.Completion.create(
      engine="davinci",
      prompt=f"What option is closest to '{answer}' from the following options: {option}?",
      max_tokens = 50,
      n = 1,
      stop = None,
      temperature=0.7
    )

    score = response.choices[0].score

    if score > closest_score:
      closest_match = option
      closest_score = score

  return closest_match
