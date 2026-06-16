import json


def extract_json(llm_response: str):

    print("\n===== JSON EXTRACTOR =====")
    print("TYPE:", type(llm_response))
    print("RAW REPR:")
    print(repr(llm_response))
    print("==========================")

    start = llm_response.find("{")
    end = llm_response.rfind("}")

    print("START =", start)
    print("END =", end)

    if start == -1:
        raise Exception(
            "No opening JSON brace found"
        )

    if end == -1:
        raise Exception(
            "No closing JSON brace found"
        )

    json_string = llm_response[
        start:end + 1
    ]

    print("\nEXTRACTED JSON:")
    print(json_string)

    return json.loads(json_string)