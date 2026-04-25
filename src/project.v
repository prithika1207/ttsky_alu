`default_nettype none

module tt_um_alu (
    input  wire [7:0] ui_in,     // A and B inputs
    output wire [7:0] uo_out,    // result
    input  wire [7:0] uio_in,    // op select
    output wire [7:0] uio_out,
    output wire [7:0] uio_oe,
    input  wire       ena,
    input  wire       clk,
    input  wire       rst_n
);

    wire [3:0] a = ui_in[3:0];
    wire [3:0] b = ui_in[7:4];
    wire [1:0] op = uio_in[1:0];

    reg [7:0] result;

    always @(*) begin
        case (op)
            2'b00: result = a + b;   // ADD
            2'b01: result = a - b;   // SUB
            2'b10: result = a & b;   // AND
            2'b11: result = a | b;   // OR
            default: result = 0;
        endcase
    end

    assign uo_out = result;

    assign uio_out = 8'b0;
    assign uio_oe  = 8'b0;

endmodule
