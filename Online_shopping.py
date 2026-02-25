products = {
    "1": {"name": "📱 Mobile", "price": 15000},
    "2": {"name": "💻 Laptop", "price": 55000},
    "3": {"name": "🎧 Headphones", "price": 2000},
    "4": {"name": "⌚ Smart Watch", "price": 5000}
}

cart = {}
def show_products():
    print("\n🛍 Available Products:")
    for key in products:
        print(key, "->", products[key]["name"], "- ₹", products[key]["price"])

def add_to_cart():
    product_id = input("\n🛒 Enter Product ID to Add: ")
    
    if product_id in products:
        quantity = int(input("📦 Enter Quantity: "))
        
        if product_id in cart:
            cart[product_id]["quantity"] += quantity
        else:
            cart[product_id] = {
                "name": products[product_id]["name"],
                "price": products[product_id]["price"],
                "quantity": quantity
            }
        
        print("✅ Item Added to Cart!")
    else:
        print("❌ Invalid Product ID!")

def view_cart():
    print("\n🛒 Your Shopping Cart:")
    total = 0
    
    if len(cart) == 0:
        print("🛍 Cart is Empty!")
        return
    
    for item in cart:
        name = cart[item]["name"]
        price = cart[item]["price"]
        quantity = cart[item]["quantity"]
        subtotal = price * quantity
        total += subtotal
        
        print(name, "| ₹", price, "x", quantity, "= ₹", subtotal)
    
    print("💰 Total Amount: ₹", total)

def remove_item():
    product_id = input("\n❌ Enter Product ID to Remove: ")
    
    if product_id in cart:
        del cart[product_id]
        print("🗑 Item Removed Successfully!")
    else:
        print("⚠ Item Not Found in Cart!")

def start_shopping():
    while True:
        print("\n🛒 Online Shopping Cart Menu")
        print("1️⃣ View Products")
        print("2️⃣ Add to Cart")
        print("3️⃣ View Cart")
        print("4️⃣ Remove Item")
        print("5️⃣ Exit")
        
        choice = input("👉 Enter Your Choice: ")
        
        if choice == "1":
            show_products()
        elif choice == "2":
            show_products()
            add_to_cart()
        elif choice == "3":
            view_cart()
        elif choice == "4":
            view_cart()
            remove_item()
        elif choice == "5":
            print("🙏 Thank You for Shopping!")
            break
        else:
            print("❌ Invalid Choice!")

start_shopping()