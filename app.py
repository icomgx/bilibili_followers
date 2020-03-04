from main import controller
import config

app = controller.app


if __name__ == '__main__':
    app.run(host=config.host, port=config.port)