import gradio as gr

auth_token = "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"
model = gr.Interface.load("models/Hello-SimpleAI/chatgpt-detector-roberta", api_key=auth_token)

def predict_en(text):
    res = model(text)[0]
    return res['label'],res['score']

with gr.Blocks() as demo:
    gr.Markdown("""
                     # 🤖 Start detecting AI Plagiarism
                     Paste in the text you want to check and get a holistic score for how much of the document is written by AI. This model is based on Hello Simple's paper [arxiv: 2301.07597](https://arxiv.org/abs/2301.07597) and Github project [Hello-SimpleAI/chatgpt-comparison-detection](https://github.com/Hello-SimpleAI/chatgpt-comparison-detection).
                """)
    with gr.Tab("English"):
        gr.Markdown("""
                    Note: Providing more text to the `Text` box can make the prediction more accurate!
                    """)
        t1 = gr.Textbox(lines=5, label='Text',value="There are a few things that can help protect your credit card information from being misused when you give it to a restaurant or any other business:\n\nEncryption: Many businesses use encryption to protect your credit card information when it is being transmitted or stored. This means that the information is transformed into a code that is difficult for anyone to read without the right key.")
        button1 = gr.Button("🤖 Predict!")
        label1 = gr.Textbox(lines=1, label='Predicted Label 🎃')
        score1 = gr.Textbox(lines=1, label='Likelihood')

    button1.click(predict_en, inputs=[t1], outputs=[label1,score1])


demo.launch()