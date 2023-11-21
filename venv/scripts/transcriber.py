import assemblyai as aai

# set the API key
aai.settings.api_key = "c8abb89b59794434bf3a389c80797f6e"

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


