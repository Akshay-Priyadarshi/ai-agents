from dotenv import load_dotenv
from uuid import uuid4
from google.adk.runners import Runner
from google.genai import types
from google.adk.sessions.in_memory_session_service import InMemorySessionService
from qna_agent import question_answering_agent
import asyncio

load_dotenv()

in_memory_session_service = InMemorySessionService()

initial_state = {
    "user_name": "Akshay",
    "user_skills": {
        "languages": [
            "Java",
            "Python",
            "C#",
            "Typescript",
            "Javascript",
            "HTML5",
            "CSS3",
            "Golang",
        ],
        "frameworks": [
            "Dotnet",
            "Spring",
            "Express",
            "Fiber"
        ],
        "clouds": [
            "Azure",
            "GCP",
            "AWS"
        ]
    }
}

APP_NAME="QnA Agent"
USER_ID="awwwkshay"
SESSION_ID=str(uuid4())

runner = Runner(
    agent=question_answering_agent,
    app_name=APP_NAME,
    session_service=in_memory_session_service
)

new_message = types.Content(
    role="user", parts=[types.Part(text="What is Akshay good at?")]
)

async def main():
    await in_memory_session_service.create_session(
        app_name=APP_NAME,
        user_id=USER_ID,
        session_id=SESSION_ID,
        state=initial_state
    )

    for event in runner.run(
        user_id=USER_ID,
        session_id=SESSION_ID,
        new_message=new_message,
    ):
        if event.is_final_response():
            if event.content and event.content.parts:
                print(f"Final Response: {event.content.parts[0].text}")

    print("==== Session Event Exploration ====")
    session = await in_memory_session_service.get_session(
        app_name=APP_NAME, user_id=USER_ID, session_id=SESSION_ID
    )

    # Log final Session state
    print("=== Final Session State ===")
    if session:  # Check if session is not None
        for key, value in session.state.items():
            print(f"{key}: {value}")
    else:
        print("Session not found.")

if __name__ == "__main__":
    asyncio.run(main())


