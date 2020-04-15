from LRU import *

def main():
    obj = LRU(5)

    assert obj.put(1,"1") == "Success"
    assert obj.put(2,"2") == "Success"
    assert obj.put(3,"3") == "Success"
    assert obj.get(1) == "1"
    assert obj.get(2) == "2"
    assert obj.get(2) == "2"
    assert obj.put(4,"4") == "Success"
    assert obj.put(5,"5") == "Success"
    assert obj.put(6,"6") == "Success"
    assert obj.put(7,"7") == "Success"
    assert obj.get_cache() == {1: '1', 2: '2', 5: '5', 6: '6', 7: '7'}
    print ("All test cases passed")

if __name__ == "__main__":
    main()