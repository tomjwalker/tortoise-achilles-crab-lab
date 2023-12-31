from tac.env.openai import OpenAIEnv


def make_env(spec):
    """API for creating an env from a spec within the TAC framework"""
    env = OpenAIEnv(spec)
    return env
