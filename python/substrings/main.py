
def run(s):
    for i in range(len(s)):
        for j in range(len(s) - i):
            x = s[j:i+j+1]
            print(f'x: {x}')
    

if __name__ == '__main__':
    run('This is a test')
