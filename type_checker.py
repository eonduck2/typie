def type_checker():
    print("tc")

def input_data():
    return input("입력: ")

def main():
    print("안녕")
    data = input_data()
    
    if type(data) == str:
        print("문자열")
    elif type(data) == int:
        print("숫자")
        
        
        
main()
