"""
 mbed CMSIS-DAP debugger
 Copyright (c) 2006-2013 ARM Limited

 Licensed under the Apache License, Version 2.0 (the "License");
 you may not use this file except in compliance with the License.
 You may obtain a copy of the License at

     http://www.apache.org/licenses/LICENSE-2.0

 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.
"""

from flash import Flash



flash_algo = { 'load_address' : 0x20000000,
               'instructions' : [
                                  0xE00ABE00, 0x062D780D, 0x24084068, 0xD3000040, 0x1E644058, 0x1C49D1FA, 0x2A001E52, 0x4770D1F2,
                                  0x6000f1a0, 0x47700ac0, 0x49544855, 0x49556081, 0x20006081, 0x49524770, 0x30f9f24c, 0x47706108, 
                                  0xf24c494f, 0x610830f9, 0x47702000, 0x47702000, 0xb5004a4b, 0x28006950, 0xf7ffda01, 0x6910ffe5, 
                                  0xd4fc03c0, 0x30f9f24c, 0x69506110, 0x0104f248, 0x61504308, 0xf4406950, 0x61503080, 0x03c06910, 
                                  0x6950d4fc, 0x61504388, 0xbd002000, 0x4a3cb510, 0x23004604, 0x28006950, 0xf7ffda01, 0x6911ffc5, 
                                  0xd4fc03c8, 0x30f9f24c, 0xf1a46110, 0x0ae06400, 0xd30228ff, 0x6300f44f, 0x6951b2c0, 0x74f8f640, 
                                  0x240243a1, 0x00c0eb04, 0x0003ea40, 0x0001ea40, 0x69506150, 0x3080f440, 0x69106150, 0xd4fc03c0, 
                                  0xf0206950, 0x61500002, 0xbd102000, 0x460eb5f0, 0x07492400, 0x2701d001, 0x2700e000, 0xf0204d20, 
                                  0x69680307, 0xda012800, 0xff8ef7ff, 0x03c06928, 0xf24cd4fc, 0x612830f9, 0x01d6eb07, 0xf040e025, 
                                  0x61680001, 0x60186810, 0xf1026850, 0x60580208, 0x0308f103, 0x03c06928, 0x6928d4fc, 0xd00107c0, 
                                  0x61282001, 0x0c08f852, 0x6c08f853, 0xd10542b0, 0x0c04f852, 0x6c04f853, 0xd00542b0, 0xf0206968, 
                                  0x61680001, 0xbdf02001, 0x69681c64, 0xd8d642a1, 0x0001f020, 0x20006168, 0x0000bdf0, 0x45670123, 
                                  0x40022000, 0xcdef89ab, 0x00000000,
                                ],
               'pc_init'          : 0x20000041,
               'pc_eraseAll'      : 0x20000051,
               'pc_erase_sector'  : 0x2000008D,
               'pc_program_page'  : 0x200000ED,
               'static_base'      : 0x20000200,
               'begin_data'       : 0x20001000, # Analyzer uses a max of 2 KB data (512 pages * 4 bytes / page)
               'page_buffers'    : [0x20001000, 0x20001800],   # Enable double buffering
               'begin_stack'      : 0x20002800,
               'min_program_length' : 8,
               'analyzer_supported' : True,
               'analyzer_address' : 0x20003000 # Analyzer 0x20003000..0x20003600
              };


class Flash_stm32l486(Flash):

    def __init__(self, target):
        super(Flash_stm32l486, self).__init__(target, flash_algo)