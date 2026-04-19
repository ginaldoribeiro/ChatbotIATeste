from langchain_ollama import OllamaLLM
from langchain_core.prompts import PromptTemplate

llm = OllamaLLM(model="llama3.2:1b")
prompt = PromptTemplate.from_template("Usuário: {pergunta}\nIA:")
chain = prompt | llm

print("Chatbot IA Local(Langchain + Ollama)")
print("Digite 'sair' para encerrar o programa!")

while True:
    pergunta = input("Você: ")
    
    if pergunta.lower() in ['sair', 'exit', 'quit']:
        print("IA: Até Logo!")
        break 

    resposta = chain.invoke({"pergunta": pergunta})
    print(f"IA: {resposta}\n")