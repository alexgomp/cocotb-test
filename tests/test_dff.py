import pathlib

from cocotb_test.simulator import run
import pytest
import os

tests_dir = os.path.dirname(__file__)


@pytest.mark.skipif(os.getenv("SIM") == "ghdl", reason="Verilog not suported")
# @pytest.mark.parametrize("seed", range(10))
def test_dff_verilog():
    run(verilog_sources=[os.path.join(tests_dir, "dff.sv")], toplevel="dff_test", module="dff_cocotb")  # sources  # top level HDL  # name of cocotb test module


@pytest.mark.skipif(os.getenv("SIM") == "verilator", reason="VHDL not suported")
@pytest.mark.skipif(os.getenv("SIM") == "icarus", reason="VHDL not suported")
def test_dff_vhdl():
    run(vhdl_sources=[os.path.join(tests_dir, "dff.vhdl")], toplevel="dff_test_vhdl", module="dff_cocotb", toplevel_lang="vhdl")


@pytest.mark.skipif(os.getenv("SIM") not in ["questa", "modelsim"], reason="TCL is not supported")
def test_dff_tcl(tmp_path: pathlib.Path):
    tcl_file_path = pathlib.Path.joinpath(tmp_path, "dff.tcl")
    with tcl_file_path.open('w') as tcl_file:
        tcl_file.write(f'vcom {os.path.join(tests_dir, "dff.vhdl")}')
    run(tcl_sources=[tcl_file_path], toplevel="work.dff_test_vhdl", module="dff_cocotb", toplevel_lang="vhdl")

if __name__ == "__main__":
    test_dff_verilog()
    # test_dff_vhdl()
