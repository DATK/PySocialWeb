from src.config import *
from Server import app



def main():
    app.run(host=HOSTS,port=PORT,debug=DEBUG)
    
    
if __name__=="__main__":
    main()
    
    
