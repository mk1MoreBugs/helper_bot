import argparse


def parse_command_line_arguments()-> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--tg_bot_key", required=True)
    parser.add_argument("--weather_api_key", required=True)
    parser.add_argument("--ai_api_key", required=True)
    return parser.parse_args()
