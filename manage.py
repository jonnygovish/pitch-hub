from app import create_app,db 
from flask_script import Manager,Server
from app.models import Pitch,Category
from flask_migrate import Migrate,MigrateCommand
#creating app instance
app = create_app('development')
app = create_app('production')

migrate = Migrate(app,db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)
manager.add_command('server',Server)
@manager.shell
def make_shell_context():
    return dict(app = app,db =db,Pitch= Pitch, Category = Category)
if __name__=='__main__':
  manager.run()