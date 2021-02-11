import socket
import time
def isPalindrome(s):
    return s == s[::-1]

def netcat(hostname, port, content):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((hostname, port))
    response = ""
    response_array = []
    while 1:
        data = s.recv(1024)
        if "!!!" in data.decode():
            print(data)
            break
        string = data.decode()
        res = string.split()  
        for i in res: 
            print(i) 
            ans = isPalindrome(i)
            if ans:
                response_array.append(i) 
                print(response_array)
            else:
                print("No")
        print("Received:", string)
        response = ' '.join([str(elem) for elem in response_array])
        response += "\n"
        print(response)
        print(response.encode())
        time.sleep(0.5)
        s.sendall(response.encode())
        response_array = []
        response = ""
    print("Connection closed.")
    s.close()

netcat("palindromer-bd7e0fc867d57915.elb.us-east-1.amazonaws.com",7777,"3")
