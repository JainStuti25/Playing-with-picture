from PIL import Image
try: 
    img  = Image.open(r"bloom.jpg") 
except IOError:
    pass

def main():
    try:
        #Relative Path
        img = Image.open(r"bloom.jpg") 
         
        #Angle given
        img = img.rotate(180) 
    except IOError:
        pass
 
if __name__ == "__main__":
    main()
    img.show()

img.save(r"bloom.jpg")


