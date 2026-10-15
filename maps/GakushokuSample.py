from maps.AbstractGakushoku import AbstractGakushoku
class GakushokuSample(AbstractGakushoku):
    def get_menu(self):
        return "オススメの学食メニューをここに書きます"
    def get_summary(self):
        return "オススメのポイントやなぜオススメできるかなど、簡単に書きます"
    def get_author(self):
        return "書いた人の名前を書きます"
    
class GakushokuKoyanagi(AbstractGakushoku):
    def get_menu(self):
        return "五八"



    def get_summary(self):
        return "担々麺の肉がうまい"
    def get_author(self):
        return "小柳冬藍"