import gradio as gr

gr.Interface(title="hello world").load("models/Hello-SimpleAI/chatgpt-detector-roberta").launch()