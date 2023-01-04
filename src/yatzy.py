class Yatzy:

    # Usamos el *args para poder para el número que queramos de parámetros.
    @staticmethod
    def chance(*args):
        total = 0
        for i in args:
            total += i
        return total

    @staticmethod
    def yatzy(*args):
        if len(set(args)) == 1:
            return 50
        else:
            return 0

    @staticmethod
    def ones(*args):
        total = 0
        for i in args:
            if i == 1:
                total += i
        return total

    @staticmethod
    def twos(*args):
        total = 0
        for i in args:
            if i == 2:
                total += i
        return total

    @staticmethod
    def threes(*args):
        total = 0
        for i in args:
            if i == 3:
                total += i
        return total

    @staticmethod
    def fours(*args):
        total = 0
        for i in args:
            if i == 4:
                total += i
        return total
    
    @staticmethod
    def fives(*args):
        total = 0
        for i in args:
            if i == 5:
                total += i
        return total
    
    @staticmethod
    def sixes(*args):
        total = 0
        for i in args:
            if i == 6:
                total += i
        return total
    
    @staticmethod
    def score_pair(*args):
        for i in range(6, 0, -1):
            if args.count(i) == 2:
                return i * 2
        return 0
    
    @staticmethod
    def two_pair(*args):
        counts = []
        score = 0
        for i in args:
            if args.count(i) > 1:
                if i not in counts:
                    counts.append(i)
                    i = i * args.count(i)
                    score += i
                    if len(counts) == 2:
                        return score
                    else:   
                        pass
        return 0

    @staticmethod
    def three_of_a_kind(*args):
        for i in args:
            if args.count(i) == 3:
                return i * 3
            else:
                return 0
    
    @staticmethod
    def four_of_a_kind(*args):
        for i in args:
            if args.count(i) == 4:
                return i * 4
            else:
                return 0
     

    @staticmethod
    def smallStraight( d1,  d2,  d3,  d4,  d5):
        tallies = [0]*6
        tallies[d1-1] += 1
        tallies[d2-1] += 1
        tallies[d3-1] += 1
        tallies[d4-1] += 1
        tallies[d5-1] += 1
        if (tallies[0] == 1 and
            tallies[1] == 1 and
            tallies[2] == 1 and
            tallies[3] == 1 and
            tallies[4] == 1):
            return 15
        return 0
    

    @staticmethod
    def largeStraight( d1,  d2,  d3,  d4,  d5):
        tallies = [0]*6
        tallies[d1-1] += 1
        tallies[d2-1] += 1
        tallies[d3-1] += 1
        tallies[d4-1] += 1
        tallies[d5-1] += 1
        if (tallies[1] == 1 and
            tallies[2] == 1 and
            tallies[3] == 1 and
            tallies[4] == 1
            and tallies[5] == 1):
            return 20
        return 0
    

    @staticmethod
    def fullHouse( d1,  d2,  d3,  d4,  d5):
        tallies = []
        _2 = False
        i = 0
        _2_at = 0
        _3 = False
        _3_at = 0

        tallies = [0]*6
        tallies[d1-1] += 1
        tallies[d2-1] += 1
        tallies[d3-1] += 1
        tallies[d4-1] += 1
        tallies[d5-1] += 1

        for i in range(6):
            if (tallies[i] == 2): 
                _2 = True
                _2_at = i+1
            

        for i in range(6):
            if (tallies[i] == 3): 
                _3 = True
                _3_at = i+1
            

        if (_2 and _3):
            return _2_at * 2 + _3_at * 3
        else:
            return 0
