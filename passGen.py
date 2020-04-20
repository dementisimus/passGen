import secrets;
import string;
import os;
import sys;

def copy(m):
    command = 'echo ' + m.strip() + '| clip';
    os.system(command);

a = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!#$%*+,-.:;?@_';
pwd = ''.join(secrets.choice(a) for i in range(int(input("Length: "))));
copy(pwd.replace("\n", ""));
sys.exit();
