# import os
import openai
from config import apikey


openai.api_key = "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"

response = openai.Completion.create(
  model="gpt-3.5-turbo-instruct",
  prompt="Write a mail to boss for resignation?",
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)
print(response)

'''
{
  "id": "cmpl-815166KEXvGsnuBFCnwsPuiVL1e20",
  "object": "text_completion",
  "created": 1695268304,
  "model": "gpt-3.5-turbo-instruct",
  "choices": [
    {
      "text": "\n\nSubject: Resignation Letter from [Your Name]\n\nDear [Boss\u2019s Name],\n\nI am writing this email to inform you of my decision to resign from my position as [Your Position] at [Company Name]. After careful consideration, I have decided to pursue other career opportunities that will enhance my professional growth and development.\n\nI am truly grateful for the experience and opportunities that I have been provided with during my time at [Company Name]. I am proud to have been a part of a dynamic and successful team, and I have learned a lot from my colleagues and superiors.\n\nI would like to assure you that I will do my best to complete my current projects and hand over my duties to my successor in a smooth and efficient manner. I am willing to assist with the transition process in any way possible and ensure that my departure does not cause any inconvenience to the company.\n\nPlease consider this letter as my two weeks\u2019 notice as per the company\u2019s policies. My last day at work will be [Date]. I will use my remaining time to complete any pending tasks and collaborate with my team to ensure a seamless transition.\n\nI would also like to express my sincere gratitude for your guidance, support, and mentorship throughout my time at [Company Name]. It has been an honor to",
      "index": 0,
      "logprobs": null,
      "finish_reason": "length"
    }
  ],
  "usage": {
    "prompt_tokens": 8,
    "completion_tokens": 256,
    "total_tokens": 264
  }
}
'''