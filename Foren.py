import os, sys

if __name__ == "__main__":
    if len(sys.argv) == 3:
        file, wordlist = sys.argv[1:3]
        file = str(file)
        wordlist = str(wordlist)
        print('+'+('-'*22)+'+\n|'+(' '*22)+'|\n|'+' '+'Foren.py by donutapn'+' '+'|\n|'+(' '*22)+'|\n+'+('-'*22)+'+')
        os.popen('exiftool ' + file + ' >> ' + file + '_exiftool.txt').read()
        os.popen('foremost ' + file + '  -o ' + file + '_foremost').read()
        os.popen('binwalk -e ' + file + ' --directory ' + file + '_binwalk').read()
        os.popen('zsteg ' + file + ' >> ' + file + '_zsteg.txt').read()
        try:
            wordlist = open(wordlist,'r',errors = 'ignore')
            for passphrase in wordlist: 
                os.popen('steghide extract -sf ' + file + ' -p '+ passphrase.strip()).read()
        except FileNotFoundError as Er:
            print('Wordlist not found.\n'*3)
    elif len(sys.argv) == 2:
        file = sys.argv[1]
        file = str(file).strip()
        print('+'+('-'*22)+'+\n|'+(' '*22)+'|\n|'+' '+'Foren.py by donutapn'+' '+'|\n|'+(' '*22)+'|\n+'+('-'*22)+'+')
        os.popen('exiftool ' + file + ' >> ' + file + '_exiftool.txt').read()
        os.popen('foremost ' + file + '  -o ' + file + '_foremost').read()
        os.popen('binwalk -e ' + file + ' --directory ' + file + '_binwalk').read()
        os.popen('zsteg ' + file + ' >> ' + file + '_zsteg.txt').read()
    else:
        print('\n  python3 Foren.py [file] [wordlist]\n\n\t  or\n\n  python3 Foren.py [file]\n')
