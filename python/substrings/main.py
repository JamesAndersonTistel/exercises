
def run(s):
    for i in range(len(s)):
        for j in range(len(s) - i):
            x = s[j:i+j+1]
            print(f'x: {x} {''.join(sorted(x))}')


if __name__ == '__main__':
    run('zThisa')
