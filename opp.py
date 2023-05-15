class Property:
    def __init__(self, purchase_price, rehab_costs, rental_income, expenses, down_payment, interest_rate, mortgage, closing_costs, property_taxes, insurance, monthly_rent_increase, HOA, selling_costs):
        self.purchase_price = purchase_price
        self.rehab_costs = rehab_costs
        self.rental_income = rental_income
        self.expenses = expenses
        self.down_payment = down_payment
        self.interest_rate = interest_rate
        self.mortgage = mortgage
        self.closing_costs = closing_costs
        self.property_taxes = property_taxes
        self.insurance = insurance
        self.monthly_rent_increase = monthly_rent_increase
        self.HOA = HOA
        self.selling_costs = selling_costs

    def calc_rate(self):
        monthly_cash_flow = self.rental_income - self.expenses
        annual_cash_flow = monthly_cash_flow * 12
        annual_mortgage_interest = (self.purchase_price + self.rehab_costs - self.down_payment) * self.interest_rate
        annual_net_operating_income = annual_cash_flow - annual_mortgage_interest - property_taxes - self.insurance 
        cap_rate = annual_net_operating_income / (self.purchase_price + self.rehab_costs)
        return cap_rate

    def calc_roi(self):
        expected_annual_appreciation = (self.monthly_rent_increase + self.HOA) * (self.purchase_price + self.rehab_costs) * 12 - self.selling_costs
        total_invested = self.purchase_price + self.rehab_costs + self.closing_costs - self.down_payment
        total_return = expected_annual_appreciation + (self.calc_rate() * total_invested)
        roi = (total_return / total_invested) * 100
        return roi


purchase_price = float(input("Enter the purchase price of the property: "))
rehab_costs = float(input("Enter the estimated renovation costs: "))

