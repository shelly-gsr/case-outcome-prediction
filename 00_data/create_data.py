import pandas as pd
import numpy as np

np.random.seed(42)  # for reproducibility

n_samples = 500

case_types = ['civil', 'criminal', 'family', 'contract']
court_levels = ['trial', 'appeal']
outcomes = ['plaintiff_win', 'defendant_win', 'settled']

data = pd.DataFrame({
    'case_id': range(1001, 1001 + n_samples),
    'case_type': np.random.choice(case_types, n_samples),
    'court_level': np.random.choice(court_levels, n_samples),
    'filing_year': np.random.randint(2015, 2023, n_samples),
    'num_parties': np.random.randint(2, 6, n_samples),
    'has_jury': np.random.choice([True, False], n_samples, p=[0.3, 0.7]),
    'num_legal_reps': np.random.randint(1, 4, n_samples),
    'duration_days': np.random.randint(30, 366, n_samples),
    'settled_pre_trial': np.random.choice([True, False], n_samples, p=[0.4, 0.6]),
    'prior_cases_same_party': np.random.randint(0, 11, n_samples),
})

# Synthetic target outcome
def assign_outcome(row):
    if row['settled_pre_trial']:
        return 'settled'
    elif row['case_type'] in ['civil', 'contract'] and row['num_legal_reps'] > 1:
        return np.random.choice(['plaintiff_win', 'defendant_win'], p=[0.6, 0.4])
    elif row['case_type'] == 'criminal':
        return np.random.choice(['plaintiff_win', 'defendant_win'], p=[0.3, 0.7])
    else:
        return np.random.choice(outcomes)

data['outcome'] = data.apply(assign_outcome, axis=1)

# Save to CSV
data.to_csv('synthetic_case_outcomes.csv', index=False)
print(data.head())