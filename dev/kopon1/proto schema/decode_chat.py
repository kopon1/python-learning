import codeium_common_pb2

def decode_chat_pb(path: str) -> None:
    data = open(path, "rb").read()
    msg = codeium_common_pb2.ContextScopeItem()
    try:
        msg.ParseFromString(data)
        print("Successfully parsed ContextScopeItem:")
        print(msg)
    except Exception as e:
        print(f"Failed to parse: {e}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python decode_chat.py chat.pb")
    else:
        decode_chat_pb(sys.argv[1])