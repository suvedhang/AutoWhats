from parser.agent_interface import gemini_agent  # or gemini_agent.py
from utils.command_validator import validate_command_json
from controller.automation_controller import AutomationController

def main():
    controller = AutomationController()
    print("Agentic AI WhatsApp Automation")

    while True:
        user_input = input(">> ")

        agent_output = gemini_agent(user_input)
        print("Agent Output:", agent_output)

        if not validate_command_json(agent_output):
            print("❌ Invalid agent output")
            continue

        result = controller.execute(agent_output)
        print("Result:", result)

if __name__ == "__main__":
    main()
