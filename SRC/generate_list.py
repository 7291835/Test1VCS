import random
a=0
for a++;a<=1000
    def generate_list():
        alist = [x for x in range(random.randint(-10,10))]
        assert len(alist)!=0
        assert sum(alist)<100
        return alist
    
    def printIt():
        print(generate_list())
    
    def main():
        printIt()
    
    if __name__=='__main__':
        print("Test printIt():")
        main()