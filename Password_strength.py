strength_levels = {
    1: "🔴 Weak Password",
    2: "🟡 Medium Password",
    3: "🟢 Strong Password"
}

def check_password(password):
    score = 0

    if len(password) >= 8:
        score += 1
    
    has_number = False
    for ch in password:
        if ch.isdigit():
            has_number = True
    if has_number:
        score += 1

    special_chars = "!@#$%^&*()_+-=<>?/{}[]"
    has_special = False
    for ch in password:
        if ch in special_chars:
            has_special = True
    if has_special:
        score += 1
    
    print("\n🔍 Checking Password Strength...")
    print("📊 Strength Level:", strength_levels[score])


def start_checker():
    print("🔐 Welcome to Password Strength Checker 🔐")
    password = input("🔑 Enter your password: ")
    check_password(password)

start_checker()