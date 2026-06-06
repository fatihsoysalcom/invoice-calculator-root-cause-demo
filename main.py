import decimal

def calculate_invoice_total(item_prices: list[str], tax_rate: decimal.Decimal) -> decimal.Decimal:
    """
    Calculates the total invoice amount by summing item prices and applying a tax rate.
    Expects item_prices as strings to simulate raw input that might need parsing.
    """
    total_items_cost = decimal.Decimal('0.00')
    for price_str in item_prices:
        try:
            total_items_cost += decimal.Decimal(price_str)
        except decimal.InvalidOperation:
            print(f"Warning: Invalid price '{price_str}' encountered. Skipping.")
            continue
    
    # ROOT CAUSE ANALOGY: This is where the 'tool' applies its logic.
    # The user might blame the 'software' for a 'wrong' total,
    # but the software is simply following its configuration (the tax_rate).
    final_total = total_items_cost * (decimal.Decimal('1') + tax_rate)
    return final_total.quantize(decimal.Decimal('0.01'))

if __name__ == "__main__":
    print("--- Invoice Calculator Root Cause Demo ---")

    # Scenario 1: User expects a simple sum, but a configured tax is applied.
    # This creates a 'problem' from the user's perspective.
    item_prices_scenario1 = ["10.50", "25.00", "12.75"]
    
    # ROOT CAUSE ANALOGY: This is the 'misconfiguration' or 'misunderstood default'.
    # The user might not be aware of this tax rate or expects it to be 0.
    configured_tax_rate = decimal.Decimal('0.08') # 8% tax

    print(f"\nScenario 1: Items = {item_prices_scenario1}, Configured Tax Rate = {configured_tax_rate * 100}%")
    
    # The 'tool' (our function) calculates correctly based on its configuration.
    calculated_total_s1 = calculate_invoice_total(item_prices_scenario1, configured_tax_rate)
    
    # What the user *might* have expected if they ignored or didn't know about the tax.
    user_expected_sum_s1 = sum(decimal.Decimal(p) for p in item_prices_scenario1)
    
    print(f"  System Calculated Total: ${calculated_total_s1}")
    print(f"  User's Expected Sum (without tax): ${user_expected_sum_s1}")
    
    if calculated_total_s1 != user_expected_sum_s1:
        print(f"  Difference: ${calculated_total_s1 - user_expected_sum_s1}")
        # ROOT CAUSE ANALOGY: The 'software' is not broken; the tax rate was applied as configured.
        print("  --> User might say: 'The software calculated the total incorrectly!'")
        print("  --> Root Cause Analysis: The tax rate was applied as per configuration, which the user might have overlooked or misunderstood.")
    else:
        print("  Totals match (tax rate was likely 0 or items were empty).")

    # Scenario 2: What if the tax rate was *intended* to be 5% but was entered as 0.5 (50%)?
    item_prices_scenario3 = ["100.00"]
    misconfigured_tax_rate = decimal.Decimal('0.50') # User intended 0.05 (5%), but entered 0.5 (50%)

    print(f"\nScenario 2: Items = {item_prices_scenario3}, Misconfigured Tax Rate = {misconfigured_tax_rate * 100}%")
    calculated_total_s3 = calculate_invoice_total(item_prices_scenario3, misconfigured_tax_rate)
    user_expected_sum_s3_intended_tax = decimal.Decimal('100.00') * (decimal.Decimal('1') + decimal.Decimal('0.05')) # User expected 5% tax
    user_expected_sum_s3_no_tax = decimal.Decimal('100.00')

    print(f"  System Calculated Total: ${calculated_total_s3}")
    print(f"  User's Expected Sum (with intended 5% tax): ${user_expected_sum_s3_intended_tax}")
    print(f"  User's Expected Sum (no tax): ${user_expected_sum_s3_no_tax}")

    if calculated_total_s3 != user_expected_sum_s3_intended_tax:
        print(f"  Difference from intended 5% tax: ${calculated_total_s3 - user_expected_sum_s3_intended_tax}")
        # ROOT CAUSE ANALOGY: The 'software' is not broken; the configuration (tax rate) was entered incorrectly.
        print("  --> User might say: 'The software is adding too much tax!'")
        print("  --> Root Cause Analysis: The tax rate was misconfigured (e.g., entered as 0.50 for 50% instead of 0.05 for 5%).")