import tkinter as tk
from tkinter import ttk, messagebox
import pyperclip
import win32com.client



# ====================================================================
# --- BAYRAK RESİMLERİ İÇİN BASE64 KODLARI ---
# ====================================================================

# 1. Amerika (İngilizce) Bayrağı
us_flag_base64 = """
iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAACXBIWXMAAADsAAAA7AF5KHG9AAAAGXRFWHRTb2Z0d2FyZQB3d3cuaW5rc2NhcGUub3Jnm+48GgAABO1JREFUWIXFl2tsFGUUht9vdqZ76Wy3WboFWmiXUisiKPxQsVLlbg0SRCFppAQMf5AIBEmJgiLGgAgGJAG1UQFLsAYVopEIyC3UAoJosZYtFLq0S7fTli4ze+nsZWY+fzRbumXpLUDfP5Occ77zPpk5OfmGoJdav79qyI1GeU2zFJnqbJEzPf6IUWpTGaE4NwJABHADQAUh5EQ4HD5ks9l8velLeipY8+1/k8/Xil+eq/E/4g8qZEHeYOwta+rIi7smxjvWBqCUEPKJxWKp6a4/c6+Ey+Uylv17s/iPK+LxY5ViTlaqnhTNGo4P5tqx4qVhSLfqu+trArCYUloliuJmSqnhXoVsvGD5ZWGM2Wwoddd6xpRflQAAla4AlkxPR4qZA6UUDZ4QAMC3fmd3IByAIknyzXctXjtn+DcbzvcIULTn0mulZY0l15pk04TsJKgaBQBQCtTfCmLutipkpRo76gOflXQHEFWazmY941r58bzh29492DkRMwPv7XVM+vz3uuO3AwqTZGThlRVQ2qmYAF3j1QdW9QYAAKAblKzqZ0+bkLFrw1/RWMcMbNp/3XLgfOMhj19hKAXefzUTevbuEflwnj0Gqi9SW0Vd5M+KU9c3FVuisY5PcFP0/nClUTalW/XYvjAbzz9mwZQxyVjzvROHKzzIzUnCp4XZeDTNiJyhJqzYU4MaQYbhlal95UjkKN0JoLAD4HSl64lpH1VOV7X24fr6ZCPG2XlcrPXjcIUHAHDmqhenLotItXAoLW9CjSADAJL3bOzPy5jtX1Y4hOd5gQGAfWUtX1n5O/Pok1WMLbqA/eeaY06dqLqN0asuwNUa6o9pZ/GKoqwDANLa2po0atVFscUbjhnIJzN5XKrz33Wya/wei6g3CkQikaEsy7IzC3Jt5LRDQmV9AFaexbBBemwsyMLGg3VoksKoEWTYbQakmDlsKRyJlSXXIIhhCGIYkYrq/gIkanLodZZSOmX1rAw4GqqhUQpfUMWCvMHIzUnC5vkjUbjDAQAIRjRsKBiB8XYey/PTsWz3NQBA66SF/QWAPn/icvbXvz15Vp5F+ZX2jReKaPjH6cc+rgkGjkFtc/uwCWIYVa4AHA1tcDYHEQip/TaOSnUJGcS26IgqtamMgSPwyu1NU8wcbvkiHc+o4sX7soi6ikm1aqzUpjBhhSKs3ElEm3c27y7eX2mSnyGiKIYAJNyXjn1XiAHgHSBzAJAYAM4BBKhlAFQMIMAlNrB1tzv4y6kBcTfMfMHNkiTTDvW6a53mC/R4P7yfYngTZRLZLwgA3JjxhiN49MyohwlgmPGcw35012gGAHTPjF+CBO6hmZMEDrrHs98EOl3JGj/fV0pMhoKHAaD55e/S3iqcHwNAKTVIknQSwIQH7H/WYrFMJoSEgE53QkJIkGXZOQBcD8qZEOJWFGVe1DwGAAB4nhc0TXsZwM0H4O9SVTU/JSWlIQYqXqXP57MFfjxyXK1zj70fzow93WGe++IUnueFrrm4f0Zms7lFKDnyrFLt/Fn+6ehURJR4ZT2KsDok5Oed442JM3iej/uz2uPyqV/0zlOa118cOnZ2HPX6e7WsmEQjTZj0dBUzOntpxpbVZd1C9qYhADiXrh/CULyt1bvz1Tr3CCr6jJpH1AEAY01WSbJZ1mWmOdnMtN8iHLc1a/vapp56AsD/o4kZCk0YxLwAAAAASUVORK5CYII=
"""

# 2. Türkiye (Türkçe) Bayrağı
tr_flag_base64 = """
iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAACXBIWXMAAADsAAAA7AF5KHG9AAAAGXRFWHRTb2Z0d2FyZQB3d3cuaW5rc2NhcGUub3Jnm+48GgAABDNJREFUWIW9l1toHFUYx39nLtlrUl3cJjVZklRSTVsvtUm8VmwFEVPBG+iTCqFFKyiphYjUILbQ1odQ9UWtiCBiQfBBrOBLi4E0Sa0mbYi0TUiCm7ZJNuY+e52d48NemqTZS2LS/9PMfN98v/9hznfmHEGe6vN4imwhvV4IdgH3AxXAbcnwFDAEdEvJaYcrfso7Pj6bT12RK2HYdscmqapNwKuAM0+/QeAH4tYxXyTQtyIDfsocwmEekkK+C2h5ghcrhpTHzZCzuZKhcN4G/DZvFaryE7B1heDF6ogTf7EiOH49p4GrTu82C+U3wLtK8KTkMIJ6nzF2MaOB5MjbVh9+w4QpZG2lERhJPVFSF4NU2FGVH9cODiDKdKn84qfMcZMB3RE+TKK91lQStuM0309bgnSr9bLy2b5czZnCqqo0AiMaQLLPc8KFw07Bw3Vo5T6s2Vlif3ZjDv2zEgNuXarNwD7R5/EU2cP6dbIsMsJWQNEHB3C/2YBwuxIPTRNpxom2dzJ14CCxS1eWa8KwO+MbNFtIr0dkgbvdeH8+ScFDNQBEO88zc6SFyNkOpBFELV6P44XdCKeD6F8XlmPAFTLUZ7Xk2p5Rt396NA03vjvJ5L79YFnpeHx0jLkvvkEtuxNUFeJxEAKkzOlACHYpZJn5+tbNOF95CQDzSj+Tb7+3AD5f8eFrCTjg3vN6TnhS92lAZaao4/n6xGiA2c+/TANyqbCpEWsuiHZXBZHf24i0tmVK3agARZmi+qaq9HWspzc7VQgKarax7vCHKB4PnhOfoW++JxscYJ2SLZoaPYCMRLMbWKEUYCZTMHb5Rmvp1XdnryQl0fNdTB88hDUxwcSed4j9fQnbE49le2ta+J3F54DapaL6lmqKO0+DEEQ7/mDsqeeym0jKvfcN5r76Np/UDnW/7q4Fti8VtQLjaJXl6PduQS0rRcZiRM92Ll1KVdOtl+96IOGU2qi5XULwcqak8JlW7I8/guorxf7kDrSN5US7e5DTyS+nadh2PIpQFKzJqbzAKSlSfCLG8LojTmUEcGVKFHYbhU2NuN9qQCksBMDsH8CamcXsH2DmaAvm5axbv6Vk2IJWiQDwO4u/BhpyvSGcDgrqatB8pVjTM0S7LhD3X10uOKUTvuDo3oSBxE6oF9BXWm2ZiloW1eXh0QEFwBcJ9CHl8VsEB0lLeXh0AObtiMyQsxnouAX49nCo8KPUzYJN6aDLW6JJ5RzgWyP4NaRZ5wv9m544C5biSiMwgpC7QQ6vAdyP4Jn58JsMAPiMsYuaojyIkK2rCG83hVXnM0Z7FgeW/BltmBsJhI2ip0F8DBj/AxyVcCQcLNw5/ywwXzkPp4Mub4ku1WaJfI0si9UiGcD3lsWx1GzPpJwGUhrD6w47lHoEOwU8QGIjM/94PigRXYrkTEEo/ut6AnP51P0P+WF54brXR8EAAAAASUVORK5CYII=
"""
# ====================================================================

# Windows SAPI (Speech API) nesnesini başlat
speaker = win32com.client.Dispatch("SAPI.SpVoice")

SVSFlagsAsync = 1
SVSFPurgeBeforeSpeak = 2
ASYNC_PURGE = SVSFlagsAsync | SVSFPurgeBeforeSpeak


# --- SES AYARLARI ---
# Sizin sistem listenize göre spesifik indeksleri sabitledik.
ENGLISH_VOICE_INDEX = 0  # Microsoft David Desktop - English (United States)
TURKISH_VOICE_INDEX = 3  # Microsoft Tolga - Turkish (Turkey)

# Varsayılan durumu Türkçe olarak başlat
current_lang = "TR"
selected_voice_index = TURKISH_VOICE_INDEX

monitor_enabled = True
app_running = True
speaking_after_id = None
clipboard_after_id = None

# Program açılırken panodaki mevcut veriyi "okundu" kabul et
try:
    last_clipboard_text = pyperclip.paste().strip()
except Exception:
    last_clipboard_text = ""

def center_window(window, width, height):
    x = int((window.winfo_screenwidth() - width) / 2)
    y = int((window.winfo_screenheight() - height) / 2)
    window.geometry(f"{width}x{height}+{x}+{y}")

def set_status(text):
    if app_running and status_label.winfo_exists():
        status_label.config(text=text)

def stop_audio():
    speaker.Speak("", ASYNC_PURGE)
    set_status("Durduruldu")
    oku_btn.config(state="normal")

def start_reading(text):
    text = text.strip()
    if not text:
        return

    # Seçilen dili/sesi SAPI'ye tanımla
    try:
        speaker.Voice = speaker.GetVoices().Item(selected_voice_index)
    except Exception as e:
        print(f"Ses seçimi hatası: {e}")
        # Hata durumunda varsayılan sesi kullanmayı dene
        pass

    # Hız değerini -10 ile +10 arasına çevir
    speed_value = speed_var.get()
    rate = int((speed_value - 100) / 10)
    rate = max(-10, min(10, rate))
    speaker.Rate = rate

    set_status(f"Okunuyor... (Hız: %{speed_value})")
    oku_btn.config(state="disabled")

    # Asenkron okumayı başlat
    speaker.Speak(text, ASYNC_PURGE)

def check_speaking_status():
    global speaking_after_id

    if not app_running:
        return

    try:
        # SAPI: 2 = konuşuyor, 1 = tamamlandı / bekliyor
        if speaker.Status.RunningState == 1:
            if status_label.cget("text").startswith("Okunuyor"):
                set_status("Hazır")
                oku_btn.config(state="normal")

        speaking_after_id = root.after(500, check_speaking_status)

    except tk.TclError:
        return

def oku():
    try:
        text = pyperclip.paste().strip()
    except Exception:
        text = ""

    if not text:
        messagebox.showwarning("Uyarı", "Panoda okunacak metin yok.")
        return

    start_reading(text)

def toggle_monitor():
    global monitor_enabled
    monitor_enabled = monitor_var.get()
    set_status("Pano izleme açık" if monitor_enabled else "Pano izleme kapalı")

def monitor_clipboard():
    global last_clipboard_text, clipboard_after_id

    if not app_running:
        return

    try:
        current_text = pyperclip.paste().strip()
    except Exception:
        current_text = ""

    if monitor_enabled and current_text and current_text != last_clipboard_text:
        last_clipboard_text = current_text
        start_reading(current_text)

    try:
        clipboard_after_id = root.after(700, monitor_clipboard)
    except tk.TclError:
        return

def update_speed_label(val):
    speed_display.config(text=f"Okuma Hızı: %{int(float(val))}")

# --- Bayrağa tıklandığında dili değiştiren fonksiyon ---
def toggle_language(event=None):
    global current_lang, selected_voice_index
    
    # Konuşmayı durdur
    speaker.Speak("", ASYNC_PURGE)

    if current_lang == "TR":
        current_lang = "EN"
        selected_voice_index = ENGLISH_VOICE_INDEX # Artık sabit 0'ı kullanır
        if img_us: flag_label.config(image=img_us)
        lang_text_label.config(text="Geçerli Dil: İNGİLİZCE (David)")
        set_status("Dil değiştirildi: İngilizce")
    else:
        current_lang = "TR"
        selected_voice_index = TURKISH_VOICE_INDEX # Artık sabit 3'ü kullanır
        if img_tr: flag_label.config(image=img_tr)
        lang_text_label.config(text="Geçerli Dil: TÜRKÇE (Tolga)")
        set_status("Dil değiştirildi: Türkçe")

def on_close():
    global app_running
    app_running = False

    try:
        speaker.Speak("", ASYNC_PURGE)
    except Exception:
        pass

    for after_id in (speaking_after_id, clipboard_after_id):
        if after_id:
            try:
                root.after_cancel(after_id)
            except tk.TclError:
                pass

    root.destroy()

# --- GUI KURULUMU ---
root = tk.Tk()
root.title("TTS Okuyucu")
root.resizable(False, False)
root.attributes("-topmost", True)
root.configure(bg="#F0F2F5")

center_window(root, 360, 310)
root.protocol("WM_DELETE_WINDOW", on_close)

# Base64 resimleri Tkinter PhotoImage nesnesine dönüştürme
img_us = None
img_tr = None
try:
    if us_flag_base64.strip() and us_flag_base64.strip() != "BURAYA_YAPIŞTIRIN":
        img_us = tk.PhotoImage(data=us_flag_base64)
    if tr_flag_base64.strip() and tr_flag_base64.strip() != "BURAYA_YAPIŞTIRIN":
        img_tr = tk.PhotoImage(data=tr_flag_base64)
except Exception as e:
    print("Resimler yüklenemedi, base64 kodunu veya formatını (PNG olmalı) kontrol edin:", e)

style = ttk.Style()
style.theme_use("clam")
style.configure("TCheckbutton", background="#F0F2F5", font=("Segoe UI", 10))
style.configure("TScale", background="#F0F2F5")

# 1. Dil Seçimi Başlığı
tk.Label(
    root,
    text="Dili değiştirmek için bayrağa tıklayın",
    bg="#F0F2F5",
    fg="#666666",
    font=("Segoe UI", 9)
).pack(pady=(15, 2))

# Tıklanabilir Bayrak Etiketi
# Resim yoksa metin gösterir
flag_kwargs = {"bg": "#F0F2F5", "cursor": "hand2"}
if img_tr:
    flag_kwargs["image"] = img_tr
else:
    flag_kwargs["text"] = "[ BAYRAK RESMİ ]"
    flag_kwargs["font"] = ("Segoe UI", 10, "bold")

flag_label = tk.Label(root, **flag_kwargs)
flag_label.pack(pady=5)
# Tıklama olayını (Sol Tık) bağlama
flag_label.bind("<Button-1>", toggle_language)

# Seçili dili metin olarak gösteren etiket
lang_text_label = tk.Label(
    root,
    text="Geçerli Dil: TÜRKÇE (Tolga)",
    bg="#F0F2F5",
    font=("Segoe UI", 10, "bold")
)
lang_text_label.pack(pady=(0, 10))


# 2. Hız ayarı
speed_display = tk.Label(
    root,
    text="Okuma Hızı: %140",
    bg="#F0F2F5",
    font=("Segoe UI", 10)
)
speed_display.pack(pady=(5, 2))

speed_var = tk.IntVar(value=140)
speed_slider = ttk.Scale(
    root,
    from_=50,
    to=200,
    variable=speed_var,
    orient="horizontal",
    command=update_speed_label,
    length=280
)
speed_slider.pack(pady=5)

# 3. Clipboard izleme
monitor_var = tk.BooleanVar(value=True)
monitor_check = ttk.Checkbutton(
    root,
    text="Panoyu otomatik oku (Clipboard)",
    variable=monitor_var,
    command=toggle_monitor
)
monitor_check.pack(pady=10)

# 4. Butonlar
btn_frame = tk.Frame(root, bg="#F0F2F5")
btn_frame.pack(pady=5)

oku_btn = tk.Button(
    btn_frame,
    text="▶ OKU",
    command=oku,
    font=("Segoe UI", 11, "bold"),
    bg="#4CAF50",
    fg="white",
    activebackground="#45A049",
    activeforeground="white",
    width=14,
    height=2,
    relief="flat",
    cursor="hand2"
)
oku_btn.pack(side="left", padx=10)

stop_btn = tk.Button(
    btn_frame,
    text="■ DURDUR",
    command=stop_audio,
    font=("Segoe UI", 11, "bold"),
    bg="#F44336",
    fg="white",
    activebackground="#E53935",
    activeforeground="white",
    width=14,
    height=2,
    relief="flat",
    cursor="hand2"
)
stop_btn.pack(side="right", padx=10)

# 5. Durum çubuğu
status_label = tk.Label(
    root,
    text="Hazır",
    bg="#F0F2F5",
    fg="#555555",
    font=("Segoe UI", 9, "italic")
)
status_label.pack(side="bottom", pady=5)

check_speaking_status()
monitor_clipboard()

root.mainloop()
