from src.decay_model import calculate_survival_prob

# Fact: [AI Agent] -> works_at -> [Startup] (Half-life estimated at 730 days)
survival = calculate_survival_prob(half_life_days=730, current_age_days=365)
print("Fact validity survival probability after 1 year:", round(survival, 4))
