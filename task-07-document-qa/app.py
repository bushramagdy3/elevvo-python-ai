import gradio
from main import getResponse

def function(query :str):
    response  = getResponse(query)
    citation_text = ""
    for i, citation in enumerate(response.citation):
            citation_text += f"Source {i+1} : {citation.source}\n"
            citation_text += f"Chunk {i+1} : {citation.chunk}\n"
            citation_text += "--------------\n"
    return response.response, citation_text

demo = gradio.Interface(fn=function,
                        inputs=gradio.Text(label="Query"),
                        outputs=[gradio.Text(label="Response"), gradio.Text(label="Citations")])

demo.launch()