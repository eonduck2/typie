import subprocess

def input_data():
    return input("입력: ")

def main():
    data = input_data()
    
    if data == "node" or data =="노드":
        subprocess.run(["node", input("노드 커맨드 입력: ")])  # 예시로 node 버전 출력
        
main() 