
class larger_func(object):
    def __init__(self):
        pass
        
    def small_one(self):
        print('This is small method ONE \n')
        print('Python identifies this function as "{}" '.format(__name__))
    
        
    def small_two(self):
        print('This is small method TWO\n')
        print('Python identifies this function as "{}" '.format(__name__))
    
    def small_three(self):
        print('This is small method THREE\n')
        print('Python identifies this function as "{}" '.format(__name__))

        
def source_file_usage():
    print('Python identifies the present "namespace" as "{}" \n'.format(__name__)) # watch what is happening with this line
    print('I have set this block to be run when this script is called directly')
    print('--' * 40)
    print('This function is usually named "main", but I feel an almost irresistible urge to name it\n')
    print("what_to_do_with_this_python_file_when_called_from_command_line".upper())
    print('\nYou have to use the import statement to be able to make use of the other functions defined here')
    
def greeter(name):
    print('Hello {}'.format(name.upper()))
    print('\nPython now identifies the "namespace" as "{}" '.format(__name__), end = ' ')
    print('and your name has {} letters: '.format(len(name)))
    
if __name__ == '__main__':
    source_file_usage()