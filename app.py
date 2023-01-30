import gradio as gr

gr.Interface(inputs=gr.inputs.Textbox(lines=5, label="Input Text")).load("models/Hello-SimpleAI/chatgpt-detector-roberta", title="🤖 Detect AI Plagiarism").launch()