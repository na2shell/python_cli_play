import pkgutil

def lib():
    print("i am lib")
    ans = pkgutil.get_data('sample_hoge', 'data/hoge.txt').decode()
    print("ans is ",ans)