import gradio as gr

gr.Interface.load("models/Hello-SimpleAI/chatgpt-detector-roberta",
                  title="🤖 Detect AI Plagiarism", 
                  inputs=gr.inputs.Textbox(lines=5, label="Input Text")
).launch()