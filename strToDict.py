


def strToDict(cookiestr):
    """
        将等号字符串转换成字典格式字符串
    :param cookiestr: "a=b;c=d;e=f"类似这样的字符串
    :return: {'a':'b','c':'d','e':'f'}
    """
    alist = []
    for c in cookiestr.split(';'):
        key = '{1}{0}{1}'.format(c.strip().split('=')[0], "'")
        value = '{1}{0}{1}{2}'.format(''.join(c.strip().split('=')[1:]).strip('"'), "'", ",")
        a = key + ':' + value
        alist.append(a)

    cookiesStr = '{' + ''.join(alist)[:-1] + '}'

    return cookiesStr


if __name__ == '__main__':

    cookies = '_zap=ed24d48d-a68a-4640-9b8a-c221f0d98a3d; _xsrf=QUEa6gFjYIXJb8K4CcnHy4lK607FEHE0; d_c0="AJAReRZKkxGPTpzdG9N8Hr5Ybo7mDPEgnFY=|1594722200"; _ga=GA1.2.1367906968.1594722202; _gid=GA1.2.629490972.1594722202; q_c1=f99f68fc3d92400dab9b7026462bc7c5|1594722244000|1594722244000; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1594722201,1594722371,1594729325; tst=r; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1594804977; _gat_gtag_UA_149949619_1=1; KLBRSID=53650870f91603bc3193342a80cf198c|1594804977|1594804548'


    # {'_zap':'ed24d48d-a68a-4640-9b8a-c221f0d98a3d','_xsrf':'QUEa6gFjYIXJb8K4CcnHy4lK607FEHE0','d_c0':'AJAReRZKkxGPTpzdG9N8Hr5Ybo7mDPEgnFY|1594722200','_ga':'GA1.2.1367906968.1594722202','_gid':'GA1.2.629490972.1594722202','q_c1':'f99f68fc3d92400dab9b7026462bc7c5|1594722244000|1594722244000','Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49':'1594722201,1594722371,1594729325','tst':'r','Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49':'1594804977','_gat_gtag_UA_149949619_1':'1','KLBRSID':'53650870f91603bc3193342a80cf198c|1594804977|1594804548'}
    print(strToDict(cookies))

