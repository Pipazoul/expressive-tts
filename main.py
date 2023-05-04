import gradio as gr
import subprocess
from fastapi import FastAPI
import gradio as gr



def tts(text,  model="macron"):
    model_path = ""
    config_path = ""
    if model == "macron":
        model_path = "models/macron/G_12000.pth"
        config_path = "models/macron/config.json"
    elif model == "yassin":
        model_path = "models/yassin/G_4000.pth"
        config_path = "models/yassin/config.json"

    subprocess.run(["pico2wave", "-l", "fr-FR", "-w", "temp.wav", text])
    # run subprocess svc infer -c models/macron/config.json -m models/macron/G-12000.pth -o output.wav temp.wav 
    subprocess.run(["svc", "infer", "-c", config_path, "-m", model_path, "-o", "output.wav", "temp.wav"])
    #return audio path__
    return "output.wav"
# input long text + select model (macron or yassin)
demo = gr.Interface(fn=tts, inputs=["text", gr.inputs.Radio(["macron", "yassin"])], outputs="audio", title="TTS Demo", description="Text to Speech Demo")
demo.launch()   