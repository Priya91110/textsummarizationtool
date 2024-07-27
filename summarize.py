import click
from langchain_community.llms import Ollama

# Initialize Ollama with the Qwen2 0.5B model
llm = Ollama(model="qwen2:0.5b")

def summarize_text(text: str) -> str:
    response = llm.invoke(text)
    return response

@click.command()
@click.option('--text', '-t', help='Text to summarize')
@click.option('--file', '-f', type=click.Path(exists=True), help='File path of the text to summarize')
def summarize(text, file):
    if text and file:
        click.echo("Please provide either text or file, not both.")
        return

    if file:
        with open(file, 'r') as f:
            content = f.read()
            content = f"summarize this text: {content}"
            summary = summarize_text(content)
            click.echo(summary)

    if text:
        content = f"summarize this text: {text}"
        summary = summarize_text(content)
        click.echo(summary)

if __name__ == '__main__':
    summarize()
# python summarize.py --file D:/textSummarizationTool/myfile.txt