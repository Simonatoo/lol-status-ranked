from controls.statusRanked import PontosRanked

ranked = PontosRanked()

class Default:
    def status(self,nickname):
        return ranked.connect(nickname)