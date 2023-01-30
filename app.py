import gradio as gr

gr.Interface.load("models/Hello-SimpleAI/chatgpt-detector-roberta", title="🤖 Detect AI Plagiarism").launch()