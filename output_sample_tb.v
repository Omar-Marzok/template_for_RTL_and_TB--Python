module output_sample_tb #(parameter WIDTH_tb = 8, DEPTH_tb = 4) ();
    reg   [WIDTH_tb-1:0] input_1_tb;
    reg   [DEPTH_tb-1:0] input_2_tb;
    reg   [15:0] input_3_tb;
    reg            CLK_tb;
    reg           RST_tb;
    wire  [15:0] out_1_tb;
    wire  [WIDTH_tb-1:0] out_2_tb;

parameter CLK_PERIOD = 10;

initial 
begin

    initialize();
    reset();

    // write test cases 

    #200 $stop;  // end stimulus here
end

//////////////////////// TASKS ///////////////////

//----------------> initialization
task initialize;
  begin
    input_1_tb = 'b0;
    input_2_tb = 'b0;
    input_3_tb = 'b0;
    CLK_tb = 'b0;
  end
endtask

//----------------> reset
task reset;
  begin
    RST_tb = 1'b1;
    #CLK_PERIOD;
    RST_tb = 1'b0;
    #CLK_PERIOD;
    RST_tb = 1'b1;
    #CLK_PERIOD;
  end
endtask 



always #(CLK_PERIOD/2) CLK_tb = ~ CLK_tb;

output_sample #(.WIDTH(WIDTH_tb), .DEPTH(DEPTH_tb)) DUT (
.input_1(input_1_tb),
.input_2(input_2_tb),
.input_3(input_3_tb),
.CLK(CLK_tb),
.RST(RST_tb),
.out_1(out_1_tb),
.out_2(out_2_tb)
);

endmodule