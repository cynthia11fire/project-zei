from agents import InteractionModule
import os
import sys

def main():
    print("Initializing Project Zei System...")
    print("Loading Multi-Agent Architecture (Logic + Persona + Interaction)...")
    
    # Simple check for API Key
    if not os.environ.get("GOOGLE_API_KEY"):
        print("\n[!] Error: GOOGLE_API_KEY environment variable not found.")
        print("Please export your API key first using:")
        print('export GOOGLE_API_KEY="your_api_key_here"')
        return

    try:
        zei_agent = InteractionModule()
        print("\n[System Online]")
    except Exception as e:
        print(f"\n[!] Initialization Error: {e}")
        return
    
    print("\n" + "="*40)
    print("   ZESTORY CAFÉ - VIRTUAL IDOL SYSTEM")
    print("   Powered by Google Gemini & ADK")
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
