#Copyright 2017 Ettus Research LLC
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

########################################################################
# Template for raw text data describing registers
# name addr[bit range inclusive] default optional enums
########################################################################
REGS_TMPL="""\
########################################################################
## address 0
########################################################################
address0		         0[20:8]    0
Reset	                 0[7]       0
Reserved_0_0             0[6:5]     0
SPI_3wire                0[4]       0          enable, disable
Reserved_0_1	         0[3:0]     0
########################################################################
## address 1
########################################################################
address1	             1[20:8]    1
Reserved_1_0	         1[7:0]     0
########################################################################
## address 2
########################################################################
address2	             2[20:8]    2
Reserved_2_0	         2[7:1]     0
Powerdown                2[0] 	    0	       normal, powerdown
########################################################################
## address 3
########################################################################
address3	             3[20:8]    3
ID_Device_Type	         3[7:0]     6
########################################################################
## address 4
########################################################################
address4	             4[20:8]    4
ID_Prod_MSB    	         4[7:0]     208
########################################################################
## address 5
########################################################################
address5	             5[20:8]    5
ID_Prod_LSB    	         5[7:0]     91
########################################################################
## address 6
########################################################################
address6	             6[20:8]    6
ID_MaskRev    	         6[7:0]     32         LMK04821=36,LMK04826=37,LMK04828=32
########################################################################
## address 12 (0x00C)
########################################################################
address12	             12[20:8]    0x00C
ID_Vendor_MSB            12[7:0]     81
########################################################################
## address 13 (0x00D)
########################################################################
address13	             13[20:8]    0x00D
ID_Vendor_LSB            13[7:0]     4
""" 
########################################################################
# Template for methods in the body of the struct
########################################################################

BODY_TMPL = """\




uint32_t get_reg(int addr){
    uint32_t reg = 0;
    switch(addr){
    % for addr in sorted(set(map(lambda r: r.get_addr(), regs))):
    case ${addr}:
        % for reg in filter(lambda r: r.get_addr() == addr, regs):
        reg |= (uint32_t(${reg.get_name()}) & ${reg.get_mask()}) << ${reg.get_shift()};
        % endfor
        break;
    % endfor
    }
    return reg;
}
"""

if __name__ == '__main__':
    import common; common.generate(
        name='lmk04828_regs',
        regs_tmpl=REGS_TMPL,
        body_tmpl=BODY_TMPL,
        file=__file__,
    )

