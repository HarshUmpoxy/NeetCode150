# Beautiful Problem and Implementation
# Put values in a counter(map of number with frequency)
# Sort the array
# And try to make groups of size groupSize popping out the values from the counter
# If at any point, a value is not present in the counter, return False

class Solution:
    def isNStraightHand(self, hand, groupSize):
        if len(hand) % groupSize:
            return False

        count = Counter(hand)
        hand.sort()
        for num in hand:
            if count[num]:
                for i in range(num, num + groupSize):
                    if not count[i]:
                        return False
                    count[i] -= 1
        return True