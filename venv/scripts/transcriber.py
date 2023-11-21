import assemblyai as aai
from keys import transcriberKey

# set the API key
aai.settings.api_key = transcriberKey

import assemblyai as aai

transcriber = aai.Transcriber()
config = aai.TranscriptionConfig(
    summarization=True,
    summary_model=aai.SummarizationModel.informative,
    summary_type=aai.SummarizationType.bullets
)

def convertAudioToText(save_path):
    transcript = transcriber.transcribe(save_path, config)
    return transcript.text


