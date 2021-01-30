#Search and Replace words in Files
def replace_keys(text, diction):
    for k, v in diction.items():
        text = text.replace(k,v)
    return text

if __name__=='__main__':
    n=int(input('How many keys to replace?\n'))
    print('Enter your keys')
    user_keys = [input() for i in range(0, n)]
    print('Enter your values')
    user_values = [input() for i in range(0,n)]
    zips=zip(user_keys,user_values)
    diction = dict(zips)
    filename=input('Enter File Path which needs search and replace \n')
    with open(filename ,'r')as f:
        text = (f.read()).replace('context.','')#the context replace is optional
        replaced=replace_keys(text, diction)
    savefilename=input('Enter File Path for new file \n')
    with open(savefilename ,'x')as f:
        f.write(replaced)
        print('Please check the new file given at your location')
