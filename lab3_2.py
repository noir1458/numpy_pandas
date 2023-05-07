# regular expression test
import re # regular standard lib

def testRegexp():
    pattern = "c[a-d]v?x*" # = {ca,cb,cc,cd,cax,caxx}
    regex = re.compile(pattern)

    pattern2 = "c[a-d]v?x*cxcx*"
    regex2 = re.compile(pattern2)

    # search
    res = regex.search("cbvxxxxxxxxxxxxcxcxx")
    print(res)
    res2 = regex2.search("cbvxxxxxxxxxxxxcxcxx")
    print(res2)
    return None

def testSSID():
    pattern = "[0-9]{6}-[0-9]{7}"

    regex = re.compile(pattern)
    res = regex.search("999999-8888808")
    print(res)

    return None

def main():
    testRegexp()
    testSSID()
    return None

if __name__ == '__main__':
    main()