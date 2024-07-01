from graph import graph


def print_stream(stream):
    for s in stream:
        message = s["messages"][-1]
        if isinstance(message, tuple):
            print(message)
        else:
            message.pretty_print()


config = {"configurable": {"thread_id": "1"}}
inputs = {"messages": [("user", "create a virtual machine")]}

print_stream(graph.stream(inputs, config=config, stream_mode="values"))
