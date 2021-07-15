from api.router import APIRouter
import os

"""
全局配置文件
"""

# 绑定的 IP, 服务器端请使用公网 IP
# 如果不确定可以使用 0.0.0.0
host = "0.0.0.0"

# API 服务的端口
port = 6001

# 绑定域名, 含协议字段不含端口号
domain = os.environ.get('DOMAIN', "https://aniapi.2sing.me")

if __name__ == '__main__':
    print('domain:', domain)
    app = APIRouter(host, port)
    app.set_real_domain(domain)
    app.run()
