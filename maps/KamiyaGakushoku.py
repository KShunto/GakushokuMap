from maps.AbstractGakushoku import AbstractGakushoku

class MoritaGakushoku(AbstractGakushoku):
    def get_menu(self):
        return "愛和食堂のカツカレー"

    def get_summary(self):
        return "程良い辛さでカツが美味しい!"

    def get_author(self):
        return "神谷泰地"