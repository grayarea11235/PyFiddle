import sys
import platform
import flask


class AppSystemInfo:
    def __init__(self, app):
        self.properties = dict()
        self.properties['python_executable'] = sys.executable
        self.properties['flask_version'] = flask.__version__
        self.properties['import_name'] = app.import_name
        self.properties['static_url_path'] = app.static_url_path 
        self.properties['static_folder'] = app.static_folder
        self.properties['template_folder'] = app.template_folder
        self.properties['instance_path'] = app.instance_path
        #self.properties['instance_relative_config'] = app.instance_relative_config
        self.properties['root_path'] = app.root_path

        self.properties['Platform Info'] = ''
        self.properties['platform_machine'] = platform.machine()
        self.properties['platform_version'] = platform.version()
        self.properties['platform_node'] = platform.node()
        self.properties['platform_processor'] = platform.processor()
        
        self.properties['platform_release'] = platform.release()
        self.properties['platform_system'] = platform.system()
