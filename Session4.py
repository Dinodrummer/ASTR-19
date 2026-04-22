class Animal:
    def __init__(self, armLength, legLength, eyesCount, tail, furry):
        self.armLength = armLength
        self.legLength = legLength
        self.eyesCount = eyesCount
        self.tail = tail
        self.furry = furry
    def print(self):
        print(f"armLength: {self.armLength} - Length of arms (FLOAT)")
        print(f"legLength: {self.legLength} - Length of legs (FLOAT)")
        print(f"eyesCount: {self.eyesCount} - Number of eyes (INT)")
        print(f"tail: {self.tail} - Has a tail (BOOL)")
        print(f"furry: {self.furry} - Is furry (BOOL)")


    


def main():
    animal = Animal(1.1,2.3,1,True,False)
    animal.print()


if __name__ == '__main__':
    main()