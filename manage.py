# encoding: utf-8
from flask_script import Manager

from project.app import create_app

app = create_app()

manager = Manager(app)

if __name__ == '__main__':
    manager.run()
