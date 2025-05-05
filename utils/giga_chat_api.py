import json
from uuid import uuid4

import requests

from config import command_line_args


def get_motivational_quote() -> str:
    prompt = "Сгенерируй мотивирующую цитату. На 50-100 символов"
    request_data = {
        "model": "GigaChat",
        "messages": [
            {
                "role": "system",
                "content": "Ты - преподаватель курса личностного роста"

            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        "stream": False,
    }
    request_data_json = json.dumps(request_data)
    headers = {
        "Authorization": get_bearer_token(),
    }

    response = requests.post(
        url="https://gigachat.devices.sberbank.ru/api/v1/chat/completions",
        verify=False,
        headers=headers,
        data=request_data_json,
    )
    response_body = response.json()
    return response_body["choices"][0]["message"]["content"]


def get_bearer_token() -> str:
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept": "application/json",
        "RqUID": str(uuid4()),
        "Authorization": f"Basic {command_line_args.ai_api_key}",
    }
    request_data = {
        "scope": "GIGACHAT_API_PERS",
    }

    response = requests.post(
        url="https://ngw.devices.sberbank.ru:9443/api/v2/oauth",
        verify=False,
        headers=headers,
        data=request_data,
    )
    response_body = response.json()

    return f"Bearer {response_body["access_token"]}"
