import random;
import clipboard;
import sys;

a = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";
if raw_input("use Aa-Zz-09 only (y/n): ") == "n":
	a += '!#$%*+,-.:;?@_';
pwd = ''.join(random.choice(a) for i in range(int(raw_input("Length: "))))
clipboard.copy(pwd);
sys.exit();
