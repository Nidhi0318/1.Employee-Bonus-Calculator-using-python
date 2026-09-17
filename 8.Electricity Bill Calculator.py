units = float(input("Enter units consumed: "))
if units < 0:
    print("Error: Units cannot be negative.")
else:
    if units <= 100:
        bill = units * 2
        print("First 100 units:", units, "x ₹2 =", bill)
    elif units <= 300:
        bill = 100 * 2 + (units - 100) * 3
        print("First 100 units: 100 x ₹2 = ₹200")
        print("Next", units - 100, "units:", units - 100, "x ₹3 =", (units - 100) * 3)
    elif units <= 600:
        bill = 100 * 2 + 200 * 3 + (units - 300) * 5
        print("First 100 units: 100 x ₹2 = ₹200")
        print("Next 200 units: 200 x ₹3 = ₹600")
        print("Next", units - 300, "units:", units - 300, "x ₹5 =", (units - 300) * 5)
    else:
        bill = 100 * 2 + 200 * 3 + 300 * 5 + (units - 600) * 8
        print("First 100 units: 100 x ₹2 = ₹200")
        print("Next 200 units: 200 x ₹3 = ₹600")
        print("Next 300 units: 300 x ₹5 = ₹1500")
        print("Above 600 units:", units - 600, "x ₹8 =", (units - 600) * 8)
    surcharge = 0
    if bill > 5000:
        surcharge = bill * 0.10
    final_bill = bill + surcharge
    print("Base Bill: ₹", bill)
    print("Surcharge: ₹", surcharge)
    print("Final Bill: ₹", final_bill)