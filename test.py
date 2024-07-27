from langchain_community.llms import Ollama


llm = Ollama(model = "qwen2:0.5b")
# takes text as input and res
def summarize(text:str)->str:
    response = llm.invoke(text)
    # "summarize this text. The Kargil War, fought between India and Pakistan in 1999, remains one of the most significant and poignant chapters in the annals of Indian military history. Taking place in the treacherous mountainous terrain of the Kargil district in Jammu and Kashmir, this conflict not only tested the mettle of the Indian Armed Forces but also demonstrated the resilience and resolve of the nation.Background and Prelude to the ConflictThe origins of the Kargil War can be traced back to the long-standing territorial disputes between India and Pakistan over the Kashmir region. The Line of Control (LoC), established as a de facto border, often witnessed skirmishes and ceasefire violations. However, the situation escalated dramatically in early 1999 when Pakistani soldiers and militants infiltrated into Indian territory across the LoC, occupying strategic heights and positions in the Kargil sector.The intrusion was part of a well-planned operation by the Pakistan Army, aiming to cut off the vital Srinagar-Leh highway, thereby disrupting the supply and communication lines to the Indian troops stationed in the Siachen Glacier and the Ladakh region. ")
    print(len(response))
    print(response)
    
def summarize_file(file_path : str)-> str:
    with open(file_path, 'r') as file:
       text = file.read()
       print(len(text))
       text = f"summarize this text. {text}"
    summary = summarize(text)
summarize_file('D:/textSummarizationTool/myfile.txt')


# Create a command line tool using python that takes a text file as a parameter and returns the summary of the text.
# It can also take text instead of text file as parameter and return the summary. 
# Please use the following tools- 
# Ollama API, Qwen2 0.5B model in Ollama, 
# Click library of Python. 
# You may substitute Python for any other language 
# but you must use Ollama ans Qwen2 0.5B model. 
