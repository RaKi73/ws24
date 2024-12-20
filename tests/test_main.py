from hello import greet

def test_print1():
    assert greet.huhu("dear user") == "Hello dear user, I wish you a wonderful day!"
    
# add more tests here 
if __name__ == "__main__":
    test_print1()
    print("All tests passed!")