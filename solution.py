import pandas as pd
import numpy as np
from scipy.stats import ks_2samp


chat_id = 1188007817 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    statistic, pvalue = ks_2samp(x, y, alternative='greater')
    if pvalue < 0.08:
        return True
    else:
        return False
