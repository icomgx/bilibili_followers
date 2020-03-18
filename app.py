from main import controller
import config

app = controller.app

# 测试主入口
if __name__ == '__main__':
    app.run(config.host, port=config.port)
