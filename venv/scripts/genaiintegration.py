import google.generativeai as palm
import os
from string import Template
from generalresources import dateTimeString
from keys import apiKey

palm.configure(api_key=apiKey)

models = [m for m in palm.list_models() if 'generateText' in m.supported_generation_methods]
model = models[0].name

prompt = Template("""

Given a description of a person's working routine, your task is to identify and summarize the actions performed and their corresponding time frames. 

Instructions:
1. Identify each action along with its specific time period. Time periods can be exact (e.g., 9am to 5pm), relative (e.g., morning, afternoon, evening), or based on days of the week.
2. Group actions that occur within the same time span.
3. Present the information in a structured format where each line begins with the time span, followed by a concise summary of actions in noun phrase form.
4. Use the date format: %d/%m/%Y %H:%M. Today's date is $date . Convert relative dates (like 'yesterday' or 'last Monday') into actual dates using $date as a reference. Assume the last occurrence of a weekday prior to $date.
5. Focus on clarity and brevity in summarizing actions.

Now, extract and summarize the information from the following description:
$text


""")


def generateSummary(text):
    completePrompt = prompt.substitute(text=text, date=dateTimeString)
    completion = palm.generate_text(
        model=model,
        prompt=completePrompt,
        temperature=0,
        # The maximum length of the response
        max_output_tokens=2000,
    )
    return completion.result + "\n\n" + text + "\n\n" + dateTimeString
