def get_bot_token():
    file_path = "./bot_token.txt"
    with open(file_path) as f:
        return f.readline()[:-1]
