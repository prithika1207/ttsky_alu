import cocotb
from cocotb.triggers import Timer


@cocotb.test()
async def test_alu(dut):
    dut._log.info("Starting ALU Test")

    # init / reset
    dut.ena.value = 1
    dut.ui_in.value = 0
    dut.uio_in.value = 0
    dut.rst_n.value = 0

    await Timer(50, unit="ns")
    dut.rst_n.value = 1
    await Timer(50, unit="ns")

    # (A, B, op, expected output)
    test_cases = [
        (3, 2, 0, 5),  # ADD
        (3, 2, 1, 1),  # SUB
        (3, 2, 2, 2),  # AND
        (3, 2, 3, 3),  # OR
    ]

    for a, b, op, expected in test_cases:

        # pack inputs (A in lower 4 bits, B in upper 4 bits)
        dut.ui_in.value = (b << 4) | a
        dut.uio_in.value = op

        await Timer(20, unit="ns")

        result = int(dut.uo_out.value)

        assert result == expected, f"FAIL: a={a} b={b} op={op} got={result}"

        dut._log.info(f"PASS: A={a}, B={b}, OP={op} → {result}")
