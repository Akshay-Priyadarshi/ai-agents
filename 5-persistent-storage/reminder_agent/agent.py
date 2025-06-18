from google.adk.agents import Agent
from google.adk.tools.tool_context import ToolContext
from .reminder import Reminder
from datetime import datetime, date as date_type, time as time_type


def add_reminder(reminder_description: str, date_str: str, time_str: str, tool_context: ToolContext) -> dict:
    """Add a new reminder to the user's reminder list.

    Args:
        reminder_description: The description for the reminder
        date_str: The date at which the user should be reminded (YYYY-MM-DD string)
        time_str: The time at which the user should be reminded (HH:MM:SS string)
        tool_context: Context for accessing and updating session state

    Returns:
        A confirmation message
    """
    print(f"--- Tool: add_reminder called for '{reminder_description}' on {date_str} at {time_str} ---")

    try:
        parsed_date = datetime.strptime(date_str, "%Y-%m-%d").date()
        parsed_time = datetime.strptime(time_str, "%H:%M:%S").time()
    except ValueError as e:
        return {
            "action": "add_reminder",
            "status": "error",
            "message": f"Invalid date or time format. Please use YYYY-MM-DD for date and HH:MM:SS for time. Error: {e}",
        }

    # Get current reminders from state
    reminders = tool_context.state.get("reminders", [])

    # Create a Reminder object
    new_reminder = Reminder(
        date=parsed_date,
        time=parsed_time,
        description=reminder_description,
        is_done=False,
    )

    # Add the new reminder after converting date and time to strings
    reminder_dict = new_reminder.model_dump()
    reminder_dict["date"] = new_reminder.date.isoformat()
    reminder_dict["time"] = new_reminder.time.isoformat()
    reminders.append(reminder_dict)

    # Update state with the new list of reminders
    tool_context.state["reminders"] = reminders

    return {
        "action": "add_reminder",
        "reminder": reminder_description,
        "message": f"Added reminder: {reminder_description} on {date_str} at {time_str}",
    }


def view_reminders(tool_context: ToolContext) -> dict:
    """View all current reminders.

    Args:
        tool_context: Context for accessing session state

    Returns:
        The list of reminders
    """
    print("--- Tool: view_reminders called ---")

    # Get reminders from state
    reminders_data = tool_context.state.get("reminders", [])
    
    # Convert string dates/times to datetime objects for Pydantic model initialization
    parsed_reminders = []
    for r_data in reminders_data:
        r_data["date"] = datetime.strptime(r_data["date"], "%Y-%m-%d").date() if isinstance(r_data.get("date"), str) else r_data.get("date")
        r_data["time"] = datetime.strptime(r_data["time"], "%H:%M:%S").time() if isinstance(r_data.get("time"), str) else r_data.get("time")
        parsed_reminders.append(Reminder(**r_data))
    reminders = parsed_reminders

    # Convert Reminder objects back to dictionaries with ISO formatted date/time strings for output
    output_reminders = []
    for r in reminders:
        r_dict = r.model_dump()
        r_dict["date"] = r.date.isoformat()
        r_dict["time"] = r.time.isoformat()
        output_reminders.append(r_dict)

    return {"action": "view_reminders", "reminders": output_reminders, "count": len(reminders)}


def update_reminder(index: int, updated_text: str, tool_context: ToolContext) -> dict:
    """Update an existing reminder.

    Args:
        index: The 1-based index of the reminder to update
        updated_text: The new text for the reminder
        tool_context: Context for accessing and updating session state

    Returns:
        A confirmation message
    """
    print(
        f"--- Tool: update_reminder called for index {index} with '{updated_text}' ---"
    )

    # Get current reminders from state
    reminders_data = tool_context.state.get("reminders", [])
    parsed_reminders = []
    for r_data in reminders_data:
        r_data["date"] = datetime.strptime(r_data["date"], "%Y-%m-%d").date() if isinstance(r_data.get("date"), str) else r_data.get("date")
        r_data["time"] = datetime.strptime(r_data["time"], "%H:%M:%S").time() if isinstance(r_data.get("time"), str) else r_data.get("time")
        parsed_reminders.append(Reminder(**r_data))
    reminders = parsed_reminders

    # Check if the index is valid
    if not reminders or index < 1 or index > len(reminders):
        return {
            "action": "update_reminder",
            "status": "error",
            "message": f"Could not find reminder at position {index}. Currently there are {len(reminders)} reminders.",
        }

    # Update the reminder (adjusting for 0-based indices)
    old_reminder = reminders[index - 1].description
    reminders[index - 1].description = updated_text

    # Update state with the modified list, converting date and time to strings
    updated_reminders_list = []
    for r in reminders:
        r_dict = r.model_dump()
        r_dict["date"] = r.date.isoformat()
        r_dict["time"] = r.time.isoformat()
        updated_reminders_list.append(r_dict)
    tool_context.state["reminders"] = updated_reminders_list

    return {
        "action": "update_reminder",
        "index": index,
        "old_text": old_reminder,
        "updated_text": updated_text,
        "message": f"Updated reminder {index} from '{old_reminder}' to '{updated_text}'",
    }


def delete_reminder(index: int, tool_context: ToolContext) -> dict:
    """Delete a reminder.

    Args:
        index: The 1-based index of the reminder to delete
        tool_context: Context for accessing and updating session state

    Returns:
        A confirmation message
    """
    print(f"--- Tool: delete_reminder called for index {index} ---")

    # Get current reminders from state
    reminders_data = tool_context.state.get("reminders", [])
    parsed_reminders = []
    for r_data in reminders_data:
        r_data["date"] = datetime.strptime(r_data["date"], "%Y-%m-%d").date() if isinstance(r_data.get("date"), str) else r_data.get("date")
        r_data["time"] = datetime.strptime(r_data["time"], "%H:%M:%S").time() if isinstance(r_data.get("time"), str) else r_data.get("time")
        parsed_reminders.append(Reminder(**r_data))
    reminders = parsed_reminders

    # Check if the index is valid
    if not reminders or index < 1 or index > len(reminders):
        return {
            "action": "delete_reminder",
            "status": "error",
            "message": f"Could not find reminder at position {index}. Currently there are {len(reminders)} reminders.",
        }

    # Remove the reminder (adjusting for 0-based indices)
    deleted_reminder = reminders.pop(index - 1)

    # Update state with the modified list, converting date and time to strings
    updated_reminders_list = []
    for r in reminders:
        r_dict = r.model_dump()
        r_dict["date"] = r.date.isoformat()
        r_dict["time"] = r.time.isoformat()
        updated_reminders_list.append(r_dict)
    tool_context.state["reminders"] = updated_reminders_list

    return {
        "action": "delete_reminder",
        "index": index,
        "deleted_reminder": deleted_reminder.description,
        "message": f"Deleted reminder {index}: '{deleted_reminder.description}'",
    }


def update_user_name(name: str, tool_context: ToolContext) -> dict:
    """Update the user's name.

    Args:
        name: The new name for the user
        tool_context: Context for accessing and updating session state

    Returns:
        A confirmation message
    """
    print(f"--- Tool: update_user_name called with '{name}' ---")

    # Get current name from state
    old_name = tool_context.state.get("user_name", "")

    # Update the name in state
    tool_context.state["user_name"] = name

    return {
        "action": "update_user_name",
        "old_name": old_name,
        "new_name": name,
        "message": f"Updated your name to: {name}",
    }


def mark_reminder_done(index: int, tool_context: ToolContext) -> dict:
    """Mark a reminder as done.

    Args:
        index: The 1-based index of the reminder to mark as done
        tool_context: Context for accessing and updating session state

    Returns:
        A confirmation message
    """
    print(f"--- Tool: mark_reminder_done called for index {index} ---")

    # Get current reminders from state
    reminders_data = tool_context.state.get("reminders", [])
    parsed_reminders = []
    for r_data in reminders_data:
        r_data["date"] = datetime.strptime(r_data["date"], "%Y-%m-%d").date() if isinstance(r_data.get("date"), str) else r_data.get("date")
        r_data["time"] = datetime.strptime(r_data["time"], "%H:%M:%S").time() if isinstance(r_data.get("time"), str) else r_data.get("time")
        parsed_reminders.append(Reminder(**r_data))
    reminders = parsed_reminders

    # Check if the index is valid
    if not reminders or index < 1 or index > len(reminders):
        return {
            "action": "mark_reminder_done",
            "status": "error",
            "message": f"Could not find reminder at position {index}. Currently there are {len(reminders)} reminders.",
        }

    # Mark the reminder as done (adjusting for 0-based indices)
    reminders[index - 1].is_done = True
    marked_reminder_description = reminders[index - 1].description

    # Update state with the modified list, converting date and time to strings
    updated_reminders_list = []
    for r in reminders:
        r_dict = r.model_dump()
        r_dict["date"] = r.date.isoformat()
        r_dict["time"] = r.time.isoformat()
        updated_reminders_list.append(r_dict)
    tool_context.state["reminders"] = updated_reminders_list

    return {
        "action": "mark_reminder_done",
        "index": index,
        "marked_reminder": marked_reminder_description,
        "message": f"Marked reminder {index}: '{marked_reminder_description}' as done.",
    }


# Create a simple persistent agent
memory_agent = Agent(
    name="memory_agent",
    model="gemini-2.0-flash",
    description="A smart reminder agent with persistent memory",
    instruction="""
    You are a friendly reminder assistant that remembers users across conversations.
    
    The user's information is stored in state:
    - User's name: {user_name}
    - Reminders: {reminders}
    - Current date: {current_date}
    - Current time: {current_time}
    
    You can help users manage their reminders with the following capabilities:
    1. Add new reminders (with a description, date, time, and a 'done' status)
    2. View existing reminders
    3. Update reminders
    4. Delete reminders
    5. Update the user's name
    6. Mark a reminder as done
    
    Always be friendly and address the user by name. If you don't know their name yet,
    use the update_user_name tool to store it when they introduce themselves.
    
    **REMINDER MANAGEMENT GUIDELINES:**
    
    When dealing with reminders, you need to be smart about finding the right reminder:
    
    1. When the user asks to update or delete a reminder but doesn't provide an index:
       - If they mention the content of the reminder (e.g., "delete my meeting reminder"), 
         look through the reminders to find a match by checking the 'description' field of each reminder object.
       - If you find an exact or close match, use that index
       - Never clarify which reminder the user is referring to, just use the first match
       - If no match is found, list all reminders and ask the user to specify
    
    2. When the user mentions a number or position:
       - Use that as the index (e.g., "delete reminder 2" means index=2)
       - Remember that indexing starts at 1 for the user
    
    3. For relative positions:
       - Handle "first", "last", "second", etc. appropriately
       - "First reminder" = index 1
       - "Last reminder" = the highest index
       - "Second reminder" = index 2, and so on
    
    4. For viewing:
       - Always use the view_reminders tool when the user asks to see their reminders
       - Format the response in a numbered list for clarity, showing the description, date, time, and whether it's done.
       - If there are no reminders, suggest adding some
    
    5. For addition:
       - Extract the actual reminder description from the user's request
       - Remove phrases like "add a reminder to" or "remind me to"
       - Focus on the task itself (e.g., "add a reminder to buy milk" → add_reminder(reminder_description="buy milk", date_str="2024-12-25", time_str="10:00:00"))
       - You MUST extract the date and time from the user's request and pass it to the add_reminder tool as strings in "YYYY-MM-DD" and "HH:MM:SS" format respectively.
       - If the user does not specify a date or time, use the current date and time from the state.
       - For relative dates:
         * "tomorrow" = current_date + 1 day
         * "next week" = current_date + 7 days
         * "next month" = current_date + 30 days
         * "next Monday" = next occurrence of Monday from current_date
         * "next Tuesday" = next occurrence of Tuesday from current_date
         * etc.
       - For relative times:
         * "morning" = "09:00:00"
         * "afternoon" = "14:00:00"
         * "evening" = "18:00:00"
         * "night" = "20:00:00"
         * "noon" = "12:00:00"
         * "midnight" = "00:00:00"
    
    6. For updates:
       - Identify both which reminder to update and what the new description should be
       - For example, "change my second reminder to pick up groceries" → update_reminder(2, "pick up groceries")
       - You MUST preserve the existing date and time for the reminder during updates.
    
    7. For deletions:
       - Confirm deletion when complete and mention which reminder was removed
       - For example, "I've deleted your reminder to 'buy milk'"

    8. For marking as done:
       - When the user asks to mark a reminder as done, use the mark_reminder_done tool.
       - Identify the reminder by index or content, similar to updates and deletions.
       - Confirm that the reminder has been marked as done.
    
    Remember to explain that you can remember their information across conversations.

    IMPORTANT:
    - use your best judgement to determine which reminder the user is referring to. 
    - You don't have to be 100% correct, but try to be as close as possible.
    - Never ask the user to clarify which reminder they are referring to.
    - Always use the current_date and current_time from state when calculating relative dates and times.
    """,
    tools=[
        add_reminder,
        view_reminders,
        update_reminder,
        delete_reminder,
        update_user_name,
        mark_reminder_done,
    ],
)