import requests

api_url = "https://script.google.com/macros/s/AKfycbwwUrkxV1eN8Y0AGckAlXhzSZpF8SPGscpeOy26LOyBLNexw8OfSWmGOhN1aiN1_KKHow/exec"

response = requests.get(url=api_url)
data_from_api = response.json()
persons_data = data_from_api.get('data23')

if persons_data is None or len(persons_data) < 0:
    print('Empty data')
else:
    large_families_under_35_years_monthly_income = 0
    large_families_count = 0
    excessive_debt_family_count = 0
    women_own_housing_count = 0

    for person in persons_data:
        if person['large_family'] is True:
            large_families_count += 1
            if person['age'] > 35:
                large_families_under_35_years_monthly_income += float(person['monthly_income'])

        if float(person['monthly_income']) < float(person['loan_costs']):
            excessive_debt_family_count += 1

        if person['gender'] == 'female':
            women_own_housing_count += 1
