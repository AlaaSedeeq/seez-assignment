def _print_event(event: dict, _printed: set, max_length=1500):
    current_state = event.get("dialog_state")
    if current_state:
        print("Currently in: ", current_state[-1])
    message = event.get("messages")
    if message:
        if isinstance(message, list):
            message = message[-1]
        if message.id not in _printed:
            msg_repr = message.pretty_repr(html=True)
            if len(msg_repr) > max_length:
                msg_repr = msg_repr[:max_length] + " ... (truncated)"
            print(msg_repr)
            _printed.add(message.id)
            
def start_chat(graph, config):
    _printed = set()
    while True:
        question = input("Write your question: (write exit to exit) ")
        if question.lower() == "exit":
            break
        events = graph.stream(
            {
                "messages": ("user", question)
            }, 
            config, 
            stream_mode="values"
        )
        for event in events:
            _print_event(event, _printed)
