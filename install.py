import os
import sys
import os.path
import platform

show_texts = '--no-info' not in sys.argv
scripts = os.listdir('install')

def fix_directory() -> None: # make sure the user's in the correct directory
    if '--stay' not in sys.argv: # --stay is not used in as a argument
        path = os.path.dirname(__file__) # the correct directory
        os.chdir(path) # switch 

        if show_texts:
            print(f'Switched directory to {path}.')
            print(f'This is done to solve some issues!')
            print(f'Use --stay to skip that.')
        
def ask_os() -> str: # returns the file name of the os-specific installer script    
    print(f'Your operating system is recognized as: {platform.freedesktop_os_release().get("ID_LIKE")}')
    print('Choose your operating system:')
    
    for number, script in enumerate(scripts): # list all the operating_systems with their given number
        system_name = ' '.join(script.title().split('.')[:-1]) # e.g. windows.bat -> Windows
        file_extension = script.split(".")[-1] # e.g. windows.bat -> bat
        
        print(f'  [{number}] · {system_name} (.{file_extension})')

    try:
        chosen = input('Enter a number and press enter: ')
    except KeyboardInterrupt: # user presses CTRL+C
        if show_texts:
            print('\nExited!')
        sys.exit(0)
    
    return scripts[int(chosen)]

def run_installation(script: str=ask_os()):
    if show_texts:
        print('This could take a while!')
        print('If you\'ll see red (orange text is okay!) text, that could mean the installation did\'t succeed.')
        print('Normally, this should take a few seconds.')
        print('The installation is done (probably) successfully when you see "Done."!')
        input('(Press enter to continue)')

    if os.system(f'install/{script}'):
        print('Done.')
    else:
        print('The installation failed!')

if '--fast-install' in sys.argv:
    if sys.argv[2] in scripts:
        run_installation(script=sys.argv[2])
        
    else:
        print('ERROR · Please type the installer script with its file extension.')
        print('EXAMPLE: "--fast-install windows.bat"')

def main():
    if show_texts:
        print(f'Tip: hate seeing these info messages? Use --no-info as an command-line argument!')
        print(f'Tip: Use "--fast-install <scipt-filename>".')
    
    fix_directory()
    run_installation()   

if __name__ == '__main__':
    main()