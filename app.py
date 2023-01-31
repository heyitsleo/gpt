import os
import gradio as gr
from transformers import pipeline

auth_token = os.environ.get("access_token")
pipeline_en = pipeline(task="text-classification", model="Hello-SimpleAI/chatgpt-detector-roberta",use_auth_token=auth_token)


def predict_en(text):
    res = pipeline_en(text)[0]
    label = res['label']
    score = round(res['score']*100, 2)
    return "%d%% chance"%score, label


with gr.Blocks() as demo:
    gr.Markdown("""
                     # 🤖 AI Plagiarism Checker by Jurnee
                     Paste in the text you want to check and get a holistic score for how much of the document is written by AI. We recommend that educators take these results as one of many pieces in their assessment of student work. This model is based on Hello Simple's paper [arxiv: 2301.07597](https://arxiv.org/abs/2301.07597) and Github project [Hello-SimpleAI/chatgpt-comparison-detection](https://github.com/Hello-SimpleAI/chatgpt-comparison-detection).
                """)
    with gr.Tab("Try it out 👇"):
        gr.Markdown("""
                    Note: Providing more text to the `Text` box can make the prediction more accurate!
                    """)
        t1 = gr.Textbox(lines=5, label='Paste the text you want to check',value="There are a few things that can help protect your credit card information from being misused when you give it to a restaurant or any other business:\n\nEncryption: Many businesses use encryption to protect your credit card information when it is being transmitted or stored. This means that the information is transformed into a code that is difficult for anyone to read without the right key.")
        button1 = gr.Button("👀 See results")
        score1 = gr.Textbox(lines=1, label='There is a')
        label1 = gr.Textbox(lines=1, label='That this text is written entirely by')

    button1.click(predict_en, inputs=[t1], outputs=[score1, label1])

demo.launch()