from maps.GakushokuSample import GakushokuSample
from maps.GakushokuKoyanagi import GakushokuKoyanagi
# ↓のリストには、メンバーの各オススメ学食が格納されます。
data = [GakushokuKoyanagi(),GakushokuSample(), ]

for rank, d in enumerate(data, start=1):
    print(f"{rank}位: {d.get_menu()}")
    print("---------------------------------")
    print(d.get_summary())
    print(d.get_author())
    print()