import requests

def author_req(ip_str, token):
    url = "http://" + ip_str + ":8080/TestServer"
    #print(url)
    payload = token

    #default setting
    headers = {
        'Content-Type': "text/plain",
        'User-Agent': "PostmanRuntime/7.15.0",
        'Accept': "*/*",
        'Cache-Control': "no-cache",
        'Postman-Token': "d5639969-8fbd-4531-9ad5-9a1bbe99089a,0c1fee63-a3e2-4a81-89ea-8b8861a0aa61",
        'Host': "192.168.1.108:8080",
        'accept-encoding': "gzip, deflate",
        'content-length': "12",
        'Connection': "keep-alive",
        'cache-control': "no-cache"
        }

    # response
    # True ：authorized
    # False: unauthorized
    response = requests.request("POST", url, data=payload, headers=headers)
    print(response.text)

# argv[1]: author_server ip
# argv[2]: token to be tested
if __name__ == "__main__":
    from sys import argv
    if len(argv) == 3:
         author_req(str(argv[1]), argv[2])