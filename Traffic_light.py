traffic_light = {
    "RED": 5,
    "YELLOW": 2,
    "GREEN": 4
}

def start_traffic_light():
    while True:
        print("\n🚦 Traffic Light Simulation Started 🚦")
        
        print("\n🔴 RED Light ON")
        print("⛔ Stop!")
        countdown(traffic_light["RED"])

        print("\n🟢 GREEN Light ON")
        print("✅ Go!")
        countdown(traffic_light["GREEN"])

        print("\n🟡 YELLOW Light ON")
        print("⚠️ Ready to Stop!")
        countdown(traffic_light["YELLOW"])


def countdown(time):
    while time > 0:
        print("⏳ Time Remaining:", time, "seconds")
        time -= 1

start_traffic_light()