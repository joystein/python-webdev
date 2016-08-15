"""
 
 Invokde file for pythen web development
 
"""

from invoke import run, task


###
# API
###

@task
def setup(ctxt):
    """
    Setup the reporting service
    """
    ctxt.run("mkdir logs")

@task
def start_dev(ctxt):
    """
    Start the uwsgi server for development
    """
    ctxt.run("uwsgi --ini-paste-logged development.ini")

@task
def start_prod(ctxt):
    """
    Start the uwsgi server
    """
    ctxt.run("uwsgi --ini production.ini")

@task
def stop(ctxt):
    """
    Stop the uwsgi server
    """
    ctxt.run("uwsgi --stop uwsgi.pid")

@task
def reload(ctxt):
    """
    Reload the uwsgi server
    """
    ctxt.run("uwsgi --reload uwsgi.pid")


###
# JS APP
###

@task
def prepare_dev_env(ctxt):
    """
    Prepare development environment
    """
    
    #run("mkdir build log")
    
    # Setup nodejs
    # We want a completely isolated environment for nodejs, including for global
    # installs
    ctxt.run("pip install nodeenv")
    ctxt.run("nodeenv -p")
    
    # To have them available on the command line. Might not be needed if only
    # used in node scripts.
    global_packages = [
        "browserify",
        "watchify",
    ]
    
    for package in global_packages:
        ctxt.run("npm -g install %s --save-dev"  % package)
    
    # Install npm packages
    ctxt.run("npm install")


js_build_args = "apps/%s/*.js --transform [ babelify --presets [ es2015 react ] ] --debug --verbose -o build/%s/main.js"

@task
def clean(ctxt, name=False):
    if not name:
        ctxt.run("rm -fr build/*")
    else:
        ctxt.run("rm build/%s/*" % name)

def build_static(ctxt, name):
    print("Building static files")
    ctxt.run("cp apps/%s/*.html apps/%s/*.png apps/*.css build/%s" % ((name,) * 3))

def build_js(ctxt, name):
    print("Building js files")
    ctxt.run("browserify %s" % js_build_args % ((name,) * 2))

def watch_js(ctxt, name):
    print("Starting watchify for %s" % name)
    ctxt.run("watchify %s" % js_build_args % ((name,) * 2))

@task
def build(ctxt, name):
    clean(ctxt, name)
    ctxt.run("mkdir -p build/%s" % name)
    build_static(ctxt, name)
    build_js(ctxt, name)

@task
def watch(ctxt, name):
    clean(ctxt, name)
    ctxt.run("mkdir -p build/%s" % name)
    build_static(ctxt, name)
    watch_js(ctxt, name)
