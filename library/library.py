import constants.constants as const


def convert_centimeters_to_inches(cm: float) -> float:
    inches = cm * const.ONE_CM_IN_INCHES_VALUE
    return inches


def get_even_numbers(numbers: [int]) -> [int]:
    even_numbers = []
    for number in numbers:
        if number % 2 == 0:
            even_numbers.append(number)

    return even_numbers


def can_get_loan(total_loan_amount: float, loan_term_years: int, monthly_income: float, interest_rate: float) -> bool:
    total_months = loan_term_years * 12
    max_monthly_payment = interest_rate / 100 * monthly_income
    monthly_payment = total_loan_amount / total_months
    is_loan_affordable = monthly_payment <= max_monthly_payment
    return is_loan_affordable
