import secrets;
import string;
import os;
import sys;

def copy(m):
    command = 'echo | set /p nul=' + m.strip() + '| clip'
    os.system(command);

a = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";
if input("use Aa-Zz-09 only (y/n): ") == "n":
	a += '!#$%*+,-.:;?@_';
pwd = ''.join(secrets.choice(a) for i in range(int(input("Length: "))));
copy(pwd);
sys.exit();
