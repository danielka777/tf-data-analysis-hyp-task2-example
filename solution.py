import pandas as pd
import numpy as np
from scipy.stats import anderson_ksamp

chat_id = 1050115025 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    alpha = 0.06
    return anderson_ksamp([x, y]).pvalue < alpha # Ваш ответ, True или False
