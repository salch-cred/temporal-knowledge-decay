import numpy as np

def calculate_survival_prob(half_life_days, current_age_days):
    # Exponential decay function for structured facts
    lambda_param = np.log(2) / half_life_days
    return np.exp(-lambda_param * current_age_days)
