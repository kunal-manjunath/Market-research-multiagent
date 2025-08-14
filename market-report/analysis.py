import gradio as gr
from dotenv import load_dotenv
from analysis_manager import AnalysisManager

load_dotenv(override=True)

async def run(query: str):
    async for chunk in AnalysisManager().run(query):
        yield chunk

with gr.Blocks(theme=gr.themes.Default(primary_hue="sky")) as ui:
    gr.Markdown("# Market analysis")
    query_textbox = gr.Textbox(label="What's your product idea?")
    run_button = gr.Button("Run", variant="primary")
    report = gr.Markdown(label="Report")
    
    run_button.click(fn=run, inputs=query_textbox, outputs=report)
    query_textbox.submit(fn=run, inputs=query_textbox, outputs=report)

ui.launch(inbrowser=True)