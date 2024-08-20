module output_sample #(parameter WIDTH = 8, DEPTH = 4) (
    input wire [WIDTH-1:0] input_1,
    input wire [DEPTH-1:0] input_2,
    input wire [15:0] input_3,
    input wire      CLK,
    input wire     RST,
    output reg [15:0] out_1,
    output wire [WIDTH-1:0] out_2
);

always @(posedge CLK or negedge RST) 
 begin
    if (!RST) 
    begin

        // Reset logic here

    end 
    else
    begin

        // the sequential  logic here  
     
    end
 end 


always @(*) 
 begin 

         // the combinational  logic here
       
 end

endmodule // output_sample