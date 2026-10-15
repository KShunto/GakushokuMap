from maps.AbstractGakushoku import AbstractGakushoku

class MoritaGakushoku(AbstractGakushoku):
    def get_menu(self):
        return "すき家の期間限定ローストポーク丼"

    def get_summary(self):
        return "脂質少なめタンパク質多めだから"

    def get_author(self):
        return "森田"
