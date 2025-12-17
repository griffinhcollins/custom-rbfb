import os
basedir = os.path.abspath(os.path.dirname(__file__))



class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY") or "when the rbfb has real and fake birds"
    
    