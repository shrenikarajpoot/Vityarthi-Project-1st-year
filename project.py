import time
import random
import webbrowser
import sys
import itertools
def title_screen():
    print("\n" + "="*60)
    print("       MOOD-BASED MUSIC PLAYER ")
    print("            by Shrenika")
    print("="*60)
    time.sleep(1)
def loading(msg="Analyzing your mood"):
    for c in itertools.cycle(['|', '/', '-', '\\']):
        sys.stdout.write(f'\r{msg} ' + c)
        sys.stdout.flush()
        time.sleep(0.2)
        if random.random() > 0.93:
            break
    print("\n")
music_library = {
    "happy": [
        "https://youtu.be/OPf0YbXqDm0?si=UwbrKIMUvan2Sz-b",
        "https://youtu.be/QGJuMBdaqIw?si=XVpUbgwKPaV1Iqb3",
        "https://youtu.be/dCmp56tSSmA?si=1MRCzzW4wCfyysTY",
        "https://youtu.be/YR12Z8f1Dh8?si=k09jKnzUPI66__wt",
        "https://youtu.be/9a4izd3Rvdw?si=bXSS_2UE9HZOFQfA",
        "https://youtu.be/wp43OdtAAkM?si=W-_tISS3Z4CuzrF2",
        "https://youtu.be/q_b8tcbRhXE?si=usr-Iv4o2BaX5whM",
        "https://youtu.be/QrOe2h9RtWI?si=AdYonVYJzFFZNgRW",
        "https://youtu.be/ApXoWvfEYVU?si=WyTcze_ehwocFsZm",
        "https://youtu.be/wnJ6LuUFpMo?si=JefLlQAtixLzyi3o",
        "https://youtu.be/tA8h_exda3E?si=Miul929zxYRVF-tS",
        "https://youtu.be/WKbwopSXLWU?si=wpIO5IjMnji_AkDO",
        "https://youtu.be/w5tWYmIOWGk?si=bG8IUsYE0g6X8bcf",
        "https://youtu.be/OBgOwAf-oVI?si=Kixc6E9prwmzh427",
        "https://youtu.be/1nWQs6IxTrY?si=arJ-OLghbiVnzJzj"
    ],
    "sad": [
        "https://youtu.be/pGuc4hPhiKw?si=hPxrURfdNzrV66Hb",
        "https://youtu.be/e5LShHAE03A?si=QsI4WN5bAQiEfLTj",
        "https://youtu.be/9T-Zbxg9X_4?si=koGxjpbfMuFj0Asf",
        "https://youtu.be/LMnJp_dSdnw?si=WvmZ5HXOwEhiqdlB",
        "https://youtu.be/2AO2Utn2eoU?si=ddhNRCtT7Tc1LAVS",
        "https://youtu.be/NRHIBKNNzAk?si=e0o91taXfSYCcLMd",
        "https://youtu.be/YLkdm2pe8hA?si=8UnMb6cBnF_z9yE6",
        "https://youtu.be/__bHEfJ29j0?si=0alUvWghEUnJ3iVI",
        "https://youtu.be/bzSTpdcs-EI?si=ZD1-NfD9Rx5AwhRO",
        "https://youtu.be/6d5SS0gS5bU?si=dzO9hdsrfyREUFSa",
        "https://youtu.be/xdZiUuwZeOI?si=pcVKZ3RnqfmjH_2f"
    ],
    "romantic": [
        "https://youtu.be/1wEtmB3z_yc?si=s6UYFbD9gascdHsk",
        "https://youtu.be/pkzOBl1p7y4?si=CXF9MoiFJAZ8joNM",
        "https://youtu.be/qgDxKAqLVgU?si=QucURNW7yKEjWG1T",
        "https://youtu.be/LSUR0075KLI?si=23OGJwMKiI6-yFIp",
        "https://youtu.be/mZQH8CPQ-wo?si=sSXbR5BSMNLy_agL",
        "https://youtu.be/SxTYjptEzZs?si=gthFv0B9VtD_JCH0",
        "https://youtu.be/0KozfDYK1EU?si=lxAUVa1zl_dlU-kf",
        "https://youtu.be/WnU0lH6C0EA?si=gXWM8TCRo995k_Go",
        "https://youtu.be/CWfCp96-yck?si=l8NrGiWgQBm70LcS",
        "https://youtu.be/vJQCAtzSfuo?si=tKpQCR60gj7jJg9E",
        "https://youtu.be/GxldQ9eX2wo?si=zUwr_mIk8Twsu4k2",
        "https://youtu.be/u7Jl-WDeUo4?si=346fLKMlBOsNk8Dl"
    ],
    "study":[
        "https://youtu.be/lkkGlVWvkLk?si=B-jampLCU_0RgfTM",
        "https://youtu.be/lTRiuFIWV54?si=z3Cnhpx1gmqTUlUr",
        "https://youtu.be/jXZAbnn1kTU?si=X2w39U0Ptvb8J5l1",
        "https://youtu.be/WPni755-Krg?si=WNC5S7VfEGeFJdEF"
        ],

    "motivational":[
        "https://youtu.be/7wtfhZwyrcc?si=eFKGH-sw_3HypEJb",
        "https://youtu.be/Ax0G_P2dSBw?si=3Tm5xcXqepRvhMPF",
        "https://youtu.be/RCgbE6eS-DU?si=6XAuLWhupXxcRbhI",
        "https://youtu.be/T94PHkuydcw?si=0gfnnnczUQK1j0w7",
        "https://youtu.be/mk48xRzuNvA?si=0WSo2ToZllli7EmV",
        "https://youtu.be/CevxZvSJLk8?si=3Utbifvseit7U6dr",
        "https://youtu.be/btPJPFnesV4?si=gINA-VVIL0VEkVvG"
    ],
    "party": [
        "https://youtu.be/sONw3dihCRs?si=8HAGssdE7_5qtugT",
        "https://youtu.be/Iu8210k9WQc?si=ckk8Nvp4d8bFzoZp",
        "https://youtu.be/4dsFQFCvVGU?si=xBqMHS9_xxlC_5dV",
        "https://youtu.be/jXlNjZnnCgc?si=aRgb5wvac7PUacs_",
        "https://youtu.be/T4tedh_11hg?si=UBsouJKWlGvVrajw",
        "https://youtu.be/jCEdTq3j-0U?si=UcteEswx_7NTxztP",
        "https://youtu.be/LEYXdZ_rVbo?si=2EduuqTIFSYg-eII",
        "https://youtu.be/pElk1ShPrcE?si=7OzOGwEwudzP2s33",
        "https://youtu.be/t4H_Zoh7G5A?si=FR4r60kAmY1ffHBe",
        "https://youtu.be/DUT5rEU6pqM?si=ypYwUl9QRaryb7LN",
        "https://youtu.be/-5HZ8mgpsik?si=6vcHRubpSV3XtEaY"
    ]
}
def music_visualizer():
    print("\n Initializing Music Visualizer...")
    bars = ["▂","▃","▄","▅","▆","▇","█"]
    for _ in range(30):
        line = "".join(random.choice(bars) for i in range(random.randint(10,20)))
        print("   " + line)
        time.sleep(0.1)
def play_music_by_mood():
    print("\nYour mood options:")
    print(" → happy\n → sad\n → romantic\n → party\n → study\n → motivational\n")
    mood = input("Tell me your mood: ").lower()
    if mood not in music_library:
        print("\n⚠ Oops! Mood not recognized. Try again.")
        return
    loading("Finding the best song for you")
    selected_song = random.choice(music_library[mood])
    print(f"\n Playing a {mood} vibe song for you… Enjoy!\n")
    music_visualizer()
    webbrowser.open(selected_song)
title_screen()
while True:
    play_music_by_mood()
    again = input("\nWant to play another mood? (yes/no): ").strip().lower()
    if again != "yes":
        print("\n Thanks for using Mood-Based Music Player. Stay Happy! \n")
        break
