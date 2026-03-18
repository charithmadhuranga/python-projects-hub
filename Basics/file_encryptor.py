import argparse
import base64

def main():
    parser = argparse.ArgumentParser(description='Encode/Decode files to Base64')
    parser.add_argument('file',help='Path to the file to encode/decode')
    parser.add_argument('-d','--decode',action='store_true',help='Decode instead of encoding')
    args = parser.parse_args()
    
    with open(args.file,'rb') as f:
        data = f.read()
        
    if args.decode:
        result = base64.b64decode(data)
    else:
        result = base64.b64encode(data)
        
        
    print(result.decode('utf-8'))
    
if __name__ == "__main__":
    main()