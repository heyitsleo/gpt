import gradio as gr

gr.Interface.load("models/Hello-SimpleAI/chatgpt-detector-roberta",
                  title="🤖 Start detecting AI Plagiarism",
                 description= "Paste in the text you want to check and get a holistic score for how much of the document is written by AI. This model is based on Hello Simple's paper [arxiv: 2301.07597](https://arxiv.org/abs/2301.07597) and Github project [Hello-SimpleAI/chatgpt-comparison-detection](https://github.com/Hello-SimpleAI/chatgpt-comparison-detection).").launch()