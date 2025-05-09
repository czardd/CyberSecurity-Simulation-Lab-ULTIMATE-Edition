import tkinter as tk
import threading
import time
import random
import pygame

# Initialize sound engine
pygame.mixer.init()

score = 0
level = 1
achievements = []

# Load sounds
def play_sound(event):
    sounds = {
        "attack": "sounds/hack.wav",
        "keylog": "sounds/key.wav",
        "trojan": "sounds/trojan.wav",
        "encrypt": "sounds/encrypt.wav",
        "portscan": "sounds/scan.wav",
        "achievement": "sounds/achievement.wav"
    }
    if event in sounds:
        try:
            pygame.mixer.music.load(sounds[event])
            pygame.mixer.music.play()
        except:
            log(f"[!] Failed to play sound: {event}")

# Update score and handle level-ups and achievements
def update_score(points):
    global score, level
    score += points
    level = (score // 50) + 1
    root.title(f"🕶️ Cyber Simulation Lab - Score: {score} | Level: {level}")
    update_dashboard()

    if score >= 100 and "Hacker Apprentice" not in achievements:
        achievements.append("Hacker Apprentice")
        log("🏆 Achievement Unlocked: Hacker Apprentice")
        play_sound("achievement")
    if score >= 200 and "Cyber Warrior" not in achievements:
        achievements.append("Cyber Warrior")
        log("🏆 Achievement Unlocked: Cyber Warrior")
        play_sound("achievement")

def log(message):
    log_text.config(state='normal')
    log_text.insert(tk.END, message + '\n')
    log_text.yview(tk.END)
    log_text.config(state='disabled')

def update_dashboard():
    dashboard_text.config(state='normal')
    dashboard_text.delete(1.0, tk.END)
    dashboard_text.insert(tk.END, f"Score: {score}\n")
    dashboard_text.insert(tk.END, f"Level: {level}\n")
    dashboard_text.insert(tk.END, "Achievements:\n")
    for ach in achievements:
        dashboard_text.insert(tk.END, f"✔️ {ach}\n")
    dashboard_text.config(state='disabled')

# Simulation functions
def simulate_encrypt_file(file_path):
    log(f"[SIMULATION] Encrypted {file_path}")
    play_sound("encrypt")

def simulated_ransomware():
    log("[SIMULATION] Starting ransomware simulation...")
    play_sound("encrypt")
    for i in range(3):
        simulate_encrypt_file(f"/fake/path/file{i}.txt")
    log("[SIMULATION] Ransomware simulation complete.")
    update_score(20)

def simulate_attack():
    target_ip = ip_entry.get()
    target_port = port_entry.get()
    log(f"[SIMULATION] Simulating DoS on {target_ip}:{target_port}")
    play_sound("attack")
    time.sleep(2)
    update_score(10)

def simulate_keylogger():
    log("[SIMULATION] Keylogger simulation active.")
    play_sound("keylog")
    fake_keys = ['a', 's', 'd', 'f', 'j', 'k', 'l']
    for i in range(10):
        key = random.choice(fake_keys)
        log(f"[SIMULATION] Logged key: {key}")
        time.sleep(0.3)
    update_score(5)

def simulate_trojan():
    log("[SIMULATION] Launching fake trojan...")
    play_sound("trojan")
    time.sleep(1)
    log("[SIMULATION] Trojan payload simulated.")
    update_score(15)

def simulate_port_scan():
    dummy_ports = {22: "open", 80: "closed", 443: "open", 3306: "closed"}
    log("[SIMULATION] Starting fake port scan...")
    play_sound("portscan")
    for port, status in dummy_ports.items():
        log(f"[SIMULATION] Port {port}: {status}")
        time.sleep(0.4)
    update_score(8)

# GUI Setup
root = tk.Tk()
root.title("🕶️ Cyber Simulation Lab")

frame = tk.Frame(root, padx=10, pady=10)
frame.pack()

tk.Label(frame, text="Target IP:").grid(row=0, column=0, sticky='e')
ip_entry = tk.Entry(frame)
ip_entry.grid(row=0, column=1)

tk.Label(frame, text="Port:").grid(row=1, column=0, sticky='e')
port_entry = tk.Entry(frame)
port_entry.grid(row=1, column=1)

tk.Button(frame, text="Simulate Ransomware", command=simulated_ransomware).grid(row=2, column=0, columnspan=2, sticky='ew')
tk.Button(frame, text="Simulate DoS", command=lambda: threading.Thread(target=simulate_attack).start()).grid(row=3, column=0, columnspan=2, sticky='ew')
tk.Button(frame, text="Simulate Keylogger", command=simulate_keylogger).grid(row=4, column=0, columnspan=2, sticky='ew')
tk.Button(frame, text="Simulate Trojan", command=simulate_trojan).grid(row=5, column=0, columnspan=2, sticky='ew')
tk.Button(frame, text="Simulate Port Scan", command=simulate_port_scan).grid(row=6, column=0, columnspan=2, sticky='ew')

log_text = tk.Text(root, height=10, state='disabled', bg='black', fg='lime')
log_text.pack(fill='both', padx=10, pady=5)

tk.Label(root, text="📊 Dashboard").pack()
dashboard_text = tk.Text(root, height=6, state='disabled', bg='navy', fg='white')
dashboard_text.pack(fill='both', padx=10, pady=5)

update_dashboard()
root.mainloop()