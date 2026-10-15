from maps.GakushokuSample import GakushokuSample
from maps.GakushokuKoyanagi import GakushokuKoyanagi
from maps.KamiyaGakushoku import KamiyaGakushoku
from maps.MoritaGakushoku import MoritaGakushoku
# ↓のリストには、メンバーの各オススメ学食が格納されます。
data = [GakushokuSample(),
        MoritaGakushoku(),
        KamiyaGakushoku(),
        GakushokuKoyanagi(), ]

for rank, d in enumerate(data, start=1):
    print(f"{rank}位: {d.get_menu()}")
    print("---------------------------------")
    print(d.get_summary())
    print(d.get_author())
    print()