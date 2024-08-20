############################################################################
###############################  THE START  ################################
############################################################################

inputs=[]
in_width=[]
outputs=[]
out_width=[]
out_type=[]
parameter=[]
pram_width=[]
clk=[]
rst=[]
reserved_words = [
    "always", "and", "assign", "automatic", "begin", "buf", "bufif0", "bufif1", "case",
    "casex", "casez", "cell", "cmos", "config", "deassign", "default", "defparam", "design",
    "disable", "edge", "else", "end", "endcase", "endconfig", "endfunction", "endgenerate",
    "endmodule", "endprimitive", "endspecify", "endtable", "endtask", "event", "for",
    "force", "forever", "fork", "function", "generate", "genvar", "highz0", "highz1",
    "if", "ifdef", "ifndef", "initial", "inout", "input", "instance", "integer", "join",
    "large", "liblist", "library", "localparam", "macromodule", "medium", "module", "nand",
    "negedge", "nmos", "nor", "noshowcancelled", "not", "notif0", "notif1", "or",
    "output", "parameter", "pmos", "posedge", "primitive", "pull0", "pull1", "pulldown",
    "pullup", "pulsestyle_onevent", "pulsestyle_ondetect", "rcmos", "real", "realtime",
    "reg", "release", "repeat", "rnmos", "rpmos", "rtran", "rtranif0", "rtranif1",
    "scalared", "showcancelled", "signed", "small", "specify", "specparam", "strong0",
    "strong1", "supply0", "supply1", "table", "task", "time", "tran", "tranif0",
    "tranif1", "tri", "tri0", "tri1", "triand", "trior", "trireg", "unsigned", "use",
    "vectored", "wait", "wand", "weak0", "weak1", "while", "wire", "wor", "xnor", "xor"]

######################### function to check the input word ###################
def is_valid_word():
    while True:
        word = input("Enter: ").strip()
        x = True
        if word == "":
            x = False
        elif word in reserved_words:
            x = False
        elif word in inputs:
            x = False
        elif word in outputs:
            x = False
        elif word in parameter:
            x = False
        elif word in clk:
            x = False
        elif word in rst:
            x = False
        elif ' ' in word:
            x = False
        elif not (word[0].isalpha() or word[0] == '_'):
            x = False
        elif not all(char.isalnum() or char == '_' for char in word):
            x = False
        if x == True:
            break
        else:
            print("Invalid word. Please try again.")
            continue
    return word


################## function to check the input number ####################
def is_valid_num():
    while True:
        num = input("Enter : ")
        if num.isdigit():
            break
        else:
            print("Invalid number. Please try again.")
            continue
    return num

######## function to assign a parameter to the reg/wire ###########
def choose_para(parameters):
    options = {chr(65 + i): parameters for i, parameters in enumerate(parameter)}
    for option, parameters in options.items():
        print(f"{option} -> {parameters}")
    
    while True:
        choice = input("Choose a parameter (A, B, ...): ").upper()
        if choice in options:
            return choice
        else:
            print("Invalid choice. Please try again.")

######################### set module name ############################## 
print(" ** Enter the module name ** ")
module_name = is_valid_word()
 
######################## set parameters #################################
print("Do you have parameters? ")
x = input ("('yes' --->  Y/y/1) ('NO' press any other button) :")
if x=='y' or x == 'Y' or x == '1':
    print("Enter the number of parameters ")
    num = int(is_valid_num())
    while num > 0:
        print("Enter the parameter name : ")
        pram_name = is_valid_word()
        parameter.append(pram_name)
        print("Enter the parameter value :")
        input_width = is_valid_num()
        pram_width.append(input_width)
        num = num - 1
  
######################## set input ports ################################
print("Enter the number of inputs ")
num = int(is_valid_num())    
while num > 0:
    print("Enter the input name ")
    input_name = is_valid_word()
    inputs.append(input_name)
    if parameter:
        print("IS this input is parameterized? ")
        x = input ("('yes' --->  Y/y/1) ('NO' press any other button) :")
        if x=='y' or x == 'Y' or x == '1':
            input_width = choose_para(parameter)
        else:
            print("Enter the width value")
            input_width = is_valid_num()
    else:
        print("Enter the width value")
        input_width = is_valid_num()
    in_width.append(input_width)
    num = num - 1

########################### set output ports ################################
print("Enter the number of outputs ")
num = int(is_valid_num())    
while num > 0:
    print("Enter the output name ")
    output_name = is_valid_word()
    outputs.append(output_name)
    print("IS this output is reg ? ")
    x = input ("('yes' --->  Y/y/1) ('NO' press any other button) :")
    if x=='y' or x == 'Y' or x == '1':
        out_type.append("reg")
    else:
        out_type.append("wire")
    if parameter:
        print("IS this output is parameterized? ")
        x = input ("('yes' --->  Y/y/1) ('NO' press any other button) :")
        if x=='y' or x == 'Y' or x == '1':
            output_width = choose_para(parameter)
        else:
            print("Enter the width value")
            output_width = is_valid_num()
    else:
        print("Enter the width value")
        output_width = is_valid_num()
    out_width.append(output_width)
    num = num - 1

########################### set clock  ##############################
print("Do you have a clock ? ")
x = input ("('yes' --->  Y/y/1) ('NO' press any other button) :")
if x=='y' or x == 'Y' or x == '1':
    print("Enter the clock name ")
    inn = is_valid_word()
    clk.append(inn)
    print("Is the clock is positive edge ")
    x = input ("('yes' --->  Y/y/1) ('NO' press any other button) :")
    if x=='y' or x == 'Y' or x == '1':
        clk.append("posedge")
    else:
        clk.append("negedge")

########################### set reset  ##############################
print("Do you have a Reset ? ")
x = input ("('yes' --->  Y/y/1) ('NO' press any other button) :")
if x=='y' or x == 'Y' or x == '1':
    print("Enter the Reset name ")
    inn = is_valid_word()
    rst.append(inn)
    print("Is the Reset is synchronous ? ")
    x = input ("('yes' --->  Y/y/1) ('NO' press any other button) :")
    if x=='y' or x == 'Y' or x == '1':
        rst.append("s")
    else:
        rst.append("a")
    print("Is the Reset is positive edge ?")
    x = input ("('yes' --->  Y/y/1) ('NO' press any other button)  :")
    if x=='y' or x == 'Y' or x == '1':
        rst.append(" ")
    else:
        rst.append("!")
    
######################## Write the module file #########################
file_name = f"{module_name}.v"

# Create the module header
module_header = f"module {module_name} "
    
# Add parameters to the header if any
if parameter:
    param_str = "#(parameter "
    for param, width in zip(parameter, pram_width):
        param_str += f"{param} = {width}, "
    param_str = param_str.rstrip(', ')  # Remove the last comma and space
    param_str += ") (\n"
    module_header += param_str
else:
    module_header += "( \n"
    
# Add ports to the header
ports = []
for input_name, width in zip(inputs, in_width):
    if width == "A" or width == "B" or width == "C" or width == "D" or width == "E":
        map_par = ord(width) - ord('A')
        width = parameter[map_par]
        ports.append(f"    input wire [{width}-1:0] {input_name}")
    elif width == "1":
        ports.append(f"    input wire           {input_name}")
    else:
        width = int(width) - 1
        ports.append(f"    input wire [{width}:0] {input_name}")
if clk:
    ports.append(f"    input wire      {clk[0]}")
if rst:
    ports.append(f"    input wire     {rst[0]}")
for output_name, width, type_ in zip(outputs, out_width, out_type):
    if width == "A" or width == "B" or width == "C" or width == "D" or width == "E":
        map_par = ord(width) - ord('A')
        width = parameter[map_par]
        ports.append(f"    output {type_} [{width}-1:0] {output_name}")
    elif width == "1":
        ports.append(f"    output {type_}            {output_name}")
    else:
        width = int(width) - 1
        ports.append(f"    output {type_} [{width}:0] {output_name}")
module_header += ",\n".join(ports) + "\n);\n"


sequen_logic = ""
if clk :
    if rst:
        if rst[2] == "!":
            edge="negedge"
        else:
            edge="posedge"
        if rst[1] == "a" :
            sequen_logic += f"""
always @({clk[1]} {clk[0]} or {edge} {rst[0]}) 
 begin
    if ({rst[2]}{rst[0]}) 
    begin\n
        // Reset logic here\n
    end 
    else
    begin\n
        // the sequential  logic here  \n     
    end
 end \n
"""
        elif rst[1] == "s":
            sequen_logic += f"""
always @({clk[1]} {clk[0]} ) 
 begin \n         
    if ({rst[2]}{rst[0]}) 
    begin\n
        // Reset logic here\n
    end 
    else
    begin\n
        // the sequential  logic here  \n     
    end
 end\n
"""
    else:
        sequen_logic += f"""
always @({clk[1]} {clk[0]} ) 
 begin \n         
        // the sequential  logic here \n  
 end\n
"""

comb_logic = """
always @(*) 
 begin \n
         // the combinational  logic here\n       
 end\n
"""
# Create the module footer
module_footer = f"endmodule // {module_name}"

# Write to the file

f = open(file_name, "w")    
with f as file:
    file.write(module_header)
    file.write(sequen_logic)
    file.write(comb_logic)
    file.write(module_footer)
f.close()


######################## Write the test bench file #########################
file_name = f"{module_name}_tb.v"

# Create the testbench header
tb_header = f"module {module_name}_tb "
    
# Add parameters to the header if any
if parameter:
    param_str = "#(parameter "
    for param, width in zip(parameter, pram_width):
        param_str += f"{param}_tb = {width}, "
    param_str = param_str.rstrip(', ')  # Remove the last comma and space
    param_str += ") ();\n"
    tb_header += param_str
else:
    tb_header +=  "();\n"

# Declare testbench signals
ports = []
for input_name, width in zip(inputs, in_width):
    if width == "A" or width == "B" or width == "C" or width == "D" or width == "E":
        map_par = ord(width) - ord('A')
        width = parameter[map_par]
        ports.append(f"    reg   [{width}_tb-1:0] {input_name}_tb")
    elif width == "1":
        ports.append(f"    reg                 {input_name}_tb")
    else:
        width = int(width) - 1
        ports.append(f"    reg   [{width}:0] {input_name}_tb")
if clk:
    ports.append(f"    reg            {clk[0]}_tb")
if rst:
    ports.append(f"    reg           {rst[0]}_tb")
for output_name, width in zip(outputs, out_width):
    if width == "A" or width == "B" or width == "C" or width == "D" or width == "E":
        map_par = ord(width) - ord('A')
        width = parameter[map_par]
        ports.append(f"    wire  [{width}_tb-1:0] {output_name}_tb")
    elif width == "1":
        ports.append(f"    wire                 {output_name}_tb")
    else:
        width = int(width) - 1
        ports.append(f"    wire  [{width}:0] {output_name}_tb")
tb_header += ";\n".join(ports) + ";\n"

# Instantiate the design module

tb_inst = f"{module_name} "
if parameter:
    pram_str = "#("
    for pram in parameter:
        pram_str += f".{pram}({pram}_tb), "
    pram_str = pram_str.rstrip(", ")  # Remove the last comma and space
    pram_str += ") DUT (\n"
    tb_inst += pram_str
else:
    tb_inst += "DUT (\n"

port = []
for input_name in inputs:
    port.append(f".{input_name}({input_name}_tb)")
if clk:
    port.append(f".{clk[0]}({clk[0]}_tb)")
if rst:
    port.append(f".{rst[0]}({rst[0]}_tb)")
for output_name in outputs:
    port.append(f".{output_name}({output_name}_tb)")
   
tb_inst += ",\n".join(port) + "\n);\n\n"

# Add initial block for stimulus
initial_block = """
parameter CLK_PERIOD = 10;

initial 
begin\n
    initialize();
    reset();

    // write test cases \n
    #200 $stop;  // end stimulus here
end
"""

tasks = """
//////////////////////// TASKS ///////////////////

//----------------> initialization
task initialize;
  begin
"""

# Automatically generate initialization lines for inputs and clock
for input_name in inputs:
    tasks += f"    {input_name}_tb = 'b0;\n"
if clk:
    tasks += f"    {clk[0]}_tb = 'b0;\n"

tasks += f"""  end
endtask

//----------------> reset
task reset;
  begin
    {rst[0]}_tb = 1'b1;
    #CLK_PERIOD;
    {rst[0]}_tb = 1'b0;
    #CLK_PERIOD;
    {rst[0]}_tb = 1'b1;
    #CLK_PERIOD;
  end
endtask \n\n
"""

Clock_generator = f"""
always #(CLK_PERIOD/2) {clk[0]}_tb = ~ {clk[0]}_tb;\n
"""

# Create the testbench footer
tb_footer = "endmodule"

    # Write to the file

ftb = open(file_name, "w")
with ftb as file:
    file.write(tb_header)
    file.write(initial_block)
    file.write(tasks)
    file.write(Clock_generator)
    file.write(tb_inst)
    file.write(tb_footer)
ftb.close()
    
############################################################################
###############################  THE END  ##################################
############################################################################