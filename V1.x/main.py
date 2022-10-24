import xmlrpc.client as mwb  # metaWebBlog
import sys  # 获取命令行的参数
import json  # 通过json导入配置文件
import os


# 获取配置文件数据
def get_json_data(path):
    with open(path, 'r') as f:
        tmp = f.read()
    return json.loads(tmp)


def start(file_names, config):
    # 获取代理对象
    proxy = mwb.ServerProxy(uri=config['MetaWeblogUrl'])

    # 构造输入参数
    params = {
        'blogid': config['blogid'],  # 暂时没有任何用处，随便写
        'username': config['username'],
        'password': config['password'],
        'file': None
    }

    # 对每一个文件进行处理
    for fn in file_names:
        # 如果文件名不包含扩展名，跳过
        if '.' not in fn:
            continue
        # 如果打开文件抛出异常，跳过
        try:
            with open(fn, 'rb') as f:
                picture_data = f.read()
        except Exception:
            continue

        # 构造参数
        file = {
            'bits': picture_data,
            'name': fn,
            'type': fn.split('.')[1]
        }
        params['file'] = file

        # 上传文件，并返回url地址
        url_data = proxy.metaWeblog.newMediaObject(params['blogid'],
                                                   params['username'],
                                                   params['password'],
                                                   params['file'])
        # 输出url
        print(url_data['url'])


if __name__ == '__main__':
    cmd_params = sys.argv
    if len(cmd_params) > 1:
        # 获取配置文件的绝对路径
        json_path = os.path.abspath(os.path.dirname(cmd_params[0])) + '/config.json'
        _config = get_json_data(json_path)

        _file_names = cmd_params[1:]
        start(file_names=_file_names, config=_config)
