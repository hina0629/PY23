# 0904_interface
# インタフェース
# 抽象基底クラスにて、
# すべてが抽象メソッドのクラス。
# つまり、口（くち）の定義だけで、
# 実処理が一切ない。
from abc import ABC, abstractmethod

class Player(ABC):
    @abstractmethod
    def play(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Myplayer(Player):
    def play(self):
        print("play")

    def stop(self):
        print("stop")

mp = Myplayer()
mp.play()
mp.stop()