import replicate

# Llama_chat() takes a string as input and returns a string as output
def Llama_chat(message : str):
    output = replicate.run(
        "meta/llama-2-70b-chat:02e509c789964a7ea8736978a43525956ef40397be9033abf9fd2badfe68c9e3",
        input={"prompt": message}
    )
    res = ""
    for item in output:
        res += item
    return str(res)

# test
if __name__ == "__main__":
    res =Llama_chat("Hello, I'm Llama. I'm a bot.")
    print(res)