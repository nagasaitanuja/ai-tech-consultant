def create_sow(meeting_request):
    """
    Checks if requirement is an existing setting or custom code.
    - Setting: 1 hour ($100)
    - Custom code: 12 hours ($1,200)
    """
    brain_result = ask_knowledge_brain(meeting_request)
    
    if "Found in Brilliant Directories" in brain_result:
        task_type = "Built-in Setting (No Custom Code Needed)"
        hours = 1
    else:
        task_type = "Custom Developer Code"
        hours = 12
        
    return (
        f"REQUIREMENT: {meeting_request}\n"
        f"TYPE: {task_type}\n"
        f"ESTIMATED HOURS: {hours} hr(s)\n"
        f"ESTIMATED COST: ${hours * 100}"
    )
