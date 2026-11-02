import os
from dotenv import load_dotenv
from google import genai

# Carrega as variáveis do arquivo .env
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("A variável GEMINI_API_KEY não foi encontrada. Verifique seu arquivo .env.")

# Inicializa o cliente do Gemini
client = genai.Client(api_key=api_key)

def main():
    print("=== Agente IA Gemini (CLI Básico) ===")
    print("Digite sua pergunta ou 'sair' para encerrar.\n")

    while True:
        try:
            user_input = input("Você: ")
            
            if user_input.strip().lower() in ["sair", "exit", "quit"]:
                print("Encerrando o agente...")
                break

            if not user_input.strip():
                continue

            # Solicitação ao modelo
            response = client.models.generate_content(
                model="gemini-3.8-flash",
                contents=user_input,
            )

            print(f"\nGemini: {response.text}\n")

        except Exception as e:
            print(f"\nErro ao processar solicitação: {e}\n")

if __name__ == "__main__":
    main()