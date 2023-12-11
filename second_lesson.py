import decimal

string_divider = "(^_^)" * 8

print(string_divider)

retirement_year = 65
usd_exchange_rate = decimal.Decimal(37.3)
camry_price = 31500

user_name = input("Enter your name >>> ")
user_age = input("Enter your age >>> ")
user_salary = input("Enter your average salary >>> ")

formatted_name = user_name.strip().capitalize()
formatted_salary = decimal.Decimal(user_salary).quantize(decimal.Decimal(".00"))

years_before_retirement = retirement_year - int(user_age)
lifetime_earnings = years_before_retirement * 12 * formatted_salary

lifetime_earnings_in_usd = decimal.Decimal(
    lifetime_earnings / usd_exchange_rate
).quantize(decimal.Decimal(".00"))

purchased_cars = lifetime_earnings_in_usd // camry_price

print(
    f" я, {formatted_name}, зможу заробити лише __{lifetime_earnings_in_usd}__ доларів, що вистачить лише  на __{purchased_cars}__ тойот, мене це не влаштовує, тому я буду змінювати своє життя і буду завзято вивчати програмування!"
)
