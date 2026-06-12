
# DATA

USERS = [
    {"username": "admin",    "password": "admin@afrah",    "role": "Admin"},
    {"username": "cashier",  "password": "cashier@afrah",  "role": "Cashier"},
    {"username": "customer", "password": "customer@afrah", "role": "Customer"},
]

# Shared product catalogue (Admin adds, Cashier & Customer can view/buy)
products = []

VALID_COUPONS = {
    "SAVE10":  10,   # 10% extra discount
    "SAVE20":  20,
    "HALF50":  50,
    "AFRAH5":   5,
}

TAX_RATES = {
    "makerere": 0.18,
    "entebbe":  0.15,
    "jinja":    0.12,
    "mbale":    0.10,
    "gulu":     0.08,
}

MAX_ATTEMPTS = 3


# HELPERS

def get_tax_rate(location: str) -> float:
    """Return tax rate for a location (case-insensitive). Defaults to 0 if unknown."""
    return TAX_RATES.get(location.strip().lower(), 0.0)


def get_discount_level(subtotal: float) -> float:
    """Return automatic discount % based on subtotal amount."""
    if subtotal >= 500_000:
        return 20.0
    elif subtotal >= 200_000:
        return 15.0
    elif subtotal >= 100_000:
        return 10.0
    elif subtotal >= 50_000:
        return 5.0
    else:
        return 0.0


def apply_coupon(coupon_code: str) -> float:
    """Validate coupon and return its discount %. Returns 0 for invalid codes."""
    code = coupon_code.strip().upper()
    if code in VALID_COUPONS:
        discount = VALID_COUPONS[code]
        print(f"  ✔ Coupon '{code}' applied — extra {discount}% off!")
        return discount
    else:
        print(f"  ✘ Coupon '{coupon_code}' is invalid or expired.")
        return 0.0


def calculate_final_price(original_price: float,
                           manual_discount_pct: float,
                           coupon_discount_pct: float,
                           subtotal_discount_pct: float,
                           tax_rate: float) -> dict:
    """Calculate full price breakdown and return as a dict."""
    total_discount_pct = manual_discount_pct + coupon_discount_pct + subtotal_discount_pct
    total_discount_pct = min(total_discount_pct, 100.0)          # cap at 100 %

    discount_amount = (total_discount_pct / 100) * original_price
    after_discount  = original_price - discount_amount
    tax_amount      = tax_rate * after_discount
    final_price     = after_discount + tax_amount

    return {
        "original_price":       original_price,
        "manual_discount_pct":  manual_discount_pct,
        "coupon_discount_pct":  coupon_discount_pct,
        "subtotal_discount_pct":subtotal_discount_pct,
        "total_discount_pct":   total_discount_pct,
        "discount_amount":      discount_amount,
        "after_discount":       after_discount,
        "tax_rate_pct":         tax_rate * 100,
        "tax_amount":           tax_amount,
        "final_price":          final_price,
    }


def print_receipt(product_name: str, coupon: str, breakdown: dict):
    print("         AFRAH E-COMMERCE — RECEIPT")
    print(f"  Product       : {product_name}")
    print(f"  Coupon used   : {coupon if coupon else 'None'}")
    print(f"  Original Price: UGX {breakdown['original_price']:>12,.2f}")
    print(f"  Manual Disc.  : {breakdown['manual_discount_pct']:.1f}%")
    print(f"  Coupon Disc.  : {breakdown['coupon_discount_pct']:.1f}%")
    print(f"  Subtotal Disc.: {breakdown['subtotal_discount_pct']:.1f}%")
    print(f"  Total Discount: {breakdown['total_discount_pct']:.1f}%  "
          f"(-UGX {breakdown['discount_amount']:,.2f})")
    print(f"  After Discount: UGX {breakdown['after_discount']:>12,.2f}")
    print(f"  Tax ({breakdown['tax_rate_pct']:.0f}%)     : UGX {breakdown['tax_amount']:>12,.2f}")
    print(f"  {'FINAL PRICE':<14}: UGX {breakdown['final_price']:>12,.2f}")
    print("=" * 45 + "\n")


def show_products():
    if not products:
        print("  No products available yet.")
        return
    print("\n  {'─' * 60}")
    print(f"  {'#':<4} {'Name':<20} {'Coupon':<10} {'Price (UGX)':>14}")
    print(f"  {'─' * 50}")
    for i, p in enumerate(products, 1):
        print(f"  {i:<4} {p['name']:<20} {p['coupon']:<10} {p['price']:>14,.2f}")
    print()


# ROLE MENUS

def admin_menu():
    print("\n╔══════════════════════════╗")
    print("║     ADMIN DASHBOARD      ║")
    print("╚══════════════════════════╝")
    while True:
        print("\n  [1] Add product")
        print("  [2] View all products")
        print("  [3] Calculate price for a product")
        print("  [4] Logout")
        print("  [5] Exit programme")
        choice = input("\n  Select option: ").strip()

        if choice == "1":
            # ── Add product ──────────────────────────
            name     = input("  Product name   : ").strip()
            coupon   = input("  Coupon code    : ").strip()
            price    = float(input("  Base price (UGX): "))
            products.append({"name": name, "coupon": coupon, "price": price})
            print(f"  ✔ '{name}' added to catalogue.")

        elif choice == "2":
            show_products()

        elif choice == "3":
            # ── Full price calculation ────────────────
            show_products()
            if not products:
                continue
            idx = int(input("  Select product # : ")) - 1
            if not (0 <= idx < len(products)):
                print("  Invalid selection.")
                continue

            p = products[idx]
            location         = input("  Customer location: ")
            tax_rate         = get_tax_rate(location)
            coupon_code      = input("  Enter coupon code (or press Enter to skip): ").strip()
            coupon_disc      = apply_coupon(coupon_code) if coupon_code else 0.0
            manual_disc      = float(input("  Manual discount % (0 if none): ") or 0)
            subtotal_disc    = get_discount_level(p["price"])

            breakdown = calculate_final_price(
                p["price"], manual_disc, coupon_disc, subtotal_disc, tax_rate
            )
            print_receipt(p["name"], coupon_code, breakdown)

        elif choice == "4":
            print("  Logged out. Returning to login screen…")
            return "logout"

        elif choice == "5":
            print("\n  Goodbye! Exiting Afrah E-Commerce…")
            exit()

        else:
            print("  Invalid option. Try again.")


def cashier_menu():
    print("\n╔══════════════════════════╗")
    print("║    CASHIER DASHBOARD     ║")
    print("╚══════════════════════════╝")
    while True:
        print("\n  [1] View products")
        print("  [2] Process a sale")
        print("  [3] Logout")
        print("  [4] Exit programme")
        choice = input("\n  Select option: ").strip()

        if choice == "1":
            show_products()

        elif choice == "2":
            # ── Process sale ──────────────────────────
            show_products()
            if not products:
                continue
            idx = int(input("  Select product # : ")) - 1
            if not (0 <= idx < len(products)):
                print("  Invalid selection.")
                continue

            p = products[idx]
            location      = input("  Customer location: ")
            tax_rate      = get_tax_rate(location)
            coupon_code   = input("  Enter coupon code (or press Enter to skip): ").strip()
            coupon_disc   = apply_coupon(coupon_code) if coupon_code else 0.0
            subtotal_disc = get_discount_level(p["price"])

            # Cashiers cannot manually set discounts — only coupons + auto levels
            breakdown = calculate_final_price(
                p["price"], 0.0, coupon_disc, subtotal_disc, tax_rate
            )
            print_receipt(p["name"], coupon_code, breakdown)

        elif choice == "3":
            print("  Logged out. Returning to login screen…")
            return "logout"

        elif choice == "4":
            print("\n  Goodbye! Exiting Afrah E-Commerce…")
            exit()

        else:
            print("  Invalid option. Try again.")


def customer_menu():
    print("\n╔══════════════════════════╗")
    print("║   CUSTOMER DASHBOARD     ║")
    print("╚══════════════════════════╝")

    location  = input("\n  Enter your location: ")
    tax_rate  = get_tax_rate(location)
    print(f"  Tax rate for {location.capitalize()}: {tax_rate * 100:.0f}%")

    while True:
        print("\n  [1] Browse products")
        print("  [2] Buy a product")
        print("  [3] Logout")
        print("  [4] Exit programme")
        choice = input("\n  Select option: ").strip()

        if choice == "1":
            show_products()

        elif choice == "2":
            show_products()
            if not products:
                continue
            idx = int(input("  Select product # : ")) - 1
            if not (0 <= idx < len(products)):
                print("  Invalid selection.")
                continue

            p = products[idx]
            coupon_code   = input("  Enter coupon code (or press Enter to skip): ").strip()
            coupon_disc   = apply_coupon(coupon_code) if coupon_code else 0.0
            subtotal_disc = get_discount_level(p["price"])

            breakdown = calculate_final_price(
                p["price"], 0.0, coupon_disc, subtotal_disc, tax_rate
            )
            print_receipt(p["name"], coupon_code, breakdown)

        elif choice == "3":
            print("  Logged out. Returning to login screen…")
            return "logout"

        elif choice == "4":
            print("\n  Goodbye! Exiting Afrah E-Commerce…")
            exit()

        else:
            print("  Invalid option. Try again.")


# REGISTER FOR CUSTOMER ACCOUNT
def register_customer():
    print("\n╔══════════════════════════════════╗")
    print("║   AFRAH E-COMMERCE — REGISTER     ║")
    print("╚══════════════════════════════════╝")

    while True:
        username = input("\n  Choose a username: ").strip()
        if any(u["username"] == username for u in USERS):
            print("  ✘ Username already taken. Try another.")
            continue

        password = input("  Choose a password: ").strip()
        USERS.append({"username": username, "password": password, "role": "Customer"})
        print(f"  ✔ Account created for '{username}'. You can now log in.")
        break



# ──────────────────────────────────────────────
# LOGIN
# ──────────────────────────────────────────────

def login():
    print("\n╔══════════════════════════════════╗")
    print("║   AFRAH E-COMMERCE — LOGIN       ║")
    print("╚══════════════════════════════════╝")

    attempts = 0
    while attempts < MAX_ATTEMPTS:
        username = input("\n  Username: ").strip()
        password = input("  Password: ").strip()

        user = next(
            (u for u in USERS if u["username"] == username and u["password"] == password),
            None
        )

        if user:
            role = user["role"]
            print(f"\n  ✔ Welcome, {role} '{username}'!")

            if role == "Admin":
                admin_menu()
            elif role == "Cashier":
                cashier_menu()
            elif role == "Customer":
                customer_menu()
            return   # exit after successful session

        else:
            attempts += 1
            remaining = MAX_ATTEMPTS - attempts
            if remaining > 0:
                print(f"  ✘ Invalid credentials. {remaining} attempt(s) remaining.")
            else:
                print("  ✘ Too many failed attempts. Access denied.")


# ──────────────────────────────────────────────
# ENTRY POINT
# ──────────────────────────────────────────────

if __name__ == "__main__":
    while True:
        print("Welcome! Choose an option:")
        print("  [1] Login")
        print("  [2] Register")
        print("  [3] Exit")
        choice = input("  Select option: ").strip()

        if choice == "1":
            login()
        elif choice == "2":
            register_customer()
        elif choice == "3":
            print("  Goodbye!")
            exit()
        else:
            print("  Invalid option. Try again.")