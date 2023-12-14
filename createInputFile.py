
def create_inp(file_name):
    content = """Shaw 3.0
   0   1   0   0
{0}.sit                                                                  
c1.wea                                                      
c1.moi                                                                   
c1.tem                                                                   
   0   0   0   24   0   0   0   0  1   24   0   0   0   24   0   0   0   0   0  0
{0}_Out/out_veg.txt                                                        
{0}_Out/temp_veg.txt                                                           
{0}_Out/moist_veg.txt                                                          
{0}_Out/liquid_veg.txt
{0}_Out/matric_veg.txt                                                          
{0}_Out/cantem_veg.txt
{0}_Out/canhum_veg.txt
{0}_Out/snowtem_veg.txt
{0}_Out/energy_veg.txt                                                          
{0}_Out/water_veg.txt                                                      
{0}_Out/wflow_veg.txt                                                    
{0}_Out/rootxt_veg.txt                                                     
{0}_Out/lateral_veg.txt
{0}_Out/frost_veg.txt                                                       
{0}_Out/salts_veg.txt                                                      
{0}_Out/solute_veg.txt                                                      
{0}_Out/profile_veg.txt                                                       
{0}_Out/extra1_veg.txt
{0}_Out/canwnd_veg.txt
""".format(file_name)

    # Write content to the file
    with open(f'{file_name}.inp', 'w',0x777) as file:
        file.write(content)

    # try:
    #     with subprocess.Popen([mkdir, file_name+'_Out'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True) as process:
    #         process.wait()
    #         print(process.returncode)
    # except subprocess.CalledProcessError as e:
    #     print(f"An error occurred: {e}")




if __name__ == "__main__":
    create_inp("c1_veg_desert")
    file_name_input = 'c1_veg.inp'
    #run_shaw(file_name_input)