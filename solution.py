import pandas as pd
import numpy as np


chat_id = 975846018 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    t = 52
    n = len(x)
    lamb = x.sum() / (n * t)
    return lamb
