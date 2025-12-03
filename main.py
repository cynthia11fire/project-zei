from agents import InteractionModule
from dotenv import load_dotenv  # 新增：讓程式能讀懂 .env 檔
import os
import sys

# 載入 .env 檔案中的環境變數 (這是關鍵！)
load_dotenv()

def main():
    print("Initializing Project Zei System...")
    print("Loading Multi-Agent Architecture (Logic + Persona + Interaction)...")
    
    # 檢查 API Key 是否存在
    if not os.environ.get("GOOGLE_API_KEY"):
        print("\n[!] Error: GOOGLE_API_KEY environment variable not found.")
        print("Please make sure you have created the '.env' file with your API key.")
        return

    try:
        zei_agent = InteractionModule()
        print("\n[System Online]")
    except Exception as e:
        print(f"\n[!] Initialization Error: {e}")
        return
    
    # 保留您原本漂亮的介面設計
    print("\n" + "="*40)
    print("    ZESTORY CAFÉ - VIRTUAL IDOL SYSTEM")
    print("    Powered by Google Gemini & ADK")
    print("="*40)
    print("Zei is ready to chat. Type 'exit' or 'quit' to end session.\n")
    
    while True:
        try:
            user_input = input("You: ")
            if user_input.lower() in ['exit', 'quit']:
                print("\nZei: See you next time at ZESTORY Café. Goodbye!")
                break
            
            if not user_input.strip():
                continue
                
            response = zei_agent.generate_response(user_input)
            print(f"Zei: {response}\n")
            
        except KeyboardInterrupt:
            print("\n\n[Session Interrupted]. Goodbye!")
            sys.exit(0)
        except Exception as e:
            print(f"\n[!] Runtime Error: {e}")

if __name__ == "__main__":
    main()
