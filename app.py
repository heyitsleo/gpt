import gradio as gr

gr.Interface.load("models/Hello-SimpleAI/chatgpt-detector-roberta",
                  title="🤖 Start detecting AI Plagiarism",
                 description= "Paste your text and get an estimation of how much is believed to be written by a human vs AI. This model is based on Hello Simple's paper [arxiv: 2301.07597](https://arxiv.org/abs/2301.07597) and Github project [Hello-SimpleAI/chatgpt-comparison-detection](https://github.com/Hello-SimpleAI/chatgpt-comparison-detection).").launch()