import urllib.request
import json
def subway():
    r = urllib.request.urlopen("http://openapi.seoul.go.kr:8088/sample/json/CardSubwayTime/1/5/202302/")
    t = r.read().decode("utf-8")
    m = json.loads(t)
    for item in m["CardSubwayTime"]["row"]:
        print(item["SUB_STA_NM"])
        print(item["EIGHTEEN_RIDE_NUM"])
    return None
def main():
    subway()
    return None

if __name__ =="__main__":
    main()
