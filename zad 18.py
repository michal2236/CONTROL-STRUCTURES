amount = int(input('Enter the amount in PLN: '))
m_amount = amount

fives = m_amount // 5
m_amount //= 5

twoes = m_amount // 2
m_amount //= 2

ones = m_amount

print(
    f"The amount of PLN {amount} in coins: \n 5 zł - {fives} \n 2 zł - {twoes} \n 1 zł - {ones}")