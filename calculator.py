def calculate_Gain():
    try:
        # Collect revenue and costs
        revenue = float(input("Enter total revenue: $"))
        costs = float(input("Enter total costs: $"))
        
        # Calculate net Gain
        net_Gain = revenue - costs
        
        print(f"\nTotal Revenue: ${revenue:.2f}")
        print(f"Total Costs: ${costs:.2f}")
        print(f"Net Gain: ${net_Gain:.2f}")
        
        if net_Gain > 0:
            print("The organization is in Gain.")
        elif net_Gain < 0:
            print("The organization is at a loss.")
        else:
            print("The organization has broken even.")
        
        # Allocating percentages of net Gain
        print("\nAllocate percentages of the net Gain:")
        admin_percentage = float(input("Percentage for Production costs: %"))
        program_percentage = float(input("Percentage for Non-Profits costs: %"))
        reserves_percentage = float(input("Percentage for Shelter: %"))
        
        # Ensuring total percentage is 100%
        total_percentage = admin_percentage + program_percentage + reserves_percentage
        if total_percentage != 100:
            print("The total allocation percentage must equal 100%. Please try again.")
            return
        
        # Calculating allocations
        admin_allocation = (admin_percentage / 100) * net_Gain
        program_allocation = (program_percentage / 100) * net_Gain
        reserves_allocation = (reserves_percentage / 100) * net_Gain
        
        # Displaying allocations
        print(f"\nAllocations of Net Gain (${net_Gain:.2f}):")
        print(f"Administrative Costs: ${admin_allocation:.2f} ({admin_percentage}%)")
        print(f"Program Costs: ${program_allocation:.2f} ({program_percentage}%)")
        print(f"Reserves: ${reserves_allocation:.2f} ({reserves_percentage}%)")
        
    except ValueError:
        print("Invalid input. Please enter numeric values.")

calculate_Gain()
