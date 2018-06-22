"""The Context Processors Module
"""

from app import app

@app.context_processor
def utility_processor():

    def format_lamina(lamina):
        return "%03d" % lamina.numero

    return dict(format_lamina=format_lamina)
