class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        hand.sort()
        
        n=len(hand)
        count=n
        while count:
            prev=-1
            currsize=0
            
            for i in range(n):
                if hand[i]==-1:
                    continue
                #print(prev)
                if prev==-1 and hand:
                    prev=hand[i]
                    currsize+=1
                    hand[i]=-1
                    count-=1
                elif hand[i]==prev+1:
                    prev=hand[i]
                    currsize+=1
                    hand[i]=-1
                    count-=1
                if currsize==groupSize:
                    break
            if currsize!=groupSize:
                return False
        return True

               



        