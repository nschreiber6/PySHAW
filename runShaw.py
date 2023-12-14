import subprocess

def run_shaw(file_name):
    try:
        # Replace 'Shaw.exe' with the actual name of your executable
        executable_path = './Shaw302.exe'

        # Start the executable
        with subprocess.Popen([executable_path], stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True) as process:
            # Send the file name as input to the subprocess
            # get output from process "Something to print"
            lines = process.stdout.readlines()
            print(lines)
            # for line in p.stdout:
            #     #line = p.stdout.readline()
            #     print(line)
            # # one_line_output = ' '
            # # while one_line_output[0] != 'E':
            # #     one_line_output = p.stdout.readline()
            # #     print(one_line_output)
            # #     if one_line_output[0] == 'E':
            # print('here')
            
            # # write 'a line\n' to the process
            # p.stdin.write(file_name+'\n')
            # print()

            # # get output from process "not time to break"
            # one_line_output = p.stdout.readline() 
            # print(one_line_output)
            #print(process.communicate(input='c1_veg.inp')[0])

            # # Wait for the process to finish
            #process.wait()
            # print(process.returncode)
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")




if __name__ == "__main__":
    file_name_input = 'c1_veg.inp'
    run_shaw(file_name_input)
