##@file
# SCINTIL API

## @defgroup pythonapi Scintil Python remote API
## Generated Scintil Python API
## @addtogroup pythonapi
## @{
# This is a generated file, do not edit !
from enum import Enum, Flag, auto
import requests
import logging
import json
import pprint
import sys
import re

from array import array


class scintil_hal_sys_chip_t (Enum):
  SCINTIL_CHIP_ASIC = 0x0
  SCINTIL_CHIP_FPGA = 0x1


class hal_sys_chip_t (Enum):
  CHIP_ASIC = 0x0
  CHIP_FPGA = 0x1


class scintil_hal_ths_t (Enum):
  THS_PIC = 0x0
  THS_TEC = 0x1


class hal_ths_t (Enum):
  THS_PIC = 0x0
  THS_TEC = 0x1


class scintil_hal_fsm_state_t (Enum):
  FSM_SERVOLOOP_RUNNING = 0x1
  FSM_SERVOLOOP_STOPPED = 0x2
  FSM_FFT = 0x3
  FSM_NONE = 0x4


class hal_fsm_state_t (Enum):
  FSM_SERVOLOOP_RUNNING = 0x1
  FSM_SERVOLOOP_STOPPED = 0x2
  FSM_FFT = 0x3
  FSM_NONE = 0x4


class scintil_hal_ll_idac_t (Enum):
  SCINTIL_HAL_IDAC1_OUT0 = 0x0
  SCINTIL_HAL_IDAC1_OUT1 = 0x1
  SCINTIL_HAL_IDAC1_OUT2 = 0x2
  SCINTIL_HAL_IDAC1_OUT3 = 0x3
  SCINTIL_HAL_IDAC1_OUT4 = 0x4
  SCINTIL_HAL_IDAC2_OUT0 = 0x5
  SCINTIL_HAL_IDAC2_OUT1 = 0x6
  SCINTIL_HAL_IDAC2_OUT2 = 0x7
  SCINTIL_HAL_IDAC2_OUT3 = 0x8
  SCINTIL_HAL_IDAC2_OUT4 = 0x9
  SCINTIL_HAL_IDAC3_OUT0 = 0xa
  SCINTIL_HAL_IDAC3_OUT1 = 0xb
  SCINTIL_HAL_IDAC3_OUT2 = 0xc
  SCINTIL_HAL_IDAC3_OUT3 = 0xd
  SCINTIL_HAL_IDAC3_OUT4 = 0xe
  SCINTIL_HAL_IDAC4_OUT0 = 0xf
  SCINTIL_HAL_IDAC4_OUT1 = 0x10
  SCINTIL_HAL_IDAC4_OUT2 = 0x11
  SCINTIL_HAL_IDAC4_OUT3 = 0x12
  SCINTIL_HAL_IDAC4_OUT4 = 0x13
  SCINTIL_HAL_IDAC5_OUT0 = 0x14
  SCINTIL_HAL_IDAC5_OUT1 = 0x15
  SCINTIL_HAL_IDAC5_OUT2 = 0x16
  SCINTIL_HAL_IDAC5_OUT3 = 0x17
  SCINTIL_HAL_IDAC5_OUT4 = 0x18
  SCINTIL_HAL_IDAC6_OUT0 = 0x19
  SCINTIL_HAL_IDAC6_OUT1 = 0x1a
  SCINTIL_HAL_IDAC6_OUT2 = 0x1b
  SCINTIL_HAL_IDAC6_OUT3 = 0x1c
  SCINTIL_HAL_IDAC6_OUT4 = 0x1d
  SCINTIL_HAL_IDAC7_OUT0 = 0x1e
  SCINTIL_HAL_IDAC7_OUT1 = 0x1f
  SCINTIL_HAL_IDAC7_OUT2 = 0x20
  SCINTIL_HAL_IDAC7_OUT3 = 0x21
  SCINTIL_HAL_IDAC_UNKNOWN = 0x22


class hal_ll_idac_t (Enum):
  HAL_IDAC1_OUT0 = 0x0
  HAL_IDAC1_OUT1 = 0x1
  HAL_IDAC1_OUT2 = 0x2
  HAL_IDAC1_OUT3 = 0x3
  HAL_IDAC1_OUT4 = 0x4
  HAL_IDAC2_OUT0 = 0x5
  HAL_IDAC2_OUT1 = 0x6
  HAL_IDAC2_OUT2 = 0x7
  HAL_IDAC2_OUT3 = 0x8
  HAL_IDAC2_OUT4 = 0x9
  HAL_IDAC3_OUT0 = 0xa
  HAL_IDAC3_OUT1 = 0xb
  HAL_IDAC3_OUT2 = 0xc
  HAL_IDAC3_OUT3 = 0xd
  HAL_IDAC3_OUT4 = 0xe
  HAL_IDAC4_OUT0 = 0xf
  HAL_IDAC4_OUT1 = 0x10
  HAL_IDAC4_OUT2 = 0x11
  HAL_IDAC4_OUT3 = 0x12
  HAL_IDAC4_OUT4 = 0x13
  HAL_IDAC5_OUT0 = 0x14
  HAL_IDAC5_OUT1 = 0x15
  HAL_IDAC5_OUT2 = 0x16
  HAL_IDAC5_OUT3 = 0x17
  HAL_IDAC5_OUT4 = 0x18
  HAL_IDAC6_OUT0 = 0x19
  HAL_IDAC6_OUT1 = 0x1a
  HAL_IDAC6_OUT2 = 0x1b
  HAL_IDAC6_OUT3 = 0x1c
  HAL_IDAC6_OUT4 = 0x1d
  HAL_IDAC7_OUT0 = 0x1e
  HAL_IDAC7_OUT1 = 0x1f
  HAL_IDAC7_OUT2 = 0x20
  HAL_IDAC7_OUT3 = 0x21
  HAL_IDAC_UNKNOWN = 0x22


class scintil_hal_ll_idac_enable_t (Enum):
  SCINTIL_HAL_IDAC_DISABLE = 0x0
  SCINTIL_HAL_IDAC_ENABLE = 0x1


class hal_ll_idac_enable_t (Enum):
  HAL_IDAC_DISABLE = 0x0
  HAL_IDAC_ENABLE = 0x1


class scintil_hal_ll_vdac_t (Enum):
  SCINTIL_HAL_VDAC1_OUT0 = 0x0
  SCINTIL_HAL_VDAC1_OUT1 = 0x1
  SCINTIL_HAL_VDAC1_OUT2 = 0x2
  SCINTIL_HAL_VDAC1_OUT3 = 0x3
  SCINTIL_HAL_VDAC1_OUT4 = 0x4
  SCINTIL_HAL_VDAC1_OUT5 = 0x5
  SCINTIL_HAL_VDAC1_OUT6 = 0x6
  SCINTIL_HAL_VDAC1_OUT7 = 0x7
  SCINTIL_HAL_VDAC2_OUT0 = 0x8
  SCINTIL_HAL_VDAC2_OUT1 = 0x9
  SCINTIL_HAL_VDAC2_OUT2 = 0xa
  SCINTIL_HAL_VDAC2_OUT3 = 0xb
  SCINTIL_HAL_VDAC2_OUT4 = 0xc
  SCINTIL_HAL_VDAC2_OUT5 = 0xd
  SCINTIL_HAL_VDAC2_OUT6 = 0xe
  SCINTIL_HAL_VDAC2_OUT7 = 0xf
  SCINTIL_HAL_VDAC3_OUT0 = 0x10
  SCINTIL_HAL_VDAC3_OUT1 = 0x11
  SCINTIL_HAL_VDAC3_OUT2 = 0x12
  SCINTIL_HAL_VDAC3_OUT3 = 0x13
  SCINTIL_HAL_VDAC3_OUT4 = 0x14
  SCINTIL_HAL_VDAC3_OUT5 = 0x15
  SCINTIL_HAL_VDAC3_OUT6 = 0x16
  SCINTIL_HAL_VDAC3_OUT7 = 0x17
  SCINTIL_HAL_VDAC4_OUT0 = 0x18
  SCINTIL_HAL_VDAC4_OUT1 = 0x19
  SCINTIL_HAL_VDAC4_OUT2 = 0x1a
  SCINTIL_HAL_VDAC4_OUT3 = 0x1b
  SCINTIL_HAL_VDAC4_OUT4 = 0x1c
  SCINTIL_HAL_VDAC4_OUT5 = 0x1d
  SCINTIL_HAL_VDAC4_OUT6 = 0x1e
  SCINTIL_HAL_VDAC4_OUT7 = 0x1f
  SCINTIL_HAL_VDAC5_OUT0 = 0x20
  SCINTIL_HAL_VDAC5_OUT1 = 0x21
  SCINTIL_HAL_VDAC5_OUT2 = 0x22
  SCINTIL_HAL_VDAC5_OUT3 = 0x23
  SCINTIL_HAL_VDAC5_OUT4 = 0x24
  SCINTIL_HAL_VDAC5_OUT5 = 0x25
  SCINTIL_HAL_VDAC5_OUT6 = 0x26
  SCINTIL_HAL_VDAC5_OUT7 = 0x27
  SCINTIL_HAL_VDAC6_OUT0 = 0x28
  SCINTIL_HAL_VDAC6_OUT1 = 0x29
  SCINTIL_HAL_VDAC6_OUT2 = 0x2a
  SCINTIL_HAL_VDAC6_OUT3 = 0x2b
  SCINTIL_HAL_VDAC6_OUT4 = 0x2c
  SCINTIL_HAL_VDAC6_OUT5 = 0x2d
  SCINTIL_HAL_VDAC6_OUT6 = 0x2e
  SCINTIL_HAL_VDAC6_OUT7 = 0x2f
  SCINTIL_HAL_VDAC7_OUT0 = 0x30
  SCINTIL_HAL_VDAC7_OUT1 = 0x31
  SCINTIL_HAL_VDAC7_OUT2 = 0x32
  SCINTIL_HAL_VDAC7_OUT3 = 0x33
  SCINTIL_HAL_VDAC7_OUT4 = 0x34
  SCINTIL_HAL_VDAC7_OUT5 = 0x35
  SCINTIL_HAL_VDAC7_OUT6 = 0x36
  SCINTIL_HAL_VDAC7_OUT7 = 0x37
  SCINTIL_HAL_VDAC_UNKNOWN = 0x38


class hal_ll_vdac_t (Enum):
  HAL_VDAC1_OUT0 = 0x0
  HAL_VDAC1_OUT1 = 0x1
  HAL_VDAC1_OUT2 = 0x2
  HAL_VDAC1_OUT3 = 0x3
  HAL_VDAC1_OUT4 = 0x4
  HAL_VDAC1_OUT5 = 0x5
  HAL_VDAC1_OUT6 = 0x6
  HAL_VDAC1_OUT7 = 0x7
  HAL_VDAC2_OUT0 = 0x8
  HAL_VDAC2_OUT1 = 0x9
  HAL_VDAC2_OUT2 = 0xa
  HAL_VDAC2_OUT3 = 0xb
  HAL_VDAC2_OUT4 = 0xc
  HAL_VDAC2_OUT5 = 0xd
  HAL_VDAC2_OUT6 = 0xe
  HAL_VDAC2_OUT7 = 0xf
  HAL_VDAC3_OUT0 = 0x10
  HAL_VDAC3_OUT1 = 0x11
  HAL_VDAC3_OUT2 = 0x12
  HAL_VDAC3_OUT3 = 0x13
  HAL_VDAC3_OUT4 = 0x14
  HAL_VDAC3_OUT5 = 0x15
  HAL_VDAC3_OUT6 = 0x16
  HAL_VDAC3_OUT7 = 0x17
  HAL_VDAC4_OUT0 = 0x18
  HAL_VDAC4_OUT1 = 0x19
  HAL_VDAC4_OUT2 = 0x1a
  HAL_VDAC4_OUT3 = 0x1b
  HAL_VDAC4_OUT4 = 0x1c
  HAL_VDAC4_OUT5 = 0x1d
  HAL_VDAC4_OUT6 = 0x1e
  HAL_VDAC4_OUT7 = 0x1f
  HAL_VDAC5_OUT0 = 0x20
  HAL_VDAC5_OUT1 = 0x21
  HAL_VDAC5_OUT2 = 0x22
  HAL_VDAC5_OUT3 = 0x23
  HAL_VDAC5_OUT4 = 0x24
  HAL_VDAC5_OUT5 = 0x25
  HAL_VDAC5_OUT6 = 0x26
  HAL_VDAC5_OUT7 = 0x27
  HAL_VDAC6_OUT0 = 0x28
  HAL_VDAC6_OUT1 = 0x29
  HAL_VDAC6_OUT2 = 0x2a
  HAL_VDAC6_OUT3 = 0x2b
  HAL_VDAC6_OUT4 = 0x2c
  HAL_VDAC6_OUT5 = 0x2d
  HAL_VDAC6_OUT6 = 0x2e
  HAL_VDAC6_OUT7 = 0x2f
  HAL_VDAC7_OUT0 = 0x30
  HAL_VDAC7_OUT1 = 0x31
  HAL_VDAC7_OUT2 = 0x32
  HAL_VDAC7_OUT3 = 0x33
  HAL_VDAC7_OUT4 = 0x34
  HAL_VDAC7_OUT5 = 0x35
  HAL_VDAC7_OUT6 = 0x36
  HAL_VDAC7_OUT7 = 0x37
  HAL_VDAC_UNKNOWN = 0x38


class scintil_hal_ll_vdac_ring_out_t (Enum):
  SCINTIL_HAL_VDAC_RING_0 = 0x0
  SCINTIL_HAL_VDAC_RING_1 = 0x1


class hal_ll_vdac_ring_out_t (Enum):
  HAL_VDAC_RING_0 = 0x0
  HAL_VDAC_RING_1 = 0x1


class scintil_hal_ll_vdac_instance_t (Enum):
  SCINTIL_HAL_VDAC_INSTANCE_1 = 0x0
  SCINTIL_HAL_VDAC_INSTANCE_2 = 0x1
  SCINTIL_HAL_VDAC_INSTANCE_3 = 0x2
  SCINTIL_HAL_VDAC_INSTANCE_4 = 0x3
  SCINTIL_HAL_VDAC_INSTANCE_5 = 0x4
  SCINTIL_HAL_VDAC_INSTANCE_6 = 0x5
  SCINTIL_HAL_VDAC_INSTANCE_7 = 0x6
  SCINTIL_HAL_VDAC_INSTANCE_8 = 0x7


class hal_ll_vdac_instance_t (Enum):
  HAL_VDAC_INSTANCE_1 = 0x0
  HAL_VDAC_INSTANCE_2 = 0x1
  HAL_VDAC_INSTANCE_3 = 0x2
  HAL_VDAC_INSTANCE_4 = 0x3
  HAL_VDAC_INSTANCE_5 = 0x4
  HAL_VDAC_INSTANCE_6 = 0x5
  HAL_VDAC_INSTANCE_7 = 0x6
  HAL_VDAC_INSTANCE_8 = 0x7


class scintil_hal_ll_vdac_reg_t (Enum):
  SCINTIL_HAL_VDAC_REG_DEVICE_ID = 0x1
  SCINTIL_HAL_VDAC_REG_CONFIG = 0x3
  SCINTIL_HAL_VDAC_REG_GAIN = 0x4
  SCINTIL_HAL_VDAC_REG_TRIGGER = 0x5
  SCINTIL_HAL_VDAC_REG_STATUS = 0x7
  SCINTIL_HAL_VDAC_REG_DAC0 = 0x8
  SCINTIL_HAL_VDAC_REG_DAC1 = 0x9
  SCINTIL_HAL_VDAC_REG_DAC2 = 0xa
  SCINTIL_HAL_VDAC_REG_DAC3 = 0xb
  SCINTIL_HAL_VDAC_REG_DAC4 = 0xc
  SCINTIL_HAL_VDAC_REG_DAC5 = 0xd
  SCINTIL_HAL_VDAC_REG_DAC6 = 0xe
  SCINTIL_HAL_VDAC_REG_DAC7 = 0xf


class hal_ll_vdac_reg_t (Enum):
  HAL_VDAC_REG_DEVICE_ID = 0x1
  HAL_VDAC_REG_CONFIG = 0x3
  HAL_VDAC_REG_GAIN = 0x4
  HAL_VDAC_REG_TRIGGER = 0x5
  HAL_VDAC_REG_STATUS = 0x7
  HAL_VDAC_REG_DAC0 = 0x8
  HAL_VDAC_REG_DAC1 = 0x9
  HAL_VDAC_REG_DAC2 = 0xa
  HAL_VDAC_REG_DAC3 = 0xb
  HAL_VDAC_REG_DAC4 = 0xc
  HAL_VDAC_REG_DAC5 = 0xd
  HAL_VDAC_REG_DAC6 = 0xe
  HAL_VDAC_REG_DAC7 = 0xf


class scintil_hal_cascade_t (Enum):
  CASCADE_NONE = 0x0
  CASCADE_BO = 0x1
  CASCADE_AO = 0x2
  CASCADE_BE = 0x3
  CASCADE_AE = 0x4
  CASCADE_UNKNOWN = 0x5


class hal_cascade_t (Enum):
  CASCADE_NONE = 0x0
  CASCADE_BO = 0x1
  CASCADE_AO = 0x2
  CASCADE_BE = 0x3
  CASCADE_AE = 0x4
  CASCADE_UNKNOWN = 0x5


class scintil_hal_stage_t (Enum):
  STAGE_1 = 0x0
  STAGE_2 = 0x1
  STAGE_3 = 0x2


class hal_stage_t (Enum):
  STAGE_1 = 0x0
  STAGE_2 = 0x1
  STAGE_3 = 0x2


class scintil_hal_node_t (Enum):
  NODE_1 = 0x0
  NODE_2 = 0x1
  NODE_3 = 0x2
  NODE_4 = 0x3


class hal_node_t (Enum):
  NODE_1 = 0x0
  NODE_2 = 0x1
  NODE_3 = 0x2
  NODE_4 = 0x3


class scintil_hal_module_t (Enum):
  MODULE_1 = 0x0
  MODULE_2 = 0x1


class hal_module_t (Enum):
  MODULE_1 = 0x0
  MODULE_2 = 0x1


class scintil_hal_error_bit_t (Flag):
  SCINTIL_HAL_ERROR_NONE = 0x0
  SCINTIL_HAL_ERROR_REGLIB_BAD_PARAMETER = 0x1
  SCINTIL_HAL_ERROR_REGLIB_UNINITIALIZED = 0x2
  SCINTIL_HAL_ERROR_REGLIB_PRIVATE_DATA_UNINITIALIZED = 0x4
  SCINTIL_HAL_ERROR_REGLIB_UNKNOWN = 0x8
  SCINTIL_HAL_ERROR_REGLIB_CHANNEL = 0x10
  SCINTIL_HAL_ERROR_INVALID_HANDLE = 0x10
  SCINTIL_HAL_ERROR_ALLOCATION = 0x20
  SCINTIL_HAL_ERROR_BAD_PARAMETER = 0x40
  SCINTIL_HAL_ERROR_CHANNEL = 0x80
  SCINTIL_HAL_ERROR_WRONG_ID = 0x100
  SCINTIL_HAL_ERROR_OTHER = 0x200
  SCINTIL_HAL_ERROR_UNKNOWN = 0x400
  SCINTIL_HAL_ERROR_NOT_SUPPORTED = 0x800
  SCINTIL_HAL_ERROR_NOT_IMPLEMENTED = 0x1000
  SCINTIL_HAL_ERROR_TIMEOUT = 0x2000
  SCINTIL_HAL_ERROR_INVALID_CLOCK_FREQUENCY = 0x4000
  SCINTIL_HAL_ERROR_INVALID_VALUE = 0x8000
  SCINTIL_HAL_ERROR_INVALID_DATA = 0x10000
  SCINTIL_HAL_ERROR_SUBSYSTEM_NOT_READY = 0x20000
  SCINTIL_HAL_ERROR_SLEEP_CALLBACK_NOT_SET = 0x40000
  SCINTIL_HAL_ERROR_FORBIDDEN = 0x80000
  SCINTIL_HAL_ERROR_INVALID_CONFIGURATION = 0x100000
  SCINTIL_HAL_ERROR_NOT_IN_REMOTE_API = 0x200000
  SCINTIL_HAL_ERROR_IN_RESET_STATE = 0x400000
  SCINTIL_HAL_ERROR_INCOMPLETE_DATA = 0x800000
  SCINTIL_HAL_ERROR_API = 0x1000000
  SCINTIL_HAL_ERROR_FIFO = 0x4000000


class hal_error_bit_t (Flag):
  HAL_ERROR_NONE = 0x0
  HAL_ERROR_REGLIB_BAD_PARAMETER = 0x1
  HAL_ERROR_REGLIB_UNINITIALIZED = 0x2
  HAL_ERROR_REGLIB_PRIVATE_DATA_UNINITIALIZED = 0x4
  HAL_ERROR_REGLIB_UNKNOWN = 0x8
  HAL_ERROR_REGLIB_CHANNEL = 0x10
  HAL_ERROR_INVALID_HANDLE = 0x10
  HAL_ERROR_ALLOCATION = 0x20
  HAL_ERROR_BAD_PARAMETER = 0x40
  HAL_ERROR_CHANNEL = 0x80
  HAL_ERROR_WRONG_ID = 0x100
  HAL_ERROR_OTHER = 0x200
  HAL_ERROR_UNKNOWN = 0x400
  HAL_ERROR_NOT_SUPPORTED = 0x800
  HAL_ERROR_NOT_IMPLEMENTED = 0x1000
  HAL_ERROR_TIMEOUT = 0x2000
  HAL_ERROR_INVALID_CLOCK_FREQUENCY = 0x4000
  HAL_ERROR_INVALID_VALUE = 0x8000
  HAL_ERROR_INVALID_DATA = 0x10000
  HAL_ERROR_SUBSYSTEM_NOT_READY = 0x20000
  HAL_ERROR_SLEEP_CALLBACK_NOT_SET = 0x40000
  HAL_ERROR_FORBIDDEN = 0x80000
  HAL_ERROR_INVALID_CONFIGURATION = 0x100000
  HAL_ERROR_NOT_IN_REMOTE_API = 0x200000
  HAL_ERROR_IN_RESET_STATE = 0x400000
  HAL_ERROR_INCOMPLETE_DATA = 0x800000
  HAL_ERROR_API = 0x1000000
  HAL_ERROR_FIFO = 0x4000000


class scintilreglib_autoinc_t (Enum):
  AUTOINCREMENT = 0x0
  NO_AUTOINCREMENT = 0x1


class scintilreglib_delay_t (Enum):
  ONE_BYTE_WAITSTATE = 0x0
  NO_WAITSTATE = 0x1


class scintil_hal_sys_reset_bit_t (Flag):
  RST_IDAC = 0x1
  RST_VDAC = 0x2
  RST_VPOLAR = 0x4
  RST_VLASER = 0x8
  RST_TEC = 0x10
  RST_TOP = 0xff


class hal_sys_reset_bit_t (Flag):
  RST_IDAC = 0x1
  RST_VDAC = 0x2
  RST_VPOLAR = 0x4
  RST_VLASER = 0x8
  RST_TEC = 0x10
  RST_TOP = 0xff


class scintil_hal_tunable_t (Enum):
  TUNABLE_CTRL_ENABLED_AT_STARTUP = 0x0
  TUNABLE_CTRL_COARSE_SEARCH_APPLY = 0x1
  TUNABLE_CTRL_INIT_VAL_PERCENT = 0x2
  TUNABLE_CTRL_COARSE_SEARCH_OFFSET_RANGE_PERCENT = 0x3
  TUNABLE_CTRL_DITHER_BASE_PERIOD_U16 = 0x4
  TUNABLE_CTRL_DITHER_PERIOD_INC_U16 = 0x5
  TUNABLE_CTRL_GAIN_U16 = 0x6
  TUNABLE_CTRL_SIM_HEATER_NOISE_U16 = 0x7
  TUNABLE_LAST = 0x8


class hal_tunable_t (Enum):
  TUNABLE_CTRL_ENABLED_AT_STARTUP = 0x0
  TUNABLE_CTRL_COARSE_SEARCH_APPLY = 0x1
  TUNABLE_CTRL_INIT_VAL_PERCENT = 0x2
  TUNABLE_CTRL_COARSE_SEARCH_OFFSET_RANGE_PERCENT = 0x3
  TUNABLE_CTRL_DITHER_BASE_PERIOD_U16 = 0x4
  TUNABLE_CTRL_DITHER_PERIOD_INC_U16 = 0x5
  TUNABLE_CTRL_GAIN_U16 = 0x6
  TUNABLE_CTRL_SIM_HEATER_NOISE_U16 = 0x7
  TUNABLE_LAST = 0x8


class scintil_hal_ll_tia_mux_out_t (Enum):
  SCINTIL_HAL_TIA_MUX_1 = 0x0
  SCINTIL_HAL_TIA_MUX_2 = 0x1
  SCINTIL_HAL_TIA_MUX_3 = 0x2
  SCINTIL_HAL_TIA_MUX_4 = 0x3
  SCINTIL_HAL_TIA_MUX_5 = 0x4
  SCINTIL_HAL_TIA_MUX_6 = 0x5
  SCINTIL_HAL_TIA_MUX_7 = 0x6
  SCINTIL_HAL_TIA_MUX_8 = 0x7
  SCINTIL_HAL_TIA_MUX_UNKNOWN = 0x8


class hal_ll_tia_mux_out_t (Enum):
  HAL_TIA_MUX_1 = 0x0
  HAL_TIA_MUX_2 = 0x1
  HAL_TIA_MUX_3 = 0x2
  HAL_TIA_MUX_4 = 0x3
  HAL_TIA_MUX_5 = 0x4
  HAL_TIA_MUX_6 = 0x5
  HAL_TIA_MUX_7 = 0x6
  HAL_TIA_MUX_8 = 0x7
  HAL_TIA_MUX_UNKNOWN = 0x8


class scintil_hal_ring_type_t (Enum):
  SCINTIL_HAL_RING_AC = 0x0
  SCINTIL_HAL_RING_DC = 0x1


class hal_ring_type_t (Enum):
  HAL_RING_AC = 0x0
  HAL_RING_DC = 0x1


class scintil_hal_ll_tia_ring_out_t (Enum):
  SCINTIL_HAL_TIA_RING_0 = 0x0
  SCINTIL_HAL_TIA_RING_1 = 0x1


class hal_ll_tia_ring_out_t (Enum):
  HAL_TIA_RING_0 = 0x0
  HAL_TIA_RING_1 = 0x1


class scintil_hal_ll_tia_laser_mpd_t (Enum):
  SCINTIL_HAL_TIA_LASER_MPD_1 = 0x0
  SCINTIL_HAL_TIA_LASER_MPD_2 = 0x1
  SCINTIL_HAL_TIA_LASER_MPD_3 = 0x2
  SCINTIL_HAL_TIA_LASER_MPD_4 = 0x3
  SCINTIL_HAL_TIA_LASER_MPD_5 = 0x4
  SCINTIL_HAL_TIA_LASER_MPD_6 = 0x5
  SCINTIL_HAL_TIA_LASER_MPD_7 = 0x6
  SCINTIL_HAL_TIA_LASER_MPD_8 = 0x7
  SCINTIL_HAL_TIA_LASER_MPD_9 = 0x8
  SCINTIL_HAL_TIA_LASER_MPD_10 = 0x9
  SCINTIL_HAL_TIA_LASER_MPD_11 = 0xa
  SCINTIL_HAL_TIA_LASER_MPD_12 = 0xb
  SCINTIL_HAL_TIA_LASER_MPD_13 = 0xc
  SCINTIL_HAL_TIA_LASER_MPD_14 = 0xd
  SCINTIL_HAL_TIA_LASER_MPD_15 = 0xe
  SCINTIL_HAL_TIA_LASER_MPD_16 = 0xf
  SCINTIL_HAL_TIA_LASER_MPD_17 = 0x10
  SCINTIL_HAL_TIA_LASER_MPD_18 = 0x11
  SCINTIL_HAL_TIA_LASER_MPD_19 = 0x12
  SCINTIL_HAL_TIA_LASER_MPD_20 = 0x13
  SCINTIL_HAL_TIA_LASER_MPD_21 = 0x14
  SCINTIL_HAL_TIA_LASER_MPD_22 = 0x15
  SCINTIL_HAL_TIA_LASER_MPD_23 = 0x16
  SCINTIL_HAL_TIA_LASER_MPD_24 = 0x17
  SCINTIL_HAL_TIA_LASER_MPD_25 = 0x18
  SCINTIL_HAL_TIA_LASER_MPD_26 = 0x19
  SCINTIL_HAL_TIA_LASER_MPD_27 = 0x1a
  SCINTIL_HAL_TIA_LASER_MPD_28 = 0x1b
  SCINTIL_HAL_TIA_LASER_MPD_29 = 0x1c
  SCINTIL_HAL_TIA_LASER_MPD_30 = 0x1d
  SCINTIL_HAL_TIA_LASER_MPD_31 = 0x1e
  SCINTIL_HAL_TIA_LASER_MPD_32 = 0x1f
  SCINTIL_HAL_TIA_LASER_MPD_UNKNOWN = 0x20


class hal_ll_tia_laser_mpd_t (Enum):
  HAL_TIA_LASER_MPD_1 = 0x0
  HAL_TIA_LASER_MPD_2 = 0x1
  HAL_TIA_LASER_MPD_3 = 0x2
  HAL_TIA_LASER_MPD_4 = 0x3
  HAL_TIA_LASER_MPD_5 = 0x4
  HAL_TIA_LASER_MPD_6 = 0x5
  HAL_TIA_LASER_MPD_7 = 0x6
  HAL_TIA_LASER_MPD_8 = 0x7
  HAL_TIA_LASER_MPD_9 = 0x8
  HAL_TIA_LASER_MPD_10 = 0x9
  HAL_TIA_LASER_MPD_11 = 0xa
  HAL_TIA_LASER_MPD_12 = 0xb
  HAL_TIA_LASER_MPD_13 = 0xc
  HAL_TIA_LASER_MPD_14 = 0xd
  HAL_TIA_LASER_MPD_15 = 0xe
  HAL_TIA_LASER_MPD_16 = 0xf
  HAL_TIA_LASER_MPD_17 = 0x10
  HAL_TIA_LASER_MPD_18 = 0x11
  HAL_TIA_LASER_MPD_19 = 0x12
  HAL_TIA_LASER_MPD_20 = 0x13
  HAL_TIA_LASER_MPD_21 = 0x14
  HAL_TIA_LASER_MPD_22 = 0x15
  HAL_TIA_LASER_MPD_23 = 0x16
  HAL_TIA_LASER_MPD_24 = 0x17
  HAL_TIA_LASER_MPD_25 = 0x18
  HAL_TIA_LASER_MPD_26 = 0x19
  HAL_TIA_LASER_MPD_27 = 0x1a
  HAL_TIA_LASER_MPD_28 = 0x1b
  HAL_TIA_LASER_MPD_29 = 0x1c
  HAL_TIA_LASER_MPD_30 = 0x1d
  HAL_TIA_LASER_MPD_31 = 0x1e
  HAL_TIA_LASER_MPD_32 = 0x1f
  HAL_TIA_LASER_MPD_UNKNOWN = 0x20


class scintil_hal_mpd_t (Enum):
  SCINTIL_HAL_MPD_P0 = 0x0
  SCINTIL_HAL_MPD_P1 = 0x1
  SCINTIL_HAL_MPD_P2 = 0x2
  SCINTIL_HAL_MPD_P3 = 0x3
  SCINTIL_HAL_MPD_P4 = 0x4
  SCINTIL_HAL_MPD_P5 = 0x5
  SCINTIL_HAL_MPD_P6 = 0x6
  SCINTIL_HAL_MPD_P7 = 0x7
  SCINTIL_HAL_MPD_P8 = 0x8
  SCINTIL_HAL_MPD_P9 = 0x9
  SCINTIL_HAL_MPD_P10 = 0xa
  SCINTIL_HAL_MPD_P11 = 0xb
  SCINTIL_HAL_MPD_P12 = 0xc
  SCINTIL_HAL_MPD_P13 = 0xd
  SCINTIL_HAL_MPD_P14 = 0xe
  SCINTIL_HAL_MPD_P15 = 0xf
  SCINTIL_HAL_MPD_AO = 0x10
  SCINTIL_HAL_MPD_BO = 0x11
  SCINTIL_HAL_MPD_AE = 0x12
  SCINTIL_HAL_MPD_BE = 0x13
  SCINTIL_HAL_MPD_LAST = 0x14


class hal_mpd_t (Enum):
  HAL_MPD_P0 = 0x0
  HAL_MPD_P1 = 0x1
  HAL_MPD_P2 = 0x2
  HAL_MPD_P3 = 0x3
  HAL_MPD_P4 = 0x4
  HAL_MPD_P5 = 0x5
  HAL_MPD_P6 = 0x6
  HAL_MPD_P7 = 0x7
  HAL_MPD_P8 = 0x8
  HAL_MPD_P9 = 0x9
  HAL_MPD_P10 = 0xa
  HAL_MPD_P11 = 0xb
  HAL_MPD_P12 = 0xc
  HAL_MPD_P13 = 0xd
  HAL_MPD_P14 = 0xe
  HAL_MPD_P15 = 0xf
  HAL_MPD_AO = 0x10
  HAL_MPD_BO = 0x11
  HAL_MPD_AE = 0x12
  HAL_MPD_BE = 0x13
  HAL_MPD_LAST = 0x14


class scintil_hal_laser_t (Enum):
  SCINTIL_HAL_LASER_0 = 0x0
  SCINTIL_HAL_LASER_1 = 0x1
  SCINTIL_HAL_LASER_2 = 0x2
  SCINTIL_HAL_LASER_3 = 0x3
  SCINTIL_HAL_LASER_4 = 0x4
  SCINTIL_HAL_LASER_5 = 0x5
  SCINTIL_HAL_LASER_6 = 0x6
  SCINTIL_HAL_LASER_7 = 0x7
  SCINTIL_HAL_LASER_8 = 0x8
  SCINTIL_HAL_LASER_9 = 0x9
  SCINTIL_HAL_LASER_10 = 0xa
  SCINTIL_HAL_LASER_11 = 0xb
  SCINTIL_HAL_LASER_12 = 0xc
  SCINTIL_HAL_LASER_13 = 0xd
  SCINTIL_HAL_LASER_14 = 0xe
  SCINTIL_HAL_LASER_15 = 0xf
  SCINTIL_HAL_LASER_ALL = 0x10


class hal_laser_t (Enum):
  HAL_LASER_0 = 0x0
  HAL_LASER_1 = 0x1
  HAL_LASER_2 = 0x2
  HAL_LASER_3 = 0x3
  HAL_LASER_4 = 0x4
  HAL_LASER_5 = 0x5
  HAL_LASER_6 = 0x6
  HAL_LASER_7 = 0x7
  HAL_LASER_8 = 0x8
  HAL_LASER_9 = 0x9
  HAL_LASER_10 = 0xa
  HAL_LASER_11 = 0xb
  HAL_LASER_12 = 0xc
  HAL_LASER_13 = 0xd
  HAL_LASER_14 = 0xe
  HAL_LASER_15 = 0xf
  HAL_LASER_ALL = 0x10


class scintil_hal_mux_heater_t (Enum):
  SCINTIL_HAL_MUX_HEATER_BO_s31 = 0x0
  SCINTIL_HAL_MUX_HEATER_BO_s33 = 0x1
  SCINTIL_HAL_MUX_HEATER_BO_s32 = 0x2
  SCINTIL_HAL_MUX_HEATER_BO_s34 = 0x3
  SCINTIL_HAL_MUX_HEATER_BO_s21 = 0x4
  SCINTIL_HAL_MUX_HEATER_BO_s22 = 0x5
  SCINTIL_HAL_MUX_HEATER_BO_s11 = 0x6
  SCINTIL_HAL_MUX_HEATER_AO_s31 = 0x7
  SCINTIL_HAL_MUX_HEATER_AO_s33 = 0x8
  SCINTIL_HAL_MUX_HEATER_AO_s32 = 0x9
  SCINTIL_HAL_MUX_HEATER_AO_s34 = 0xa
  SCINTIL_HAL_MUX_HEATER_AO_s21 = 0xb
  SCINTIL_HAL_MUX_HEATER_AO_s22 = 0xc
  SCINTIL_HAL_MUX_HEATER_AO_s11 = 0xd
  SCINTIL_HAL_MUX_HEATER_BE_s31 = 0xe
  SCINTIL_HAL_MUX_HEATER_BE_s33 = 0xf
  SCINTIL_HAL_MUX_HEATER_BE_s32 = 0x10
  SCINTIL_HAL_MUX_HEATER_BE_s34 = 0x11
  SCINTIL_HAL_MUX_HEATER_BE_s21 = 0x12
  SCINTIL_HAL_MUX_HEATER_BE_s22 = 0x13
  SCINTIL_HAL_MUX_HEATER_BE_s11 = 0x14
  SCINTIL_HAL_MUX_HEATER_AE_s31 = 0x15
  SCINTIL_HAL_MUX_HEATER_AE_s33 = 0x16
  SCINTIL_HAL_MUX_HEATER_AE_s32 = 0x17
  SCINTIL_HAL_MUX_HEATER_AE_s34 = 0x18
  SCINTIL_HAL_MUX_HEATER_AE_s21 = 0x19
  SCINTIL_HAL_MUX_HEATER_AE_s22 = 0x1a
  SCINTIL_HAL_MUX_HEATER_AE_s11 = 0x1b
  SCINTIL_HAL_MUX_HEATER_LAST = 0x1c
  SCINTIL_HAL_MUX_HEATER_UNKNOWN = 0x1d


class hal_mux_heater_t (Enum):
  HAL_MUX_HEATER_BO_s31 = 0x0
  HAL_MUX_HEATER_BO_s33 = 0x1
  HAL_MUX_HEATER_BO_s32 = 0x2
  HAL_MUX_HEATER_BO_s34 = 0x3
  HAL_MUX_HEATER_BO_s21 = 0x4
  HAL_MUX_HEATER_BO_s22 = 0x5
  HAL_MUX_HEATER_BO_s11 = 0x6
  HAL_MUX_HEATER_AO_s31 = 0x7
  HAL_MUX_HEATER_AO_s33 = 0x8
  HAL_MUX_HEATER_AO_s32 = 0x9
  HAL_MUX_HEATER_AO_s34 = 0xa
  HAL_MUX_HEATER_AO_s21 = 0xb
  HAL_MUX_HEATER_AO_s22 = 0xc
  HAL_MUX_HEATER_AO_s11 = 0xd
  HAL_MUX_HEATER_BE_s31 = 0xe
  HAL_MUX_HEATER_BE_s33 = 0xf
  HAL_MUX_HEATER_BE_s32 = 0x10
  HAL_MUX_HEATER_BE_s34 = 0x11
  HAL_MUX_HEATER_BE_s21 = 0x12
  HAL_MUX_HEATER_BE_s22 = 0x13
  HAL_MUX_HEATER_BE_s11 = 0x14
  HAL_MUX_HEATER_AE_s31 = 0x15
  HAL_MUX_HEATER_AE_s33 = 0x16
  HAL_MUX_HEATER_AE_s32 = 0x17
  HAL_MUX_HEATER_AE_s34 = 0x18
  HAL_MUX_HEATER_AE_s21 = 0x19
  HAL_MUX_HEATER_AE_s22 = 0x1a
  HAL_MUX_HEATER_AE_s11 = 0x1b
  HAL_MUX_HEATER_LAST = 0x1c
  HAL_MUX_HEATER_UNKNOWN = 0x1d


class scintil_hal_vpolar_out_t (Enum):
  SCINTIL_HAL_VPOLAR_OUT_LAS = 0x0
  SCINTIL_HAL_VPOLAR_OUT_RING = 0x1


class hal_vpolar_out_t (Enum):
  HAL_VPOLAR_OUT_LAS = 0x0
  HAL_VPOLAR_OUT_RING = 0x1


class scintil_hal_tec_instance_t (Enum):
  INSTANCE_1 = 0x1
  INSTANCE_2 = 0x2


class hal_tec_instance_t (Enum):
  INSTANCE_1 = 0x1
  INSTANCE_2 = 0x2


class scintil_hal_tec_object_source_t (Enum):
  HR_1 = 0x0
  HR_2 = 0x1
  LR_1 = 0x2
  LR_2 = 0x3
  LR_3 = 0x4
  LR_4 = 0x5


class hal_tec_object_source_t (Enum):
  HR_1 = 0x0
  HR_2 = 0x1
  LR_1 = 0x2
  LR_2 = 0x3
  LR_3 = 0x4
  LR_4 = 0x5


class scintil_hal_temp_t (Enum):
  SCINTIL_HAL_TEMPERATURE_PIC_1 = 0x0
  SCINTIL_HAL_TEMPERATURE_PIC_2 = 0x1
  SCINTIL_HAL_TEMPERATURE_MAINBOARD = 0x2
  SCINTIL_HAL_TEMPERATURE_INTERPOSER_1 = 0x3
  SCINTIL_HAL_TEMPERATURE_INTERPOSER_2 = 0x4


class hal_temp_t (Enum):
  HAL_TEMPERATURE_PIC_1 = 0x0
  HAL_TEMPERATURE_PIC_2 = 0x1
  HAL_TEMPERATURE_MAINBOARD = 0x2
  HAL_TEMPERATURE_INTERPOSER_1 = 0x3
  HAL_TEMPERATURE_INTERPOSER_2 = 0x4


class scintil_hal_temp_type_t (Enum):
  SCINTIL_HAL_TEMPERATURE_LOCAL = 0x0
  SCINTIL_HAL_TEMPERATURE_REMOTE = 0x1


class hal_temp_type_t (Enum):
  HAL_TEMPERATURE_LOCAL = 0x0
  HAL_TEMPERATURE_REMOTE = 0x1


class scintil_hal_threshold_type_t (Enum):
  THRESHOLD_MIN = 0x0
  THRESHOLD_MAX = 0x1


class hal_threshold_type_t (Enum):
  THRESHOLD_MIN = 0x0
  THRESHOLD_MAX = 0x1


class scintil_hal_threshold_channel_t (Enum):
  INTERPOSER = 0x0
  TEC_HEATSINK = 0x1
  TEC_COLD = 0x2


class hal_threshold_channel_t (Enum):
  INTERPOSER = 0x0
  TEC_HEATSINK = 0x1
  TEC_COLD = 0x2



# Struct scintil_hal_sys_status_t found in scintil_hal_sys.h
class scintil_hal_sys_status_t:
  def __init__(self, chip_id: int,eco: int,cut: int,tag: int,week: int,year: int,wpe: float):
    self.chip_id = chip_id
    self.eco = eco
    self.cut = cut
    self.tag = tag
    self.week = week
    self.year = year
    self.wpe = wpe

  @classmethod
  def fromstring(cls, braced_string):
    if braced_string.startswith('{') and braced_string.endswith('}'):
      stripped_string = braced_string.strip('{}')
      values = stripped_string.split(',')
      if len(values) != 7:
        raise ValueError(f'Wrong number of tokens in init string "{braced_string}", got ' + str(len(values)) + ' expected 7')
    else:
      raise ValueError('Malformed init string "'+ braced_string + '": missing {braces}')
    return cls(int(values[0]),int(values[1]),int(values[2]),int(values[3]),int(values[4]),int(values[5]),float(values[6])) 

  def __str__(self):
    output = '{'
    output += str(self.chip_id) + ","
    output += str(self.eco) + ","
    output += str(self.cut) + ","
    output += str(self.tag) + ","
    output += str(self.week) + ","
    output += str(self.year) + ","
    output += str(self.wpe)
    output += "}"
    return output

  def __repr__(self):
    output = 'scintil_hal_sys_status_t('
    output += "chip_id=" + str(self.chip_id) + ","
    output += "eco=" + str(self.eco) + ","
    output += "cut=" + str(self.cut) + ","
    output += "tag=" + str(self.tag) + ","
    output += "week=" + str(self.week) + ","
    output += "year=" + str(self.year) + ","
    output += "wpe=" + str(self.wpe)
    output += ")"
    return output
  def  to_dict(self):
    return {key: value for key, value in self.__dict__.items()}

# Struct scintil_hal_sys_sw_version_t found in scintil_hal_sys.h
class scintil_hal_sys_sw_version_t:
  def __init__(self, major: int,minor: int,patch: int):
    self.major = major
    self.minor = minor
    self.patch = patch

  @classmethod
  def fromstring(cls, braced_string):
    if braced_string.startswith('{') and braced_string.endswith('}'):
      stripped_string = braced_string.strip('{}')
      values = stripped_string.split(',')
      if len(values) != 3:
        raise ValueError(f'Wrong number of tokens in init string "{braced_string}", got ' + str(len(values)) + ' expected 3')
    else:
      raise ValueError('Malformed init string "'+ braced_string + '": missing {braces}')
    return cls(int(values[0]),int(values[1]),int(values[2])) 

  def __str__(self):
    output = '{'
    output += str(self.major) + ","
    output += str(self.minor) + ","
    output += str(self.patch)
    output += "}"
    return output

  def __repr__(self):
    output = 'scintil_hal_sys_sw_version_t('
    output += "major=" + str(self.major) + ","
    output += "minor=" + str(self.minor) + ","
    output += "patch=" + str(self.patch)
    output += ")"
    return output
  def  to_dict(self):
    return {key: value for key, value in self.__dict__.items()}

# Struct scintil_hal_sys_fpga_version_t found in scintil_hal_sys.h
class scintil_hal_sys_fpga_version_t:
  def __init__(self, year: int,month: int,day: int,hour: int,minute: int):
    self.year = year
    self.month = month
    self.day = day
    self.hour = hour
    self.minute = minute

  @classmethod
  def fromstring(cls, braced_string):
    if braced_string.startswith('{') and braced_string.endswith('}'):
      stripped_string = braced_string.strip('{}')
      values = stripped_string.split(',')
      if len(values) != 5:
        raise ValueError(f'Wrong number of tokens in init string "{braced_string}", got ' + str(len(values)) + ' expected 5')
    else:
      raise ValueError('Malformed init string "'+ braced_string + '": missing {braces}')
    return cls(int(values[0]),int(values[1]),int(values[2]),int(values[3]),int(values[4])) 

  def __str__(self):
    output = '{'
    output += str(self.year) + ","
    output += str(self.month) + ","
    output += str(self.day) + ","
    output += str(self.hour) + ","
    output += str(self.minute)
    output += "}"
    return output

  def __repr__(self):
    output = 'scintil_hal_sys_fpga_version_t('
    output += "year=" + str(self.year) + ","
    output += "month=" + str(self.month) + ","
    output += "day=" + str(self.day) + ","
    output += "hour=" + str(self.hour) + ","
    output += "minute=" + str(self.minute)
    output += ")"
    return output
  def  to_dict(self):
    return {key: value for key, value in self.__dict__.items()}

# Struct scintil_hal_controller_context_t found in scintil_hal_controller.h
class scintil_hal_controller_context_t:
  def __init__(self, controller_k: int,controller_dt: float,controller_gain: float,controller_t: float,controller_lpf_alpha: float,controller_hpf_alpha: float,controller_eff_hpf: float,controller_efficiency: float,u_base_0: float,v_0: float,v_optimal_0: float,period_drift_0: float,period_drift_rate_0: float,phase_drift_0: float,phase_drift_rate_0: float,u_base_1: float,v_1: float,v_optimal_1: float,period_drift_1: float,period_drift_rate_1: float,phase_drift_1: float,phase_drift_rate_1: float,u_base_2: float,v_2: float,v_optimal_2: float,period_drift_2: float,period_drift_rate_2: float,phase_drift_2: float,phase_drift_rate_2: float,u_base_3: float,v_3: float,v_optimal_3: float,period_drift_3: float,period_drift_rate_3: float,phase_drift_3: float,phase_drift_rate_3: float,u_base_4: float,v_4: float,v_optimal_4: float,period_drift_4: float,period_drift_rate_4: float,phase_drift_4: float,phase_drift_rate_4: float,u_base_5: float,v_5: float,v_optimal_5: float,period_drift_5: float,period_drift_rate_5: float,phase_drift_5: float,phase_drift_rate_5: float,u_base_6: float,v_6: float,v_optimal_6: float,period_drift_6: float,period_drift_rate_6: float,phase_drift_6: float,phase_drift_rate_6: float,time_step: int,step_interval: int):
    self.controller_k = controller_k
    self.controller_dt = controller_dt
    self.controller_gain = controller_gain
    self.controller_t = controller_t
    self.controller_lpf_alpha = controller_lpf_alpha
    self.controller_hpf_alpha = controller_hpf_alpha
    self.controller_eff_hpf = controller_eff_hpf
    self.controller_efficiency = controller_efficiency
    self.u_base_0 = u_base_0
    self.v_0 = v_0
    self.v_optimal_0 = v_optimal_0
    self.period_drift_0 = period_drift_0
    self.period_drift_rate_0 = period_drift_rate_0
    self.phase_drift_0 = phase_drift_0
    self.phase_drift_rate_0 = phase_drift_rate_0
    self.u_base_1 = u_base_1
    self.v_1 = v_1
    self.v_optimal_1 = v_optimal_1
    self.period_drift_1 = period_drift_1
    self.period_drift_rate_1 = period_drift_rate_1
    self.phase_drift_1 = phase_drift_1
    self.phase_drift_rate_1 = phase_drift_rate_1
    self.u_base_2 = u_base_2
    self.v_2 = v_2
    self.v_optimal_2 = v_optimal_2
    self.period_drift_2 = period_drift_2
    self.period_drift_rate_2 = period_drift_rate_2
    self.phase_drift_2 = phase_drift_2
    self.phase_drift_rate_2 = phase_drift_rate_2
    self.u_base_3 = u_base_3
    self.v_3 = v_3
    self.v_optimal_3 = v_optimal_3
    self.period_drift_3 = period_drift_3
    self.period_drift_rate_3 = period_drift_rate_3
    self.phase_drift_3 = phase_drift_3
    self.phase_drift_rate_3 = phase_drift_rate_3
    self.u_base_4 = u_base_4
    self.v_4 = v_4
    self.v_optimal_4 = v_optimal_4
    self.period_drift_4 = period_drift_4
    self.period_drift_rate_4 = period_drift_rate_4
    self.phase_drift_4 = phase_drift_4
    self.phase_drift_rate_4 = phase_drift_rate_4
    self.u_base_5 = u_base_5
    self.v_5 = v_5
    self.v_optimal_5 = v_optimal_5
    self.period_drift_5 = period_drift_5
    self.period_drift_rate_5 = period_drift_rate_5
    self.phase_drift_5 = phase_drift_5
    self.phase_drift_rate_5 = phase_drift_rate_5
    self.u_base_6 = u_base_6
    self.v_6 = v_6
    self.v_optimal_6 = v_optimal_6
    self.period_drift_6 = period_drift_6
    self.period_drift_rate_6 = period_drift_rate_6
    self.phase_drift_6 = phase_drift_6
    self.phase_drift_rate_6 = phase_drift_rate_6
    self.time_step = time_step
    self.step_interval = step_interval

  @classmethod
  def fromstring(cls, braced_string):
    if braced_string.startswith('{') and braced_string.endswith('}'):
      stripped_string = braced_string.strip('{}')
      values = stripped_string.split(',')
      if len(values) != 59:
        raise ValueError(f'Wrong number of tokens in init string "{braced_string}", got ' + str(len(values)) + ' expected 59')
    else:
      raise ValueError('Malformed init string "'+ braced_string + '": missing {braces}')
    return cls(int(values[0]),float(values[1]),float(values[2]),float(values[3]),float(values[4]),float(values[5]),float(values[6]),float(values[7]),float(values[8]),float(values[9]),float(values[10]),float(values[11]),float(values[12]),float(values[13]),float(values[14]),float(values[15]),float(values[16]),float(values[17]),float(values[18]),float(values[19]),float(values[20]),float(values[21]),float(values[22]),float(values[23]),float(values[24]),float(values[25]),float(values[26]),float(values[27]),float(values[28]),float(values[29]),float(values[30]),float(values[31]),float(values[32]),float(values[33]),float(values[34]),float(values[35]),float(values[36]),float(values[37]),float(values[38]),float(values[39]),float(values[40]),float(values[41]),float(values[42]),float(values[43]),float(values[44]),float(values[45]),float(values[46]),float(values[47]),float(values[48]),float(values[49]),float(values[50]),float(values[51]),float(values[52]),float(values[53]),float(values[54]),float(values[55]),float(values[56]),int(values[57]),int(values[58])) 

  def __str__(self):
    output = '{'
    output += str(self.controller_k) + ","
    output += str(self.controller_dt) + ","
    output += str(self.controller_gain) + ","
    output += str(self.controller_t) + ","
    output += str(self.controller_lpf_alpha) + ","
    output += str(self.controller_hpf_alpha) + ","
    output += str(self.controller_eff_hpf) + ","
    output += str(self.controller_efficiency) + ","
    output += str(self.u_base_0) + ","
    output += str(self.v_0) + ","
    output += str(self.v_optimal_0) + ","
    output += str(self.period_drift_0) + ","
    output += str(self.period_drift_rate_0) + ","
    output += str(self.phase_drift_0) + ","
    output += str(self.phase_drift_rate_0) + ","
    output += str(self.u_base_1) + ","
    output += str(self.v_1) + ","
    output += str(self.v_optimal_1) + ","
    output += str(self.period_drift_1) + ","
    output += str(self.period_drift_rate_1) + ","
    output += str(self.phase_drift_1) + ","
    output += str(self.phase_drift_rate_1) + ","
    output += str(self.u_base_2) + ","
    output += str(self.v_2) + ","
    output += str(self.v_optimal_2) + ","
    output += str(self.period_drift_2) + ","
    output += str(self.period_drift_rate_2) + ","
    output += str(self.phase_drift_2) + ","
    output += str(self.phase_drift_rate_2) + ","
    output += str(self.u_base_3) + ","
    output += str(self.v_3) + ","
    output += str(self.v_optimal_3) + ","
    output += str(self.period_drift_3) + ","
    output += str(self.period_drift_rate_3) + ","
    output += str(self.phase_drift_3) + ","
    output += str(self.phase_drift_rate_3) + ","
    output += str(self.u_base_4) + ","
    output += str(self.v_4) + ","
    output += str(self.v_optimal_4) + ","
    output += str(self.period_drift_4) + ","
    output += str(self.period_drift_rate_4) + ","
    output += str(self.phase_drift_4) + ","
    output += str(self.phase_drift_rate_4) + ","
    output += str(self.u_base_5) + ","
    output += str(self.v_5) + ","
    output += str(self.v_optimal_5) + ","
    output += str(self.period_drift_5) + ","
    output += str(self.period_drift_rate_5) + ","
    output += str(self.phase_drift_5) + ","
    output += str(self.phase_drift_rate_5) + ","
    output += str(self.u_base_6) + ","
    output += str(self.v_6) + ","
    output += str(self.v_optimal_6) + ","
    output += str(self.period_drift_6) + ","
    output += str(self.period_drift_rate_6) + ","
    output += str(self.phase_drift_6) + ","
    output += str(self.phase_drift_rate_6) + ","
    output += str(self.time_step) + ","
    output += str(self.step_interval)
    output += "}"
    return output

  def __repr__(self):
    output = 'scintil_hal_controller_context_t('
    output += "controller_k=" + str(self.controller_k) + ","
    output += "controller_dt=" + str(self.controller_dt) + ","
    output += "controller_gain=" + str(self.controller_gain) + ","
    output += "controller_t=" + str(self.controller_t) + ","
    output += "controller_lpf_alpha=" + str(self.controller_lpf_alpha) + ","
    output += "controller_hpf_alpha=" + str(self.controller_hpf_alpha) + ","
    output += "controller_eff_hpf=" + str(self.controller_eff_hpf) + ","
    output += "controller_efficiency=" + str(self.controller_efficiency) + ","
    output += "u_base_0=" + str(self.u_base_0) + ","
    output += "v_0=" + str(self.v_0) + ","
    output += "v_optimal_0=" + str(self.v_optimal_0) + ","
    output += "period_drift_0=" + str(self.period_drift_0) + ","
    output += "period_drift_rate_0=" + str(self.period_drift_rate_0) + ","
    output += "phase_drift_0=" + str(self.phase_drift_0) + ","
    output += "phase_drift_rate_0=" + str(self.phase_drift_rate_0) + ","
    output += "u_base_1=" + str(self.u_base_1) + ","
    output += "v_1=" + str(self.v_1) + ","
    output += "v_optimal_1=" + str(self.v_optimal_1) + ","
    output += "period_drift_1=" + str(self.period_drift_1) + ","
    output += "period_drift_rate_1=" + str(self.period_drift_rate_1) + ","
    output += "phase_drift_1=" + str(self.phase_drift_1) + ","
    output += "phase_drift_rate_1=" + str(self.phase_drift_rate_1) + ","
    output += "u_base_2=" + str(self.u_base_2) + ","
    output += "v_2=" + str(self.v_2) + ","
    output += "v_optimal_2=" + str(self.v_optimal_2) + ","
    output += "period_drift_2=" + str(self.period_drift_2) + ","
    output += "period_drift_rate_2=" + str(self.period_drift_rate_2) + ","
    output += "phase_drift_2=" + str(self.phase_drift_2) + ","
    output += "phase_drift_rate_2=" + str(self.phase_drift_rate_2) + ","
    output += "u_base_3=" + str(self.u_base_3) + ","
    output += "v_3=" + str(self.v_3) + ","
    output += "v_optimal_3=" + str(self.v_optimal_3) + ","
    output += "period_drift_3=" + str(self.period_drift_3) + ","
    output += "period_drift_rate_3=" + str(self.period_drift_rate_3) + ","
    output += "phase_drift_3=" + str(self.phase_drift_3) + ","
    output += "phase_drift_rate_3=" + str(self.phase_drift_rate_3) + ","
    output += "u_base_4=" + str(self.u_base_4) + ","
    output += "v_4=" + str(self.v_4) + ","
    output += "v_optimal_4=" + str(self.v_optimal_4) + ","
    output += "period_drift_4=" + str(self.period_drift_4) + ","
    output += "period_drift_rate_4=" + str(self.period_drift_rate_4) + ","
    output += "phase_drift_4=" + str(self.phase_drift_4) + ","
    output += "phase_drift_rate_4=" + str(self.phase_drift_rate_4) + ","
    output += "u_base_5=" + str(self.u_base_5) + ","
    output += "v_5=" + str(self.v_5) + ","
    output += "v_optimal_5=" + str(self.v_optimal_5) + ","
    output += "period_drift_5=" + str(self.period_drift_5) + ","
    output += "period_drift_rate_5=" + str(self.period_drift_rate_5) + ","
    output += "phase_drift_5=" + str(self.phase_drift_5) + ","
    output += "phase_drift_rate_5=" + str(self.phase_drift_rate_5) + ","
    output += "u_base_6=" + str(self.u_base_6) + ","
    output += "v_6=" + str(self.v_6) + ","
    output += "v_optimal_6=" + str(self.v_optimal_6) + ","
    output += "period_drift_6=" + str(self.period_drift_6) + ","
    output += "period_drift_rate_6=" + str(self.period_drift_rate_6) + ","
    output += "phase_drift_6=" + str(self.phase_drift_6) + ","
    output += "phase_drift_rate_6=" + str(self.phase_drift_rate_6) + ","
    output += "time_step=" + str(self.time_step) + ","
    output += "step_interval=" + str(self.step_interval)
    output += ")"
    return output
  def  to_dict(self):
    return {key: value for key, value in self.__dict__.items()}

# Struct heater_setpoint_t found in scintil_hal_controller.h
class heater_setpoint_t:
  def __init__(self, index: int,v_optimal: float):
    self.index = index
    self.v_optimal = v_optimal

  @classmethod
  def fromstring(cls, braced_string):
    if braced_string.startswith('{') and braced_string.endswith('}'):
      stripped_string = braced_string.strip('{}')
      values = stripped_string.split(',')
      if len(values) != 2:
        raise ValueError(f'Wrong number of tokens in init string "{braced_string}", got ' + str(len(values)) + ' expected 2')
    else:
      raise ValueError('Malformed init string "'+ braced_string + '": missing {braces}')
    return cls(int(values[0]),float(values[1])) 

  def __str__(self):
    output = '{'
    output += str(self.index) + ","
    output += str(self.v_optimal)
    output += "}"
    return output

  def __repr__(self):
    output = 'heater_setpoint_t('
    output += "index=" + str(self.index) + ","
    output += "v_optimal=" + str(self.v_optimal)
    output += ")"
    return output
  def  to_dict(self):
    return {key: value for key, value in self.__dict__.items()}

# Struct scintil_hal_servoloop_laser_t found in scintil_hal_config.h
class scintil_hal_servoloop_laser_t:
  def __init__(self, i_setting: float,d_amplitude: float,d_frequency: int,i_start: float,i_stop: float,i_step: float,fine_istep: float):
    self.i_setting = i_setting
    self.d_amplitude = d_amplitude
    self.d_frequency = d_frequency
    self.i_start = i_start
    self.i_stop = i_stop
    self.i_step = i_step
    self.fine_istep = fine_istep

  @classmethod
  def fromstring(cls, braced_string):
    if braced_string.startswith('{') and braced_string.endswith('}'):
      stripped_string = braced_string.strip('{}')
      values = stripped_string.split(',')
      if len(values) != 7:
        raise ValueError(f'Wrong number of tokens in init string "{braced_string}", got ' + str(len(values)) + ' expected 7')
    else:
      raise ValueError('Malformed init string "'+ braced_string + '": missing {braces}')
    return cls(float(values[0]),float(values[1]),int(values[2]),float(values[3]),float(values[4]),float(values[5]),float(values[6])) 

  def __str__(self):
    output = '{'
    output += str(self.i_setting) + ","
    output += str(self.d_amplitude) + ","
    output += str(self.d_frequency) + ","
    output += str(self.i_start) + ","
    output += str(self.i_stop) + ","
    output += str(self.i_step) + ","
    output += str(self.fine_istep)
    output += "}"
    return output

  def __repr__(self):
    output = 'scintil_hal_servoloop_laser_t('
    output += "i_setting=" + str(self.i_setting) + ","
    output += "d_amplitude=" + str(self.d_amplitude) + ","
    output += "d_frequency=" + str(self.d_frequency) + ","
    output += "i_start=" + str(self.i_start) + ","
    output += "i_stop=" + str(self.i_stop) + ","
    output += "i_step=" + str(self.i_step) + ","
    output += "fine_istep=" + str(self.fine_istep)
    output += ")"
    return output
  def  to_dict(self):
    return {key: value for key, value in self.__dict__.items()}

# Struct scintil_hal_servoloop_heater_t found in scintil_hal_config.h
class scintil_hal_servoloop_heater_t:
  def __init__(self, v_init: float,tune_vstart: float,tune_vstop: float,tune_nsteps: int,servoloop_vstep: float,tab_crit_lock_mux: float):
    self.v_init = v_init
    self.tune_vstart = tune_vstart
    self.tune_vstop = tune_vstop
    self.tune_nsteps = tune_nsteps
    self.servoloop_vstep = servoloop_vstep
    self.tab_crit_lock_mux = tab_crit_lock_mux

  @classmethod
  def fromstring(cls, braced_string):
    if braced_string.startswith('{') and braced_string.endswith('}'):
      stripped_string = braced_string.strip('{}')
      values = stripped_string.split(',')
      if len(values) != 6:
        raise ValueError(f'Wrong number of tokens in init string "{braced_string}", got ' + str(len(values)) + ' expected 6')
    else:
      raise ValueError('Malformed init string "'+ braced_string + '": missing {braces}')
    return cls(float(values[0]),float(values[1]),float(values[2]),int(values[3]),float(values[4]),float(values[5])) 

  def __str__(self):
    output = '{'
    output += str(self.v_init) + ","
    output += str(self.tune_vstart) + ","
    output += str(self.tune_vstop) + ","
    output += str(self.tune_nsteps) + ","
    output += str(self.servoloop_vstep) + ","
    output += str(self.tab_crit_lock_mux)
    output += "}"
    return output

  def __repr__(self):
    output = 'scintil_hal_servoloop_heater_t('
    output += "v_init=" + str(self.v_init) + ","
    output += "tune_vstart=" + str(self.tune_vstart) + ","
    output += "tune_vstop=" + str(self.tune_vstop) + ","
    output += "tune_nsteps=" + str(self.tune_nsteps) + ","
    output += "servoloop_vstep=" + str(self.servoloop_vstep) + ","
    output += "tab_crit_lock_mux=" + str(self.tab_crit_lock_mux)
    output += ")"
    return output
  def  to_dict(self):
    return {key: value for key, value in self.__dict__.items()}

# Struct scintil_hal_servoloop_ring_t found in scintil_hal_config.h
class scintil_hal_servoloop_ring_t:
  def __init__(self, vring_init: float,tune_vstart: float,tune_vstop: float,tune_nsteps: int,fine_vstep: float,RING_STEP_THRESHOLD: float,RING_FINE_TUNING_MAX_TRIES: int):
    self.vring_init = vring_init
    self.tune_vstart = tune_vstart
    self.tune_vstop = tune_vstop
    self.tune_nsteps = tune_nsteps
    self.fine_vstep = fine_vstep
    self.RING_STEP_THRESHOLD = RING_STEP_THRESHOLD
    self.RING_FINE_TUNING_MAX_TRIES = RING_FINE_TUNING_MAX_TRIES

  @classmethod
  def fromstring(cls, braced_string):
    if braced_string.startswith('{') and braced_string.endswith('}'):
      stripped_string = braced_string.strip('{}')
      values = stripped_string.split(',')
      if len(values) != 7:
        raise ValueError(f'Wrong number of tokens in init string "{braced_string}", got ' + str(len(values)) + ' expected 7')
    else:
      raise ValueError('Malformed init string "'+ braced_string + '": missing {braces}')
    return cls(float(values[0]),float(values[1]),float(values[2]),int(values[3]),float(values[4]),float(values[5]),int(values[6])) 

  def __str__(self):
    output = '{'
    output += str(self.vring_init) + ","
    output += str(self.tune_vstart) + ","
    output += str(self.tune_vstop) + ","
    output += str(self.tune_nsteps) + ","
    output += str(self.fine_vstep) + ","
    output += str(self.RING_STEP_THRESHOLD) + ","
    output += str(self.RING_FINE_TUNING_MAX_TRIES)
    output += "}"
    return output

  def __repr__(self):
    output = 'scintil_hal_servoloop_ring_t('
    output += "vring_init=" + str(self.vring_init) + ","
    output += "tune_vstart=" + str(self.tune_vstart) + ","
    output += "tune_vstop=" + str(self.tune_vstop) + ","
    output += "tune_nsteps=" + str(self.tune_nsteps) + ","
    output += "fine_vstep=" + str(self.fine_vstep) + ","
    output += "RING_STEP_THRESHOLD=" + str(self.RING_STEP_THRESHOLD) + ","
    output += "RING_FINE_TUNING_MAX_TRIES=" + str(self.RING_FINE_TUNING_MAX_TRIES)
    output += ")"
    return output
  def  to_dict(self):
    return {key: value for key, value in self.__dict__.items()}

# Struct scintil_hal_servoloop_common_t found in scintil_hal_config.h
class scintil_hal_servoloop_common_t:
  def __init__(self, vpolar_las_init: float,vpolar_ring_init: float,temp_stability_diff: float,temp_stability_timeout: int,laser_fine_tuning_max_tries: int):
    self.vpolar_las_init = vpolar_las_init
    self.vpolar_ring_init = vpolar_ring_init
    self.temp_stability_diff = temp_stability_diff
    self.temp_stability_timeout = temp_stability_timeout
    self.laser_fine_tuning_max_tries = laser_fine_tuning_max_tries

  @classmethod
  def fromstring(cls, braced_string):
    if braced_string.startswith('{') and braced_string.endswith('}'):
      stripped_string = braced_string.strip('{}')
      values = stripped_string.split(',')
      if len(values) != 5:
        raise ValueError(f'Wrong number of tokens in init string "{braced_string}", got ' + str(len(values)) + ' expected 5')
    else:
      raise ValueError('Malformed init string "'+ braced_string + '": missing {braces}')
    return cls(float(values[0]),float(values[1]),float(values[2]),int(values[3]),int(values[4])) 

  def __str__(self):
    output = '{'
    output += str(self.vpolar_las_init) + ","
    output += str(self.vpolar_ring_init) + ","
    output += str(self.temp_stability_diff) + ","
    output += str(self.temp_stability_timeout) + ","
    output += str(self.laser_fine_tuning_max_tries)
    output += "}"
    return output

  def __repr__(self):
    output = 'scintil_hal_servoloop_common_t('
    output += "vpolar_las_init=" + str(self.vpolar_las_init) + ","
    output += "vpolar_ring_init=" + str(self.vpolar_ring_init) + ","
    output += "temp_stability_diff=" + str(self.temp_stability_diff) + ","
    output += "temp_stability_timeout=" + str(self.temp_stability_timeout) + ","
    output += "laser_fine_tuning_max_tries=" + str(self.laser_fine_tuning_max_tries)
    output += ")"
    return output
  def  to_dict(self):
    return {key: value for key, value in self.__dict__.items()}

class ScintilError(Exception):
  """Exception raised for Scintil HAL calls errors.
  Attributes:
      errcode -- Scintil error code
      output_params -- Scintil error code
  """
  def __init__(self, errcode=scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN, output_params={"errcode":scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN}):
      self.errcode = errcode
      self.output_params = output_params
      super().__init__("SCINTIL error : " + errcode.name + " -- " + output_params["err_str"])

class ScintilHAL:
  def __init__(self, server='127.0.0.1', port=80, timestamp=True, file=None, loglevel=logging.INFO, token=None, strictversion=False, strictcutversion=True, stricthwversion=False, delegate=True):
    self.server = server
    self.port = port
    self.token = token
    self.shouldraise = False
    self.disconnected = False
    self.halversion = "0.9.18"
    self.halversion_num = "9018"
    self.cut = 1
    self.isFPGA = False
    self.apihash = "b41aa68f7718"
    self.delegate = True
    if timestamp:
      tsformat = '[%(asctime)s] '
    else:
      tsformat = ''
    logging.basicConfig(level=loglevel, format= tsformat + '%(levelname)s: %(message)s')
    if file:
      logging.info(f'Logging to file : {file}')
      logging.basicConfig(file=file)
    
    request = f'http://{self.server}:{self.port}/lockstate'
    logging.debug(f'Request : {request}')
    try:
      response = requests.get(request)
      self.lockstate = json.loads(response.text)
      if (self.lockstate['state'] != 'LOCK_AVAILABLE'):
        logging.info(f'LOCK IS HELD : !')
        logging.info(pprint.pformat(self.lockstate))
    except requests.exceptions.RequestException as e:
      logging.exception(f'Could not retrieve lock state from {self.server}:{self.port}!')
      if (self.shouldraise):
         raise ScintilError(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL, {})
      else:
         self.disconnected = True
    request = f'http://{self.server}:{self.port}/halapi/version'
    if self.token:
      request += f'?lock-token=' + self.token
    logging.debug(f'Request : {request}')
    try:
      response = requests.get(request)
      self.serverversion = response.text
      if ({response.text} != {self.halversion}):
        if (strictversion):
          logging.error(f'STRICT MODE: API VERSION MISMATCH ! local:{self.halversion} remote:{response.text}')
          sys.exit(1)
        else:
          logging.warning(f'API VERSION MISMATCH ! local:{self.halversion} remote:{response.text}')
      else:
        logging.info(f'Remote api version : {response.text} local version : {self.halversion}')
    except requests.exceptions.RequestException as e:
      logging.exception('Could not retrieve remote API version !')
      if (self.shouldraise):
         raise ScintilError(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL, {})
      else:
         self.disconnected = True
    request = f'http://{self.server}:{self.port}/halapi/cut'
    if self.token:
      request += f'?lock-token=' + self.token
    logging.debug(f'Request : {request}')
    try:
      response = requests.get(request)
      self.servercut = response.text
      if ({int(response.text)} != {int(self.cut)}):
        if (strictcutversion):
          logging.error(f'STRICT MODE: CUT VERSION MISMATCH ! local:{self.cut} remote:{self.servercut}')
          sys.exit(1)
        else:
          logging.warning(f'CUT VERSION MISMATCH ! local:{self.cut} remote:{self.servercut}')
      else:
        logging.info(f'Remote cut : {self.servercut} - local build cut : {self.cut}')
    except requests.exceptions.RequestException as e:
      logging.exception('Could not retrieve remote HW cut !')
      if (self.shouldraise):
         raise ScintilError(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL, {})
      else:
         self.disconnected = True
    request = f'http://{self.server}:{self.port}/halapi/fpga'
    if self.token:
      request += f'?lock-token=' + self.token
    logging.debug(f'Request : {request}')
    try:
      response = requests.get(request)
      if response.text:
         self.serverIsFPGA = bool(int(response.text))
      else:
         self.serverIsFPGA = None
      if ({self.serverIsFPGA} != {self.isFPGA}):
        if (stricthwversion):
          logging.error(f'STRICT MODE: HW TARGET MISMATCH ! local:fpga={self.isFPGA} remote:{self.serverIsFPGA}')
          sys.exit(1)
        else:
          logging.warning(f'HW VERSION MISMATCH ! local:{self.fpga} remote:{response.serverIsFPGA}')
      else:
        logging.info(f'Remote hw target is FPGA: {self.serverIsFPGA} - local build is for FPGA: {self.isFPGA}')
    except requests.exceptions.RequestException as e:
      logging.exception('Could not retrieve remote HW build type !')
      if (self.shouldraise):
         raise ScintilError(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL, {})
      else:
         self.disconnected = True

  def setToken(self, token):
    self.token = token

  def getErrorString(self, err):
    if err == 0:
        return "SCINTIL_HAL_ERROR_NONE"
    errorstring = ""
    for _enum in scintil_hal_error_bit_t:
        if (err & _enum.value):
            errorstring += _enum.name + "|"
    errorstring = errorstring.rstrip("|")
    return errorstring


  def scintil_hal_sys_check_id(self):
    # 0 input arguments
    # 1 output arguments
    output_params = {}
    request = f"http://{self.server}:{self.port}/hal{'delegate' if self.delegate else ''}/scintil_hal_sys_check_id"
    if self.token:
      request += f"?lock-token=" + self.token
    logging.debug("Request : " + request)
    try:
      response = requests.get(request)
      #output_params['response'] = response.text
      logging.debug("Response : " + response.text)
      err_match = re.match(r'.*\nerr=(0x\S+)\n.*', response.text, flags=re.DOTALL)
      err_api_match = re.match(r'(Invalid method.*)', response.text, flags=re.DOTALL)
      output_params['status_code'] = response.status_code
      if err_match:
         output_params['err'] = int(err_match.groups()[0],0)
         output_params['err_hex'] = err_match.groups()[0]
         try:
           output_params['err_str'] = self.getErrorString(output_params['err']) + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      elif err_api_match:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value)
         try:
           output_params['err_str'] = "API Error: " + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      else:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value
         output_params['err_str'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.name
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value)
         output_params['errcode'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN
      if (output_params['err'] and self.shouldraise):
         raise ScintilError(output_params['errcode'] or scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN, output_params)
      chip_id_match = re.match(r".*\*chip_id=(\S+)", response.text, flags=re.DOTALL)
      if chip_id_match:
         output_params['chip_id'] = int(chip_id_match.groups()[0])
      else:
         output_params['chip_id'] = None
    except requests.exceptions.RequestException as e:
      ch_error = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL
      output_params['err'] = ch_error.value
      output_params['err_str'] = ch_error.name
      output_params['errcode'] = ch_error
      if (self.shouldraise):
         raise ScintilError(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL, output_params)
    return output_params

  def scintil_hal_sys_get_hw_version(self):
    # 0 input arguments
    # 6 output arguments
    output_params = {}
    request = f"http://{self.server}:{self.port}/hal{'delegate' if self.delegate else ''}/scintil_hal_sys_get_hw_version"
    if self.token:
      request += f"?lock-token=" + self.token
    logging.debug("Request : " + request)
    try:
      response = requests.get(request)
      #output_params['response'] = response.text
      logging.debug("Response : " + response.text)
      err_match = re.match(r'.*\nerr=(0x\S+)\n.*', response.text, flags=re.DOTALL)
      err_api_match = re.match(r'(Invalid method.*)', response.text, flags=re.DOTALL)
      output_params['status_code'] = response.status_code
      if err_match:
         output_params['err'] = int(err_match.groups()[0],0)
         output_params['err_hex'] = err_match.groups()[0]
         try:
           output_params['err_str'] = self.getErrorString(output_params['err']) + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      elif err_api_match:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value)
         try:
           output_params['err_str'] = "API Error: " + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      else:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value
         output_params['err_str'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.name
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value)
         output_params['errcode'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN
      if (output_params['err'] and self.shouldraise):
         raise ScintilError(output_params['errcode'] or scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN, output_params)
      chipid_match = re.match(r".*\*chipid=(\S+)", response.text, flags=re.DOTALL)
      if chipid_match:
         output_params['chipid'] = int(chipid_match.groups()[0])
      else:
         output_params['chipid'] = None
      eco_match = re.match(r".*\*eco=(\S+)", response.text, flags=re.DOTALL)
      if eco_match:
         output_params['eco'] = int(eco_match.groups()[0])
      else:
         output_params['eco'] = None
      cut_match = re.match(r".*\*cut=(\S+)", response.text, flags=re.DOTALL)
      if cut_match:
         output_params['cut'] = int(cut_match.groups()[0])
      else:
         output_params['cut'] = None
      tag_match = re.match(r".*\*tag=(\S+)", response.text, flags=re.DOTALL)
      if tag_match:
         output_params['tag'] = int(tag_match.groups()[0])
      else:
         output_params['tag'] = None
      week_match = re.match(r".*\*week=(\S+)", response.text, flags=re.DOTALL)
      if week_match:
         output_params['week'] = int(week_match.groups()[0])
      else:
         output_params['week'] = None
      year_match = re.match(r".*\*year=(\S+)", response.text, flags=re.DOTALL)
      if year_match:
         output_params['year'] = int(year_match.groups()[0])
      else:
         output_params['year'] = None
    except requests.exceptions.RequestException as e:
      ch_error = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL
      output_params['err'] = ch_error.value
      output_params['err_str'] = ch_error.name
      output_params['errcode'] = ch_error
      if (self.shouldraise):
         raise ScintilError(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL, output_params)
    return output_params

  def scintil_hal_sys_check_api_hash( self, expected_hash: int):
    # 1 input arguments
    # 1 output arguments
    output_params = {}
    request = f"http://{self.server}:{self.port}/hal{'delegate' if self.delegate else ''}/scintil_hal_sys_check_api_hash/{expected_hash}"
    if self.token:
      request += f"?lock-token=" + self.token
    logging.debug("Request : " + request)
    try:
      response = requests.get(request)
      #output_params['response'] = response.text
      logging.debug("Response : " + response.text)
      err_match = re.match(r'.*\nerr=(0x\S+)\n.*', response.text, flags=re.DOTALL)
      err_api_match = re.match(r'(Invalid method.*)', response.text, flags=re.DOTALL)
      output_params['status_code'] = response.status_code
      if err_match:
         output_params['err'] = int(err_match.groups()[0],0)
         output_params['err_hex'] = err_match.groups()[0]
         try:
           output_params['err_str'] = self.getErrorString(output_params['err']) + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      elif err_api_match:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value)
         try:
           output_params['err_str'] = "API Error: " + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      else:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value
         output_params['err_str'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.name
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value)
         output_params['errcode'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN
      if (output_params['err'] and self.shouldraise):
         raise ScintilError(output_params['errcode'] or scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN, output_params)
      current_hash_match = re.match(r".*\*current_hash=(\S+)", response.text, flags=re.DOTALL)
      if current_hash_match:
         output_params['current_hash'] = int(current_hash_match.groups()[0])
      else:
         output_params['current_hash'] = None
    except requests.exceptions.RequestException as e:
      ch_error = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL
      output_params['err'] = ch_error.value
      output_params['err_str'] = ch_error.name
      output_params['errcode'] = ch_error
      if (self.shouldraise):
         raise ScintilError(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL, output_params)
    return output_params

  def scintil_hal_sys_enabled(self):
    # 0 input arguments
    # 1 output arguments
    output_params = {}
    request = f"http://{self.server}:{self.port}/hal{'delegate' if self.delegate else ''}/scintil_hal_sys_enabled"
    if self.token:
      request += f"?lock-token=" + self.token
    logging.debug("Request : " + request)
    try:
      response = requests.get(request)
      #output_params['response'] = response.text
      logging.debug("Response : " + response.text)
      err_match = re.match(r'.*\nerr=(0x\S+)\n.*', response.text, flags=re.DOTALL)
      err_api_match = re.match(r'(Invalid method.*)', response.text, flags=re.DOTALL)
      output_params['status_code'] = response.status_code
      if err_match:
         output_params['err'] = int(err_match.groups()[0],0)
         output_params['err_hex'] = err_match.groups()[0]
         try:
           output_params['err_str'] = self.getErrorString(output_params['err']) + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      elif err_api_match:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value)
         try:
           output_params['err_str'] = "API Error: " + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      else:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value
         output_params['err_str'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.name
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value)
         output_params['errcode'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN
      if (output_params['err'] and self.shouldraise):
         raise ScintilError(output_params['errcode'] or scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN, output_params)
      enabled_match = re.match(r".*\*enabled=(\S+)", response.text, flags=re.DOTALL)
      if enabled_match:
         output_params['enabled'] = int(enabled_match.groups()[0])
      else:
         output_params['enabled'] = None
    except requests.exceptions.RequestException as e:
      ch_error = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL
      output_params['err'] = ch_error.value
      output_params['err_str'] = ch_error.name
      output_params['errcode'] = ch_error
      if (self.shouldraise):
         raise ScintilError(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL, output_params)
    return output_params

  def scintil_hal_sys_enable( self, enable: bool):
    # 1 input arguments
    # 0 output arguments
    output_params = {}
    request = f"http://{self.server}:{self.port}/hal{'delegate' if self.delegate else ''}/scintil_hal_sys_enable/{int(enable)}"
    if self.token:
      request += f"?lock-token=" + self.token
    logging.debug("Request : " + request)
    try:
      response = requests.get(request)
      #output_params['response'] = response.text
      logging.debug("Response : " + response.text)
      err_match = re.match(r'.*\nerr=(0x\S+)\n.*', response.text, flags=re.DOTALL)
      err_api_match = re.match(r'(Invalid method.*)', response.text, flags=re.DOTALL)
      output_params['status_code'] = response.status_code
      if err_match:
         output_params['err'] = int(err_match.groups()[0],0)
         output_params['err_hex'] = err_match.groups()[0]
         try:
           output_params['err_str'] = self.getErrorString(output_params['err']) + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      elif err_api_match:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value)
         try:
           output_params['err_str'] = "API Error: " + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      else:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value
         output_params['err_str'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.name
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value)
         output_params['errcode'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN
      if (output_params['err'] and self.shouldraise):
         raise ScintilError(output_params['errcode'] or scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN, output_params)
    except requests.exceptions.RequestException as e:
      ch_error = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL
      output_params['err'] = ch_error.value
      output_params['err_str'] = ch_error.name
      output_params['errcode'] = ch_error
      if (self.shouldraise):
         raise ScintilError(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL, output_params)
    return output_params

  def scintil_hal_sys_calibrate(self):
    # 0 input arguments
    # 0 output arguments
    output_params = {}
    request = f"http://{self.server}:{self.port}/hal{'delegate' if self.delegate else ''}/scintil_hal_sys_calibrate"
    if self.token:
      request += f"?lock-token=" + self.token
    logging.debug("Request : " + request)
    try:
      response = requests.get(request)
      #output_params['response'] = response.text
      logging.debug("Response : " + response.text)
      err_match = re.match(r'.*\nerr=(0x\S+)\n.*', response.text, flags=re.DOTALL)
      err_api_match = re.match(r'(Invalid method.*)', response.text, flags=re.DOTALL)
      output_params['status_code'] = response.status_code
      if err_match:
         output_params['err'] = int(err_match.groups()[0],0)
         output_params['err_hex'] = err_match.groups()[0]
         try:
           output_params['err_str'] = self.getErrorString(output_params['err']) + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      elif err_api_match:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value)
         try:
           output_params['err_str'] = "API Error: " + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      else:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value
         output_params['err_str'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.name
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value)
         output_params['errcode'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN
      if (output_params['err'] and self.shouldraise):
         raise ScintilError(output_params['errcode'] or scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN, output_params)
    except requests.exceptions.RequestException as e:
      ch_error = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL
      output_params['err'] = ch_error.value
      output_params['err_str'] = ch_error.name
      output_params['errcode'] = ch_error
      if (self.shouldraise):
         raise ScintilError(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL, output_params)
    return output_params

  def scintil_hal_sys_read_thermal_sensor( self, sensor: scintil_hal_ths_t):
    # 1 input arguments
    # 1 output arguments
    output_params = {}
    request = f"http://{self.server}:{self.port}/hal{'delegate' if self.delegate else ''}/scintil_hal_sys_read_thermal_sensor/{sensor.value if hasattr(sensor,'value') else sensor}"
    if self.token:
      request += f"?lock-token=" + self.token
    logging.debug("Request : " + request)
    try:
      response = requests.get(request)
      #output_params['response'] = response.text
      logging.debug("Response : " + response.text)
      err_match = re.match(r'.*\nerr=(0x\S+)\n.*', response.text, flags=re.DOTALL)
      err_api_match = re.match(r'(Invalid method.*)', response.text, flags=re.DOTALL)
      output_params['status_code'] = response.status_code
      if err_match:
         output_params['err'] = int(err_match.groups()[0],0)
         output_params['err_hex'] = err_match.groups()[0]
         try:
           output_params['err_str'] = self.getErrorString(output_params['err']) + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      elif err_api_match:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value)
         try:
           output_params['err_str'] = "API Error: " + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      else:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value
         output_params['err_str'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.name
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value)
         output_params['errcode'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN
      if (output_params['err'] and self.shouldraise):
         raise ScintilError(output_params['errcode'] or scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN, output_params)
      temp_match = re.match(r".*\*temp=(\S+)", response.text, flags=re.DOTALL)
      if temp_match:
         output_params['temp'] = float(temp_match.groups()[0])
      else:
         output_params['temp'] = None
    except requests.exceptions.RequestException as e:
      ch_error = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL
      output_params['err'] = ch_error.value
      output_params['err_str'] = ch_error.name
      output_params['errcode'] = ch_error
      if (self.shouldraise):
         raise ScintilError(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL, output_params)
    return output_params

  def scintil_hal_sys_get_wpe(self):
    # 0 input arguments
    # 1 output arguments
    output_params = {}
    request = f"http://{self.server}:{self.port}/hal{'delegate' if self.delegate else ''}/scintil_hal_sys_get_wpe"
    if self.token:
      request += f"?lock-token=" + self.token
    logging.debug("Request : " + request)
    try:
      response = requests.get(request)
      #output_params['response'] = response.text
      logging.debug("Response : " + response.text)
      err_match = re.match(r'.*\nerr=(0x\S+)\n.*', response.text, flags=re.DOTALL)
      err_api_match = re.match(r'(Invalid method.*)', response.text, flags=re.DOTALL)
      output_params['status_code'] = response.status_code
      if err_match:
         output_params['err'] = int(err_match.groups()[0],0)
         output_params['err_hex'] = err_match.groups()[0]
         try:
           output_params['err_str'] = self.getErrorString(output_params['err']) + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      elif err_api_match:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value)
         try:
           output_params['err_str'] = "API Error: " + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      else:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value
         output_params['err_str'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.name
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value)
         output_params['errcode'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN
      if (output_params['err'] and self.shouldraise):
         raise ScintilError(output_params['errcode'] or scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN, output_params)
      wpe_match = re.match(r".*\*wpe=(\S+)", response.text, flags=re.DOTALL)
      if wpe_match:
         output_params['wpe'] = float(wpe_match.groups()[0])
      else:
         output_params['wpe'] = None
    except requests.exceptions.RequestException as e:
      ch_error = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL
      output_params['err'] = ch_error.value
      output_params['err_str'] = ch_error.name
      output_params['errcode'] = ch_error
      if (self.shouldraise):
         raise ScintilError(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL, output_params)
    return output_params

  def scintil_hal_sys_get_status(self):
    # 0 input arguments
    # 1 output arguments
    output_params = {}
    request = f"http://{self.server}:{self.port}/hal{'delegate' if self.delegate else ''}/scintil_hal_sys_get_status"
    if self.token:
      request += f"?lock-token=" + self.token
    logging.debug("Request : " + request)
    try:
      response = requests.get(request)
      #output_params['response'] = response.text
      logging.debug("Response : " + response.text)
      err_match = re.match(r'.*\nerr=(0x\S+)\n.*', response.text, flags=re.DOTALL)
      err_api_match = re.match(r'(Invalid method.*)', response.text, flags=re.DOTALL)
      output_params['status_code'] = response.status_code
      if err_match:
         output_params['err'] = int(err_match.groups()[0],0)
         output_params['err_hex'] = err_match.groups()[0]
         try:
           output_params['err_str'] = self.getErrorString(output_params['err']) + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      elif err_api_match:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value)
         try:
           output_params['err_str'] = "API Error: " + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      else:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value
         output_params['err_str'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.name
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value)
         output_params['errcode'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN
      if (output_params['err'] and self.shouldraise):
         raise ScintilError(output_params['errcode'] or scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN, output_params)
      status_match = re.match(r".*\*status=\s*({\S+})", response.text, flags=re.DOTALL)
      if status_match:
         output_params['status'] = scintil_hal_sys_status_t.fromstring(status_match.groups()[0])
      else:
         output_params['status'] = None
    except requests.exceptions.RequestException as e:
      ch_error = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL
      output_params['err'] = ch_error.value
      output_params['err_str'] = ch_error.name
      output_params['errcode'] = ch_error
      if (self.shouldraise):
         raise ScintilError(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL, output_params)
    return output_params

  def scintil_hal_sys_get_sw_version(self):
    # 0 input arguments
    # 1 output arguments
    output_params = {}
    request = f"http://{self.server}:{self.port}/hal{'delegate' if self.delegate else ''}/scintil_hal_sys_get_sw_version"
    if self.token:
      request += f"?lock-token=" + self.token
    logging.debug("Request : " + request)
    try:
      response = requests.get(request)
      #output_params['response'] = response.text
      logging.debug("Response : " + response.text)
      err_match = re.match(r'.*\nerr=(0x\S+)\n.*', response.text, flags=re.DOTALL)
      err_api_match = re.match(r'(Invalid method.*)', response.text, flags=re.DOTALL)
      output_params['status_code'] = response.status_code
      if err_match:
         output_params['err'] = int(err_match.groups()[0],0)
         output_params['err_hex'] = err_match.groups()[0]
         try:
           output_params['err_str'] = self.getErrorString(output_params['err']) + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      elif err_api_match:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value)
         try:
           output_params['err_str'] = "API Error: " + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      else:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value
         output_params['err_str'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.name
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value)
         output_params['errcode'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN
      if (output_params['err'] and self.shouldraise):
         raise ScintilError(output_params['errcode'] or scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN, output_params)
      version_match = re.match(r".*\*version=\s*({\S+})", response.text, flags=re.DOTALL)
      if version_match:
         output_params['version'] = scintil_hal_sys_sw_version_t.fromstring(version_match.groups()[0])
      else:
         output_params['version'] = None
    except requests.exceptions.RequestException as e:
      ch_error = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL
      output_params['err'] = ch_error.value
      output_params['err_str'] = ch_error.name
      output_params['errcode'] = ch_error
      if (self.shouldraise):
         raise ScintilError(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL, output_params)
    return output_params

  def scintil_hal_sys_get_fpga_version(self):
    # 0 input arguments
    # 1 output arguments
    output_params = {}
    request = f"http://{self.server}:{self.port}/hal{'delegate' if self.delegate else ''}/scintil_hal_sys_get_fpga_version"
    if self.token:
      request += f"?lock-token=" + self.token
    logging.debug("Request : " + request)
    try:
      response = requests.get(request)
      #output_params['response'] = response.text
      logging.debug("Response : " + response.text)
      err_match = re.match(r'.*\nerr=(0x\S+)\n.*', response.text, flags=re.DOTALL)
      err_api_match = re.match(r'(Invalid method.*)', response.text, flags=re.DOTALL)
      output_params['status_code'] = response.status_code
      if err_match:
         output_params['err'] = int(err_match.groups()[0],0)
         output_params['err_hex'] = err_match.groups()[0]
         try:
           output_params['err_str'] = self.getErrorString(output_params['err']) + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      elif err_api_match:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value)
         try:
           output_params['err_str'] = "API Error: " + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      else:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value
         output_params['err_str'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.name
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value)
         output_params['errcode'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN
      if (output_params['err'] and self.shouldraise):
         raise ScintilError(output_params['errcode'] or scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN, output_params)
      version_match = re.match(r".*\*version=\s*({\S+})", response.text, flags=re.DOTALL)
      if version_match:
         output_params['version'] = scintil_hal_sys_fpga_version_t.fromstring(version_match.groups()[0])
      else:
         output_params['version'] = None
    except requests.exceptions.RequestException as e:
      ch_error = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL
      output_params['err'] = ch_error.value
      output_params['err_str'] = ch_error.name
      output_params['errcode'] = ch_error
      if (self.shouldraise):
         raise ScintilError(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL, output_params)
    return output_params

  def scintil_hal_controller_calibrate_mux( self, module: scintil_hal_module_t, heater: scintil_hal_mux_heater_t, output_mpd: scintil_hal_mpd_t):
    # 3 input arguments
    # 1 output arguments
    output_params = {}
    request = f"http://{self.server}:{self.port}/hal{'delegate' if self.delegate else ''}/scintil_hal_controller_calibrate_mux/{module.value if hasattr(module,'value') else module}/{heater.value if hasattr(heater,'value') else heater}/{output_mpd.value if hasattr(output_mpd,'value') else output_mpd}"
    if self.token:
      request += f"?lock-token=" + self.token
    logging.debug("Request : " + request)
    try:
      response = requests.get(request)
      #output_params['response'] = response.text
      logging.debug("Response : " + response.text)
      err_match = re.match(r'.*\nerr=(0x\S+)\n.*', response.text, flags=re.DOTALL)
      err_api_match = re.match(r'(Invalid method.*)', response.text, flags=re.DOTALL)
      output_params['status_code'] = response.status_code
      if err_match:
         output_params['err'] = int(err_match.groups()[0],0)
         output_params['err_hex'] = err_match.groups()[0]
         try:
           output_params['err_str'] = self.getErrorString(output_params['err']) + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      elif err_api_match:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value)
         try:
           output_params['err_str'] = "API Error: " + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      else:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value
         output_params['err_str'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.name
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value)
         output_params['errcode'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN
      if (output_params['err'] and self.shouldraise):
         raise ScintilError(output_params['errcode'] or scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN, output_params)
      best_match = re.match(r".*\*best=(\S+)", response.text, flags=re.DOTALL)
      if best_match:
         output_params['best'] = float(best_match.groups()[0])
      else:
         output_params['best'] = None
    except requests.exceptions.RequestException as e:
      ch_error = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL
      output_params['err'] = ch_error.value
      output_params['err_str'] = ch_error.name
      output_params['errcode'] = ch_error
      if (self.shouldraise):
         raise ScintilError(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL, output_params)
    return output_params

  def scintil_hal_controller_mux_loop_start( self, module: scintil_hal_module_t):
    # 1 input arguments
    # 0 output arguments
    output_params = {}
    request = f"http://{self.server}:{self.port}/hal{'delegate' if self.delegate else ''}/scintil_hal_controller_mux_loop_start/{module.value if hasattr(module,'value') else module}"
    if self.token:
      request += f"?lock-token=" + self.token
    logging.debug("Request : " + request)
    try:
      response = requests.get(request)
      #output_params['response'] = response.text
      logging.debug("Response : " + response.text)
      err_match = re.match(r'.*\nerr=(0x\S+)\n.*', response.text, flags=re.DOTALL)
      err_api_match = re.match(r'(Invalid method.*)', response.text, flags=re.DOTALL)
      output_params['status_code'] = response.status_code
      if err_match:
         output_params['err'] = int(err_match.groups()[0],0)
         output_params['err_hex'] = err_match.groups()[0]
         try:
           output_params['err_str'] = self.getErrorString(output_params['err']) + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      elif err_api_match:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value)
         try:
           output_params['err_str'] = "API Error: " + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      else:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value
         output_params['err_str'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.name
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value)
         output_params['errcode'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN
      if (output_params['err'] and self.shouldraise):
         raise ScintilError(output_params['errcode'] or scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN, output_params)
    except requests.exceptions.RequestException as e:
      ch_error = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL
      output_params['err'] = ch_error.value
      output_params['err_str'] = ch_error.name
      output_params['errcode'] = ch_error
      if (self.shouldraise):
         raise ScintilError(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL, output_params)
    return output_params

  def scintil_hal_controller_mux_loop_stop( self, module: scintil_hal_module_t):
    # 1 input arguments
    # 0 output arguments
    output_params = {}
    request = f"http://{self.server}:{self.port}/hal{'delegate' if self.delegate else ''}/scintil_hal_controller_mux_loop_stop/{module.value if hasattr(module,'value') else module}"
    if self.token:
      request += f"?lock-token=" + self.token
    logging.debug("Request : " + request)
    try:
      response = requests.get(request)
      #output_params['response'] = response.text
      logging.debug("Response : " + response.text)
      err_match = re.match(r'.*\nerr=(0x\S+)\n.*', response.text, flags=re.DOTALL)
      err_api_match = re.match(r'(Invalid method.*)', response.text, flags=re.DOTALL)
      output_params['status_code'] = response.status_code
      if err_match:
         output_params['err'] = int(err_match.groups()[0],0)
         output_params['err_hex'] = err_match.groups()[0]
         try:
           output_params['err_str'] = self.getErrorString(output_params['err']) + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      elif err_api_match:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value)
         try:
           output_params['err_str'] = "API Error: " + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      else:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value
         output_params['err_str'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.name
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value)
         output_params['errcode'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN
      if (output_params['err'] and self.shouldraise):
         raise ScintilError(output_params['errcode'] or scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN, output_params)
    except requests.exceptions.RequestException as e:
      ch_error = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL
      output_params['err'] = ch_error.value
      output_params['err_str'] = ch_error.name
      output_params['errcode'] = ch_error
      if (self.shouldraise):
         raise ScintilError(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL, output_params)
    return output_params

  def scintil_hal_controller_mux_set_rand_values( self, module: scintil_hal_module_t):
    # 1 input arguments
    # 0 output arguments
    output_params = {}
    request = f"http://{self.server}:{self.port}/hal{'delegate' if self.delegate else ''}/scintil_hal_controller_mux_set_rand_values/{module.value if hasattr(module,'value') else module}"
    if self.token:
      request += f"?lock-token=" + self.token
    logging.debug("Request : " + request)
    try:
      response = requests.get(request)
      #output_params['response'] = response.text
      logging.debug("Response : " + response.text)
      err_match = re.match(r'.*\nerr=(0x\S+)\n.*', response.text, flags=re.DOTALL)
      err_api_match = re.match(r'(Invalid method.*)', response.text, flags=re.DOTALL)
      output_params['status_code'] = response.status_code
      if err_match:
         output_params['err'] = int(err_match.groups()[0],0)
         output_params['err_hex'] = err_match.groups()[0]
         try:
           output_params['err_str'] = self.getErrorString(output_params['err']) + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      elif err_api_match:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value)
         try:
           output_params['err_str'] = "API Error: " + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      else:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value
         output_params['err_str'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.name
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value)
         output_params['errcode'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN
      if (output_params['err'] and self.shouldraise):
         raise ScintilError(output_params['errcode'] or scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN, output_params)
    except requests.exceptions.RequestException as e:
      ch_error = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL
      output_params['err'] = ch_error.value
      output_params['err_str'] = ch_error.name
      output_params['errcode'] = ch_error
      if (self.shouldraise):
         raise ScintilError(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL, output_params)
    return output_params

  def scintil_hal_controller_mux_set_value( self, module: scintil_hal_module_t, common_val: float):
    # 2 input arguments
    # 0 output arguments
    output_params = {}
    request = f"http://{self.server}:{self.port}/hal{'delegate' if self.delegate else ''}/scintil_hal_controller_mux_set_value/{module.value if hasattr(module,'value') else module}/{common_val}"
    if self.token:
      request += f"?lock-token=" + self.token
    logging.debug("Request : " + request)
    try:
      response = requests.get(request)
      #output_params['response'] = response.text
      logging.debug("Response : " + response.text)
      err_match = re.match(r'.*\nerr=(0x\S+)\n.*', response.text, flags=re.DOTALL)
      err_api_match = re.match(r'(Invalid method.*)', response.text, flags=re.DOTALL)
      output_params['status_code'] = response.status_code
      if err_match:
         output_params['err'] = int(err_match.groups()[0],0)
         output_params['err_hex'] = err_match.groups()[0]
         try:
           output_params['err_str'] = self.getErrorString(output_params['err']) + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      elif err_api_match:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value)
         try:
           output_params['err_str'] = "API Error: " + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      else:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value
         output_params['err_str'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.name
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value)
         output_params['errcode'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN
      if (output_params['err'] and self.shouldraise):
         raise ScintilError(output_params['errcode'] or scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN, output_params)
    except requests.exceptions.RequestException as e:
      ch_error = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL
      output_params['err'] = ch_error.value
      output_params['err_str'] = ch_error.name
      output_params['errcode'] = ch_error
      if (self.shouldraise):
         raise ScintilError(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL, output_params)
    return output_params

  def scintil_hal_controller_laser_set_value( self, module: scintil_hal_module_t, common_val: float):
    # 2 input arguments
    # 0 output arguments
    output_params = {}
    request = f"http://{self.server}:{self.port}/hal{'delegate' if self.delegate else ''}/scintil_hal_controller_laser_set_value/{module.value if hasattr(module,'value') else module}/{common_val}"
    if self.token:
      request += f"?lock-token=" + self.token
    logging.debug("Request : " + request)
    try:
      response = requests.get(request)
      #output_params['response'] = response.text
      logging.debug("Response : " + response.text)
      err_match = re.match(r'.*\nerr=(0x\S+)\n.*', response.text, flags=re.DOTALL)
      err_api_match = re.match(r'(Invalid method.*)', response.text, flags=re.DOTALL)
      output_params['status_code'] = response.status_code
      if err_match:
         output_params['err'] = int(err_match.groups()[0],0)
         output_params['err_hex'] = err_match.groups()[0]
         try:
           output_params['err_str'] = self.getErrorString(output_params['err']) + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      elif err_api_match:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value)
         try:
           output_params['err_str'] = "API Error: " + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      else:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value
         output_params['err_str'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.name
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value)
         output_params['errcode'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN
      if (output_params['err'] and self.shouldraise):
         raise ScintilError(output_params['errcode'] or scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN, output_params)
    except requests.exceptions.RequestException as e:
      ch_error = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL
      output_params['err'] = ch_error.value
      output_params['err_str'] = ch_error.name
      output_params['errcode'] = ch_error
      if (self.shouldraise):
         raise ScintilError(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL, output_params)
    return output_params

  def scintil_hal_controller_laser_even_set_value( self, module: scintil_hal_module_t, common_val: float):
    # 2 input arguments
    # 0 output arguments
    output_params = {}
    request = f"http://{self.server}:{self.port}/hal{'delegate' if self.delegate else ''}/scintil_hal_controller_laser_even_set_value/{module.value if hasattr(module,'value') else module}/{common_val}"
    if self.token:
      request += f"?lock-token=" + self.token
    logging.debug("Request : " + request)
    try:
      response = requests.get(request)
      #output_params['response'] = response.text
      logging.debug("Response : " + response.text)
      err_match = re.match(r'.*\nerr=(0x\S+)\n.*', response.text, flags=re.DOTALL)
      err_api_match = re.match(r'(Invalid method.*)', response.text, flags=re.DOTALL)
      output_params['status_code'] = response.status_code
      if err_match:
         output_params['err'] = int(err_match.groups()[0],0)
         output_params['err_hex'] = err_match.groups()[0]
         try:
           output_params['err_str'] = self.getErrorString(output_params['err']) + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      elif err_api_match:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value)
         try:
           output_params['err_str'] = "API Error: " + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      else:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value
         output_params['err_str'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.name
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value)
         output_params['errcode'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN
      if (output_params['err'] and self.shouldraise):
         raise ScintilError(output_params['errcode'] or scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN, output_params)
    except requests.exceptions.RequestException as e:
      ch_error = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL
      output_params['err'] = ch_error.value
      output_params['err_str'] = ch_error.name
      output_params['errcode'] = ch_error
      if (self.shouldraise):
         raise ScintilError(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL, output_params)
    return output_params

  def scintil_hal_controller_laser_odd_set_value( self, module: scintil_hal_module_t, common_val: float):
    # 2 input arguments
    # 0 output arguments
    output_params = {}
    request = f"http://{self.server}:{self.port}/hal{'delegate' if self.delegate else ''}/scintil_hal_controller_laser_odd_set_value/{module.value if hasattr(module,'value') else module}/{common_val}"
    if self.token:
      request += f"?lock-token=" + self.token
    logging.debug("Request : " + request)
    try:
      response = requests.get(request)
      #output_params['response'] = response.text
      logging.debug("Response : " + response.text)
      err_match = re.match(r'.*\nerr=(0x\S+)\n.*', response.text, flags=re.DOTALL)
      err_api_match = re.match(r'(Invalid method.*)', response.text, flags=re.DOTALL)
      output_params['status_code'] = response.status_code
      if err_match:
         output_params['err'] = int(err_match.groups()[0],0)
         output_params['err_hex'] = err_match.groups()[0]
         try:
           output_params['err_str'] = self.getErrorString(output_params['err']) + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      elif err_api_match:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value)
         try:
           output_params['err_str'] = "API Error: " + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      else:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value
         output_params['err_str'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.name
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value)
         output_params['errcode'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN
      if (output_params['err'] and self.shouldraise):
         raise ScintilError(output_params['errcode'] or scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN, output_params)
    except requests.exceptions.RequestException as e:
      ch_error = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL
      output_params['err'] = ch_error.value
      output_params['err_str'] = ch_error.name
      output_params['errcode'] = ch_error
      if (self.shouldraise):
         raise ScintilError(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL, output_params)
    return output_params

  def scintil_hal_controller_laser_apply_offset( self, module: scintil_hal_module_t, offset_value: float):
    # 2 input arguments
    # 0 output arguments
    output_params = {}
    request = f"http://{self.server}:{self.port}/hal{'delegate' if self.delegate else ''}/scintil_hal_controller_laser_apply_offset/{module.value if hasattr(module,'value') else module}/{offset_value}"
    if self.token:
      request += f"?lock-token=" + self.token
    logging.debug("Request : " + request)
    try:
      response = requests.get(request)
      #output_params['response'] = response.text
      logging.debug("Response : " + response.text)
      err_match = re.match(r'.*\nerr=(0x\S+)\n.*', response.text, flags=re.DOTALL)
      err_api_match = re.match(r'(Invalid method.*)', response.text, flags=re.DOTALL)
      output_params['status_code'] = response.status_code
      if err_match:
         output_params['err'] = int(err_match.groups()[0],0)
         output_params['err_hex'] = err_match.groups()[0]
         try:
           output_params['err_str'] = self.getErrorString(output_params['err']) + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      elif err_api_match:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value)
         try:
           output_params['err_str'] = "API Error: " + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      else:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value
         output_params['err_str'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.name
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value)
         output_params['errcode'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN
      if (output_params['err'] and self.shouldraise):
         raise ScintilError(output_params['errcode'] or scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN, output_params)
    except requests.exceptions.RequestException as e:
      ch_error = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL
      output_params['err'] = ch_error.value
      output_params['err_str'] = ch_error.name
      output_params['errcode'] = ch_error
      if (self.shouldraise):
         raise ScintilError(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL, output_params)
    return output_params

  def scintil_hal_controller_laser_even_apply_offset( self, module: scintil_hal_module_t, offset_value: float):
    # 2 input arguments
    # 0 output arguments
    output_params = {}
    request = f"http://{self.server}:{self.port}/hal{'delegate' if self.delegate else ''}/scintil_hal_controller_laser_even_apply_offset/{module.value if hasattr(module,'value') else module}/{offset_value}"
    if self.token:
      request += f"?lock-token=" + self.token
    logging.debug("Request : " + request)
    try:
      response = requests.get(request)
      #output_params['response'] = response.text
      logging.debug("Response : " + response.text)
      err_match = re.match(r'.*\nerr=(0x\S+)\n.*', response.text, flags=re.DOTALL)
      err_api_match = re.match(r'(Invalid method.*)', response.text, flags=re.DOTALL)
      output_params['status_code'] = response.status_code
      if err_match:
         output_params['err'] = int(err_match.groups()[0],0)
         output_params['err_hex'] = err_match.groups()[0]
         try:
           output_params['err_str'] = self.getErrorString(output_params['err']) + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      elif err_api_match:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value)
         try:
           output_params['err_str'] = "API Error: " + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      else:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value
         output_params['err_str'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.name
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value)
         output_params['errcode'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN
      if (output_params['err'] and self.shouldraise):
         raise ScintilError(output_params['errcode'] or scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN, output_params)
    except requests.exceptions.RequestException as e:
      ch_error = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL
      output_params['err'] = ch_error.value
      output_params['err_str'] = ch_error.name
      output_params['errcode'] = ch_error
      if (self.shouldraise):
         raise ScintilError(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL, output_params)
    return output_params

  def scintil_hal_controller_laser_odd_apply_offset( self, module: scintil_hal_module_t, offset_value: float):
    # 2 input arguments
    # 0 output arguments
    output_params = {}
    request = f"http://{self.server}:{self.port}/hal{'delegate' if self.delegate else ''}/scintil_hal_controller_laser_odd_apply_offset/{module.value if hasattr(module,'value') else module}/{offset_value}"
    if self.token:
      request += f"?lock-token=" + self.token
    logging.debug("Request : " + request)
    try:
      response = requests.get(request)
      #output_params['response'] = response.text
      logging.debug("Response : " + response.text)
      err_match = re.match(r'.*\nerr=(0x\S+)\n.*', response.text, flags=re.DOTALL)
      err_api_match = re.match(r'(Invalid method.*)', response.text, flags=re.DOTALL)
      output_params['status_code'] = response.status_code
      if err_match:
         output_params['err'] = int(err_match.groups()[0],0)
         output_params['err_hex'] = err_match.groups()[0]
         try:
           output_params['err_str'] = self.getErrorString(output_params['err']) + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      elif err_api_match:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value)
         try:
           output_params['err_str'] = "API Error: " + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      else:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value
         output_params['err_str'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.name
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value)
         output_params['errcode'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN
      if (output_params['err'] and self.shouldraise):
         raise ScintilError(output_params['errcode'] or scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN, output_params)
    except requests.exceptions.RequestException as e:
      ch_error = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL
      output_params['err'] = ch_error.value
      output_params['err_str'] = ch_error.name
      output_params['errcode'] = ch_error
      if (self.shouldraise):
         raise ScintilError(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL, output_params)
    return output_params

  def scintil_hal_controller_heater_initial_cal( self, module: scintil_hal_module_t, cascade: scintil_hal_cascade_t):
    # 2 input arguments
    # 0 output arguments
    output_params = {}
    request = f"http://{self.server}:{self.port}/hal{'delegate' if self.delegate else ''}/scintil_hal_controller_heater_initial_cal/{module.value if hasattr(module,'value') else module}/{cascade.value if hasattr(cascade,'value') else cascade}"
    if self.token:
      request += f"?lock-token=" + self.token
    logging.debug("Request : " + request)
    try:
      response = requests.get(request)
      #output_params['response'] = response.text
      logging.debug("Response : " + response.text)
      err_match = re.match(r'.*\nerr=(0x\S+)\n.*', response.text, flags=re.DOTALL)
      err_api_match = re.match(r'(Invalid method.*)', response.text, flags=re.DOTALL)
      output_params['status_code'] = response.status_code
      if err_match:
         output_params['err'] = int(err_match.groups()[0],0)
         output_params['err_hex'] = err_match.groups()[0]
         try:
           output_params['err_str'] = self.getErrorString(output_params['err']) + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      elif err_api_match:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value)
         try:
           output_params['err_str'] = "API Error: " + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      else:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value
         output_params['err_str'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.name
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value)
         output_params['errcode'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN
      if (output_params['err'] and self.shouldraise):
         raise ScintilError(output_params['errcode'] or scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN, output_params)
    except requests.exceptions.RequestException as e:
      ch_error = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL
      output_params['err'] = ch_error.value
      output_params['err_str'] = ch_error.name
      output_params['errcode'] = ch_error
      if (self.shouldraise):
         raise ScintilError(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL, output_params)
    return output_params

  def scintil_hal_controller_heater_initial_cal_all( self, module: scintil_hal_module_t):
    # 1 input arguments
    # 0 output arguments
    output_params = {}
    request = f"http://{self.server}:{self.port}/hal{'delegate' if self.delegate else ''}/scintil_hal_controller_heater_initial_cal_all/{module.value if hasattr(module,'value') else module}"
    if self.token:
      request += f"?lock-token=" + self.token
    logging.debug("Request : " + request)
    try:
      response = requests.get(request)
      #output_params['response'] = response.text
      logging.debug("Response : " + response.text)
      err_match = re.match(r'.*\nerr=(0x\S+)\n.*', response.text, flags=re.DOTALL)
      err_api_match = re.match(r'(Invalid method.*)', response.text, flags=re.DOTALL)
      output_params['status_code'] = response.status_code
      if err_match:
         output_params['err'] = int(err_match.groups()[0],0)
         output_params['err_hex'] = err_match.groups()[0]
         try:
           output_params['err_str'] = self.getErrorString(output_params['err']) + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      elif err_api_match:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value)
         try:
           output_params['err_str'] = "API Error: " + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      else:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value
         output_params['err_str'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.name
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value)
         output_params['errcode'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN
      if (output_params['err'] and self.shouldraise):
         raise ScintilError(output_params['errcode'] or scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN, output_params)
    except requests.exceptions.RequestException as e:
      ch_error = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL
      output_params['err'] = ch_error.value
      output_params['err_str'] = ch_error.name
      output_params['errcode'] = ch_error
      if (self.shouldraise):
         raise ScintilError(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL, output_params)
    return output_params

  def scintil_hal_controller_init_all( self, module: scintil_hal_module_t):
    # 1 input arguments
    # 0 output arguments
    output_params = {}
    request = f"http://{self.server}:{self.port}/hal{'delegate' if self.delegate else ''}/scintil_hal_controller_init_all/{module.value if hasattr(module,'value') else module}"
    if self.token:
      request += f"?lock-token=" + self.token
    logging.debug("Request : " + request)
    try:
      response = requests.get(request)
      #output_params['response'] = response.text
      logging.debug("Response : " + response.text)
      err_match = re.match(r'.*\nerr=(0x\S+)\n.*', response.text, flags=re.DOTALL)
      err_api_match = re.match(r'(Invalid method.*)', response.text, flags=re.DOTALL)
      output_params['status_code'] = response.status_code
      if err_match:
         output_params['err'] = int(err_match.groups()[0],0)
         output_params['err_hex'] = err_match.groups()[0]
         try:
           output_params['err_str'] = self.getErrorString(output_params['err']) + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      elif err_api_match:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value)
         try:
           output_params['err_str'] = "API Error: " + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      else:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value
         output_params['err_str'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.name
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value)
         output_params['errcode'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN
      if (output_params['err'] and self.shouldraise):
         raise ScintilError(output_params['errcode'] or scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN, output_params)
    except requests.exceptions.RequestException as e:
      ch_error = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL
      output_params['err'] = ch_error.value
      output_params['err_str'] = ch_error.name
      output_params['errcode'] = ch_error
      if (self.shouldraise):
         raise ScintilError(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL, output_params)
    return output_params

  def scintil_hal_controller_pause_all( self, module: scintil_hal_module_t):
    # 1 input arguments
    # 0 output arguments
    output_params = {}
    request = f"http://{self.server}:{self.port}/hal{'delegate' if self.delegate else ''}/scintil_hal_controller_pause_all/{module.value if hasattr(module,'value') else module}"
    if self.token:
      request += f"?lock-token=" + self.token
    logging.debug("Request : " + request)
    try:
      response = requests.get(request)
      #output_params['response'] = response.text
      logging.debug("Response : " + response.text)
      err_match = re.match(r'.*\nerr=(0x\S+)\n.*', response.text, flags=re.DOTALL)
      err_api_match = re.match(r'(Invalid method.*)', response.text, flags=re.DOTALL)
      output_params['status_code'] = response.status_code
      if err_match:
         output_params['err'] = int(err_match.groups()[0],0)
         output_params['err_hex'] = err_match.groups()[0]
         try:
           output_params['err_str'] = self.getErrorString(output_params['err']) + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      elif err_api_match:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value)
         try:
           output_params['err_str'] = "API Error: " + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      else:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value
         output_params['err_str'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.name
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value)
         output_params['errcode'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN
      if (output_params['err'] and self.shouldraise):
         raise ScintilError(output_params['errcode'] or scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN, output_params)
    except requests.exceptions.RequestException as e:
      ch_error = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL
      output_params['err'] = ch_error.value
      output_params['err_str'] = ch_error.name
      output_params['errcode'] = ch_error
      if (self.shouldraise):
         raise ScintilError(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL, output_params)
    return output_params

  def scintil_hal_controller_run_all( self, module: scintil_hal_module_t):
    # 1 input arguments
    # 0 output arguments
    output_params = {}
    request = f"http://{self.server}:{self.port}/hal{'delegate' if self.delegate else ''}/scintil_hal_controller_run_all/{module.value if hasattr(module,'value') else module}"
    if self.token:
      request += f"?lock-token=" + self.token
    logging.debug("Request : " + request)
    try:
      response = requests.get(request)
      #output_params['response'] = response.text
      logging.debug("Response : " + response.text)
      err_match = re.match(r'.*\nerr=(0x\S+)\n.*', response.text, flags=re.DOTALL)
      err_api_match = re.match(r'(Invalid method.*)', response.text, flags=re.DOTALL)
      output_params['status_code'] = response.status_code
      if err_match:
         output_params['err'] = int(err_match.groups()[0],0)
         output_params['err_hex'] = err_match.groups()[0]
         try:
           output_params['err_str'] = self.getErrorString(output_params['err']) + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      elif err_api_match:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value)
         try:
           output_params['err_str'] = "API Error: " + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      else:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value
         output_params['err_str'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.name
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value)
         output_params['errcode'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN
      if (output_params['err'] and self.shouldraise):
         raise ScintilError(output_params['errcode'] or scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN, output_params)
    except requests.exceptions.RequestException as e:
      ch_error = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL
      output_params['err'] = ch_error.value
      output_params['err_str'] = ch_error.name
      output_params['errcode'] = ch_error
      if (self.shouldraise):
         raise ScintilError(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL, output_params)
    return output_params

  def scintil_hal_controller_init( self, module: scintil_hal_module_t, cascade: scintil_hal_cascade_t):
    # 2 input arguments
    # 0 output arguments
    output_params = {}
    request = f"http://{self.server}:{self.port}/hal{'delegate' if self.delegate else ''}/scintil_hal_controller_init/{module.value if hasattr(module,'value') else module}/{cascade.value if hasattr(cascade,'value') else cascade}"
    if self.token:
      request += f"?lock-token=" + self.token
    logging.debug("Request : " + request)
    try:
      response = requests.get(request)
      #output_params['response'] = response.text
      logging.debug("Response : " + response.text)
      err_match = re.match(r'.*\nerr=(0x\S+)\n.*', response.text, flags=re.DOTALL)
      err_api_match = re.match(r'(Invalid method.*)', response.text, flags=re.DOTALL)
      output_params['status_code'] = response.status_code
      if err_match:
         output_params['err'] = int(err_match.groups()[0],0)
         output_params['err_hex'] = err_match.groups()[0]
         try:
           output_params['err_str'] = self.getErrorString(output_params['err']) + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      elif err_api_match:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value)
         try:
           output_params['err_str'] = "API Error: " + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      else:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value
         output_params['err_str'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.name
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value)
         output_params['errcode'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN
      if (output_params['err'] and self.shouldraise):
         raise ScintilError(output_params['errcode'] or scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN, output_params)
    except requests.exceptions.RequestException as e:
      ch_error = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL
      output_params['err'] = ch_error.value
      output_params['err_str'] = ch_error.name
      output_params['errcode'] = ch_error
      if (self.shouldraise):
         raise ScintilError(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL, output_params)
    return output_params

  def scintil_hal_controller_set_interval( self, module: scintil_hal_module_t, cascade: scintil_hal_cascade_t, interval_ns: int):
    # 3 input arguments
    # 0 output arguments
    output_params = {}
    request = f"http://{self.server}:{self.port}/hal{'delegate' if self.delegate else ''}/scintil_hal_controller_set_interval/{module.value if hasattr(module,'value') else module}/{cascade.value if hasattr(cascade,'value') else cascade}/{interval_ns}"
    if self.token:
      request += f"?lock-token=" + self.token
    logging.debug("Request : " + request)
    try:
      response = requests.get(request)
      #output_params['response'] = response.text
      logging.debug("Response : " + response.text)
      err_match = re.match(r'.*\nerr=(0x\S+)\n.*', response.text, flags=re.DOTALL)
      err_api_match = re.match(r'(Invalid method.*)', response.text, flags=re.DOTALL)
      output_params['status_code'] = response.status_code
      if err_match:
         output_params['err'] = int(err_match.groups()[0],0)
         output_params['err_hex'] = err_match.groups()[0]
         try:
           output_params['err_str'] = self.getErrorString(output_params['err']) + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      elif err_api_match:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value)
         try:
           output_params['err_str'] = "API Error: " + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      else:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value
         output_params['err_str'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.name
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value)
         output_params['errcode'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN
      if (output_params['err'] and self.shouldraise):
         raise ScintilError(output_params['errcode'] or scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN, output_params)
    except requests.exceptions.RequestException as e:
      ch_error = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL
      output_params['err'] = ch_error.value
      output_params['err_str'] = ch_error.name
      output_params['errcode'] = ch_error
      if (self.shouldraise):
         raise ScintilError(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL, output_params)
    return output_params

  def scintil_hal_controller_get_interval( self, module: scintil_hal_module_t, cascade: scintil_hal_cascade_t):
    # 2 input arguments
    # 1 output arguments
    output_params = {}
    request = f"http://{self.server}:{self.port}/hal{'delegate' if self.delegate else ''}/scintil_hal_controller_get_interval/{module.value if hasattr(module,'value') else module}/{cascade.value if hasattr(cascade,'value') else cascade}"
    if self.token:
      request += f"?lock-token=" + self.token
    logging.debug("Request : " + request)
    try:
      response = requests.get(request)
      #output_params['response'] = response.text
      logging.debug("Response : " + response.text)
      err_match = re.match(r'.*\nerr=(0x\S+)\n.*', response.text, flags=re.DOTALL)
      err_api_match = re.match(r'(Invalid method.*)', response.text, flags=re.DOTALL)
      output_params['status_code'] = response.status_code
      if err_match:
         output_params['err'] = int(err_match.groups()[0],0)
         output_params['err_hex'] = err_match.groups()[0]
         try:
           output_params['err_str'] = self.getErrorString(output_params['err']) + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      elif err_api_match:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value)
         try:
           output_params['err_str'] = "API Error: " + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      else:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value
         output_params['err_str'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.name
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value)
         output_params['errcode'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN
      if (output_params['err'] and self.shouldraise):
         raise ScintilError(output_params['errcode'] or scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN, output_params)
      interval_ns_match = re.match(r".*\*interval_ns=(\S+)", response.text, flags=re.DOTALL)
      if interval_ns_match:
         output_params['interval_ns'] = int(interval_ns_match.groups()[0])
      else:
         output_params['interval_ns'] = None
    except requests.exceptions.RequestException as e:
      ch_error = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL
      output_params['err'] = ch_error.value
      output_params['err_str'] = ch_error.name
      output_params['errcode'] = ch_error
      if (self.shouldraise):
         raise ScintilError(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL, output_params)
    return output_params

  def scintil_hal_controller_should_wait( self, module: scintil_hal_module_t, cascade: scintil_hal_cascade_t):
    # 2 input arguments
    # 2 output arguments
    output_params = {}
    request = f"http://{self.server}:{self.port}/hal{'delegate' if self.delegate else ''}/scintil_hal_controller_should_wait/{module.value if hasattr(module,'value') else module}/{cascade.value if hasattr(cascade,'value') else cascade}"
    if self.token:
      request += f"?lock-token=" + self.token
    logging.debug("Request : " + request)
    try:
      response = requests.get(request)
      #output_params['response'] = response.text
      logging.debug("Response : " + response.text)
      err_match = re.match(r'.*\nerr=(0x\S+)\n.*', response.text, flags=re.DOTALL)
      err_api_match = re.match(r'(Invalid method.*)', response.text, flags=re.DOTALL)
      output_params['status_code'] = response.status_code
      if err_match:
         output_params['err'] = int(err_match.groups()[0],0)
         output_params['err_hex'] = err_match.groups()[0]
         try:
           output_params['err_str'] = self.getErrorString(output_params['err']) + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      elif err_api_match:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value)
         try:
           output_params['err_str'] = "API Error: " + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      else:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value
         output_params['err_str'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.name
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value)
         output_params['errcode'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN
      if (output_params['err'] and self.shouldraise):
         raise ScintilError(output_params['errcode'] or scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN, output_params)
      should_wait_match = re.match(r".*\*should_wait=(\S+)", response.text, flags=re.DOTALL)
      if should_wait_match:
         output_params['should_wait'] = int(should_wait_match.groups()[0])
      else:
         output_params['should_wait'] = None
      wait_ns_match = re.match(r".*\*wait_ns=(\S+)", response.text, flags=re.DOTALL)
      if wait_ns_match:
         output_params['wait_ns'] = int(wait_ns_match.groups()[0])
      else:
         output_params['wait_ns'] = None
    except requests.exceptions.RequestException as e:
      ch_error = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL
      output_params['err'] = ch_error.value
      output_params['err_str'] = ch_error.name
      output_params['errcode'] = ch_error
      if (self.shouldraise):
         raise ScintilError(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL, output_params)
    return output_params

  def scintil_hal_controller_run( self, module: scintil_hal_module_t, cascade: scintil_hal_cascade_t, run: bool):
    # 3 input arguments
    # 0 output arguments
    output_params = {}
    request = f"http://{self.server}:{self.port}/hal{'delegate' if self.delegate else ''}/scintil_hal_controller_run/{module.value if hasattr(module,'value') else module}/{cascade.value if hasattr(cascade,'value') else cascade}/{int(run)}"
    if self.token:
      request += f"?lock-token=" + self.token
    logging.debug("Request : " + request)
    try:
      response = requests.get(request)
      #output_params['response'] = response.text
      logging.debug("Response : " + response.text)
      err_match = re.match(r'.*\nerr=(0x\S+)\n.*', response.text, flags=re.DOTALL)
      err_api_match = re.match(r'(Invalid method.*)', response.text, flags=re.DOTALL)
      output_params['status_code'] = response.status_code
      if err_match:
         output_params['err'] = int(err_match.groups()[0],0)
         output_params['err_hex'] = err_match.groups()[0]
         try:
           output_params['err_str'] = self.getErrorString(output_params['err']) + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      elif err_api_match:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value)
         try:
           output_params['err_str'] = "API Error: " + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      else:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value
         output_params['err_str'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.name
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value)
         output_params['errcode'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN
      if (output_params['err'] and self.shouldraise):
         raise ScintilError(output_params['errcode'] or scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN, output_params)
    except requests.exceptions.RequestException as e:
      ch_error = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL
      output_params['err'] = ch_error.value
      output_params['err_str'] = ch_error.name
      output_params['errcode'] = ch_error
      if (self.shouldraise):
         raise ScintilError(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL, output_params)
    return output_params

  def scintil_hal_controller_running( self, module: scintil_hal_module_t, cascade: scintil_hal_cascade_t):
    # 2 input arguments
    # 1 output arguments
    output_params = {}
    request = f"http://{self.server}:{self.port}/hal{'delegate' if self.delegate else ''}/scintil_hal_controller_running/{module.value if hasattr(module,'value') else module}/{cascade.value if hasattr(cascade,'value') else cascade}"
    if self.token:
      request += f"?lock-token=" + self.token
    logging.debug("Request : " + request)
    try:
      response = requests.get(request)
      #output_params['response'] = response.text
      logging.debug("Response : " + response.text)
      err_match = re.match(r'.*\nerr=(0x\S+)\n.*', response.text, flags=re.DOTALL)
      err_api_match = re.match(r'(Invalid method.*)', response.text, flags=re.DOTALL)
      output_params['status_code'] = response.status_code
      if err_match:
         output_params['err'] = int(err_match.groups()[0],0)
         output_params['err_hex'] = err_match.groups()[0]
         try:
           output_params['err_str'] = self.getErrorString(output_params['err']) + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      elif err_api_match:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value)
         try:
           output_params['err_str'] = "API Error: " + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      else:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value
         output_params['err_str'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.name
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value)
         output_params['errcode'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN
      if (output_params['err'] and self.shouldraise):
         raise ScintilError(output_params['errcode'] or scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN, output_params)
      running_match = re.match(r".*\*running=(\S+)", response.text, flags=re.DOTALL)
      if running_match:
         output_params['running'] = int(running_match.groups()[0])
      else:
         output_params['running'] = None
    except requests.exceptions.RequestException as e:
      ch_error = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL
      output_params['err'] = ch_error.value
      output_params['err_str'] = ch_error.name
      output_params['errcode'] = ch_error
      if (self.shouldraise):
         raise ScintilError(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL, output_params)
    return output_params

  def scintil_hal_controller_run_toggle( self, module: scintil_hal_module_t, cascade: scintil_hal_cascade_t):
    # 2 input arguments
    # 0 output arguments
    output_params = {}
    request = f"http://{self.server}:{self.port}/hal{'delegate' if self.delegate else ''}/scintil_hal_controller_run_toggle/{module.value if hasattr(module,'value') else module}/{cascade.value if hasattr(cascade,'value') else cascade}"
    if self.token:
      request += f"?lock-token=" + self.token
    logging.debug("Request : " + request)
    try:
      response = requests.get(request)
      #output_params['response'] = response.text
      logging.debug("Response : " + response.text)
      err_match = re.match(r'.*\nerr=(0x\S+)\n.*', response.text, flags=re.DOTALL)
      err_api_match = re.match(r'(Invalid method.*)', response.text, flags=re.DOTALL)
      output_params['status_code'] = response.status_code
      if err_match:
         output_params['err'] = int(err_match.groups()[0],0)
         output_params['err_hex'] = err_match.groups()[0]
         try:
           output_params['err_str'] = self.getErrorString(output_params['err']) + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      elif err_api_match:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value)
         try:
           output_params['err_str'] = "API Error: " + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      else:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value
         output_params['err_str'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.name
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value)
         output_params['errcode'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN
      if (output_params['err'] and self.shouldraise):
         raise ScintilError(output_params['errcode'] or scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN, output_params)
    except requests.exceptions.RequestException as e:
      ch_error = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL
      output_params['err'] = ch_error.value
      output_params['err_str'] = ch_error.name
      output_params['errcode'] = ch_error
      if (self.shouldraise):
         raise ScintilError(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL, output_params)
    return output_params

  def scintil_hal_controller_get_context( self, module: scintil_hal_module_t, cascade: scintil_hal_cascade_t):
    # 2 input arguments
    # 1 output arguments
    output_params = {}
    request = f"http://{self.server}:{self.port}/hal{'delegate' if self.delegate else ''}/scintil_hal_controller_get_context/{module.value if hasattr(module,'value') else module}/{cascade.value if hasattr(cascade,'value') else cascade}"
    if self.token:
      request += f"?lock-token=" + self.token
    logging.debug("Request : " + request)
    try:
      response = requests.get(request)
      #output_params['response'] = response.text
      logging.debug("Response : " + response.text)
      err_match = re.match(r'.*\nerr=(0x\S+)\n.*', response.text, flags=re.DOTALL)
      err_api_match = re.match(r'(Invalid method.*)', response.text, flags=re.DOTALL)
      output_params['status_code'] = response.status_code
      if err_match:
         output_params['err'] = int(err_match.groups()[0],0)
         output_params['err_hex'] = err_match.groups()[0]
         try:
           output_params['err_str'] = self.getErrorString(output_params['err']) + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      elif err_api_match:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value)
         try:
           output_params['err_str'] = "API Error: " + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      else:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value
         output_params['err_str'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.name
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value)
         output_params['errcode'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN
      if (output_params['err'] and self.shouldraise):
         raise ScintilError(output_params['errcode'] or scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN, output_params)
      ctrl_context_match = re.match(r".*\*ctrl_context=\s*({\S+})", response.text, flags=re.DOTALL)
      if ctrl_context_match:
         output_params['ctrl_context'] = scintil_hal_controller_context_t.fromstring(ctrl_context_match.groups()[0])
      else:
         output_params['ctrl_context'] = None
    except requests.exceptions.RequestException as e:
      ch_error = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL
      output_params['err'] = ch_error.value
      output_params['err_str'] = ch_error.name
      output_params['errcode'] = ch_error
      if (self.shouldraise):
         raise ScintilError(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL, output_params)
    return output_params

  def scintil_hal_controller_output_mpd_simulate( self, module: scintil_hal_module_t, simulate: bool):
    # 2 input arguments
    # 0 output arguments
    output_params = {}
    request = f"http://{self.server}:{self.port}/hal{'delegate' if self.delegate else ''}/scintil_hal_controller_output_mpd_simulate/{module.value if hasattr(module,'value') else module}/{int(simulate)}"
    if self.token:
      request += f"?lock-token=" + self.token
    logging.debug("Request : " + request)
    try:
      response = requests.get(request)
      #output_params['response'] = response.text
      logging.debug("Response : " + response.text)
      err_match = re.match(r'.*\nerr=(0x\S+)\n.*', response.text, flags=re.DOTALL)
      err_api_match = re.match(r'(Invalid method.*)', response.text, flags=re.DOTALL)
      output_params['status_code'] = response.status_code
      if err_match:
         output_params['err'] = int(err_match.groups()[0],0)
         output_params['err_hex'] = err_match.groups()[0]
         try:
           output_params['err_str'] = self.getErrorString(output_params['err']) + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      elif err_api_match:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value)
         try:
           output_params['err_str'] = "API Error: " + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      else:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value
         output_params['err_str'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.name
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value)
         output_params['errcode'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN
      if (output_params['err'] and self.shouldraise):
         raise ScintilError(output_params['errcode'] or scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN, output_params)
    except requests.exceptions.RequestException as e:
      ch_error = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL
      output_params['err'] = ch_error.value
      output_params['err_str'] = ch_error.name
      output_params['errcode'] = ch_error
      if (self.shouldraise):
         raise ScintilError(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL, output_params)
    return output_params

  def scintil_hal_controller_output_mpd_simulated( self, module: scintil_hal_module_t):
    # 1 input arguments
    # 1 output arguments
    output_params = {}
    request = f"http://{self.server}:{self.port}/hal{'delegate' if self.delegate else ''}/scintil_hal_controller_output_mpd_simulated/{module.value if hasattr(module,'value') else module}"
    if self.token:
      request += f"?lock-token=" + self.token
    logging.debug("Request : " + request)
    try:
      response = requests.get(request)
      #output_params['response'] = response.text
      logging.debug("Response : " + response.text)
      err_match = re.match(r'.*\nerr=(0x\S+)\n.*', response.text, flags=re.DOTALL)
      err_api_match = re.match(r'(Invalid method.*)', response.text, flags=re.DOTALL)
      output_params['status_code'] = response.status_code
      if err_match:
         output_params['err'] = int(err_match.groups()[0],0)
         output_params['err_hex'] = err_match.groups()[0]
         try:
           output_params['err_str'] = self.getErrorString(output_params['err']) + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      elif err_api_match:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value)
         try:
           output_params['err_str'] = "API Error: " + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      else:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value
         output_params['err_str'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.name
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value)
         output_params['errcode'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN
      if (output_params['err'] and self.shouldraise):
         raise ScintilError(output_params['errcode'] or scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN, output_params)
      simulated_match = re.match(r".*\*simulated=(\S+)", response.text, flags=re.DOTALL)
      if simulated_match:
         output_params['simulated'] = int(simulated_match.groups()[0])
      else:
         output_params['simulated'] = None
    except requests.exceptions.RequestException as e:
      ch_error = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL
      output_params['err'] = ch_error.value
      output_params['err_str'] = ch_error.name
      output_params['errcode'] = ch_error
      if (self.shouldraise):
         raise ScintilError(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL, output_params)
    return output_params

  def scintil_hal_controller_set_fsm( self, state: scintil_hal_fsm_state_t):
    # 1 input arguments
    # 0 output arguments
    output_params = {}
    request = f"http://{self.server}:{self.port}/hal{'delegate' if self.delegate else ''}/scintil_hal_controller_set_fsm/{state.value if hasattr(state,'value') else state}"
    if self.token:
      request += f"?lock-token=" + self.token
    logging.debug("Request : " + request)
    try:
      response = requests.get(request)
      #output_params['response'] = response.text
      logging.debug("Response : " + response.text)
      err_match = re.match(r'.*\nerr=(0x\S+)\n.*', response.text, flags=re.DOTALL)
      err_api_match = re.match(r'(Invalid method.*)', response.text, flags=re.DOTALL)
      output_params['status_code'] = response.status_code
      if err_match:
         output_params['err'] = int(err_match.groups()[0],0)
         output_params['err_hex'] = err_match.groups()[0]
         try:
           output_params['err_str'] = self.getErrorString(output_params['err']) + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      elif err_api_match:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value)
         try:
           output_params['err_str'] = "API Error: " + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      else:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value
         output_params['err_str'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.name
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value)
         output_params['errcode'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN
      if (output_params['err'] and self.shouldraise):
         raise ScintilError(output_params['errcode'] or scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN, output_params)
    except requests.exceptions.RequestException as e:
      ch_error = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL
      output_params['err'] = ch_error.value
      output_params['err_str'] = ch_error.name
      output_params['errcode'] = ch_error
      if (self.shouldraise):
         raise ScintilError(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL, output_params)
    return output_params

  def scintil_hal_ll_idac_init(self):
    # 0 input arguments
    # 0 output arguments
    output_params = {}
    request = f"http://{self.server}:{self.port}/hal{'delegate' if self.delegate else ''}/scintil_hal_ll_idac_init"
    if self.token:
      request += f"?lock-token=" + self.token
    logging.debug("Request : " + request)
    try:
      response = requests.get(request)
      #output_params['response'] = response.text
      logging.debug("Response : " + response.text)
      err_match = re.match(r'.*\nerr=(0x\S+)\n.*', response.text, flags=re.DOTALL)
      err_api_match = re.match(r'(Invalid method.*)', response.text, flags=re.DOTALL)
      output_params['status_code'] = response.status_code
      if err_match:
         output_params['err'] = int(err_match.groups()[0],0)
         output_params['err_hex'] = err_match.groups()[0]
         try:
           output_params['err_str'] = self.getErrorString(output_params['err']) + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      elif err_api_match:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value)
         try:
           output_params['err_str'] = "API Error: " + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      else:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value
         output_params['err_str'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.name
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value)
         output_params['errcode'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN
      if (output_params['err'] and self.shouldraise):
         raise ScintilError(output_params['errcode'] or scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN, output_params)
    except requests.exceptions.RequestException as e:
      ch_error = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL
      output_params['err'] = ch_error.value
      output_params['err_str'] = ch_error.name
      output_params['errcode'] = ch_error
      if (self.shouldraise):
         raise ScintilError(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL, output_params)
    return output_params

  def scintil_hal_ll_idac_start(self):
    # 0 input arguments
    # 0 output arguments
    output_params = {}
    request = f"http://{self.server}:{self.port}/hal{'delegate' if self.delegate else ''}/scintil_hal_ll_idac_start"
    if self.token:
      request += f"?lock-token=" + self.token
    logging.debug("Request : " + request)
    try:
      response = requests.get(request)
      #output_params['response'] = response.text
      logging.debug("Response : " + response.text)
      err_match = re.match(r'.*\nerr=(0x\S+)\n.*', response.text, flags=re.DOTALL)
      err_api_match = re.match(r'(Invalid method.*)', response.text, flags=re.DOTALL)
      output_params['status_code'] = response.status_code
      if err_match:
         output_params['err'] = int(err_match.groups()[0],0)
         output_params['err_hex'] = err_match.groups()[0]
         try:
           output_params['err_str'] = self.getErrorString(output_params['err']) + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      elif err_api_match:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value)
         try:
           output_params['err_str'] = "API Error: " + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      else:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value
         output_params['err_str'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.name
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value)
         output_params['errcode'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN
      if (output_params['err'] and self.shouldraise):
         raise ScintilError(output_params['errcode'] or scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN, output_params)
    except requests.exceptions.RequestException as e:
      ch_error = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL
      output_params['err'] = ch_error.value
      output_params['err_str'] = ch_error.name
      output_params['errcode'] = ch_error
      if (self.shouldraise):
         raise ScintilError(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL, output_params)
    return output_params

  def scintil_hal_ll_idac_stop(self):
    # 0 input arguments
    # 0 output arguments
    output_params = {}
    request = f"http://{self.server}:{self.port}/hal{'delegate' if self.delegate else ''}/scintil_hal_ll_idac_stop"
    if self.token:
      request += f"?lock-token=" + self.token
    logging.debug("Request : " + request)
    try:
      response = requests.get(request)
      #output_params['response'] = response.text
      logging.debug("Response : " + response.text)
      err_match = re.match(r'.*\nerr=(0x\S+)\n.*', response.text, flags=re.DOTALL)
      err_api_match = re.match(r'(Invalid method.*)', response.text, flags=re.DOTALL)
      output_params['status_code'] = response.status_code
      if err_match:
         output_params['err'] = int(err_match.groups()[0],0)
         output_params['err_hex'] = err_match.groups()[0]
         try:
           output_params['err_str'] = self.getErrorString(output_params['err']) + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      elif err_api_match:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value)
         try:
           output_params['err_str'] = "API Error: " + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      else:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value
         output_params['err_str'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.name
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value)
         output_params['errcode'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN
      if (output_params['err'] and self.shouldraise):
         raise ScintilError(output_params['errcode'] or scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN, output_params)
    except requests.exceptions.RequestException as e:
      ch_error = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL
      output_params['err'] = ch_error.value
      output_params['err_str'] = ch_error.name
      output_params['errcode'] = ch_error
      if (self.shouldraise):
         raise ScintilError(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL, output_params)
    return output_params

  def scintil_hal_ll_idac_get_val( self, dummy: scintil_hal_ll_idac_t):
    # 1 input arguments
    # 1 output arguments
    output_params = {}
    request = f"http://{self.server}:{self.port}/hal{'delegate' if self.delegate else ''}/scintil_hal_ll_idac_get_val/{dummy.value if hasattr(dummy,'value') else dummy}"
    if self.token:
      request += f"?lock-token=" + self.token
    logging.debug("Request : " + request)
    try:
      response = requests.get(request)
      #output_params['response'] = response.text
      logging.debug("Response : " + response.text)
      err_match = re.match(r'.*\nerr=(0x\S+)\n.*', response.text, flags=re.DOTALL)
      err_api_match = re.match(r'(Invalid method.*)', response.text, flags=re.DOTALL)
      output_params['status_code'] = response.status_code
      if err_match:
         output_params['err'] = int(err_match.groups()[0],0)
         output_params['err_hex'] = err_match.groups()[0]
         try:
           output_params['err_str'] = self.getErrorString(output_params['err']) + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      elif err_api_match:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value)
         try:
           output_params['err_str'] = "API Error: " + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      else:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value
         output_params['err_str'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.name
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value)
         output_params['errcode'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN
      if (output_params['err'] and self.shouldraise):
         raise ScintilError(output_params['errcode'] or scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN, output_params)
      val_match = re.match(r".*\*val=(\S+)", response.text, flags=re.DOTALL)
      if val_match:
         output_params['val'] = float(val_match.groups()[0])
      else:
         output_params['val'] = None
    except requests.exceptions.RequestException as e:
      ch_error = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL
      output_params['err'] = ch_error.value
      output_params['err_str'] = ch_error.name
      output_params['errcode'] = ch_error
      if (self.shouldraise):
         raise ScintilError(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL, output_params)
    return output_params

  def scintil_hal_ll_idac_set_val_dc( self, channel: scintil_hal_ll_idac_t, enable: bool, val: float):
    # 3 input arguments
    # 0 output arguments
    output_params = {}
    request = f"http://{self.server}:{self.port}/hal{'delegate' if self.delegate else ''}/scintil_hal_ll_idac_set_val_dc/{channel.value if hasattr(channel,'value') else channel}/{int(enable)}/{val}"
    if self.token:
      request += f"?lock-token=" + self.token
    logging.debug("Request : " + request)
    try:
      response = requests.get(request)
      #output_params['response'] = response.text
      logging.debug("Response : " + response.text)
      err_match = re.match(r'.*\nerr=(0x\S+)\n.*', response.text, flags=re.DOTALL)
      err_api_match = re.match(r'(Invalid method.*)', response.text, flags=re.DOTALL)
      output_params['status_code'] = response.status_code
      if err_match:
         output_params['err'] = int(err_match.groups()[0],0)
         output_params['err_hex'] = err_match.groups()[0]
         try:
           output_params['err_str'] = self.getErrorString(output_params['err']) + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      elif err_api_match:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value)
         try:
           output_params['err_str'] = "API Error: " + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      else:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value
         output_params['err_str'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.name
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value)
         output_params['errcode'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN
      if (output_params['err'] and self.shouldraise):
         raise ScintilError(output_params['errcode'] or scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN, output_params)
    except requests.exceptions.RequestException as e:
      ch_error = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL
      output_params['err'] = ch_error.value
      output_params['err_str'] = ch_error.name
      output_params['errcode'] = ch_error
      if (self.shouldraise):
         raise ScintilError(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL, output_params)
    return output_params

  def scintil_hal_ll_idac_set_val_ac( self, channel: scintil_hal_ll_idac_t, enable: bool, sample_idx: int, val: float):
    # 4 input arguments
    # 0 output arguments
    output_params = {}
    request = f"http://{self.server}:{self.port}/hal{'delegate' if self.delegate else ''}/scintil_hal_ll_idac_set_val_ac/{channel.value if hasattr(channel,'value') else channel}/{int(enable)}/{sample_idx}/{val}"
    if self.token:
      request += f"?lock-token=" + self.token
    logging.debug("Request : " + request)
    try:
      response = requests.get(request)
      #output_params['response'] = response.text
      logging.debug("Response : " + response.text)
      err_match = re.match(r'.*\nerr=(0x\S+)\n.*', response.text, flags=re.DOTALL)
      err_api_match = re.match(r'(Invalid method.*)', response.text, flags=re.DOTALL)
      output_params['status_code'] = response.status_code
      if err_match:
         output_params['err'] = int(err_match.groups()[0],0)
         output_params['err_hex'] = err_match.groups()[0]
         try:
           output_params['err_str'] = self.getErrorString(output_params['err']) + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      elif err_api_match:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value)
         try:
           output_params['err_str'] = "API Error: " + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      else:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value
         output_params['err_str'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.name
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value)
         output_params['errcode'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN
      if (output_params['err'] and self.shouldraise):
         raise ScintilError(output_params['errcode'] or scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN, output_params)
    except requests.exceptions.RequestException as e:
      ch_error = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL
      output_params['err'] = ch_error.value
      output_params['err_str'] = ch_error.name
      output_params['errcode'] = ch_error
      if (self.shouldraise):
         raise ScintilError(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL, output_params)
    return output_params

  def scintil_hal_ll_idac_set_ac_vals( self, channel: scintil_hal_ll_idac_t, array: array):
    # 2 input arguments
    # 0 output arguments
    output_params = {}
    request = f"http://{self.server}:{self.port}/hal{'delegate' if self.delegate else ''}/scintil_hal_ll_idac_set_ac_vals/{channel.value if hasattr(channel,'value') else channel}/{array}/{len(array)}"
    if self.token:
      request += f"?lock-token=" + self.token
    logging.debug("Request : " + request)
    try:
      response = requests.get(request)
      #output_params['response'] = response.text
      logging.debug("Response : " + response.text)
      err_match = re.match(r'.*\nerr=(0x\S+)\n.*', response.text, flags=re.DOTALL)
      err_api_match = re.match(r'(Invalid method.*)', response.text, flags=re.DOTALL)
      output_params['status_code'] = response.status_code
      if err_match:
         output_params['err'] = int(err_match.groups()[0],0)
         output_params['err_hex'] = err_match.groups()[0]
         try:
           output_params['err_str'] = self.getErrorString(output_params['err']) + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      elif err_api_match:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value)
         try:
           output_params['err_str'] = "API Error: " + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      else:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value
         output_params['err_str'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.name
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value)
         output_params['errcode'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN
      if (output_params['err'] and self.shouldraise):
         raise ScintilError(output_params['errcode'] or scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN, output_params)
    except requests.exceptions.RequestException as e:
      ch_error = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL
      output_params['err'] = ch_error.value
      output_params['err_str'] = ch_error.name
      output_params['errcode'] = ch_error
      if (self.shouldraise):
         raise ScintilError(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL, output_params)
    return output_params

  def scintil_hal_ll_vdac_init(self):
    # 0 input arguments
    # 0 output arguments
    output_params = {}
    request = f"http://{self.server}:{self.port}/hal{'delegate' if self.delegate else ''}/scintil_hal_ll_vdac_init"
    if self.token:
      request += f"?lock-token=" + self.token
    logging.debug("Request : " + request)
    try:
      response = requests.get(request)
      #output_params['response'] = response.text
      logging.debug("Response : " + response.text)
      err_match = re.match(r'.*\nerr=(0x\S+)\n.*', response.text, flags=re.DOTALL)
      err_api_match = re.match(r'(Invalid method.*)', response.text, flags=re.DOTALL)
      output_params['status_code'] = response.status_code
      if err_match:
         output_params['err'] = int(err_match.groups()[0],0)
         output_params['err_hex'] = err_match.groups()[0]
         try:
           output_params['err_str'] = self.getErrorString(output_params['err']) + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      elif err_api_match:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value)
         try:
           output_params['err_str'] = "API Error: " + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      else:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value
         output_params['err_str'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.name
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value)
         output_params['errcode'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN
      if (output_params['err'] and self.shouldraise):
         raise ScintilError(output_params['errcode'] or scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN, output_params)
    except requests.exceptions.RequestException as e:
      ch_error = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL
      output_params['err'] = ch_error.value
      output_params['err_str'] = ch_error.name
      output_params['errcode'] = ch_error
      if (self.shouldraise):
         raise ScintilError(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL, output_params)
    return output_params

  def scintil_hal_ll_test(self):
    # 0 input arguments
    # 0 output arguments
    output_params = {}
    request = f"http://{self.server}:{self.port}/hal{'delegate' if self.delegate else ''}/scintil_hal_ll_test"
    if self.token:
      request += f"?lock-token=" + self.token
    logging.debug("Request : " + request)
    try:
      response = requests.get(request)
      #output_params['response'] = response.text
      logging.debug("Response : " + response.text)
      err_match = re.match(r'.*\nerr=(0x\S+)\n.*', response.text, flags=re.DOTALL)
      err_api_match = re.match(r'(Invalid method.*)', response.text, flags=re.DOTALL)
      output_params['status_code'] = response.status_code
      if err_match:
         output_params['err'] = int(err_match.groups()[0],0)
         output_params['err_hex'] = err_match.groups()[0]
         try:
           output_params['err_str'] = self.getErrorString(output_params['err']) + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      elif err_api_match:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value)
         try:
           output_params['err_str'] = "API Error: " + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      else:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value
         output_params['err_str'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.name
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value)
         output_params['errcode'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN
      if (output_params['err'] and self.shouldraise):
         raise ScintilError(output_params['errcode'] or scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN, output_params)
    except requests.exceptions.RequestException as e:
      ch_error = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL
      output_params['err'] = ch_error.value
      output_params['err_str'] = ch_error.name
      output_params['errcode'] = ch_error
      if (self.shouldraise):
         raise ScintilError(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL, output_params)
    return output_params

  def scintil_hal_ll_vdac_set_mux_val( self, channel: scintil_hal_ll_vdac_t, val: float):
    # 2 input arguments
    # 0 output arguments
    output_params = {}
    request = f"http://{self.server}:{self.port}/hal{'delegate' if self.delegate else ''}/scintil_hal_ll_vdac_set_mux_val/{channel.value if hasattr(channel,'value') else channel}/{val}"
    if self.token:
      request += f"?lock-token=" + self.token
    logging.debug("Request : " + request)
    try:
      response = requests.get(request)
      #output_params['response'] = response.text
      logging.debug("Response : " + response.text)
      err_match = re.match(r'.*\nerr=(0x\S+)\n.*', response.text, flags=re.DOTALL)
      err_api_match = re.match(r'(Invalid method.*)', response.text, flags=re.DOTALL)
      output_params['status_code'] = response.status_code
      if err_match:
         output_params['err'] = int(err_match.groups()[0],0)
         output_params['err_hex'] = err_match.groups()[0]
         try:
           output_params['err_str'] = self.getErrorString(output_params['err']) + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      elif err_api_match:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value)
         try:
           output_params['err_str'] = "API Error: " + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      else:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value
         output_params['err_str'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.name
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value)
         output_params['errcode'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN
      if (output_params['err'] and self.shouldraise):
         raise ScintilError(output_params['errcode'] or scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN, output_params)
    except requests.exceptions.RequestException as e:
      ch_error = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL
      output_params['err'] = ch_error.value
      output_params['err_str'] = ch_error.name
      output_params['errcode'] = ch_error
      if (self.shouldraise):
         raise ScintilError(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL, output_params)
    return output_params

  def scintil_hal_ll_vdac_get_mux_val( self, channel: scintil_hal_ll_vdac_t):
    # 1 input arguments
    # 1 output arguments
    output_params = {}
    request = f"http://{self.server}:{self.port}/hal{'delegate' if self.delegate else ''}/scintil_hal_ll_vdac_get_mux_val/{channel.value if hasattr(channel,'value') else channel}"
    if self.token:
      request += f"?lock-token=" + self.token
    logging.debug("Request : " + request)
    try:
      response = requests.get(request)
      #output_params['response'] = response.text
      logging.debug("Response : " + response.text)
      err_match = re.match(r'.*\nerr=(0x\S+)\n.*', response.text, flags=re.DOTALL)
      err_api_match = re.match(r'(Invalid method.*)', response.text, flags=re.DOTALL)
      output_params['status_code'] = response.status_code
      if err_match:
         output_params['err'] = int(err_match.groups()[0],0)
         output_params['err_hex'] = err_match.groups()[0]
         try:
           output_params['err_str'] = self.getErrorString(output_params['err']) + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      elif err_api_match:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value)
         try:
           output_params['err_str'] = "API Error: " + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      else:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value
         output_params['err_str'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.name
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value)
         output_params['errcode'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN
      if (output_params['err'] and self.shouldraise):
         raise ScintilError(output_params['errcode'] or scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN, output_params)
      val_match = re.match(r".*\*val=(\S+)", response.text, flags=re.DOTALL)
      if val_match:
         output_params['val'] = float(val_match.groups()[0])
      else:
         output_params['val'] = None
    except requests.exceptions.RequestException as e:
      ch_error = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL
      output_params['err'] = ch_error.value
      output_params['err_str'] = ch_error.name
      output_params['errcode'] = ch_error
      if (self.shouldraise):
         raise ScintilError(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL, output_params)
    return output_params

  def scintil_hal_ll_vdac_set_ring_val( self, channel: scintil_hal_ll_vdac_ring_out_t, val: float):
    # 2 input arguments
    # 0 output arguments
    output_params = {}
    request = f"http://{self.server}:{self.port}/hal{'delegate' if self.delegate else ''}/scintil_hal_ll_vdac_set_ring_val/{channel.value if hasattr(channel,'value') else channel}/{val}"
    if self.token:
      request += f"?lock-token=" + self.token
    logging.debug("Request : " + request)
    try:
      response = requests.get(request)
      #output_params['response'] = response.text
      logging.debug("Response : " + response.text)
      err_match = re.match(r'.*\nerr=(0x\S+)\n.*', response.text, flags=re.DOTALL)
      err_api_match = re.match(r'(Invalid method.*)', response.text, flags=re.DOTALL)
      output_params['status_code'] = response.status_code
      if err_match:
         output_params['err'] = int(err_match.groups()[0],0)
         output_params['err_hex'] = err_match.groups()[0]
         try:
           output_params['err_str'] = self.getErrorString(output_params['err']) + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      elif err_api_match:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value)
         try:
           output_params['err_str'] = "API Error: " + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      else:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value
         output_params['err_str'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.name
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value)
         output_params['errcode'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN
      if (output_params['err'] and self.shouldraise):
         raise ScintilError(output_params['errcode'] or scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN, output_params)
    except requests.exceptions.RequestException as e:
      ch_error = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL
      output_params['err'] = ch_error.value
      output_params['err_str'] = ch_error.name
      output_params['errcode'] = ch_error
      if (self.shouldraise):
         raise ScintilError(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL, output_params)
    return output_params

  def scintil_hal_ll_vdac_set_instance_reg( self, instance: scintil_hal_ll_vdac_instance_t, reg: scintil_hal_ll_vdac_reg_t, val: int):
    # 3 input arguments
    # 0 output arguments
    output_params = {}
    request = f"http://{self.server}:{self.port}/hal{'delegate' if self.delegate else ''}/scintil_hal_ll_vdac_set_instance_reg/{instance.value if hasattr(instance,'value') else instance}/{reg.value if hasattr(reg,'value') else reg}/{val}"
    if self.token:
      request += f"?lock-token=" + self.token
    logging.debug("Request : " + request)
    try:
      response = requests.get(request)
      #output_params['response'] = response.text
      logging.debug("Response : " + response.text)
      err_match = re.match(r'.*\nerr=(0x\S+)\n.*', response.text, flags=re.DOTALL)
      err_api_match = re.match(r'(Invalid method.*)', response.text, flags=re.DOTALL)
      output_params['status_code'] = response.status_code
      if err_match:
         output_params['err'] = int(err_match.groups()[0],0)
         output_params['err_hex'] = err_match.groups()[0]
         try:
           output_params['err_str'] = self.getErrorString(output_params['err']) + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      elif err_api_match:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value)
         try:
           output_params['err_str'] = "API Error: " + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      else:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value
         output_params['err_str'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.name
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value)
         output_params['errcode'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN
      if (output_params['err'] and self.shouldraise):
         raise ScintilError(output_params['errcode'] or scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN, output_params)
    except requests.exceptions.RequestException as e:
      ch_error = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL
      output_params['err'] = ch_error.value
      output_params['err_str'] = ch_error.name
      output_params['errcode'] = ch_error
      if (self.shouldraise):
         raise ScintilError(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL, output_params)
    return output_params

  def scintil_hal_ll_vdac_get_instance_reg( self, instance: scintil_hal_ll_vdac_instance_t, reg: scintil_hal_ll_vdac_reg_t):
    # 2 input arguments
    # 1 output arguments
    output_params = {}
    request = f"http://{self.server}:{self.port}/hal{'delegate' if self.delegate else ''}/scintil_hal_ll_vdac_get_instance_reg/{instance.value if hasattr(instance,'value') else instance}/{reg.value if hasattr(reg,'value') else reg}"
    if self.token:
      request += f"?lock-token=" + self.token
    logging.debug("Request : " + request)
    try:
      response = requests.get(request)
      #output_params['response'] = response.text
      logging.debug("Response : " + response.text)
      err_match = re.match(r'.*\nerr=(0x\S+)\n.*', response.text, flags=re.DOTALL)
      err_api_match = re.match(r'(Invalid method.*)', response.text, flags=re.DOTALL)
      output_params['status_code'] = response.status_code
      if err_match:
         output_params['err'] = int(err_match.groups()[0],0)
         output_params['err_hex'] = err_match.groups()[0]
         try:
           output_params['err_str'] = self.getErrorString(output_params['err']) + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      elif err_api_match:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value)
         try:
           output_params['err_str'] = "API Error: " + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      else:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value
         output_params['err_str'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.name
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value)
         output_params['errcode'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN
      if (output_params['err'] and self.shouldraise):
         raise ScintilError(output_params['errcode'] or scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN, output_params)
      val_match = re.match(r".*\*val=(\S+)", response.text, flags=re.DOTALL)
      if val_match:
         output_params['val'] = int(val_match.groups()[0])
      else:
         output_params['val'] = None
    except requests.exceptions.RequestException as e:
      ch_error = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL
      output_params['err'] = ch_error.value
      output_params['err_str'] = ch_error.name
      output_params['errcode'] = ch_error
      if (self.shouldraise):
         raise ScintilError(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL, output_params)
    return output_params

  def scintil_hal_fft( self, module: scintil_hal_module_t, allocated: int):
    # 1 input arguments
    # 1 output arguments
    output_params = {}
    request = f"http://{self.server}:{self.port}/hal{'delegate' if self.delegate else ''}/scintil_hal_fft/{module.value if hasattr(module,'value') else module}/{allocated}"
    if self.token:
      request += f"?lock-token=" + self.token
    logging.debug("Request : " + request)
    try:
      response = requests.get(request)
      #output_params['response'] = response.text
      logging.debug("Response : " + response.text)
      err_match = re.match(r'.*\nerr=(0x\S+)\n.*', response.text, flags=re.DOTALL)
      err_api_match = re.match(r'(Invalid method.*)', response.text, flags=re.DOTALL)
      output_params['status_code'] = response.status_code
      if err_match:
         output_params['err'] = int(err_match.groups()[0],0)
         output_params['err_hex'] = err_match.groups()[0]
         try:
           output_params['err_str'] = self.getErrorString(output_params['err']) + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      elif err_api_match:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value)
         try:
           output_params['err_str'] = "API Error: " + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      else:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value
         output_params['err_str'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.name
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value)
         output_params['errcode'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN
      if (output_params['err'] and self.shouldraise):
         raise ScintilError(output_params['errcode'] or scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN, output_params)
      fft_samples_match = re.match(r".*\*fft_samples=(\S+)", response.text, flags=re.DOTALL)
      if fft_samples_match:
         output_params['fft_samples'] = json.loads(fft_samples_match.groups()[0])
      else:
         output_params['fft_samples'] = None
    except requests.exceptions.RequestException as e:
      ch_error = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL
      output_params['err'] = ch_error.value
      output_params['err_str'] = ch_error.name
      output_params['errcode'] = ch_error
      if (self.shouldraise):
         raise ScintilError(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL, output_params)
    return output_params

  def scintil_hal_fft_stop(self):
    # 0 input arguments
    # 0 output arguments
    output_params = {}
    request = f"http://{self.server}:{self.port}/hal{'delegate' if self.delegate else ''}/scintil_hal_fft_stop"
    if self.token:
      request += f"?lock-token=" + self.token
    logging.debug("Request : " + request)
    try:
      response = requests.get(request)
      #output_params['response'] = response.text
      logging.debug("Response : " + response.text)
      err_match = re.match(r'.*\nerr=(0x\S+)\n.*', response.text, flags=re.DOTALL)
      err_api_match = re.match(r'(Invalid method.*)', response.text, flags=re.DOTALL)
      output_params['status_code'] = response.status_code
      if err_match:
         output_params['err'] = int(err_match.groups()[0],0)
         output_params['err_hex'] = err_match.groups()[0]
         try:
           output_params['err_str'] = self.getErrorString(output_params['err']) + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      elif err_api_match:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value)
         try:
           output_params['err_str'] = "API Error: " + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      else:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value
         output_params['err_str'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.name
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value)
         output_params['errcode'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN
      if (output_params['err'] and self.shouldraise):
         raise ScintilError(output_params['errcode'] or scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN, output_params)
    except requests.exceptions.RequestException as e:
      ch_error = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL
      output_params['err'] = ch_error.value
      output_params['err_str'] = ch_error.name
      output_params['errcode'] = ch_error
      if (self.shouldraise):
         raise ScintilError(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL, output_params)
    return output_params

  def scintil_hal_fft_delay( self, delay: int):
    # 1 input arguments
    # 0 output arguments
    output_params = {}
    request = f"http://{self.server}:{self.port}/hal{'delegate' if self.delegate else ''}/scintil_hal_fft_delay/{delay}"
    if self.token:
      request += f"?lock-token=" + self.token
    logging.debug("Request : " + request)
    try:
      response = requests.get(request)
      #output_params['response'] = response.text
      logging.debug("Response : " + response.text)
      err_match = re.match(r'.*\nerr=(0x\S+)\n.*', response.text, flags=re.DOTALL)
      err_api_match = re.match(r'(Invalid method.*)', response.text, flags=re.DOTALL)
      output_params['status_code'] = response.status_code
      if err_match:
         output_params['err'] = int(err_match.groups()[0],0)
         output_params['err_hex'] = err_match.groups()[0]
         try:
           output_params['err_str'] = self.getErrorString(output_params['err']) + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      elif err_api_match:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value)
         try:
           output_params['err_str'] = "API Error: " + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      else:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value
         output_params['err_str'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.name
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value)
         output_params['errcode'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN
      if (output_params['err'] and self.shouldraise):
         raise ScintilError(output_params['errcode'] or scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN, output_params)
    except requests.exceptions.RequestException as e:
      ch_error = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL
      output_params['err'] = ch_error.value
      output_params['err_str'] = ch_error.name
      output_params['errcode'] = ch_error
      if (self.shouldraise):
         raise ScintilError(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL, output_params)
    return output_params

  def scintil_hal_fft_fpga_sample( self, ring_idx: scintil_hal_ll_tia_ring_out_t, sample_idx: int):
    # 2 input arguments
    # 1 output arguments
    output_params = {}
    request = f"http://{self.server}:{self.port}/hal{'delegate' if self.delegate else ''}/scintil_hal_fft_fpga_sample/{ring_idx.value if hasattr(ring_idx,'value') else ring_idx}/{sample_idx}"
    if self.token:
      request += f"?lock-token=" + self.token
    logging.debug("Request : " + request)
    try:
      response = requests.get(request)
      #output_params['response'] = response.text
      logging.debug("Response : " + response.text)
      err_match = re.match(r'.*\nerr=(0x\S+)\n.*', response.text, flags=re.DOTALL)
      err_api_match = re.match(r'(Invalid method.*)', response.text, flags=re.DOTALL)
      output_params['status_code'] = response.status_code
      if err_match:
         output_params['err'] = int(err_match.groups()[0],0)
         output_params['err_hex'] = err_match.groups()[0]
         try:
           output_params['err_str'] = self.getErrorString(output_params['err']) + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      elif err_api_match:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value)
         try:
           output_params['err_str'] = "API Error: " + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      else:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value
         output_params['err_str'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.name
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value)
         output_params['errcode'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN
      if (output_params['err'] and self.shouldraise):
         raise ScintilError(output_params['errcode'] or scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN, output_params)
      data_match = re.match(r".*\*data=(\S+)", response.text, flags=re.DOTALL)
      if data_match:
         output_params['data'] = float(data_match.groups()[0])
      else:
         output_params['data'] = None
    except requests.exceptions.RequestException as e:
      ch_error = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL
      output_params['err'] = ch_error.value
      output_params['err_str'] = ch_error.name
      output_params['errcode'] = ch_error
      if (self.shouldraise):
         raise ScintilError(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL, output_params)
    return output_params

  def scintil_hal_fft_fpga( self, ring_idx: scintil_hal_ll_tia_ring_out_t, allocated: int):
    # 1 input arguments
    # 1 output arguments
    output_params = {}
    request = f"http://{self.server}:{self.port}/hal{'delegate' if self.delegate else ''}/scintil_hal_fft_fpga/{ring_idx.value if hasattr(ring_idx,'value') else ring_idx}/{allocated}"
    if self.token:
      request += f"?lock-token=" + self.token
    logging.debug("Request : " + request)
    try:
      response = requests.get(request)
      #output_params['response'] = response.text
      logging.debug("Response : " + response.text)
      err_match = re.match(r'.*\nerr=(0x\S+)\n.*', response.text, flags=re.DOTALL)
      err_api_match = re.match(r'(Invalid method.*)', response.text, flags=re.DOTALL)
      output_params['status_code'] = response.status_code
      if err_match:
         output_params['err'] = int(err_match.groups()[0],0)
         output_params['err_hex'] = err_match.groups()[0]
         try:
           output_params['err_str'] = self.getErrorString(output_params['err']) + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      elif err_api_match:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value)
         try:
           output_params['err_str'] = "API Error: " + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      else:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value
         output_params['err_str'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.name
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value)
         output_params['errcode'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN
      if (output_params['err'] and self.shouldraise):
         raise ScintilError(output_params['errcode'] or scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN, output_params)
      fft_samples_match = re.match(r".*\*fft_samples=(\S+)", response.text, flags=re.DOTALL)
      if fft_samples_match:
         output_params['fft_samples'] = json.loads(fft_samples_match.groups()[0])
      else:
         output_params['fft_samples'] = None
    except requests.exceptions.RequestException as e:
      ch_error = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL
      output_params['err'] = ch_error.value
      output_params['err_str'] = ch_error.name
      output_params['errcode'] = ch_error
      if (self.shouldraise):
         raise ScintilError(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL, output_params)
    return output_params

  def scintil_hal_fft_fpga_fs(self):
    # 0 input arguments
    # 1 output arguments
    output_params = {}
    request = f"http://{self.server}:{self.port}/hal{'delegate' if self.delegate else ''}/scintil_hal_fft_fpga_fs"
    if self.token:
      request += f"?lock-token=" + self.token
    logging.debug("Request : " + request)
    try:
      response = requests.get(request)
      #output_params['response'] = response.text
      logging.debug("Response : " + response.text)
      err_match = re.match(r'.*\nerr=(0x\S+)\n.*', response.text, flags=re.DOTALL)
      err_api_match = re.match(r'(Invalid method.*)', response.text, flags=re.DOTALL)
      output_params['status_code'] = response.status_code
      if err_match:
         output_params['err'] = int(err_match.groups()[0],0)
         output_params['err_hex'] = err_match.groups()[0]
         try:
           output_params['err_str'] = self.getErrorString(output_params['err']) + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      elif err_api_match:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value)
         try:
           output_params['err_str'] = "API Error: " + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      else:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value
         output_params['err_str'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.name
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value)
         output_params['errcode'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN
      if (output_params['err'] and self.shouldraise):
         raise ScintilError(output_params['errcode'] or scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN, output_params)
      fs_match = re.match(r".*\*fs=(\S+)", response.text, flags=re.DOTALL)
      if fs_match:
         output_params['fs'] = int(fs_match.groups()[0])
      else:
         output_params['fs'] = None
    except requests.exceptions.RequestException as e:
      ch_error = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL
      output_params['err'] = ch_error.value
      output_params['err_str'] = ch_error.name
      output_params['errcode'] = ch_error
      if (self.shouldraise):
         raise ScintilError(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL, output_params)
    return output_params

  def scintil_hal_fft_get_laser_fundamental( self, module: scintil_hal_module_t, laser: scintil_hal_laser_t):
    # 2 input arguments
    # 1 output arguments
    output_params = {}
    request = f"http://{self.server}:{self.port}/hal{'delegate' if self.delegate else ''}/scintil_hal_fft_get_laser_fundamental/{module.value if hasattr(module,'value') else module}/{laser.value if hasattr(laser,'value') else laser}"
    if self.token:
      request += f"?lock-token=" + self.token
    logging.debug("Request : " + request)
    try:
      response = requests.get(request)
      #output_params['response'] = response.text
      logging.debug("Response : " + response.text)
      err_match = re.match(r'.*\nerr=(0x\S+)\n.*', response.text, flags=re.DOTALL)
      err_api_match = re.match(r'(Invalid method.*)', response.text, flags=re.DOTALL)
      output_params['status_code'] = response.status_code
      if err_match:
         output_params['err'] = int(err_match.groups()[0],0)
         output_params['err_hex'] = err_match.groups()[0]
         try:
           output_params['err_str'] = self.getErrorString(output_params['err']) + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      elif err_api_match:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value)
         try:
           output_params['err_str'] = "API Error: " + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      else:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value
         output_params['err_str'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.name
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value)
         output_params['errcode'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN
      if (output_params['err'] and self.shouldraise):
         raise ScintilError(output_params['errcode'] or scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN, output_params)
      fundamental_match = re.match(r".*\*fundamental=(\S+)", response.text, flags=re.DOTALL)
      if fundamental_match:
         output_params['fundamental'] = float(fundamental_match.groups()[0])
      else:
         output_params['fundamental'] = None
    except requests.exceptions.RequestException as e:
      ch_error = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL
      output_params['err'] = ch_error.value
      output_params['err_str'] = ch_error.name
      output_params['errcode'] = ch_error
      if (self.shouldraise):
         raise ScintilError(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL, output_params)
    return output_params

  def scintil_hal_fft_get_laser_first_harmonic( self, module: scintil_hal_module_t, laser: scintil_hal_laser_t):
    # 2 input arguments
    # 1 output arguments
    output_params = {}
    request = f"http://{self.server}:{self.port}/hal{'delegate' if self.delegate else ''}/scintil_hal_fft_get_laser_first_harmonic/{module.value if hasattr(module,'value') else module}/{laser.value if hasattr(laser,'value') else laser}"
    if self.token:
      request += f"?lock-token=" + self.token
    logging.debug("Request : " + request)
    try:
      response = requests.get(request)
      #output_params['response'] = response.text
      logging.debug("Response : " + response.text)
      err_match = re.match(r'.*\nerr=(0x\S+)\n.*', response.text, flags=re.DOTALL)
      err_api_match = re.match(r'(Invalid method.*)', response.text, flags=re.DOTALL)
      output_params['status_code'] = response.status_code
      if err_match:
         output_params['err'] = int(err_match.groups()[0],0)
         output_params['err_hex'] = err_match.groups()[0]
         try:
           output_params['err_str'] = self.getErrorString(output_params['err']) + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      elif err_api_match:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value)
         try:
           output_params['err_str'] = "API Error: " + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      else:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value
         output_params['err_str'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.name
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value)
         output_params['errcode'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN
      if (output_params['err'] and self.shouldraise):
         raise ScintilError(output_params['errcode'] or scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN, output_params)
      first_harmonic_match = re.match(r".*\*first_harmonic=(\S+)", response.text, flags=re.DOTALL)
      if first_harmonic_match:
         output_params['first_harmonic'] = float(first_harmonic_match.groups()[0])
      else:
         output_params['first_harmonic'] = None
    except requests.exceptions.RequestException as e:
      ch_error = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL
      output_params['err'] = ch_error.value
      output_params['err_str'] = ch_error.name
      output_params['errcode'] = ch_error
      if (self.shouldraise):
         raise ScintilError(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL, output_params)
    return output_params

  def scintil_hal_fft_get_laser_phase( self, module: scintil_hal_module_t, laser: scintil_hal_laser_t):
    # 2 input arguments
    # 1 output arguments
    output_params = {}
    request = f"http://{self.server}:{self.port}/hal{'delegate' if self.delegate else ''}/scintil_hal_fft_get_laser_phase/{module.value if hasattr(module,'value') else module}/{laser.value if hasattr(laser,'value') else laser}"
    if self.token:
      request += f"?lock-token=" + self.token
    logging.debug("Request : " + request)
    try:
      response = requests.get(request)
      #output_params['response'] = response.text
      logging.debug("Response : " + response.text)
      err_match = re.match(r'.*\nerr=(0x\S+)\n.*', response.text, flags=re.DOTALL)
      err_api_match = re.match(r'(Invalid method.*)', response.text, flags=re.DOTALL)
      output_params['status_code'] = response.status_code
      if err_match:
         output_params['err'] = int(err_match.groups()[0],0)
         output_params['err_hex'] = err_match.groups()[0]
         try:
           output_params['err_str'] = self.getErrorString(output_params['err']) + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      elif err_api_match:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value)
         try:
           output_params['err_str'] = "API Error: " + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      else:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value
         output_params['err_str'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.name
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value)
         output_params['errcode'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN
      if (output_params['err'] and self.shouldraise):
         raise ScintilError(output_params['errcode'] or scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN, output_params)
      phase_match = re.match(r".*\*phase=(\S+)", response.text, flags=re.DOTALL)
      if phase_match:
         output_params['phase'] = float(phase_match.groups()[0])
      else:
         output_params['phase'] = None
    except requests.exceptions.RequestException as e:
      ch_error = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL
      output_params['err'] = ch_error.value
      output_params['err_str'] = ch_error.name
      output_params['errcode'] = ch_error
      if (self.shouldraise):
         raise ScintilError(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL, output_params)
    return output_params

  def scintil_hal_fft_get_laser_magnitude( self, module: scintil_hal_module_t, laser: scintil_hal_laser_t):
    # 2 input arguments
    # 1 output arguments
    output_params = {}
    request = f"http://{self.server}:{self.port}/hal{'delegate' if self.delegate else ''}/scintil_hal_fft_get_laser_magnitude/{module.value if hasattr(module,'value') else module}/{laser.value if hasattr(laser,'value') else laser}"
    if self.token:
      request += f"?lock-token=" + self.token
    logging.debug("Request : " + request)
    try:
      response = requests.get(request)
      #output_params['response'] = response.text
      logging.debug("Response : " + response.text)
      err_match = re.match(r'.*\nerr=(0x\S+)\n.*', response.text, flags=re.DOTALL)
      err_api_match = re.match(r'(Invalid method.*)', response.text, flags=re.DOTALL)
      output_params['status_code'] = response.status_code
      if err_match:
         output_params['err'] = int(err_match.groups()[0],0)
         output_params['err_hex'] = err_match.groups()[0]
         try:
           output_params['err_str'] = self.getErrorString(output_params['err']) + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      elif err_api_match:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value)
         try:
           output_params['err_str'] = "API Error: " + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      else:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value
         output_params['err_str'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.name
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value)
         output_params['errcode'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN
      if (output_params['err'] and self.shouldraise):
         raise ScintilError(output_params['errcode'] or scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN, output_params)
      magnitude_match = re.match(r".*\*magnitude=(\S+)", response.text, flags=re.DOTALL)
      if magnitude_match:
         output_params['magnitude'] = float(magnitude_match.groups()[0])
      else:
         output_params['magnitude'] = None
    except requests.exceptions.RequestException as e:
      ch_error = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL
      output_params['err'] = ch_error.value
      output_params['err_str'] = ch_error.name
      output_params['errcode'] = ch_error
      if (self.shouldraise):
         raise ScintilError(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL, output_params)
    return output_params

  def scintil_hal_wait_us( self, microseconds: int):
    # 1 input arguments
    # 0 output arguments
    output_params = {}
    request = f"http://{self.server}:{self.port}/hal{'delegate' if self.delegate else ''}/scintil_hal_wait_us/{microseconds}"
    if self.token:
      request += f"?lock-token=" + self.token
    logging.debug("Request : " + request)
    try:
      response = requests.get(request)
      #output_params['response'] = response.text
      logging.debug("Response : " + response.text)
      err_match = re.match(r'.*\nerr=(0x\S+)\n.*', response.text, flags=re.DOTALL)
      err_api_match = re.match(r'(Invalid method.*)', response.text, flags=re.DOTALL)
      output_params['status_code'] = response.status_code
      if err_match:
         output_params['err'] = int(err_match.groups()[0],0)
         output_params['err_hex'] = err_match.groups()[0]
         try:
           output_params['err_str'] = self.getErrorString(output_params['err']) + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      elif err_api_match:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value)
         try:
           output_params['err_str'] = "API Error: " + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      else:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value
         output_params['err_str'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.name
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value)
         output_params['errcode'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN
      if (output_params['err'] and self.shouldraise):
         raise ScintilError(output_params['errcode'] or scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN, output_params)
    except requests.exceptions.RequestException as e:
      ch_error = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL
      output_params['err'] = ch_error.value
      output_params['err_str'] = ch_error.name
      output_params['errcode'] = ch_error
      if (self.shouldraise):
         raise ScintilError(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL, output_params)
    return output_params

  def scintil_release_instance(self):
    # 0 input arguments
    # 0 output arguments
    output_params = {}
    request = f"http://{self.server}:{self.port}/hal{'delegate' if self.delegate else ''}/scintil_release_instance"
    if self.token:
      request += f"?lock-token=" + self.token
    logging.debug("Request : " + request)
    try:
      response = requests.get(request)
      #output_params['response'] = response.text
      logging.debug("Response : " + response.text)
      err_match = re.match(r'.*\nerr=(0x\S+)\n.*', response.text, flags=re.DOTALL)
      err_api_match = re.match(r'(Invalid method.*)', response.text, flags=re.DOTALL)
      output_params['status_code'] = response.status_code
      if err_match:
         output_params['err'] = int(err_match.groups()[0],0)
         output_params['err_hex'] = err_match.groups()[0]
         try:
           output_params['err_str'] = self.getErrorString(output_params['err']) + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      elif err_api_match:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value)
         try:
           output_params['err_str'] = "API Error: " + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      else:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value
         output_params['err_str'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.name
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value)
         output_params['errcode'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN
      if (output_params['err'] and self.shouldraise):
         raise ScintilError(output_params['errcode'] or scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN, output_params)
    except requests.exceptions.RequestException as e:
      ch_error = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL
      output_params['err'] = ch_error.value
      output_params['err_str'] = ch_error.name
      output_params['errcode'] = ch_error
      if (self.shouldraise):
         raise ScintilError(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL, output_params)
    return output_params

  def scintil_hal_init(self):
    # 0 input arguments
    # 0 output arguments
    output_params = {}
    request = f"http://{self.server}:{self.port}/hal{'delegate' if self.delegate else ''}/scintil_hal_init"
    if self.token:
      request += f"?lock-token=" + self.token
    logging.debug("Request : " + request)
    try:
      response = requests.get(request)
      #output_params['response'] = response.text
      logging.debug("Response : " + response.text)
      err_match = re.match(r'.*\nerr=(0x\S+)\n.*', response.text, flags=re.DOTALL)
      err_api_match = re.match(r'(Invalid method.*)', response.text, flags=re.DOTALL)
      output_params['status_code'] = response.status_code
      if err_match:
         output_params['err'] = int(err_match.groups()[0],0)
         output_params['err_hex'] = err_match.groups()[0]
         try:
           output_params['err_str'] = self.getErrorString(output_params['err']) + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      elif err_api_match:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value)
         try:
           output_params['err_str'] = "API Error: " + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      else:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value
         output_params['err_str'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.name
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value)
         output_params['errcode'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN
      if (output_params['err'] and self.shouldraise):
         raise ScintilError(output_params['errcode'] or scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN, output_params)
    except requests.exceptions.RequestException as e:
      ch_error = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL
      output_params['err'] = ch_error.value
      output_params['err_str'] = ch_error.name
      output_params['errcode'] = ch_error
      if (self.shouldraise):
         raise ScintilError(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL, output_params)
    return output_params

  def scintil_hal_reg_get_single( self, addr: int):
    # 1 input arguments
    # 1 output arguments
    output_params = {}
    request = f"http://{self.server}:{self.port}/hal{'delegate' if self.delegate else ''}/scintil_hal_reg_get_single/{addr}"
    if self.token:
      request += f"?lock-token=" + self.token
    logging.debug("Request : " + request)
    try:
      response = requests.get(request)
      #output_params['response'] = response.text
      logging.debug("Response : " + response.text)
      err_match = re.match(r'.*\nerr=(0x\S+)\n.*', response.text, flags=re.DOTALL)
      err_api_match = re.match(r'(Invalid method.*)', response.text, flags=re.DOTALL)
      output_params['status_code'] = response.status_code
      if err_match:
         output_params['err'] = int(err_match.groups()[0],0)
         output_params['err_hex'] = err_match.groups()[0]
         try:
           output_params['err_str'] = self.getErrorString(output_params['err']) + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      elif err_api_match:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value)
         try:
           output_params['err_str'] = "API Error: " + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      else:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value
         output_params['err_str'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.name
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value)
         output_params['errcode'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN
      if (output_params['err'] and self.shouldraise):
         raise ScintilError(output_params['errcode'] or scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN, output_params)
      value_match = re.match(r".*\*value=(\S+)", response.text, flags=re.DOTALL)
      if value_match:
         output_params['value'] = int(value_match.groups()[0])
      else:
         output_params['value'] = None
    except requests.exceptions.RequestException as e:
      ch_error = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL
      output_params['err'] = ch_error.value
      output_params['err_str'] = ch_error.name
      output_params['errcode'] = ch_error
      if (self.shouldraise):
         raise ScintilError(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL, output_params)
    return output_params

  def scintil_hal_reg_get_single_signed( self, addr: int):
    # 1 input arguments
    # 1 output arguments
    output_params = {}
    request = f"http://{self.server}:{self.port}/hal{'delegate' if self.delegate else ''}/scintil_hal_reg_get_single_signed/{addr}"
    if self.token:
      request += f"?lock-token=" + self.token
    logging.debug("Request : " + request)
    try:
      response = requests.get(request)
      #output_params['response'] = response.text
      logging.debug("Response : " + response.text)
      err_match = re.match(r'.*\nerr=(0x\S+)\n.*', response.text, flags=re.DOTALL)
      err_api_match = re.match(r'(Invalid method.*)', response.text, flags=re.DOTALL)
      output_params['status_code'] = response.status_code
      if err_match:
         output_params['err'] = int(err_match.groups()[0],0)
         output_params['err_hex'] = err_match.groups()[0]
         try:
           output_params['err_str'] = self.getErrorString(output_params['err']) + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      elif err_api_match:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value)
         try:
           output_params['err_str'] = "API Error: " + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      else:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value
         output_params['err_str'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.name
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value)
         output_params['errcode'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN
      if (output_params['err'] and self.shouldraise):
         raise ScintilError(output_params['errcode'] or scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN, output_params)
      signed_reg_match = re.match(r".*\*signed_reg=(\S+)", response.text, flags=re.DOTALL)
      if signed_reg_match:
         output_params['signed_reg'] = int(signed_reg_match.groups()[0])
      else:
         output_params['signed_reg'] = None
    except requests.exceptions.RequestException as e:
      ch_error = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL
      output_params['err'] = ch_error.value
      output_params['err_str'] = ch_error.name
      output_params['errcode'] = ch_error
      if (self.shouldraise):
         raise ScintilError(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL, output_params)
    return output_params

  def scintil_hal_reg_set_single( self, addr: int, value: int):
    # 2 input arguments
    # 0 output arguments
    output_params = {}
    request = f"http://{self.server}:{self.port}/hal{'delegate' if self.delegate else ''}/scintil_hal_reg_set_single/{addr}/{value}"
    if self.token:
      request += f"?lock-token=" + self.token
    logging.debug("Request : " + request)
    try:
      response = requests.get(request)
      #output_params['response'] = response.text
      logging.debug("Response : " + response.text)
      err_match = re.match(r'.*\nerr=(0x\S+)\n.*', response.text, flags=re.DOTALL)
      err_api_match = re.match(r'(Invalid method.*)', response.text, flags=re.DOTALL)
      output_params['status_code'] = response.status_code
      if err_match:
         output_params['err'] = int(err_match.groups()[0],0)
         output_params['err_hex'] = err_match.groups()[0]
         try:
           output_params['err_str'] = self.getErrorString(output_params['err']) + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      elif err_api_match:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value)
         try:
           output_params['err_str'] = "API Error: " + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      else:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value
         output_params['err_str'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.name
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value)
         output_params['errcode'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN
      if (output_params['err'] and self.shouldraise):
         raise ScintilError(output_params['errcode'] or scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN, output_params)
    except requests.exceptions.RequestException as e:
      ch_error = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL
      output_params['err'] = ch_error.value
      output_params['err_str'] = ch_error.name
      output_params['errcode'] = ch_error
      if (self.shouldraise):
         raise ScintilError(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL, output_params)
    return output_params

  def scintil_hal_mem_read( self, addr: int, allocated_size: int):
    # 1 input arguments
    # 1 output arguments
    output_params = {}
    request = f"http://{self.server}:{self.port}/hal{'delegate' if self.delegate else ''}/scintil_hal_mem_read/{addr}/{allocated_size}"
    if self.token:
      request += f"?lock-token=" + self.token
    logging.debug("Request : " + request)
    try:
      response = requests.get(request)
      #output_params['response'] = response.text
      logging.debug("Response : " + response.text)
      err_match = re.match(r'.*\nerr=(0x\S+)\n.*', response.text, flags=re.DOTALL)
      err_api_match = re.match(r'(Invalid method.*)', response.text, flags=re.DOTALL)
      output_params['status_code'] = response.status_code
      if err_match:
         output_params['err'] = int(err_match.groups()[0],0)
         output_params['err_hex'] = err_match.groups()[0]
         try:
           output_params['err_str'] = self.getErrorString(output_params['err']) + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      elif err_api_match:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value)
         try:
           output_params['err_str'] = "API Error: " + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      else:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value
         output_params['err_str'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.name
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value)
         output_params['errcode'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN
      if (output_params['err'] and self.shouldraise):
         raise ScintilError(output_params['errcode'] or scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN, output_params)
      array_match = re.match(r".*\*array=(\S+)", response.text, flags=re.DOTALL)
      if array_match:
         output_params['array'] = json.loads(array_match.groups()[0])
      else:
         output_params['array'] = None
    except requests.exceptions.RequestException as e:
      ch_error = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL
      output_params['err'] = ch_error.value
      output_params['err_str'] = ch_error.name
      output_params['errcode'] = ch_error
      if (self.shouldraise):
         raise ScintilError(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL, output_params)
    return output_params

  def scintil_hal_mem_write( self, addr: int, array: array):
    # 2 input arguments
    # 0 output arguments
    output_params = {}
    request = f"http://{self.server}:{self.port}/hal{'delegate' if self.delegate else ''}/scintil_hal_mem_write/{addr}/{array}/{len(array)}"
    if self.token:
      request += f"?lock-token=" + self.token
    logging.debug("Request : " + request)
    try:
      response = requests.get(request)
      #output_params['response'] = response.text
      logging.debug("Response : " + response.text)
      err_match = re.match(r'.*\nerr=(0x\S+)\n.*', response.text, flags=re.DOTALL)
      err_api_match = re.match(r'(Invalid method.*)', response.text, flags=re.DOTALL)
      output_params['status_code'] = response.status_code
      if err_match:
         output_params['err'] = int(err_match.groups()[0],0)
         output_params['err_hex'] = err_match.groups()[0]
         try:
           output_params['err_str'] = self.getErrorString(output_params['err']) + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      elif err_api_match:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value)
         try:
           output_params['err_str'] = "API Error: " + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      else:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value
         output_params['err_str'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.name
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value)
         output_params['errcode'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN
      if (output_params['err'] and self.shouldraise):
         raise ScintilError(output_params['errcode'] or scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN, output_params)
    except requests.exceptions.RequestException as e:
      ch_error = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL
      output_params['err'] = ch_error.value
      output_params['err_str'] = ch_error.name
      output_params['errcode'] = ch_error
      if (self.shouldraise):
         raise ScintilError(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL, output_params)
    return output_params

  def scintil_hal_sys_reset( self, reset_type: scintil_hal_sys_reset_bit_t):
    # 1 input arguments
    # 0 output arguments
    output_params = {}
    request = f"http://{self.server}:{self.port}/hal{'delegate' if self.delegate else ''}/scintil_hal_sys_reset/{reset_type.value if hasattr(reset_type,'value') else reset_type}"
    if self.token:
      request += f"?lock-token=" + self.token
    logging.debug("Request : " + request)
    try:
      response = requests.get(request)
      #output_params['response'] = response.text
      logging.debug("Response : " + response.text)
      err_match = re.match(r'.*\nerr=(0x\S+)\n.*', response.text, flags=re.DOTALL)
      err_api_match = re.match(r'(Invalid method.*)', response.text, flags=re.DOTALL)
      output_params['status_code'] = response.status_code
      if err_match:
         output_params['err'] = int(err_match.groups()[0],0)
         output_params['err_hex'] = err_match.groups()[0]
         try:
           output_params['err_str'] = self.getErrorString(output_params['err']) + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      elif err_api_match:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value)
         try:
           output_params['err_str'] = "API Error: " + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      else:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value
         output_params['err_str'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.name
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value)
         output_params['errcode'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN
      if (output_params['err'] and self.shouldraise):
         raise ScintilError(output_params['errcode'] or scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN, output_params)
    except requests.exceptions.RequestException as e:
      ch_error = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL
      output_params['err'] = ch_error.value
      output_params['err_str'] = ch_error.name
      output_params['errcode'] = ch_error
      if (self.shouldraise):
         raise ScintilError(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL, output_params)
    return output_params

  def scintil_hal_sys_reset_top(self):
    # 0 input arguments
    # 0 output arguments
    output_params = {}
    request = f"http://{self.server}:{self.port}/hal{'delegate' if self.delegate else ''}/scintil_hal_sys_reset_top"
    if self.token:
      request += f"?lock-token=" + self.token
    logging.debug("Request : " + request)
    try:
      response = requests.get(request)
      #output_params['response'] = response.text
      logging.debug("Response : " + response.text)
      err_match = re.match(r'.*\nerr=(0x\S+)\n.*', response.text, flags=re.DOTALL)
      err_api_match = re.match(r'(Invalid method.*)', response.text, flags=re.DOTALL)
      output_params['status_code'] = response.status_code
      if err_match:
         output_params['err'] = int(err_match.groups()[0],0)
         output_params['err_hex'] = err_match.groups()[0]
         try:
           output_params['err_str'] = self.getErrorString(output_params['err']) + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      elif err_api_match:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value)
         try:
           output_params['err_str'] = "API Error: " + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      else:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value
         output_params['err_str'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.name
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value)
         output_params['errcode'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN
      if (output_params['err'] and self.shouldraise):
         raise ScintilError(output_params['errcode'] or scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN, output_params)
    except requests.exceptions.RequestException as e:
      ch_error = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL
      output_params['err'] = ch_error.value
      output_params['err_str'] = ch_error.name
      output_params['errcode'] = ch_error
      if (self.shouldraise):
         raise ScintilError(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL, output_params)
    return output_params

  def scintil_hal_tunable_set_defaults(self):
    # 0 input arguments
    # 0 output arguments
    output_params = {}
    request = f"http://{self.server}:{self.port}/hal{'delegate' if self.delegate else ''}/scintil_hal_tunable_set_defaults"
    if self.token:
      request += f"?lock-token=" + self.token
    logging.debug("Request : " + request)
    try:
      response = requests.get(request)
      #output_params['response'] = response.text
      logging.debug("Response : " + response.text)
      err_match = re.match(r'.*\nerr=(0x\S+)\n.*', response.text, flags=re.DOTALL)
      err_api_match = re.match(r'(Invalid method.*)', response.text, flags=re.DOTALL)
      output_params['status_code'] = response.status_code
      if err_match:
         output_params['err'] = int(err_match.groups()[0],0)
         output_params['err_hex'] = err_match.groups()[0]
         try:
           output_params['err_str'] = self.getErrorString(output_params['err']) + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      elif err_api_match:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value)
         try:
           output_params['err_str'] = "API Error: " + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      else:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value
         output_params['err_str'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.name
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value)
         output_params['errcode'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN
      if (output_params['err'] and self.shouldraise):
         raise ScintilError(output_params['errcode'] or scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN, output_params)
    except requests.exceptions.RequestException as e:
      ch_error = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL
      output_params['err'] = ch_error.value
      output_params['err_str'] = ch_error.name
      output_params['errcode'] = ch_error
      if (self.shouldraise):
         raise ScintilError(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL, output_params)
    return output_params

  def scintil_hal_tunable_get_default( self, tunable: scintil_hal_tunable_t):
    # 1 input arguments
    # 2 output arguments
    output_params = {}
    request = f"http://{self.server}:{self.port}/hal{'delegate' if self.delegate else ''}/scintil_hal_tunable_get_default/{tunable.value if hasattr(tunable,'value') else tunable}"
    if self.token:
      request += f"?lock-token=" + self.token
    logging.debug("Request : " + request)
    try:
      response = requests.get(request)
      #output_params['response'] = response.text
      logging.debug("Response : " + response.text)
      err_match = re.match(r'.*\nerr=(0x\S+)\n.*', response.text, flags=re.DOTALL)
      err_api_match = re.match(r'(Invalid method.*)', response.text, flags=re.DOTALL)
      output_params['status_code'] = response.status_code
      if err_match:
         output_params['err'] = int(err_match.groups()[0],0)
         output_params['err_hex'] = err_match.groups()[0]
         try:
           output_params['err_str'] = self.getErrorString(output_params['err']) + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      elif err_api_match:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value)
         try:
           output_params['err_str'] = "API Error: " + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      else:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value
         output_params['err_str'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.name
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value)
         output_params['errcode'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN
      if (output_params['err'] and self.shouldraise):
         raise ScintilError(output_params['errcode'] or scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN, output_params)
      default_value_match = re.match(r".*\*default_value=(\S+)", response.text, flags=re.DOTALL)
      if default_value_match:
         output_params['default_value'] = int(default_value_match.groups()[0])
      else:
         output_params['default_value'] = None
      current_value_match = re.match(r".*\*current_value=(\S+)", response.text, flags=re.DOTALL)
      if current_value_match:
         output_params['current_value'] = int(current_value_match.groups()[0])
      else:
         output_params['current_value'] = None
    except requests.exceptions.RequestException as e:
      ch_error = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL
      output_params['err'] = ch_error.value
      output_params['err_str'] = ch_error.name
      output_params['errcode'] = ch_error
      if (self.shouldraise):
         raise ScintilError(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL, output_params)
    return output_params

  def scintil_hal_tunable_get( self, tunable: scintil_hal_tunable_t):
    # 1 input arguments
    # 1 output arguments
    output_params = {}
    request = f"http://{self.server}:{self.port}/hal{'delegate' if self.delegate else ''}/scintil_hal_tunable_get/{tunable.value if hasattr(tunable,'value') else tunable}"
    if self.token:
      request += f"?lock-token=" + self.token
    logging.debug("Request : " + request)
    try:
      response = requests.get(request)
      #output_params['response'] = response.text
      logging.debug("Response : " + response.text)
      err_match = re.match(r'.*\nerr=(0x\S+)\n.*', response.text, flags=re.DOTALL)
      err_api_match = re.match(r'(Invalid method.*)', response.text, flags=re.DOTALL)
      output_params['status_code'] = response.status_code
      if err_match:
         output_params['err'] = int(err_match.groups()[0],0)
         output_params['err_hex'] = err_match.groups()[0]
         try:
           output_params['err_str'] = self.getErrorString(output_params['err']) + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      elif err_api_match:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value)
         try:
           output_params['err_str'] = "API Error: " + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      else:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value
         output_params['err_str'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.name
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value)
         output_params['errcode'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN
      if (output_params['err'] and self.shouldraise):
         raise ScintilError(output_params['errcode'] or scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN, output_params)
      tunable_value_match = re.match(r".*\*tunable_value=(\S+)", response.text, flags=re.DOTALL)
      if tunable_value_match:
         output_params['tunable_value'] = int(tunable_value_match.groups()[0])
      else:
         output_params['tunable_value'] = None
    except requests.exceptions.RequestException as e:
      ch_error = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL
      output_params['err'] = ch_error.value
      output_params['err_str'] = ch_error.name
      output_params['errcode'] = ch_error
      if (self.shouldraise):
         raise ScintilError(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL, output_params)
    return output_params

  def scintil_hal_tunable_set( self, tunable: scintil_hal_tunable_t, tunable_value: int):
    # 2 input arguments
    # 0 output arguments
    output_params = {}
    request = f"http://{self.server}:{self.port}/hal{'delegate' if self.delegate else ''}/scintil_hal_tunable_set/{tunable.value if hasattr(tunable,'value') else tunable}/{tunable_value}"
    if self.token:
      request += f"?lock-token=" + self.token
    logging.debug("Request : " + request)
    try:
      response = requests.get(request)
      #output_params['response'] = response.text
      logging.debug("Response : " + response.text)
      err_match = re.match(r'.*\nerr=(0x\S+)\n.*', response.text, flags=re.DOTALL)
      err_api_match = re.match(r'(Invalid method.*)', response.text, flags=re.DOTALL)
      output_params['status_code'] = response.status_code
      if err_match:
         output_params['err'] = int(err_match.groups()[0],0)
         output_params['err_hex'] = err_match.groups()[0]
         try:
           output_params['err_str'] = self.getErrorString(output_params['err']) + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      elif err_api_match:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value)
         try:
           output_params['err_str'] = "API Error: " + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      else:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value
         output_params['err_str'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.name
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value)
         output_params['errcode'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN
      if (output_params['err'] and self.shouldraise):
         raise ScintilError(output_params['errcode'] or scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN, output_params)
    except requests.exceptions.RequestException as e:
      ch_error = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL
      output_params['err'] = ch_error.value
      output_params['err_str'] = ch_error.name
      output_params['errcode'] = ch_error
      if (self.shouldraise):
         raise ScintilError(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL, output_params)
    return output_params

  def scintil_hal_ll_tia_get_mux_out( self, channel_idx: scintil_hal_ll_tia_mux_out_t):
    # 1 input arguments
    # 1 output arguments
    output_params = {}
    request = f"http://{self.server}:{self.port}/hal{'delegate' if self.delegate else ''}/scintil_hal_ll_tia_get_mux_out/{channel_idx.value if hasattr(channel_idx,'value') else channel_idx}"
    if self.token:
      request += f"?lock-token=" + self.token
    logging.debug("Request : " + request)
    try:
      response = requests.get(request)
      #output_params['response'] = response.text
      logging.debug("Response : " + response.text)
      err_match = re.match(r'.*\nerr=(0x\S+)\n.*', response.text, flags=re.DOTALL)
      err_api_match = re.match(r'(Invalid method.*)', response.text, flags=re.DOTALL)
      output_params['status_code'] = response.status_code
      if err_match:
         output_params['err'] = int(err_match.groups()[0],0)
         output_params['err_hex'] = err_match.groups()[0]
         try:
           output_params['err_str'] = self.getErrorString(output_params['err']) + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      elif err_api_match:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value)
         try:
           output_params['err_str'] = "API Error: " + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      else:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value
         output_params['err_str'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.name
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value)
         output_params['errcode'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN
      if (output_params['err'] and self.shouldraise):
         raise ScintilError(output_params['errcode'] or scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN, output_params)
      val_match = re.match(r".*\*val=(\S+)", response.text, flags=re.DOTALL)
      if val_match:
         output_params['val'] = float(val_match.groups()[0])
      else:
         output_params['val'] = None
    except requests.exceptions.RequestException as e:
      ch_error = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL
      output_params['err'] = ch_error.value
      output_params['err_str'] = ch_error.name
      output_params['errcode'] = ch_error
      if (self.shouldraise):
         raise ScintilError(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL, output_params)
    return output_params

  def scintil_hal_ll_tia_get_ring_value( self, ring_idx: scintil_hal_ll_tia_ring_out_t, ring_type: scintil_hal_ring_type_t):
    # 2 input arguments
    # 1 output arguments
    output_params = {}
    request = f"http://{self.server}:{self.port}/hal{'delegate' if self.delegate else ''}/scintil_hal_ll_tia_get_ring_value/{ring_idx.value if hasattr(ring_idx,'value') else ring_idx}/{ring_type.value if hasattr(ring_type,'value') else ring_type}"
    if self.token:
      request += f"?lock-token=" + self.token
    logging.debug("Request : " + request)
    try:
      response = requests.get(request)
      #output_params['response'] = response.text
      logging.debug("Response : " + response.text)
      err_match = re.match(r'.*\nerr=(0x\S+)\n.*', response.text, flags=re.DOTALL)
      err_api_match = re.match(r'(Invalid method.*)', response.text, flags=re.DOTALL)
      output_params['status_code'] = response.status_code
      if err_match:
         output_params['err'] = int(err_match.groups()[0],0)
         output_params['err_hex'] = err_match.groups()[0]
         try:
           output_params['err_str'] = self.getErrorString(output_params['err']) + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      elif err_api_match:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value)
         try:
           output_params['err_str'] = "API Error: " + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      else:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value
         output_params['err_str'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.name
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value)
         output_params['errcode'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN
      if (output_params['err'] and self.shouldraise):
         raise ScintilError(output_params['errcode'] or scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN, output_params)
      val_match = re.match(r".*\*val=(\S+)", response.text, flags=re.DOTALL)
      if val_match:
         output_params['val'] = float(val_match.groups()[0])
      else:
         output_params['val'] = None
    except requests.exceptions.RequestException as e:
      ch_error = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL
      output_params['err'] = ch_error.value
      output_params['err_str'] = ch_error.name
      output_params['errcode'] = ch_error
      if (self.shouldraise):
         raise ScintilError(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL, output_params)
    return output_params

  def scintil_hal_ll_tia_get_fpga_mux_out( self, channel_idx: scintil_hal_ll_tia_mux_out_t):
    # 1 input arguments
    # 1 output arguments
    output_params = {}
    request = f"http://{self.server}:{self.port}/hal{'delegate' if self.delegate else ''}/scintil_hal_ll_tia_get_fpga_mux_out/{channel_idx.value if hasattr(channel_idx,'value') else channel_idx}"
    if self.token:
      request += f"?lock-token=" + self.token
    logging.debug("Request : " + request)
    try:
      response = requests.get(request)
      #output_params['response'] = response.text
      logging.debug("Response : " + response.text)
      err_match = re.match(r'.*\nerr=(0x\S+)\n.*', response.text, flags=re.DOTALL)
      err_api_match = re.match(r'(Invalid method.*)', response.text, flags=re.DOTALL)
      output_params['status_code'] = response.status_code
      if err_match:
         output_params['err'] = int(err_match.groups()[0],0)
         output_params['err_hex'] = err_match.groups()[0]
         try:
           output_params['err_str'] = self.getErrorString(output_params['err']) + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      elif err_api_match:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value)
         try:
           output_params['err_str'] = "API Error: " + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      else:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value
         output_params['err_str'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.name
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value)
         output_params['errcode'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN
      if (output_params['err'] and self.shouldraise):
         raise ScintilError(output_params['errcode'] or scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN, output_params)
      val_match = re.match(r".*\*val=(\S+)", response.text, flags=re.DOTALL)
      if val_match:
         output_params['val'] = float(val_match.groups()[0])
      else:
         output_params['val'] = None
    except requests.exceptions.RequestException as e:
      ch_error = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL
      output_params['err'] = ch_error.value
      output_params['err_str'] = ch_error.name
      output_params['errcode'] = ch_error
      if (self.shouldraise):
         raise ScintilError(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL, output_params)
    return output_params

  def scintil_hal_ll_tia_get_fpga_ring_value( self, ring_idx: scintil_hal_ll_tia_ring_out_t):
    # 1 input arguments
    # 1 output arguments
    output_params = {}
    request = f"http://{self.server}:{self.port}/hal{'delegate' if self.delegate else ''}/scintil_hal_ll_tia_get_fpga_ring_value/{ring_idx.value if hasattr(ring_idx,'value') else ring_idx}"
    if self.token:
      request += f"?lock-token=" + self.token
    logging.debug("Request : " + request)
    try:
      response = requests.get(request)
      #output_params['response'] = response.text
      logging.debug("Response : " + response.text)
      err_match = re.match(r'.*\nerr=(0x\S+)\n.*', response.text, flags=re.DOTALL)
      err_api_match = re.match(r'(Invalid method.*)', response.text, flags=re.DOTALL)
      output_params['status_code'] = response.status_code
      if err_match:
         output_params['err'] = int(err_match.groups()[0],0)
         output_params['err_hex'] = err_match.groups()[0]
         try:
           output_params['err_str'] = self.getErrorString(output_params['err']) + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      elif err_api_match:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value)
         try:
           output_params['err_str'] = "API Error: " + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      else:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value
         output_params['err_str'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.name
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value)
         output_params['errcode'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN
      if (output_params['err'] and self.shouldraise):
         raise ScintilError(output_params['errcode'] or scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN, output_params)
      val_match = re.match(r".*\*val=(\S+)", response.text, flags=re.DOTALL)
      if val_match:
         output_params['val'] = float(val_match.groups()[0])
      else:
         output_params['val'] = None
    except requests.exceptions.RequestException as e:
      ch_error = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL
      output_params['err'] = ch_error.value
      output_params['err_str'] = ch_error.name
      output_params['errcode'] = ch_error
      if (self.shouldraise):
         raise ScintilError(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL, output_params)
    return output_params

  def scintil_hal_ll_tia_get_laser_mpd( self, laser: scintil_hal_ll_tia_laser_mpd_t):
    # 1 input arguments
    # 1 output arguments
    output_params = {}
    request = f"http://{self.server}:{self.port}/hal{'delegate' if self.delegate else ''}/scintil_hal_ll_tia_get_laser_mpd/{laser.value if hasattr(laser,'value') else laser}"
    if self.token:
      request += f"?lock-token=" + self.token
    logging.debug("Request : " + request)
    try:
      response = requests.get(request)
      #output_params['response'] = response.text
      logging.debug("Response : " + response.text)
      err_match = re.match(r'.*\nerr=(0x\S+)\n.*', response.text, flags=re.DOTALL)
      err_api_match = re.match(r'(Invalid method.*)', response.text, flags=re.DOTALL)
      output_params['status_code'] = response.status_code
      if err_match:
         output_params['err'] = int(err_match.groups()[0],0)
         output_params['err_hex'] = err_match.groups()[0]
         try:
           output_params['err_str'] = self.getErrorString(output_params['err']) + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      elif err_api_match:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value)
         try:
           output_params['err_str'] = "API Error: " + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      else:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value
         output_params['err_str'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.name
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value)
         output_params['errcode'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN
      if (output_params['err'] and self.shouldraise):
         raise ScintilError(output_params['errcode'] or scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN, output_params)
      voltage_match = re.match(r".*\*voltage=(\S+)", response.text, flags=re.DOTALL)
      if voltage_match:
         output_params['voltage'] = float(voltage_match.groups()[0])
      else:
         output_params['voltage'] = None
    except requests.exceptions.RequestException as e:
      ch_error = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL
      output_params['err'] = ch_error.value
      output_params['err_str'] = ch_error.name
      output_params['errcode'] = ch_error
      if (self.shouldraise):
         raise ScintilError(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL, output_params)
    return output_params

  def scintil_hal_mpd_set_bias( self, module: scintil_hal_module_t, mpd: scintil_hal_mpd_t, bias: float):
    # 3 input arguments
    # 0 output arguments
    output_params = {}
    request = f"http://{self.server}:{self.port}/hal{'delegate' if self.delegate else ''}/scintil_hal_mpd_set_bias/{module.value if hasattr(module,'value') else module}/{mpd.value if hasattr(mpd,'value') else mpd}/{bias}"
    if self.token:
      request += f"?lock-token=" + self.token
    logging.debug("Request : " + request)
    try:
      response = requests.get(request)
      #output_params['response'] = response.text
      logging.debug("Response : " + response.text)
      err_match = re.match(r'.*\nerr=(0x\S+)\n.*', response.text, flags=re.DOTALL)
      err_api_match = re.match(r'(Invalid method.*)', response.text, flags=re.DOTALL)
      output_params['status_code'] = response.status_code
      if err_match:
         output_params['err'] = int(err_match.groups()[0],0)
         output_params['err_hex'] = err_match.groups()[0]
         try:
           output_params['err_str'] = self.getErrorString(output_params['err']) + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      elif err_api_match:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value)
         try:
           output_params['err_str'] = "API Error: " + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      else:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value
         output_params['err_str'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.name
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value)
         output_params['errcode'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN
      if (output_params['err'] and self.shouldraise):
         raise ScintilError(output_params['errcode'] or scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN, output_params)
    except requests.exceptions.RequestException as e:
      ch_error = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL
      output_params['err'] = ch_error.value
      output_params['err_str'] = ch_error.name
      output_params['errcode'] = ch_error
      if (self.shouldraise):
         raise ScintilError(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL, output_params)
    return output_params

  def scintil_hal_mpd_get_init_current( self, module: scintil_hal_module_t, mpd: scintil_hal_mpd_t):
    # 2 input arguments
    # 1 output arguments
    output_params = {}
    request = f"http://{self.server}:{self.port}/hal{'delegate' if self.delegate else ''}/scintil_hal_mpd_get_init_current/{module.value if hasattr(module,'value') else module}/{mpd.value if hasattr(mpd,'value') else mpd}"
    if self.token:
      request += f"?lock-token=" + self.token
    logging.debug("Request : " + request)
    try:
      response = requests.get(request)
      #output_params['response'] = response.text
      logging.debug("Response : " + response.text)
      err_match = re.match(r'.*\nerr=(0x\S+)\n.*', response.text, flags=re.DOTALL)
      err_api_match = re.match(r'(Invalid method.*)', response.text, flags=re.DOTALL)
      output_params['status_code'] = response.status_code
      if err_match:
         output_params['err'] = int(err_match.groups()[0],0)
         output_params['err_hex'] = err_match.groups()[0]
         try:
           output_params['err_str'] = self.getErrorString(output_params['err']) + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      elif err_api_match:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value)
         try:
           output_params['err_str'] = "API Error: " + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      else:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value
         output_params['err_str'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.name
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value)
         output_params['errcode'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN
      if (output_params['err'] and self.shouldraise):
         raise ScintilError(output_params['errcode'] or scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN, output_params)
      init_current_match = re.match(r".*\*init_current=(\S+)", response.text, flags=re.DOTALL)
      if init_current_match:
         output_params['init_current'] = float(init_current_match.groups()[0])
      else:
         output_params['init_current'] = None
    except requests.exceptions.RequestException as e:
      ch_error = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL
      output_params['err'] = ch_error.value
      output_params['err_str'] = ch_error.name
      output_params['errcode'] = ch_error
      if (self.shouldraise):
         raise ScintilError(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL, output_params)
    return output_params

  def scintil_hal_mpd_get_voltage( self, module: scintil_hal_module_t, index: scintil_hal_mpd_t):
    # 2 input arguments
    # 1 output arguments
    output_params = {}
    request = f"http://{self.server}:{self.port}/hal{'delegate' if self.delegate else ''}/scintil_hal_mpd_get_voltage/{module.value if hasattr(module,'value') else module}/{index.value if hasattr(index,'value') else index}"
    if self.token:
      request += f"?lock-token=" + self.token
    logging.debug("Request : " + request)
    try:
      response = requests.get(request)
      #output_params['response'] = response.text
      logging.debug("Response : " + response.text)
      err_match = re.match(r'.*\nerr=(0x\S+)\n.*', response.text, flags=re.DOTALL)
      err_api_match = re.match(r'(Invalid method.*)', response.text, flags=re.DOTALL)
      output_params['status_code'] = response.status_code
      if err_match:
         output_params['err'] = int(err_match.groups()[0],0)
         output_params['err_hex'] = err_match.groups()[0]
         try:
           output_params['err_str'] = self.getErrorString(output_params['err']) + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      elif err_api_match:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value)
         try:
           output_params['err_str'] = "API Error: " + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      else:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value
         output_params['err_str'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.name
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value)
         output_params['errcode'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN
      if (output_params['err'] and self.shouldraise):
         raise ScintilError(output_params['errcode'] or scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN, output_params)
      voltage_match = re.match(r".*\*voltage=(\S+)", response.text, flags=re.DOTALL)
      if voltage_match:
         output_params['voltage'] = float(voltage_match.groups()[0])
      else:
         output_params['voltage'] = None
    except requests.exceptions.RequestException as e:
      ch_error = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL
      output_params['err'] = ch_error.value
      output_params['err_str'] = ch_error.name
      output_params['errcode'] = ch_error
      if (self.shouldraise):
         raise ScintilError(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL, output_params)
    return output_params

  def scintil_hal_mpd_get_current( self, module: scintil_hal_module_t, index: scintil_hal_mpd_t):
    # 2 input arguments
    # 1 output arguments
    output_params = {}
    request = f"http://{self.server}:{self.port}/hal{'delegate' if self.delegate else ''}/scintil_hal_mpd_get_current/{module.value if hasattr(module,'value') else module}/{index.value if hasattr(index,'value') else index}"
    if self.token:
      request += f"?lock-token=" + self.token
    logging.debug("Request : " + request)
    try:
      response = requests.get(request)
      #output_params['response'] = response.text
      logging.debug("Response : " + response.text)
      err_match = re.match(r'.*\nerr=(0x\S+)\n.*', response.text, flags=re.DOTALL)
      err_api_match = re.match(r'(Invalid method.*)', response.text, flags=re.DOTALL)
      output_params['status_code'] = response.status_code
      if err_match:
         output_params['err'] = int(err_match.groups()[0],0)
         output_params['err_hex'] = err_match.groups()[0]
         try:
           output_params['err_str'] = self.getErrorString(output_params['err']) + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      elif err_api_match:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value)
         try:
           output_params['err_str'] = "API Error: " + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      else:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value
         output_params['err_str'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.name
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value)
         output_params['errcode'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN
      if (output_params['err'] and self.shouldraise):
         raise ScintilError(output_params['errcode'] or scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN, output_params)
      current_match = re.match(r".*\*current=(\S+)", response.text, flags=re.DOTALL)
      if current_match:
         output_params['current'] = float(current_match.groups()[0])
      else:
         output_params['current'] = None
    except requests.exceptions.RequestException as e:
      ch_error = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL
      output_params['err'] = ch_error.value
      output_params['err_str'] = ch_error.name
      output_params['errcode'] = ch_error
      if (self.shouldraise):
         raise ScintilError(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL, output_params)
    return output_params

  def scintil_hal_mpd_get_optical_power( self, module: scintil_hal_module_t, index: scintil_hal_mpd_t):
    # 2 input arguments
    # 1 output arguments
    output_params = {}
    request = f"http://{self.server}:{self.port}/hal{'delegate' if self.delegate else ''}/scintil_hal_mpd_get_optical_power/{module.value if hasattr(module,'value') else module}/{index.value if hasattr(index,'value') else index}"
    if self.token:
      request += f"?lock-token=" + self.token
    logging.debug("Request : " + request)
    try:
      response = requests.get(request)
      #output_params['response'] = response.text
      logging.debug("Response : " + response.text)
      err_match = re.match(r'.*\nerr=(0x\S+)\n.*', response.text, flags=re.DOTALL)
      err_api_match = re.match(r'(Invalid method.*)', response.text, flags=re.DOTALL)
      output_params['status_code'] = response.status_code
      if err_match:
         output_params['err'] = int(err_match.groups()[0],0)
         output_params['err_hex'] = err_match.groups()[0]
         try:
           output_params['err_str'] = self.getErrorString(output_params['err']) + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      elif err_api_match:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value)
         try:
           output_params['err_str'] = "API Error: " + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      else:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value
         output_params['err_str'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.name
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value)
         output_params['errcode'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN
      if (output_params['err'] and self.shouldraise):
         raise ScintilError(output_params['errcode'] or scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN, output_params)
      power_match = re.match(r".*\*power=(\S+)", response.text, flags=re.DOTALL)
      if power_match:
         output_params['power'] = float(power_match.groups()[0])
      else:
         output_params['power'] = None
    except requests.exceptions.RequestException as e:
      ch_error = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL
      output_params['err'] = ch_error.value
      output_params['err_str'] = ch_error.name
      output_params['errcode'] = ch_error
      if (self.shouldraise):
         raise ScintilError(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL, output_params)
    return output_params

  def scintil_hal_laser_set_current( self, module: scintil_hal_module_t, laser: scintil_hal_laser_t, current: float):
    # 3 input arguments
    # 0 output arguments
    output_params = {}
    request = f"http://{self.server}:{self.port}/hal{'delegate' if self.delegate else ''}/scintil_hal_laser_set_current/{module.value if hasattr(module,'value') else module}/{laser.value if hasattr(laser,'value') else laser}/{current}"
    if self.token:
      request += f"?lock-token=" + self.token
    logging.debug("Request : " + request)
    try:
      response = requests.get(request)
      #output_params['response'] = response.text
      logging.debug("Response : " + response.text)
      err_match = re.match(r'.*\nerr=(0x\S+)\n.*', response.text, flags=re.DOTALL)
      err_api_match = re.match(r'(Invalid method.*)', response.text, flags=re.DOTALL)
      output_params['status_code'] = response.status_code
      if err_match:
         output_params['err'] = int(err_match.groups()[0],0)
         output_params['err_hex'] = err_match.groups()[0]
         try:
           output_params['err_str'] = self.getErrorString(output_params['err']) + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      elif err_api_match:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value)
         try:
           output_params['err_str'] = "API Error: " + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      else:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value
         output_params['err_str'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.name
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value)
         output_params['errcode'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN
      if (output_params['err'] and self.shouldraise):
         raise ScintilError(output_params['errcode'] or scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN, output_params)
    except requests.exceptions.RequestException as e:
      ch_error = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL
      output_params['err'] = ch_error.value
      output_params['err_str'] = ch_error.name
      output_params['errcode'] = ch_error
      if (self.shouldraise):
         raise ScintilError(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL, output_params)
    return output_params

  def scintil_hal_laser_alignment_get_current( self, module: scintil_hal_module_t):
    # 1 input arguments
    # 1 output arguments
    output_params = {}
    request = f"http://{self.server}:{self.port}/hal{'delegate' if self.delegate else ''}/scintil_hal_laser_alignment_get_current/{module.value if hasattr(module,'value') else module}"
    if self.token:
      request += f"?lock-token=" + self.token
    logging.debug("Request : " + request)
    try:
      response = requests.get(request)
      #output_params['response'] = response.text
      logging.debug("Response : " + response.text)
      err_match = re.match(r'.*\nerr=(0x\S+)\n.*', response.text, flags=re.DOTALL)
      err_api_match = re.match(r'(Invalid method.*)', response.text, flags=re.DOTALL)
      output_params['status_code'] = response.status_code
      if err_match:
         output_params['err'] = int(err_match.groups()[0],0)
         output_params['err_hex'] = err_match.groups()[0]
         try:
           output_params['err_str'] = self.getErrorString(output_params['err']) + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      elif err_api_match:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value)
         try:
           output_params['err_str'] = "API Error: " + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      else:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value
         output_params['err_str'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.name
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value)
         output_params['errcode'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN
      if (output_params['err'] and self.shouldraise):
         raise ScintilError(output_params['errcode'] or scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN, output_params)
      alignment_match = re.match(r".*\*alignment=(\S+)", response.text, flags=re.DOTALL)
      if alignment_match:
         output_params['alignment'] = float(alignment_match.groups()[0])
      else:
         output_params['alignment'] = None
    except requests.exceptions.RequestException as e:
      ch_error = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL
      output_params['err'] = ch_error.value
      output_params['err_str'] = ch_error.name
      output_params['errcode'] = ch_error
      if (self.shouldraise):
         raise ScintilError(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL, output_params)
    return output_params

  def scintil_hal_laser_alignment_set_current( self, module: scintil_hal_module_t, alignment: float):
    # 2 input arguments
    # 0 output arguments
    output_params = {}
    request = f"http://{self.server}:{self.port}/hal{'delegate' if self.delegate else ''}/scintil_hal_laser_alignment_set_current/{module.value if hasattr(module,'value') else module}/{alignment}"
    if self.token:
      request += f"?lock-token=" + self.token
    logging.debug("Request : " + request)
    try:
      response = requests.get(request)
      #output_params['response'] = response.text
      logging.debug("Response : " + response.text)
      err_match = re.match(r'.*\nerr=(0x\S+)\n.*', response.text, flags=re.DOTALL)
      err_api_match = re.match(r'(Invalid method.*)', response.text, flags=re.DOTALL)
      output_params['status_code'] = response.status_code
      if err_match:
         output_params['err'] = int(err_match.groups()[0],0)
         output_params['err_hex'] = err_match.groups()[0]
         try:
           output_params['err_str'] = self.getErrorString(output_params['err']) + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      elif err_api_match:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value)
         try:
           output_params['err_str'] = "API Error: " + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      else:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value
         output_params['err_str'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.name
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value)
         output_params['errcode'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN
      if (output_params['err'] and self.shouldraise):
         raise ScintilError(output_params['errcode'] or scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN, output_params)
    except requests.exceptions.RequestException as e:
      ch_error = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL
      output_params['err'] = ch_error.value
      output_params['err_str'] = ch_error.name
      output_params['errcode'] = ch_error
      if (self.shouldraise):
         raise ScintilError(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL, output_params)
    return output_params

  def scintil_hal_laser_get_applied_current( self, module: scintil_hal_module_t, laser: scintil_hal_laser_t):
    # 2 input arguments
    # 1 output arguments
    output_params = {}
    request = f"http://{self.server}:{self.port}/hal{'delegate' if self.delegate else ''}/scintil_hal_laser_get_applied_current/{module.value if hasattr(module,'value') else module}/{laser.value if hasattr(laser,'value') else laser}"
    if self.token:
      request += f"?lock-token=" + self.token
    logging.debug("Request : " + request)
    try:
      response = requests.get(request)
      #output_params['response'] = response.text
      logging.debug("Response : " + response.text)
      err_match = re.match(r'.*\nerr=(0x\S+)\n.*', response.text, flags=re.DOTALL)
      err_api_match = re.match(r'(Invalid method.*)', response.text, flags=re.DOTALL)
      output_params['status_code'] = response.status_code
      if err_match:
         output_params['err'] = int(err_match.groups()[0],0)
         output_params['err_hex'] = err_match.groups()[0]
         try:
           output_params['err_str'] = self.getErrorString(output_params['err']) + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      elif err_api_match:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value)
         try:
           output_params['err_str'] = "API Error: " + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      else:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value
         output_params['err_str'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.name
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value)
         output_params['errcode'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN
      if (output_params['err'] and self.shouldraise):
         raise ScintilError(output_params['errcode'] or scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN, output_params)
      current_match = re.match(r".*\*current=(\S+)", response.text, flags=re.DOTALL)
      if current_match:
         output_params['current'] = float(current_match.groups()[0])
      else:
         output_params['current'] = None
    except requests.exceptions.RequestException as e:
      ch_error = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL
      output_params['err'] = ch_error.value
      output_params['err_str'] = ch_error.name
      output_params['errcode'] = ch_error
      if (self.shouldraise):
         raise ScintilError(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL, output_params)
    return output_params

  def scintil_hal_laser_get_measured_current( self, module: scintil_hal_module_t, laser: scintil_hal_laser_t):
    # 2 input arguments
    # 1 output arguments
    output_params = {}
    request = f"http://{self.server}:{self.port}/hal{'delegate' if self.delegate else ''}/scintil_hal_laser_get_measured_current/{module.value if hasattr(module,'value') else module}/{laser.value if hasattr(laser,'value') else laser}"
    if self.token:
      request += f"?lock-token=" + self.token
    logging.debug("Request : " + request)
    try:
      response = requests.get(request)
      #output_params['response'] = response.text
      logging.debug("Response : " + response.text)
      err_match = re.match(r'.*\nerr=(0x\S+)\n.*', response.text, flags=re.DOTALL)
      err_api_match = re.match(r'(Invalid method.*)', response.text, flags=re.DOTALL)
      output_params['status_code'] = response.status_code
      if err_match:
         output_params['err'] = int(err_match.groups()[0],0)
         output_params['err_hex'] = err_match.groups()[0]
         try:
           output_params['err_str'] = self.getErrorString(output_params['err']) + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      elif err_api_match:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value)
         try:
           output_params['err_str'] = "API Error: " + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      else:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value
         output_params['err_str'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.name
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value)
         output_params['errcode'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN
      if (output_params['err'] and self.shouldraise):
         raise ScintilError(output_params['errcode'] or scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN, output_params)
      current_match = re.match(r".*\*current=(\S+)", response.text, flags=re.DOTALL)
      if current_match:
         output_params['current'] = float(current_match.groups()[0])
      else:
         output_params['current'] = None
    except requests.exceptions.RequestException as e:
      ch_error = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL
      output_params['err'] = ch_error.value
      output_params['err_str'] = ch_error.name
      output_params['errcode'] = ch_error
      if (self.shouldraise):
         raise ScintilError(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL, output_params)
    return output_params

  def scintil_hal_laser_configure_AWG( self, module: scintil_hal_module_t, laser: scintil_hal_laser_t, array: array):
    # 3 input arguments
    # 0 output arguments
    output_params = {}
    request = f"http://{self.server}:{self.port}/hal{'delegate' if self.delegate else ''}/scintil_hal_laser_configure_AWG/{module.value if hasattr(module,'value') else module}/{laser.value if hasattr(laser,'value') else laser}/{array}/{len(array)}"
    if self.token:
      request += f"?lock-token=" + self.token
    logging.debug("Request : " + request)
    try:
      response = requests.get(request)
      #output_params['response'] = response.text
      logging.debug("Response : " + response.text)
      err_match = re.match(r'.*\nerr=(0x\S+)\n.*', response.text, flags=re.DOTALL)
      err_api_match = re.match(r'(Invalid method.*)', response.text, flags=re.DOTALL)
      output_params['status_code'] = response.status_code
      if err_match:
         output_params['err'] = int(err_match.groups()[0],0)
         output_params['err_hex'] = err_match.groups()[0]
         try:
           output_params['err_str'] = self.getErrorString(output_params['err']) + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      elif err_api_match:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value)
         try:
           output_params['err_str'] = "API Error: " + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      else:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value
         output_params['err_str'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.name
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value)
         output_params['errcode'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN
      if (output_params['err'] and self.shouldraise):
         raise ScintilError(output_params['errcode'] or scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN, output_params)
    except requests.exceptions.RequestException as e:
      ch_error = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL
      output_params['err'] = ch_error.value
      output_params['err_str'] = ch_error.name
      output_params['errcode'] = ch_error
      if (self.shouldraise):
         raise ScintilError(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL, output_params)
    return output_params

  def scintil_hal_laser_start_AWG(self):
    # 0 input arguments
    # 0 output arguments
    output_params = {}
    request = f"http://{self.server}:{self.port}/hal{'delegate' if self.delegate else ''}/scintil_hal_laser_start_AWG"
    if self.token:
      request += f"?lock-token=" + self.token
    logging.debug("Request : " + request)
    try:
      response = requests.get(request)
      #output_params['response'] = response.text
      logging.debug("Response : " + response.text)
      err_match = re.match(r'.*\nerr=(0x\S+)\n.*', response.text, flags=re.DOTALL)
      err_api_match = re.match(r'(Invalid method.*)', response.text, flags=re.DOTALL)
      output_params['status_code'] = response.status_code
      if err_match:
         output_params['err'] = int(err_match.groups()[0],0)
         output_params['err_hex'] = err_match.groups()[0]
         try:
           output_params['err_str'] = self.getErrorString(output_params['err']) + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      elif err_api_match:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value)
         try:
           output_params['err_str'] = "API Error: " + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      else:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value
         output_params['err_str'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.name
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value)
         output_params['errcode'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN
      if (output_params['err'] and self.shouldraise):
         raise ScintilError(output_params['errcode'] or scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN, output_params)
    except requests.exceptions.RequestException as e:
      ch_error = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL
      output_params['err'] = ch_error.value
      output_params['err_str'] = ch_error.name
      output_params['errcode'] = ch_error
      if (self.shouldraise):
         raise ScintilError(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL, output_params)
    return output_params

  def scintil_hal_laser_stop_AWG(self):
    # 0 input arguments
    # 0 output arguments
    output_params = {}
    request = f"http://{self.server}:{self.port}/hal{'delegate' if self.delegate else ''}/scintil_hal_laser_stop_AWG"
    if self.token:
      request += f"?lock-token=" + self.token
    logging.debug("Request : " + request)
    try:
      response = requests.get(request)
      #output_params['response'] = response.text
      logging.debug("Response : " + response.text)
      err_match = re.match(r'.*\nerr=(0x\S+)\n.*', response.text, flags=re.DOTALL)
      err_api_match = re.match(r'(Invalid method.*)', response.text, flags=re.DOTALL)
      output_params['status_code'] = response.status_code
      if err_match:
         output_params['err'] = int(err_match.groups()[0],0)
         output_params['err_hex'] = err_match.groups()[0]
         try:
           output_params['err_str'] = self.getErrorString(output_params['err']) + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      elif err_api_match:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value)
         try:
           output_params['err_str'] = "API Error: " + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      else:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value
         output_params['err_str'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.name
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value)
         output_params['errcode'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN
      if (output_params['err'] and self.shouldraise):
         raise ScintilError(output_params['errcode'] or scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN, output_params)
    except requests.exceptions.RequestException as e:
      ch_error = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL
      output_params['err'] = ch_error.value
      output_params['err_str'] = ch_error.name
      output_params['errcode'] = ch_error
      if (self.shouldraise):
         raise ScintilError(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL, output_params)
    return output_params

  def scintil_hal_laser_get_dither_state( self, module: scintil_hal_module_t, laser: scintil_hal_laser_t):
    # 2 input arguments
    # 1 output arguments
    output_params = {}
    request = f"http://{self.server}:{self.port}/hal{'delegate' if self.delegate else ''}/scintil_hal_laser_get_dither_state/{module.value if hasattr(module,'value') else module}/{laser.value if hasattr(laser,'value') else laser}"
    if self.token:
      request += f"?lock-token=" + self.token
    logging.debug("Request : " + request)
    try:
      response = requests.get(request)
      #output_params['response'] = response.text
      logging.debug("Response : " + response.text)
      err_match = re.match(r'.*\nerr=(0x\S+)\n.*', response.text, flags=re.DOTALL)
      err_api_match = re.match(r'(Invalid method.*)', response.text, flags=re.DOTALL)
      output_params['status_code'] = response.status_code
      if err_match:
         output_params['err'] = int(err_match.groups()[0],0)
         output_params['err_hex'] = err_match.groups()[0]
         try:
           output_params['err_str'] = self.getErrorString(output_params['err']) + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      elif err_api_match:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value)
         try:
           output_params['err_str'] = "API Error: " + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      else:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value
         output_params['err_str'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.name
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value)
         output_params['errcode'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN
      if (output_params['err'] and self.shouldraise):
         raise ScintilError(output_params['errcode'] or scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN, output_params)
      enable_match = re.match(r".*\*enable=(\S+)", response.text, flags=re.DOTALL)
      if enable_match:
         output_params['enable'] = int(enable_match.groups()[0])
      else:
         output_params['enable'] = None
    except requests.exceptions.RequestException as e:
      ch_error = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL
      output_params['err'] = ch_error.value
      output_params['err_str'] = ch_error.name
      output_params['errcode'] = ch_error
      if (self.shouldraise):
         raise ScintilError(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL, output_params)
    return output_params

  def scintil_hal_laser_set_dither_state( self, module: scintil_hal_module_t, laser: scintil_hal_laser_t, enable: bool):
    # 3 input arguments
    # 0 output arguments
    output_params = {}
    request = f"http://{self.server}:{self.port}/hal{'delegate' if self.delegate else ''}/scintil_hal_laser_set_dither_state/{module.value if hasattr(module,'value') else module}/{laser.value if hasattr(laser,'value') else laser}/{int(enable)}"
    if self.token:
      request += f"?lock-token=" + self.token
    logging.debug("Request : " + request)
    try:
      response = requests.get(request)
      #output_params['response'] = response.text
      logging.debug("Response : " + response.text)
      err_match = re.match(r'.*\nerr=(0x\S+)\n.*', response.text, flags=re.DOTALL)
      err_api_match = re.match(r'(Invalid method.*)', response.text, flags=re.DOTALL)
      output_params['status_code'] = response.status_code
      if err_match:
         output_params['err'] = int(err_match.groups()[0],0)
         output_params['err_hex'] = err_match.groups()[0]
         try:
           output_params['err_str'] = self.getErrorString(output_params['err']) + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      elif err_api_match:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value)
         try:
           output_params['err_str'] = "API Error: " + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      else:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value
         output_params['err_str'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.name
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value)
         output_params['errcode'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN
      if (output_params['err'] and self.shouldraise):
         raise ScintilError(output_params['errcode'] or scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN, output_params)
    except requests.exceptions.RequestException as e:
      ch_error = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL
      output_params['err'] = ch_error.value
      output_params['err_str'] = ch_error.name
      output_params['errcode'] = ch_error
      if (self.shouldraise):
         raise ScintilError(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL, output_params)
    return output_params

  def scintil_hal_laser_set_dither_state_all( self, module: scintil_hal_module_t, enable: bool):
    # 2 input arguments
    # 0 output arguments
    output_params = {}
    request = f"http://{self.server}:{self.port}/hal{'delegate' if self.delegate else ''}/scintil_hal_laser_set_dither_state_all/{module.value if hasattr(module,'value') else module}/{int(enable)}"
    if self.token:
      request += f"?lock-token=" + self.token
    logging.debug("Request : " + request)
    try:
      response = requests.get(request)
      #output_params['response'] = response.text
      logging.debug("Response : " + response.text)
      err_match = re.match(r'.*\nerr=(0x\S+)\n.*', response.text, flags=re.DOTALL)
      err_api_match = re.match(r'(Invalid method.*)', response.text, flags=re.DOTALL)
      output_params['status_code'] = response.status_code
      if err_match:
         output_params['err'] = int(err_match.groups()[0],0)
         output_params['err_hex'] = err_match.groups()[0]
         try:
           output_params['err_str'] = self.getErrorString(output_params['err']) + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      elif err_api_match:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value)
         try:
           output_params['err_str'] = "API Error: " + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      else:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value
         output_params['err_str'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.name
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value)
         output_params['errcode'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN
      if (output_params['err'] and self.shouldraise):
         raise ScintilError(output_params['errcode'] or scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN, output_params)
    except requests.exceptions.RequestException as e:
      ch_error = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL
      output_params['err'] = ch_error.value
      output_params['err_str'] = ch_error.name
      output_params['errcode'] = ch_error
      if (self.shouldraise):
         raise ScintilError(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL, output_params)
    return output_params

  def scintil_hal_laser_get_electrical_power( self, module: scintil_hal_module_t, laser: scintil_hal_laser_t):
    # 2 input arguments
    # 1 output arguments
    output_params = {}
    request = f"http://{self.server}:{self.port}/hal{'delegate' if self.delegate else ''}/scintil_hal_laser_get_electrical_power/{module.value if hasattr(module,'value') else module}/{laser.value if hasattr(laser,'value') else laser}"
    if self.token:
      request += f"?lock-token=" + self.token
    logging.debug("Request : " + request)
    try:
      response = requests.get(request)
      #output_params['response'] = response.text
      logging.debug("Response : " + response.text)
      err_match = re.match(r'.*\nerr=(0x\S+)\n.*', response.text, flags=re.DOTALL)
      err_api_match = re.match(r'(Invalid method.*)', response.text, flags=re.DOTALL)
      output_params['status_code'] = response.status_code
      if err_match:
         output_params['err'] = int(err_match.groups()[0],0)
         output_params['err_hex'] = err_match.groups()[0]
         try:
           output_params['err_str'] = self.getErrorString(output_params['err']) + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      elif err_api_match:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value)
         try:
           output_params['err_str'] = "API Error: " + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      else:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value
         output_params['err_str'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.name
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value)
         output_params['errcode'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN
      if (output_params['err'] and self.shouldraise):
         raise ScintilError(output_params['errcode'] or scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN, output_params)
      power_match = re.match(r".*\*power=(\S+)", response.text, flags=re.DOTALL)
      if power_match:
         output_params['power'] = float(power_match.groups()[0])
      else:
         output_params['power'] = None
    except requests.exceptions.RequestException as e:
      ch_error = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL
      output_params['err'] = ch_error.value
      output_params['err_str'] = ch_error.name
      output_params['errcode'] = ch_error
      if (self.shouldraise):
         raise ScintilError(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL, output_params)
    return output_params

  def scintil_hal_laser_get_optical_power( self, module: scintil_hal_module_t, laser: scintil_hal_laser_t):
    # 2 input arguments
    # 1 output arguments
    output_params = {}
    request = f"http://{self.server}:{self.port}/hal{'delegate' if self.delegate else ''}/scintil_hal_laser_get_optical_power/{module.value if hasattr(module,'value') else module}/{laser.value if hasattr(laser,'value') else laser}"
    if self.token:
      request += f"?lock-token=" + self.token
    logging.debug("Request : " + request)
    try:
      response = requests.get(request)
      #output_params['response'] = response.text
      logging.debug("Response : " + response.text)
      err_match = re.match(r'.*\nerr=(0x\S+)\n.*', response.text, flags=re.DOTALL)
      err_api_match = re.match(r'(Invalid method.*)', response.text, flags=re.DOTALL)
      output_params['status_code'] = response.status_code
      if err_match:
         output_params['err'] = int(err_match.groups()[0],0)
         output_params['err_hex'] = err_match.groups()[0]
         try:
           output_params['err_str'] = self.getErrorString(output_params['err']) + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      elif err_api_match:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value)
         try:
           output_params['err_str'] = "API Error: " + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      else:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value
         output_params['err_str'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.name
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value)
         output_params['errcode'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN
      if (output_params['err'] and self.shouldraise):
         raise ScintilError(output_params['errcode'] or scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN, output_params)
      power_match = re.match(r".*\*power=(\S+)", response.text, flags=re.DOTALL)
      if power_match:
         output_params['power'] = float(power_match.groups()[0])
      else:
         output_params['power'] = None
    except requests.exceptions.RequestException as e:
      ch_error = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL
      output_params['err'] = ch_error.value
      output_params['err_str'] = ch_error.name
      output_params['errcode'] = ch_error
      if (self.shouldraise):
         raise ScintilError(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL, output_params)
    return output_params

  def scintil_hal_laser_configure_AWG_from_period( self, module: scintil_hal_module_t, laser: scintil_hal_laser_t, periods: int, amplitude: float, phase: float):
    # 5 input arguments
    # 0 output arguments
    output_params = {}
    request = f"http://{self.server}:{self.port}/hal{'delegate' if self.delegate else ''}/scintil_hal_laser_configure_AWG_from_period/{module.value if hasattr(module,'value') else module}/{laser.value if hasattr(laser,'value') else laser}/{periods}/{amplitude}/{phase}"
    if self.token:
      request += f"?lock-token=" + self.token
    logging.debug("Request : " + request)
    try:
      response = requests.get(request)
      #output_params['response'] = response.text
      logging.debug("Response : " + response.text)
      err_match = re.match(r'.*\nerr=(0x\S+)\n.*', response.text, flags=re.DOTALL)
      err_api_match = re.match(r'(Invalid method.*)', response.text, flags=re.DOTALL)
      output_params['status_code'] = response.status_code
      if err_match:
         output_params['err'] = int(err_match.groups()[0],0)
         output_params['err_hex'] = err_match.groups()[0]
         try:
           output_params['err_str'] = self.getErrorString(output_params['err']) + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      elif err_api_match:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value)
         try:
           output_params['err_str'] = "API Error: " + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      else:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value
         output_params['err_str'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.name
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value)
         output_params['errcode'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN
      if (output_params['err'] and self.shouldraise):
         raise ScintilError(output_params['errcode'] or scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN, output_params)
    except requests.exceptions.RequestException as e:
      ch_error = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL
      output_params['err'] = ch_error.value
      output_params['err_str'] = ch_error.name
      output_params['errcode'] = ch_error
      if (self.shouldraise):
         raise ScintilError(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL, output_params)
    return output_params

  def scintil_hal_laser_apply_offset( self, module: scintil_hal_module_t, laser: scintil_hal_laser_t, offset_value: float):
    # 3 input arguments
    # 0 output arguments
    output_params = {}
    request = f"http://{self.server}:{self.port}/hal{'delegate' if self.delegate else ''}/scintil_hal_laser_apply_offset/{module.value if hasattr(module,'value') else module}/{laser.value if hasattr(laser,'value') else laser}/{offset_value}"
    if self.token:
      request += f"?lock-token=" + self.token
    logging.debug("Request : " + request)
    try:
      response = requests.get(request)
      #output_params['response'] = response.text
      logging.debug("Response : " + response.text)
      err_match = re.match(r'.*\nerr=(0x\S+)\n.*', response.text, flags=re.DOTALL)
      err_api_match = re.match(r'(Invalid method.*)', response.text, flags=re.DOTALL)
      output_params['status_code'] = response.status_code
      if err_match:
         output_params['err'] = int(err_match.groups()[0],0)
         output_params['err_hex'] = err_match.groups()[0]
         try:
           output_params['err_str'] = self.getErrorString(output_params['err']) + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      elif err_api_match:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value)
         try:
           output_params['err_str'] = "API Error: " + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      else:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value
         output_params['err_str'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.name
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value)
         output_params['errcode'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN
      if (output_params['err'] and self.shouldraise):
         raise ScintilError(output_params['errcode'] or scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN, output_params)
    except requests.exceptions.RequestException as e:
      ch_error = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL
      output_params['err'] = ch_error.value
      output_params['err_str'] = ch_error.name
      output_params['errcode'] = ch_error
      if (self.shouldraise):
         raise ScintilError(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL, output_params)
    return output_params

  def scintil_hal_mux_heater_set_voltage( self, module: scintil_hal_module_t, heater: scintil_hal_mux_heater_t, voltage: float):
    # 3 input arguments
    # 0 output arguments
    output_params = {}
    request = f"http://{self.server}:{self.port}/hal{'delegate' if self.delegate else ''}/scintil_hal_mux_heater_set_voltage/{module.value if hasattr(module,'value') else module}/{heater.value if hasattr(heater,'value') else heater}/{voltage}"
    if self.token:
      request += f"?lock-token=" + self.token
    logging.debug("Request : " + request)
    try:
      response = requests.get(request)
      #output_params['response'] = response.text
      logging.debug("Response : " + response.text)
      err_match = re.match(r'.*\nerr=(0x\S+)\n.*', response.text, flags=re.DOTALL)
      err_api_match = re.match(r'(Invalid method.*)', response.text, flags=re.DOTALL)
      output_params['status_code'] = response.status_code
      if err_match:
         output_params['err'] = int(err_match.groups()[0],0)
         output_params['err_hex'] = err_match.groups()[0]
         try:
           output_params['err_str'] = self.getErrorString(output_params['err']) + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      elif err_api_match:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value)
         try:
           output_params['err_str'] = "API Error: " + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      else:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value
         output_params['err_str'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.name
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value)
         output_params['errcode'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN
      if (output_params['err'] and self.shouldraise):
         raise ScintilError(output_params['errcode'] or scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN, output_params)
    except requests.exceptions.RequestException as e:
      ch_error = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL
      output_params['err'] = ch_error.value
      output_params['err_str'] = ch_error.name
      output_params['errcode'] = ch_error
      if (self.shouldraise):
         raise ScintilError(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL, output_params)
    return output_params

  def scintil_hal_mux_heater_get_voltage( self, module: scintil_hal_module_t, heater: scintil_hal_mux_heater_t):
    # 2 input arguments
    # 1 output arguments
    output_params = {}
    request = f"http://{self.server}:{self.port}/hal{'delegate' if self.delegate else ''}/scintil_hal_mux_heater_get_voltage/{module.value if hasattr(module,'value') else module}/{heater.value if hasattr(heater,'value') else heater}"
    if self.token:
      request += f"?lock-token=" + self.token
    logging.debug("Request : " + request)
    try:
      response = requests.get(request)
      #output_params['response'] = response.text
      logging.debug("Response : " + response.text)
      err_match = re.match(r'.*\nerr=(0x\S+)\n.*', response.text, flags=re.DOTALL)
      err_api_match = re.match(r'(Invalid method.*)', response.text, flags=re.DOTALL)
      output_params['status_code'] = response.status_code
      if err_match:
         output_params['err'] = int(err_match.groups()[0],0)
         output_params['err_hex'] = err_match.groups()[0]
         try:
           output_params['err_str'] = self.getErrorString(output_params['err']) + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      elif err_api_match:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value)
         try:
           output_params['err_str'] = "API Error: " + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      else:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value
         output_params['err_str'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.name
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value)
         output_params['errcode'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN
      if (output_params['err'] and self.shouldraise):
         raise ScintilError(output_params['errcode'] or scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN, output_params)
      voltage_match = re.match(r".*\*voltage=(\S+)", response.text, flags=re.DOTALL)
      if voltage_match:
         output_params['voltage'] = float(voltage_match.groups()[0])
      else:
         output_params['voltage'] = None
    except requests.exceptions.RequestException as e:
      ch_error = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL
      output_params['err'] = ch_error.value
      output_params['err_str'] = ch_error.name
      output_params['errcode'] = ch_error
      if (self.shouldraise):
         raise ScintilError(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL, output_params)
    return output_params

  def scintil_hal_mux_heater_get_mpd_stage_voltage( self, module: scintil_hal_module_t, heater: scintil_hal_mux_heater_t):
    # 2 input arguments
    # 1 output arguments
    output_params = {}
    request = f"http://{self.server}:{self.port}/hal{'delegate' if self.delegate else ''}/scintil_hal_mux_heater_get_mpd_stage_voltage/{module.value if hasattr(module,'value') else module}/{heater.value if hasattr(heater,'value') else heater}"
    if self.token:
      request += f"?lock-token=" + self.token
    logging.debug("Request : " + request)
    try:
      response = requests.get(request)
      #output_params['response'] = response.text
      logging.debug("Response : " + response.text)
      err_match = re.match(r'.*\nerr=(0x\S+)\n.*', response.text, flags=re.DOTALL)
      err_api_match = re.match(r'(Invalid method.*)', response.text, flags=re.DOTALL)
      output_params['status_code'] = response.status_code
      if err_match:
         output_params['err'] = int(err_match.groups()[0],0)
         output_params['err_hex'] = err_match.groups()[0]
         try:
           output_params['err_str'] = self.getErrorString(output_params['err']) + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      elif err_api_match:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value)
         try:
           output_params['err_str'] = "API Error: " + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      else:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value
         output_params['err_str'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.name
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value)
         output_params['errcode'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN
      if (output_params['err'] and self.shouldraise):
         raise ScintilError(output_params['errcode'] or scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN, output_params)
      voltage_match = re.match(r".*\*voltage=(\S+)", response.text, flags=re.DOTALL)
      if voltage_match:
         output_params['voltage'] = float(voltage_match.groups()[0])
      else:
         output_params['voltage'] = None
    except requests.exceptions.RequestException as e:
      ch_error = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL
      output_params['err'] = ch_error.value
      output_params['err_str'] = ch_error.name
      output_params['errcode'] = ch_error
      if (self.shouldraise):
         raise ScintilError(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL, output_params)
    return output_params

  def scintil_hal_mux_heater_set_level_all( self, module: scintil_hal_module_t, voltage: float):
    # 2 input arguments
    # 0 output arguments
    output_params = {}
    request = f"http://{self.server}:{self.port}/hal{'delegate' if self.delegate else ''}/scintil_hal_mux_heater_set_level_all/{module.value if hasattr(module,'value') else module}/{voltage}"
    if self.token:
      request += f"?lock-token=" + self.token
    logging.debug("Request : " + request)
    try:
      response = requests.get(request)
      #output_params['response'] = response.text
      logging.debug("Response : " + response.text)
      err_match = re.match(r'.*\nerr=(0x\S+)\n.*', response.text, flags=re.DOTALL)
      err_api_match = re.match(r'(Invalid method.*)', response.text, flags=re.DOTALL)
      output_params['status_code'] = response.status_code
      if err_match:
         output_params['err'] = int(err_match.groups()[0],0)
         output_params['err_hex'] = err_match.groups()[0]
         try:
           output_params['err_str'] = self.getErrorString(output_params['err']) + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      elif err_api_match:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value)
         try:
           output_params['err_str'] = "API Error: " + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      else:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value
         output_params['err_str'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.name
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value)
         output_params['errcode'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN
      if (output_params['err'] and self.shouldraise):
         raise ScintilError(output_params['errcode'] or scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN, output_params)
    except requests.exceptions.RequestException as e:
      ch_error = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL
      output_params['err'] = ch_error.value
      output_params['err_str'] = ch_error.name
      output_params['errcode'] = ch_error
      if (self.shouldraise):
         raise ScintilError(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL, output_params)
    return output_params

  def scintil_hal_vpolar_init(self):
    # 0 input arguments
    # 0 output arguments
    output_params = {}
    request = f"http://{self.server}:{self.port}/hal{'delegate' if self.delegate else ''}/scintil_hal_vpolar_init"
    if self.token:
      request += f"?lock-token=" + self.token
    logging.debug("Request : " + request)
    try:
      response = requests.get(request)
      #output_params['response'] = response.text
      logging.debug("Response : " + response.text)
      err_match = re.match(r'.*\nerr=(0x\S+)\n.*', response.text, flags=re.DOTALL)
      err_api_match = re.match(r'(Invalid method.*)', response.text, flags=re.DOTALL)
      output_params['status_code'] = response.status_code
      if err_match:
         output_params['err'] = int(err_match.groups()[0],0)
         output_params['err_hex'] = err_match.groups()[0]
         try:
           output_params['err_str'] = self.getErrorString(output_params['err']) + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      elif err_api_match:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value)
         try:
           output_params['err_str'] = "API Error: " + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      else:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value
         output_params['err_str'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.name
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value)
         output_params['errcode'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN
      if (output_params['err'] and self.shouldraise):
         raise ScintilError(output_params['errcode'] or scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN, output_params)
    except requests.exceptions.RequestException as e:
      ch_error = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL
      output_params['err'] = ch_error.value
      output_params['err_str'] = ch_error.name
      output_params['errcode'] = ch_error
      if (self.shouldraise):
         raise ScintilError(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL, output_params)
    return output_params

  def scintil_hal_vpolar_set_out_val( self, channel: scintil_hal_vpolar_out_t, val: float):
    # 2 input arguments
    # 0 output arguments
    output_params = {}
    request = f"http://{self.server}:{self.port}/hal{'delegate' if self.delegate else ''}/scintil_hal_vpolar_set_out_val/{channel.value if hasattr(channel,'value') else channel}/{val}"
    if self.token:
      request += f"?lock-token=" + self.token
    logging.debug("Request : " + request)
    try:
      response = requests.get(request)
      #output_params['response'] = response.text
      logging.debug("Response : " + response.text)
      err_match = re.match(r'.*\nerr=(0x\S+)\n.*', response.text, flags=re.DOTALL)
      err_api_match = re.match(r'(Invalid method.*)', response.text, flags=re.DOTALL)
      output_params['status_code'] = response.status_code
      if err_match:
         output_params['err'] = int(err_match.groups()[0],0)
         output_params['err_hex'] = err_match.groups()[0]
         try:
           output_params['err_str'] = self.getErrorString(output_params['err']) + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      elif err_api_match:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value)
         try:
           output_params['err_str'] = "API Error: " + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      else:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value
         output_params['err_str'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.name
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value)
         output_params['errcode'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN
      if (output_params['err'] and self.shouldraise):
         raise ScintilError(output_params['errcode'] or scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN, output_params)
    except requests.exceptions.RequestException as e:
      ch_error = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL
      output_params['err'] = ch_error.value
      output_params['err_str'] = ch_error.name
      output_params['errcode'] = ch_error
      if (self.shouldraise):
         raise ScintilError(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL, output_params)
    return output_params

  def scintil_hal_vpolar_get_out_val( self, channel: scintil_hal_vpolar_out_t):
    # 1 input arguments
    # 1 output arguments
    output_params = {}
    request = f"http://{self.server}:{self.port}/hal{'delegate' if self.delegate else ''}/scintil_hal_vpolar_get_out_val/{channel.value if hasattr(channel,'value') else channel}"
    if self.token:
      request += f"?lock-token=" + self.token
    logging.debug("Request : " + request)
    try:
      response = requests.get(request)
      #output_params['response'] = response.text
      logging.debug("Response : " + response.text)
      err_match = re.match(r'.*\nerr=(0x\S+)\n.*', response.text, flags=re.DOTALL)
      err_api_match = re.match(r'(Invalid method.*)', response.text, flags=re.DOTALL)
      output_params['status_code'] = response.status_code
      if err_match:
         output_params['err'] = int(err_match.groups()[0],0)
         output_params['err_hex'] = err_match.groups()[0]
         try:
           output_params['err_str'] = self.getErrorString(output_params['err']) + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      elif err_api_match:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value)
         try:
           output_params['err_str'] = "API Error: " + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      else:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value
         output_params['err_str'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.name
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value)
         output_params['errcode'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN
      if (output_params['err'] and self.shouldraise):
         raise ScintilError(output_params['errcode'] or scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN, output_params)
      val_match = re.match(r".*\*val=(\S+)", response.text, flags=re.DOTALL)
      if val_match:
         output_params['val'] = float(val_match.groups()[0])
      else:
         output_params['val'] = None
    except requests.exceptions.RequestException as e:
      ch_error = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL
      output_params['err'] = ch_error.value
      output_params['err_str'] = ch_error.name
      output_params['errcode'] = ch_error
      if (self.shouldraise):
         raise ScintilError(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL, output_params)
    return output_params

  def scintil_hal_vlaser_init(self):
    # 0 input arguments
    # 0 output arguments
    output_params = {}
    request = f"http://{self.server}:{self.port}/hal{'delegate' if self.delegate else ''}/scintil_hal_vlaser_init"
    if self.token:
      request += f"?lock-token=" + self.token
    logging.debug("Request : " + request)
    try:
      response = requests.get(request)
      #output_params['response'] = response.text
      logging.debug("Response : " + response.text)
      err_match = re.match(r'.*\nerr=(0x\S+)\n.*', response.text, flags=re.DOTALL)
      err_api_match = re.match(r'(Invalid method.*)', response.text, flags=re.DOTALL)
      output_params['status_code'] = response.status_code
      if err_match:
         output_params['err'] = int(err_match.groups()[0],0)
         output_params['err_hex'] = err_match.groups()[0]
         try:
           output_params['err_str'] = self.getErrorString(output_params['err']) + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      elif err_api_match:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value)
         try:
           output_params['err_str'] = "API Error: " + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      else:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value
         output_params['err_str'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.name
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value)
         output_params['errcode'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN
      if (output_params['err'] and self.shouldraise):
         raise ScintilError(output_params['errcode'] or scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN, output_params)
    except requests.exceptions.RequestException as e:
      ch_error = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL
      output_params['err'] = ch_error.value
      output_params['err_str'] = ch_error.name
      output_params['errcode'] = ch_error
      if (self.shouldraise):
         raise ScintilError(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL, output_params)
    return output_params

  def scintil_hal_vlaser_pwrgd(self):
    # 0 input arguments
    # 1 output arguments
    output_params = {}
    request = f"http://{self.server}:{self.port}/hal{'delegate' if self.delegate else ''}/scintil_hal_vlaser_pwrgd"
    if self.token:
      request += f"?lock-token=" + self.token
    logging.debug("Request : " + request)
    try:
      response = requests.get(request)
      #output_params['response'] = response.text
      logging.debug("Response : " + response.text)
      err_match = re.match(r'.*\nerr=(0x\S+)\n.*', response.text, flags=re.DOTALL)
      err_api_match = re.match(r'(Invalid method.*)', response.text, flags=re.DOTALL)
      output_params['status_code'] = response.status_code
      if err_match:
         output_params['err'] = int(err_match.groups()[0],0)
         output_params['err_hex'] = err_match.groups()[0]
         try:
           output_params['err_str'] = self.getErrorString(output_params['err']) + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      elif err_api_match:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value)
         try:
           output_params['err_str'] = "API Error: " + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      else:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value
         output_params['err_str'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.name
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value)
         output_params['errcode'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN
      if (output_params['err'] and self.shouldraise):
         raise ScintilError(output_params['errcode'] or scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN, output_params)
      pwrgd_match = re.match(r".*\*pwrgd=(\S+)", response.text, flags=re.DOTALL)
      if pwrgd_match:
         output_params['pwrgd'] = int(pwrgd_match.groups()[0])
      else:
         output_params['pwrgd'] = None
    except requests.exceptions.RequestException as e:
      ch_error = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL
      output_params['err'] = ch_error.value
      output_params['err_str'] = ch_error.name
      output_params['errcode'] = ch_error
      if (self.shouldraise):
         raise ScintilError(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL, output_params)
    return output_params

  def scintil_hal_vlaser_enable( self, enable: bool):
    # 1 input arguments
    # 0 output arguments
    output_params = {}
    request = f"http://{self.server}:{self.port}/hal{'delegate' if self.delegate else ''}/scintil_hal_vlaser_enable/{int(enable)}"
    if self.token:
      request += f"?lock-token=" + self.token
    logging.debug("Request : " + request)
    try:
      response = requests.get(request)
      #output_params['response'] = response.text
      logging.debug("Response : " + response.text)
      err_match = re.match(r'.*\nerr=(0x\S+)\n.*', response.text, flags=re.DOTALL)
      err_api_match = re.match(r'(Invalid method.*)', response.text, flags=re.DOTALL)
      output_params['status_code'] = response.status_code
      if err_match:
         output_params['err'] = int(err_match.groups()[0],0)
         output_params['err_hex'] = err_match.groups()[0]
         try:
           output_params['err_str'] = self.getErrorString(output_params['err']) + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      elif err_api_match:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value)
         try:
           output_params['err_str'] = "API Error: " + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      else:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value
         output_params['err_str'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.name
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value)
         output_params['errcode'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN
      if (output_params['err'] and self.shouldraise):
         raise ScintilError(output_params['errcode'] or scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN, output_params)
    except requests.exceptions.RequestException as e:
      ch_error = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL
      output_params['err'] = ch_error.value
      output_params['err_str'] = ch_error.name
      output_params['errcode'] = ch_error
      if (self.shouldraise):
         raise ScintilError(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL, output_params)
    return output_params

  def scintil_hal_vlaser_is_enable(self):
    # 0 input arguments
    # 1 output arguments
    output_params = {}
    request = f"http://{self.server}:{self.port}/hal{'delegate' if self.delegate else ''}/scintil_hal_vlaser_is_enable"
    if self.token:
      request += f"?lock-token=" + self.token
    logging.debug("Request : " + request)
    try:
      response = requests.get(request)
      #output_params['response'] = response.text
      logging.debug("Response : " + response.text)
      err_match = re.match(r'.*\nerr=(0x\S+)\n.*', response.text, flags=re.DOTALL)
      err_api_match = re.match(r'(Invalid method.*)', response.text, flags=re.DOTALL)
      output_params['status_code'] = response.status_code
      if err_match:
         output_params['err'] = int(err_match.groups()[0],0)
         output_params['err_hex'] = err_match.groups()[0]
         try:
           output_params['err_str'] = self.getErrorString(output_params['err']) + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      elif err_api_match:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value)
         try:
           output_params['err_str'] = "API Error: " + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      else:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value
         output_params['err_str'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.name
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value)
         output_params['errcode'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN
      if (output_params['err'] and self.shouldraise):
         raise ScintilError(output_params['errcode'] or scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN, output_params)
      enable_match = re.match(r".*\*enable=(\S+)", response.text, flags=re.DOTALL)
      if enable_match:
         output_params['enable'] = int(enable_match.groups()[0])
      else:
         output_params['enable'] = None
    except requests.exceptions.RequestException as e:
      ch_error = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL
      output_params['err'] = ch_error.value
      output_params['err_str'] = ch_error.name
      output_params['errcode'] = ch_error
      if (self.shouldraise):
         raise ScintilError(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL, output_params)
    return output_params

  def scintil_hal_vlaser_set_pot( self, value: float):
    # 1 input arguments
    # 0 output arguments
    output_params = {}
    request = f"http://{self.server}:{self.port}/hal{'delegate' if self.delegate else ''}/scintil_hal_vlaser_set_pot/{value}"
    if self.token:
      request += f"?lock-token=" + self.token
    logging.debug("Request : " + request)
    try:
      response = requests.get(request)
      #output_params['response'] = response.text
      logging.debug("Response : " + response.text)
      err_match = re.match(r'.*\nerr=(0x\S+)\n.*', response.text, flags=re.DOTALL)
      err_api_match = re.match(r'(Invalid method.*)', response.text, flags=re.DOTALL)
      output_params['status_code'] = response.status_code
      if err_match:
         output_params['err'] = int(err_match.groups()[0],0)
         output_params['err_hex'] = err_match.groups()[0]
         try:
           output_params['err_str'] = self.getErrorString(output_params['err']) + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      elif err_api_match:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value)
         try:
           output_params['err_str'] = "API Error: " + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      else:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value
         output_params['err_str'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.name
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value)
         output_params['errcode'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN
      if (output_params['err'] and self.shouldraise):
         raise ScintilError(output_params['errcode'] or scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN, output_params)
    except requests.exceptions.RequestException as e:
      ch_error = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL
      output_params['err'] = ch_error.value
      output_params['err_str'] = ch_error.name
      output_params['errcode'] = ch_error
      if (self.shouldraise):
         raise ScintilError(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL, output_params)
    return output_params

  def scintil_hal_vlaser_get_pot(self):
    # 0 input arguments
    # 1 output arguments
    output_params = {}
    request = f"http://{self.server}:{self.port}/hal{'delegate' if self.delegate else ''}/scintil_hal_vlaser_get_pot"
    if self.token:
      request += f"?lock-token=" + self.token
    logging.debug("Request : " + request)
    try:
      response = requests.get(request)
      #output_params['response'] = response.text
      logging.debug("Response : " + response.text)
      err_match = re.match(r'.*\nerr=(0x\S+)\n.*', response.text, flags=re.DOTALL)
      err_api_match = re.match(r'(Invalid method.*)', response.text, flags=re.DOTALL)
      output_params['status_code'] = response.status_code
      if err_match:
         output_params['err'] = int(err_match.groups()[0],0)
         output_params['err_hex'] = err_match.groups()[0]
         try:
           output_params['err_str'] = self.getErrorString(output_params['err']) + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      elif err_api_match:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value)
         try:
           output_params['err_str'] = "API Error: " + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      else:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value
         output_params['err_str'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.name
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value)
         output_params['errcode'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN
      if (output_params['err'] and self.shouldraise):
         raise ScintilError(output_params['errcode'] or scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN, output_params)
      value_match = re.match(r".*\*value=(\S+)", response.text, flags=re.DOTALL)
      if value_match:
         output_params['value'] = float(value_match.groups()[0])
      else:
         output_params['value'] = None
    except requests.exceptions.RequestException as e:
      ch_error = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL
      output_params['err'] = ch_error.value
      output_params['err_str'] = ch_error.name
      output_params['errcode'] = ch_error
      if (self.shouldraise):
         raise ScintilError(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL, output_params)
    return output_params

  def scintil_hal_vlaser_get_value(self):
    # 0 input arguments
    # 1 output arguments
    output_params = {}
    request = f"http://{self.server}:{self.port}/hal{'delegate' if self.delegate else ''}/scintil_hal_vlaser_get_value"
    if self.token:
      request += f"?lock-token=" + self.token
    logging.debug("Request : " + request)
    try:
      response = requests.get(request)
      #output_params['response'] = response.text
      logging.debug("Response : " + response.text)
      err_match = re.match(r'.*\nerr=(0x\S+)\n.*', response.text, flags=re.DOTALL)
      err_api_match = re.match(r'(Invalid method.*)', response.text, flags=re.DOTALL)
      output_params['status_code'] = response.status_code
      if err_match:
         output_params['err'] = int(err_match.groups()[0],0)
         output_params['err_hex'] = err_match.groups()[0]
         try:
           output_params['err_str'] = self.getErrorString(output_params['err']) + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      elif err_api_match:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value)
         try:
           output_params['err_str'] = "API Error: " + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      else:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value
         output_params['err_str'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.name
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value)
         output_params['errcode'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN
      if (output_params['err'] and self.shouldraise):
         raise ScintilError(output_params['errcode'] or scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN, output_params)
      value_match = re.match(r".*\*value=(\S+)", response.text, flags=re.DOTALL)
      if value_match:
         output_params['value'] = float(value_match.groups()[0])
      else:
         output_params['value'] = None
    except requests.exceptions.RequestException as e:
      ch_error = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL
      output_params['err'] = ch_error.value
      output_params['err_str'] = ch_error.name
      output_params['errcode'] = ch_error
      if (self.shouldraise):
         raise ScintilError(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL, output_params)
    return output_params

  def scintil_hal_fan_init(self):
    # 0 input arguments
    # 0 output arguments
    output_params = {}
    request = f"http://{self.server}:{self.port}/hal{'delegate' if self.delegate else ''}/scintil_hal_fan_init"
    if self.token:
      request += f"?lock-token=" + self.token
    logging.debug("Request : " + request)
    try:
      response = requests.get(request)
      #output_params['response'] = response.text
      logging.debug("Response : " + response.text)
      err_match = re.match(r'.*\nerr=(0x\S+)\n.*', response.text, flags=re.DOTALL)
      err_api_match = re.match(r'(Invalid method.*)', response.text, flags=re.DOTALL)
      output_params['status_code'] = response.status_code
      if err_match:
         output_params['err'] = int(err_match.groups()[0],0)
         output_params['err_hex'] = err_match.groups()[0]
         try:
           output_params['err_str'] = self.getErrorString(output_params['err']) + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      elif err_api_match:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value)
         try:
           output_params['err_str'] = "API Error: " + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      else:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value
         output_params['err_str'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.name
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value)
         output_params['errcode'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN
      if (output_params['err'] and self.shouldraise):
         raise ScintilError(output_params['errcode'] or scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN, output_params)
    except requests.exceptions.RequestException as e:
      ch_error = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL
      output_params['err'] = ch_error.value
      output_params['err_str'] = ch_error.name
      output_params['errcode'] = ch_error
      if (self.shouldraise):
         raise ScintilError(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL, output_params)
    return output_params

  def scintil_hal_fan_start(self):
    # 0 input arguments
    # 0 output arguments
    output_params = {}
    request = f"http://{self.server}:{self.port}/hal{'delegate' if self.delegate else ''}/scintil_hal_fan_start"
    if self.token:
      request += f"?lock-token=" + self.token
    logging.debug("Request : " + request)
    try:
      response = requests.get(request)
      #output_params['response'] = response.text
      logging.debug("Response : " + response.text)
      err_match = re.match(r'.*\nerr=(0x\S+)\n.*', response.text, flags=re.DOTALL)
      err_api_match = re.match(r'(Invalid method.*)', response.text, flags=re.DOTALL)
      output_params['status_code'] = response.status_code
      if err_match:
         output_params['err'] = int(err_match.groups()[0],0)
         output_params['err_hex'] = err_match.groups()[0]
         try:
           output_params['err_str'] = self.getErrorString(output_params['err']) + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      elif err_api_match:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value)
         try:
           output_params['err_str'] = "API Error: " + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      else:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value
         output_params['err_str'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.name
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value)
         output_params['errcode'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN
      if (output_params['err'] and self.shouldraise):
         raise ScintilError(output_params['errcode'] or scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN, output_params)
    except requests.exceptions.RequestException as e:
      ch_error = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL
      output_params['err'] = ch_error.value
      output_params['err_str'] = ch_error.name
      output_params['errcode'] = ch_error
      if (self.shouldraise):
         raise ScintilError(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL, output_params)
    return output_params

  def scintil_hal_fan_stop(self):
    # 0 input arguments
    # 0 output arguments
    output_params = {}
    request = f"http://{self.server}:{self.port}/hal{'delegate' if self.delegate else ''}/scintil_hal_fan_stop"
    if self.token:
      request += f"?lock-token=" + self.token
    logging.debug("Request : " + request)
    try:
      response = requests.get(request)
      #output_params['response'] = response.text
      logging.debug("Response : " + response.text)
      err_match = re.match(r'.*\nerr=(0x\S+)\n.*', response.text, flags=re.DOTALL)
      err_api_match = re.match(r'(Invalid method.*)', response.text, flags=re.DOTALL)
      output_params['status_code'] = response.status_code
      if err_match:
         output_params['err'] = int(err_match.groups()[0],0)
         output_params['err_hex'] = err_match.groups()[0]
         try:
           output_params['err_str'] = self.getErrorString(output_params['err']) + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      elif err_api_match:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value)
         try:
           output_params['err_str'] = "API Error: " + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      else:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value
         output_params['err_str'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.name
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value)
         output_params['errcode'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN
      if (output_params['err'] and self.shouldraise):
         raise ScintilError(output_params['errcode'] or scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN, output_params)
    except requests.exceptions.RequestException as e:
      ch_error = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL
      output_params['err'] = ch_error.value
      output_params['err_str'] = ch_error.name
      output_params['errcode'] = ch_error
      if (self.shouldraise):
         raise ScintilError(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL, output_params)
    return output_params

  def scintil_hal_fan_get_dc(self):
    # 0 input arguments
    # 1 output arguments
    output_params = {}
    request = f"http://{self.server}:{self.port}/hal{'delegate' if self.delegate else ''}/scintil_hal_fan_get_dc"
    if self.token:
      request += f"?lock-token=" + self.token
    logging.debug("Request : " + request)
    try:
      response = requests.get(request)
      #output_params['response'] = response.text
      logging.debug("Response : " + response.text)
      err_match = re.match(r'.*\nerr=(0x\S+)\n.*', response.text, flags=re.DOTALL)
      err_api_match = re.match(r'(Invalid method.*)', response.text, flags=re.DOTALL)
      output_params['status_code'] = response.status_code
      if err_match:
         output_params['err'] = int(err_match.groups()[0],0)
         output_params['err_hex'] = err_match.groups()[0]
         try:
           output_params['err_str'] = self.getErrorString(output_params['err']) + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      elif err_api_match:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value)
         try:
           output_params['err_str'] = "API Error: " + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      else:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value
         output_params['err_str'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.name
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value)
         output_params['errcode'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN
      if (output_params['err'] and self.shouldraise):
         raise ScintilError(output_params['errcode'] or scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN, output_params)
      duty_cycle_match = re.match(r".*\*duty_cycle=(\S+)", response.text, flags=re.DOTALL)
      if duty_cycle_match:
         output_params['duty_cycle'] = int(duty_cycle_match.groups()[0])
      else:
         output_params['duty_cycle'] = None
    except requests.exceptions.RequestException as e:
      ch_error = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL
      output_params['err'] = ch_error.value
      output_params['err_str'] = ch_error.name
      output_params['errcode'] = ch_error
      if (self.shouldraise):
         raise ScintilError(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL, output_params)
    return output_params

  def scintil_hal_fan_set_dc( self, duty_cycle: int):
    # 1 input arguments
    # 0 output arguments
    output_params = {}
    request = f"http://{self.server}:{self.port}/hal{'delegate' if self.delegate else ''}/scintil_hal_fan_set_dc/{duty_cycle}"
    if self.token:
      request += f"?lock-token=" + self.token
    logging.debug("Request : " + request)
    try:
      response = requests.get(request)
      #output_params['response'] = response.text
      logging.debug("Response : " + response.text)
      err_match = re.match(r'.*\nerr=(0x\S+)\n.*', response.text, flags=re.DOTALL)
      err_api_match = re.match(r'(Invalid method.*)', response.text, flags=re.DOTALL)
      output_params['status_code'] = response.status_code
      if err_match:
         output_params['err'] = int(err_match.groups()[0],0)
         output_params['err_hex'] = err_match.groups()[0]
         try:
           output_params['err_str'] = self.getErrorString(output_params['err']) + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      elif err_api_match:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value)
         try:
           output_params['err_str'] = "API Error: " + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      else:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value
         output_params['err_str'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.name
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value)
         output_params['errcode'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN
      if (output_params['err'] and self.shouldraise):
         raise ScintilError(output_params['errcode'] or scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN, output_params)
    except requests.exceptions.RequestException as e:
      ch_error = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL
      output_params['err'] = ch_error.value
      output_params['err_str'] = ch_error.name
      output_params['errcode'] = ch_error
      if (self.shouldraise):
         raise ScintilError(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL, output_params)
    return output_params

  def scintil_hal_tec_get_serial_number(self):
    # 0 input arguments
    # 1 output arguments
    output_params = {}
    request = f"http://{self.server}:{self.port}/hal{'delegate' if self.delegate else ''}/scintil_hal_tec_get_serial_number"
    if self.token:
      request += f"?lock-token=" + self.token
    logging.debug("Request : " + request)
    try:
      response = requests.get(request)
      #output_params['response'] = response.text
      logging.debug("Response : " + response.text)
      err_match = re.match(r'.*\nerr=(0x\S+)\n.*', response.text, flags=re.DOTALL)
      err_api_match = re.match(r'(Invalid method.*)', response.text, flags=re.DOTALL)
      output_params['status_code'] = response.status_code
      if err_match:
         output_params['err'] = int(err_match.groups()[0],0)
         output_params['err_hex'] = err_match.groups()[0]
         try:
           output_params['err_str'] = self.getErrorString(output_params['err']) + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      elif err_api_match:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value)
         try:
           output_params['err_str'] = "API Error: " + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      else:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value
         output_params['err_str'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.name
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value)
         output_params['errcode'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN
      if (output_params['err'] and self.shouldraise):
         raise ScintilError(output_params['errcode'] or scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN, output_params)
      sn_match = re.match(r".*\*sn=(\S+)", response.text, flags=re.DOTALL)
      if sn_match:
         output_params['sn'] = int(sn_match.groups()[0])
      else:
         output_params['sn'] = None
    except requests.exceptions.RequestException as e:
      ch_error = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL
      output_params['err'] = ch_error.value
      output_params['err_str'] = ch_error.name
      output_params['errcode'] = ch_error
      if (self.shouldraise):
         raise ScintilError(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL, output_params)
    return output_params

  def scintil_hal_tec_get_firmware_version(self):
    # 0 input arguments
    # 1 output arguments
    output_params = {}
    request = f"http://{self.server}:{self.port}/hal{'delegate' if self.delegate else ''}/scintil_hal_tec_get_firmware_version"
    if self.token:
      request += f"?lock-token=" + self.token
    logging.debug("Request : " + request)
    try:
      response = requests.get(request)
      #output_params['response'] = response.text
      logging.debug("Response : " + response.text)
      err_match = re.match(r'.*\nerr=(0x\S+)\n.*', response.text, flags=re.DOTALL)
      err_api_match = re.match(r'(Invalid method.*)', response.text, flags=re.DOTALL)
      output_params['status_code'] = response.status_code
      if err_match:
         output_params['err'] = int(err_match.groups()[0],0)
         output_params['err_hex'] = err_match.groups()[0]
         try:
           output_params['err_str'] = self.getErrorString(output_params['err']) + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      elif err_api_match:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value)
         try:
           output_params['err_str'] = "API Error: " + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      else:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value
         output_params['err_str'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.name
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value)
         output_params['errcode'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN
      if (output_params['err'] and self.shouldraise):
         raise ScintilError(output_params['errcode'] or scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN, output_params)
      fw_match = re.match(r".*\*fw=(\S+)", response.text, flags=re.DOTALL)
      if fw_match:
         output_params['fw'] = float(fw_match.groups()[0])
      else:
         output_params['fw'] = None
    except requests.exceptions.RequestException as e:
      ch_error = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL
      output_params['err'] = ch_error.value
      output_params['err_str'] = ch_error.name
      output_params['errcode'] = ch_error
      if (self.shouldraise):
         raise ScintilError(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL, output_params)
    return output_params

  def scintil_hal_tec_get_hardware_version(self):
    # 0 input arguments
    # 1 output arguments
    output_params = {}
    request = f"http://{self.server}:{self.port}/hal{'delegate' if self.delegate else ''}/scintil_hal_tec_get_hardware_version"
    if self.token:
      request += f"?lock-token=" + self.token
    logging.debug("Request : " + request)
    try:
      response = requests.get(request)
      #output_params['response'] = response.text
      logging.debug("Response : " + response.text)
      err_match = re.match(r'.*\nerr=(0x\S+)\n.*', response.text, flags=re.DOTALL)
      err_api_match = re.match(r'(Invalid method.*)', response.text, flags=re.DOTALL)
      output_params['status_code'] = response.status_code
      if err_match:
         output_params['err'] = int(err_match.groups()[0],0)
         output_params['err_hex'] = err_match.groups()[0]
         try:
           output_params['err_str'] = self.getErrorString(output_params['err']) + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      elif err_api_match:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value)
         try:
           output_params['err_str'] = "API Error: " + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      else:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value
         output_params['err_str'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.name
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value)
         output_params['errcode'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN
      if (output_params['err'] and self.shouldraise):
         raise ScintilError(output_params['errcode'] or scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN, output_params)
      hw_match = re.match(r".*\*hw=(\S+)", response.text, flags=re.DOTALL)
      if hw_match:
         output_params['hw'] = float(hw_match.groups()[0])
      else:
         output_params['hw'] = None
    except requests.exceptions.RequestException as e:
      ch_error = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL
      output_params['err'] = ch_error.value
      output_params['err_str'] = ch_error.name
      output_params['errcode'] = ch_error
      if (self.shouldraise):
         raise ScintilError(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL, output_params)
    return output_params

  def scintil_hal_tec_get_object_temp( self, module: scintil_hal_module_t):
    # 1 input arguments
    # 1 output arguments
    output_params = {}
    request = f"http://{self.server}:{self.port}/hal{'delegate' if self.delegate else ''}/scintil_hal_tec_get_object_temp/{module.value if hasattr(module,'value') else module}"
    if self.token:
      request += f"?lock-token=" + self.token
    logging.debug("Request : " + request)
    try:
      response = requests.get(request)
      #output_params['response'] = response.text
      logging.debug("Response : " + response.text)
      err_match = re.match(r'.*\nerr=(0x\S+)\n.*', response.text, flags=re.DOTALL)
      err_api_match = re.match(r'(Invalid method.*)', response.text, flags=re.DOTALL)
      output_params['status_code'] = response.status_code
      if err_match:
         output_params['err'] = int(err_match.groups()[0],0)
         output_params['err_hex'] = err_match.groups()[0]
         try:
           output_params['err_str'] = self.getErrorString(output_params['err']) + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      elif err_api_match:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value)
         try:
           output_params['err_str'] = "API Error: " + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      else:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value
         output_params['err_str'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.name
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value)
         output_params['errcode'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN
      if (output_params['err'] and self.shouldraise):
         raise ScintilError(output_params['errcode'] or scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN, output_params)
      temperature_match = re.match(r".*\*temperature=(\S+)", response.text, flags=re.DOTALL)
      if temperature_match:
         output_params['temperature'] = float(temperature_match.groups()[0])
      else:
         output_params['temperature'] = None
    except requests.exceptions.RequestException as e:
      ch_error = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL
      output_params['err'] = ch_error.value
      output_params['err_str'] = ch_error.name
      output_params['errcode'] = ch_error
      if (self.shouldraise):
         raise ScintilError(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL, output_params)
    return output_params

  def scintil_hal_tec_get_sink_temp( self, module: scintil_hal_module_t):
    # 1 input arguments
    # 1 output arguments
    output_params = {}
    request = f"http://{self.server}:{self.port}/hal{'delegate' if self.delegate else ''}/scintil_hal_tec_get_sink_temp/{module.value if hasattr(module,'value') else module}"
    if self.token:
      request += f"?lock-token=" + self.token
    logging.debug("Request : " + request)
    try:
      response = requests.get(request)
      #output_params['response'] = response.text
      logging.debug("Response : " + response.text)
      err_match = re.match(r'.*\nerr=(0x\S+)\n.*', response.text, flags=re.DOTALL)
      err_api_match = re.match(r'(Invalid method.*)', response.text, flags=re.DOTALL)
      output_params['status_code'] = response.status_code
      if err_match:
         output_params['err'] = int(err_match.groups()[0],0)
         output_params['err_hex'] = err_match.groups()[0]
         try:
           output_params['err_str'] = self.getErrorString(output_params['err']) + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      elif err_api_match:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value)
         try:
           output_params['err_str'] = "API Error: " + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      else:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value
         output_params['err_str'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.name
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value)
         output_params['errcode'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN
      if (output_params['err'] and self.shouldraise):
         raise ScintilError(output_params['errcode'] or scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN, output_params)
      temperature_match = re.match(r".*\*temperature=(\S+)", response.text, flags=re.DOTALL)
      if temperature_match:
         output_params['temperature'] = float(temperature_match.groups()[0])
      else:
         output_params['temperature'] = None
    except requests.exceptions.RequestException as e:
      ch_error = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL
      output_params['err'] = ch_error.value
      output_params['err_str'] = ch_error.name
      output_params['errcode'] = ch_error
      if (self.shouldraise):
         raise ScintilError(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL, output_params)
    return output_params

  def scintil_hal_tec_get_target_object_temp( self, module: scintil_hal_module_t):
    # 1 input arguments
    # 1 output arguments
    output_params = {}
    request = f"http://{self.server}:{self.port}/hal{'delegate' if self.delegate else ''}/scintil_hal_tec_get_target_object_temp/{module.value if hasattr(module,'value') else module}"
    if self.token:
      request += f"?lock-token=" + self.token
    logging.debug("Request : " + request)
    try:
      response = requests.get(request)
      #output_params['response'] = response.text
      logging.debug("Response : " + response.text)
      err_match = re.match(r'.*\nerr=(0x\S+)\n.*', response.text, flags=re.DOTALL)
      err_api_match = re.match(r'(Invalid method.*)', response.text, flags=re.DOTALL)
      output_params['status_code'] = response.status_code
      if err_match:
         output_params['err'] = int(err_match.groups()[0],0)
         output_params['err_hex'] = err_match.groups()[0]
         try:
           output_params['err_str'] = self.getErrorString(output_params['err']) + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      elif err_api_match:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value)
         try:
           output_params['err_str'] = "API Error: " + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      else:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value
         output_params['err_str'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.name
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value)
         output_params['errcode'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN
      if (output_params['err'] and self.shouldraise):
         raise ScintilError(output_params['errcode'] or scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN, output_params)
      temperature_match = re.match(r".*\*temperature=(\S+)", response.text, flags=re.DOTALL)
      if temperature_match:
         output_params['temperature'] = float(temperature_match.groups()[0])
      else:
         output_params['temperature'] = None
    except requests.exceptions.RequestException as e:
      ch_error = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL
      output_params['err'] = ch_error.value
      output_params['err_str'] = ch_error.name
      output_params['errcode'] = ch_error
      if (self.shouldraise):
         raise ScintilError(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL, output_params)
    return output_params

  def scintil_hal_tec_set_target_object_temp( self, module: scintil_hal_module_t, temperature: float):
    # 2 input arguments
    # 0 output arguments
    output_params = {}
    request = f"http://{self.server}:{self.port}/hal{'delegate' if self.delegate else ''}/scintil_hal_tec_set_target_object_temp/{module.value if hasattr(module,'value') else module}/{temperature}"
    if self.token:
      request += f"?lock-token=" + self.token
    logging.debug("Request : " + request)
    try:
      response = requests.get(request)
      #output_params['response'] = response.text
      logging.debug("Response : " + response.text)
      err_match = re.match(r'.*\nerr=(0x\S+)\n.*', response.text, flags=re.DOTALL)
      err_api_match = re.match(r'(Invalid method.*)', response.text, flags=re.DOTALL)
      output_params['status_code'] = response.status_code
      if err_match:
         output_params['err'] = int(err_match.groups()[0],0)
         output_params['err_hex'] = err_match.groups()[0]
         try:
           output_params['err_str'] = self.getErrorString(output_params['err']) + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      elif err_api_match:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value)
         try:
           output_params['err_str'] = "API Error: " + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      else:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value
         output_params['err_str'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.name
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value)
         output_params['errcode'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN
      if (output_params['err'] and self.shouldraise):
         raise ScintilError(output_params['errcode'] or scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN, output_params)
    except requests.exceptions.RequestException as e:
      ch_error = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL
      output_params['err'] = ch_error.value
      output_params['err_str'] = ch_error.name
      output_params['errcode'] = ch_error
      if (self.shouldraise):
         raise ScintilError(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL, output_params)
    return output_params

  def scintil_hal_tec_device_temperature(self):
    # 0 input arguments
    # 1 output arguments
    output_params = {}
    request = f"http://{self.server}:{self.port}/hal{'delegate' if self.delegate else ''}/scintil_hal_tec_device_temperature"
    if self.token:
      request += f"?lock-token=" + self.token
    logging.debug("Request : " + request)
    try:
      response = requests.get(request)
      #output_params['response'] = response.text
      logging.debug("Response : " + response.text)
      err_match = re.match(r'.*\nerr=(0x\S+)\n.*', response.text, flags=re.DOTALL)
      err_api_match = re.match(r'(Invalid method.*)', response.text, flags=re.DOTALL)
      output_params['status_code'] = response.status_code
      if err_match:
         output_params['err'] = int(err_match.groups()[0],0)
         output_params['err_hex'] = err_match.groups()[0]
         try:
           output_params['err_str'] = self.getErrorString(output_params['err']) + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      elif err_api_match:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value)
         try:
           output_params['err_str'] = "API Error: " + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      else:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value
         output_params['err_str'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.name
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value)
         output_params['errcode'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN
      if (output_params['err'] and self.shouldraise):
         raise ScintilError(output_params['errcode'] or scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN, output_params)
      temperature_match = re.match(r".*\*temperature=(\S+)", response.text, flags=re.DOTALL)
      if temperature_match:
         output_params['temperature'] = float(temperature_match.groups()[0])
      else:
         output_params['temperature'] = None
    except requests.exceptions.RequestException as e:
      ch_error = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL
      output_params['err'] = ch_error.value
      output_params['err_str'] = ch_error.name
      output_params['errcode'] = ch_error
      if (self.shouldraise):
         raise ScintilError(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL, output_params)
    return output_params

  def scintil_hal_tec_output_set_enable( self, module: scintil_hal_module_t, enable: bool):
    # 2 input arguments
    # 0 output arguments
    output_params = {}
    request = f"http://{self.server}:{self.port}/hal{'delegate' if self.delegate else ''}/scintil_hal_tec_output_set_enable/{module.value if hasattr(module,'value') else module}/{int(enable)}"
    if self.token:
      request += f"?lock-token=" + self.token
    logging.debug("Request : " + request)
    try:
      response = requests.get(request)
      #output_params['response'] = response.text
      logging.debug("Response : " + response.text)
      err_match = re.match(r'.*\nerr=(0x\S+)\n.*', response.text, flags=re.DOTALL)
      err_api_match = re.match(r'(Invalid method.*)', response.text, flags=re.DOTALL)
      output_params['status_code'] = response.status_code
      if err_match:
         output_params['err'] = int(err_match.groups()[0],0)
         output_params['err_hex'] = err_match.groups()[0]
         try:
           output_params['err_str'] = self.getErrorString(output_params['err']) + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      elif err_api_match:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value)
         try:
           output_params['err_str'] = "API Error: " + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      else:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value
         output_params['err_str'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.name
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value)
         output_params['errcode'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN
      if (output_params['err'] and self.shouldraise):
         raise ScintilError(output_params['errcode'] or scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN, output_params)
    except requests.exceptions.RequestException as e:
      ch_error = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL
      output_params['err'] = ch_error.value
      output_params['err_str'] = ch_error.name
      output_params['errcode'] = ch_error
      if (self.shouldraise):
         raise ScintilError(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL, output_params)
    return output_params

  def scintil_hal_tec_output_get_enable( self, module: scintil_hal_module_t):
    # 1 input arguments
    # 1 output arguments
    output_params = {}
    request = f"http://{self.server}:{self.port}/hal{'delegate' if self.delegate else ''}/scintil_hal_tec_output_get_enable/{module.value if hasattr(module,'value') else module}"
    if self.token:
      request += f"?lock-token=" + self.token
    logging.debug("Request : " + request)
    try:
      response = requests.get(request)
      #output_params['response'] = response.text
      logging.debug("Response : " + response.text)
      err_match = re.match(r'.*\nerr=(0x\S+)\n.*', response.text, flags=re.DOTALL)
      err_api_match = re.match(r'(Invalid method.*)', response.text, flags=re.DOTALL)
      output_params['status_code'] = response.status_code
      if err_match:
         output_params['err'] = int(err_match.groups()[0],0)
         output_params['err_hex'] = err_match.groups()[0]
         try:
           output_params['err_str'] = self.getErrorString(output_params['err']) + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      elif err_api_match:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value)
         try:
           output_params['err_str'] = "API Error: " + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      else:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value
         output_params['err_str'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.name
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value)
         output_params['errcode'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN
      if (output_params['err'] and self.shouldraise):
         raise ScintilError(output_params['errcode'] or scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN, output_params)
      enable_match = re.match(r".*\*enable=(\S+)", response.text, flags=re.DOTALL)
      if enable_match:
         output_params['enable'] = int(enable_match.groups()[0])
      else:
         output_params['enable'] = None
    except requests.exceptions.RequestException as e:
      ch_error = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL
      output_params['err'] = ch_error.value
      output_params['err_str'] = ch_error.name
      output_params['errcode'] = ch_error
      if (self.shouldraise):
         raise ScintilError(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL, output_params)
    return output_params

  def scintil_hal_tec_set_static_current( self, module: scintil_hal_module_t, current: float):
    # 2 input arguments
    # 0 output arguments
    output_params = {}
    request = f"http://{self.server}:{self.port}/hal{'delegate' if self.delegate else ''}/scintil_hal_tec_set_static_current/{module.value if hasattr(module,'value') else module}/{current}"
    if self.token:
      request += f"?lock-token=" + self.token
    logging.debug("Request : " + request)
    try:
      response = requests.get(request)
      #output_params['response'] = response.text
      logging.debug("Response : " + response.text)
      err_match = re.match(r'.*\nerr=(0x\S+)\n.*', response.text, flags=re.DOTALL)
      err_api_match = re.match(r'(Invalid method.*)', response.text, flags=re.DOTALL)
      output_params['status_code'] = response.status_code
      if err_match:
         output_params['err'] = int(err_match.groups()[0],0)
         output_params['err_hex'] = err_match.groups()[0]
         try:
           output_params['err_str'] = self.getErrorString(output_params['err']) + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      elif err_api_match:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value)
         try:
           output_params['err_str'] = "API Error: " + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      else:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value
         output_params['err_str'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.name
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value)
         output_params['errcode'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN
      if (output_params['err'] and self.shouldraise):
         raise ScintilError(output_params['errcode'] or scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN, output_params)
    except requests.exceptions.RequestException as e:
      ch_error = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL
      output_params['err'] = ch_error.value
      output_params['err_str'] = ch_error.name
      output_params['errcode'] = ch_error
      if (self.shouldraise):
         raise ScintilError(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL, output_params)
    return output_params

  def scintil_hal_tec_set_static_voltage( self, module: scintil_hal_module_t, voltage: float):
    # 2 input arguments
    # 0 output arguments
    output_params = {}
    request = f"http://{self.server}:{self.port}/hal{'delegate' if self.delegate else ''}/scintil_hal_tec_set_static_voltage/{module.value if hasattr(module,'value') else module}/{voltage}"
    if self.token:
      request += f"?lock-token=" + self.token
    logging.debug("Request : " + request)
    try:
      response = requests.get(request)
      #output_params['response'] = response.text
      logging.debug("Response : " + response.text)
      err_match = re.match(r'.*\nerr=(0x\S+)\n.*', response.text, flags=re.DOTALL)
      err_api_match = re.match(r'(Invalid method.*)', response.text, flags=re.DOTALL)
      output_params['status_code'] = response.status_code
      if err_match:
         output_params['err'] = int(err_match.groups()[0],0)
         output_params['err_hex'] = err_match.groups()[0]
         try:
           output_params['err_str'] = self.getErrorString(output_params['err']) + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      elif err_api_match:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value)
         try:
           output_params['err_str'] = "API Error: " + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      else:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value
         output_params['err_str'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.name
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value)
         output_params['errcode'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN
      if (output_params['err'] and self.shouldraise):
         raise ScintilError(output_params['errcode'] or scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN, output_params)
    except requests.exceptions.RequestException as e:
      ch_error = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL
      output_params['err'] = ch_error.value
      output_params['err_str'] = ch_error.name
      output_params['errcode'] = ch_error
      if (self.shouldraise):
         raise ScintilError(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL, output_params)
    return output_params

  def scintil_hal_tec_get_actual_current_output( self, module: scintil_hal_module_t):
    # 1 input arguments
    # 1 output arguments
    output_params = {}
    request = f"http://{self.server}:{self.port}/hal{'delegate' if self.delegate else ''}/scintil_hal_tec_get_actual_current_output/{module.value if hasattr(module,'value') else module}"
    if self.token:
      request += f"?lock-token=" + self.token
    logging.debug("Request : " + request)
    try:
      response = requests.get(request)
      #output_params['response'] = response.text
      logging.debug("Response : " + response.text)
      err_match = re.match(r'.*\nerr=(0x\S+)\n.*', response.text, flags=re.DOTALL)
      err_api_match = re.match(r'(Invalid method.*)', response.text, flags=re.DOTALL)
      output_params['status_code'] = response.status_code
      if err_match:
         output_params['err'] = int(err_match.groups()[0],0)
         output_params['err_hex'] = err_match.groups()[0]
         try:
           output_params['err_str'] = self.getErrorString(output_params['err']) + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      elif err_api_match:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value)
         try:
           output_params['err_str'] = "API Error: " + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      else:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value
         output_params['err_str'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.name
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value)
         output_params['errcode'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN
      if (output_params['err'] and self.shouldraise):
         raise ScintilError(output_params['errcode'] or scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN, output_params)
      current_match = re.match(r".*\*current=(\S+)", response.text, flags=re.DOTALL)
      if current_match:
         output_params['current'] = float(current_match.groups()[0])
      else:
         output_params['current'] = None
    except requests.exceptions.RequestException as e:
      ch_error = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL
      output_params['err'] = ch_error.value
      output_params['err_str'] = ch_error.name
      output_params['errcode'] = ch_error
      if (self.shouldraise):
         raise ScintilError(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL, output_params)
    return output_params

  def scintil_hal_tec_get_actual_voltage_output( self, module: scintil_hal_module_t):
    # 1 input arguments
    # 1 output arguments
    output_params = {}
    request = f"http://{self.server}:{self.port}/hal{'delegate' if self.delegate else ''}/scintil_hal_tec_get_actual_voltage_output/{module.value if hasattr(module,'value') else module}"
    if self.token:
      request += f"?lock-token=" + self.token
    logging.debug("Request : " + request)
    try:
      response = requests.get(request)
      #output_params['response'] = response.text
      logging.debug("Response : " + response.text)
      err_match = re.match(r'.*\nerr=(0x\S+)\n.*', response.text, flags=re.DOTALL)
      err_api_match = re.match(r'(Invalid method.*)', response.text, flags=re.DOTALL)
      output_params['status_code'] = response.status_code
      if err_match:
         output_params['err'] = int(err_match.groups()[0],0)
         output_params['err_hex'] = err_match.groups()[0]
         try:
           output_params['err_str'] = self.getErrorString(output_params['err']) + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      elif err_api_match:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value)
         try:
           output_params['err_str'] = "API Error: " + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      else:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value
         output_params['err_str'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.name
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value)
         output_params['errcode'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN
      if (output_params['err'] and self.shouldraise):
         raise ScintilError(output_params['errcode'] or scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN, output_params)
      voltage_match = re.match(r".*\*voltage=(\S+)", response.text, flags=re.DOTALL)
      if voltage_match:
         output_params['voltage'] = float(voltage_match.groups()[0])
      else:
         output_params['voltage'] = None
    except requests.exceptions.RequestException as e:
      ch_error = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL
      output_params['err'] = ch_error.value
      output_params['err_str'] = ch_error.name
      output_params['errcode'] = ch_error
      if (self.shouldraise):
         raise ScintilError(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL, output_params)
    return output_params

  def scintil_hal_tec_get_max_possible_voltage( self, module: scintil_hal_module_t):
    # 1 input arguments
    # 1 output arguments
    output_params = {}
    request = f"http://{self.server}:{self.port}/hal{'delegate' if self.delegate else ''}/scintil_hal_tec_get_max_possible_voltage/{module.value if hasattr(module,'value') else module}"
    if self.token:
      request += f"?lock-token=" + self.token
    logging.debug("Request : " + request)
    try:
      response = requests.get(request)
      #output_params['response'] = response.text
      logging.debug("Response : " + response.text)
      err_match = re.match(r'.*\nerr=(0x\S+)\n.*', response.text, flags=re.DOTALL)
      err_api_match = re.match(r'(Invalid method.*)', response.text, flags=re.DOTALL)
      output_params['status_code'] = response.status_code
      if err_match:
         output_params['err'] = int(err_match.groups()[0],0)
         output_params['err_hex'] = err_match.groups()[0]
         try:
           output_params['err_str'] = self.getErrorString(output_params['err']) + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      elif err_api_match:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value)
         try:
           output_params['err_str'] = "API Error: " + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      else:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value
         output_params['err_str'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.name
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value)
         output_params['errcode'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN
      if (output_params['err'] and self.shouldraise):
         raise ScintilError(output_params['errcode'] or scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN, output_params)
      voltage_match = re.match(r".*\*voltage=(\S+)", response.text, flags=re.DOTALL)
      if voltage_match:
         output_params['voltage'] = float(voltage_match.groups()[0])
      else:
         output_params['voltage'] = None
    except requests.exceptions.RequestException as e:
      ch_error = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL
      output_params['err'] = ch_error.value
      output_params['err_str'] = ch_error.name
      output_params['errcode'] = ch_error
      if (self.shouldraise):
         raise ScintilError(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL, output_params)
    return output_params

  def scintil_hal_tec_test_peltier( self, module: scintil_hal_module_t):
    # 1 input arguments
    # 0 output arguments
    output_params = {}
    request = f"http://{self.server}:{self.port}/hal{'delegate' if self.delegate else ''}/scintil_hal_tec_test_peltier/{module.value if hasattr(module,'value') else module}"
    if self.token:
      request += f"?lock-token=" + self.token
    logging.debug("Request : " + request)
    try:
      response = requests.get(request)
      #output_params['response'] = response.text
      logging.debug("Response : " + response.text)
      err_match = re.match(r'.*\nerr=(0x\S+)\n.*', response.text, flags=re.DOTALL)
      err_api_match = re.match(r'(Invalid method.*)', response.text, flags=re.DOTALL)
      output_params['status_code'] = response.status_code
      if err_match:
         output_params['err'] = int(err_match.groups()[0],0)
         output_params['err_hex'] = err_match.groups()[0]
         try:
           output_params['err_str'] = self.getErrorString(output_params['err']) + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      elif err_api_match:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value)
         try:
           output_params['err_str'] = "API Error: " + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      else:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value
         output_params['err_str'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.name
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value)
         output_params['errcode'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN
      if (output_params['err'] and self.shouldraise):
         raise ScintilError(output_params['errcode'] or scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN, output_params)
    except requests.exceptions.RequestException as e:
      ch_error = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL
      output_params['err'] = ch_error.value
      output_params['err_str'] = ch_error.name
      output_params['errcode'] = ch_error
      if (self.shouldraise):
         raise ScintilError(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL, output_params)
    return output_params

  def scintil_hal_tec_get_object_source_selection( self, module: scintil_hal_module_t):
    # 1 input arguments
    # 1 output arguments
    output_params = {}
    request = f"http://{self.server}:{self.port}/hal{'delegate' if self.delegate else ''}/scintil_hal_tec_get_object_source_selection/{module.value if hasattr(module,'value') else module}"
    if self.token:
      request += f"?lock-token=" + self.token
    logging.debug("Request : " + request)
    try:
      response = requests.get(request)
      #output_params['response'] = response.text
      logging.debug("Response : " + response.text)
      err_match = re.match(r'.*\nerr=(0x\S+)\n.*', response.text, flags=re.DOTALL)
      err_api_match = re.match(r'(Invalid method.*)', response.text, flags=re.DOTALL)
      output_params['status_code'] = response.status_code
      if err_match:
         output_params['err'] = int(err_match.groups()[0],0)
         output_params['err_hex'] = err_match.groups()[0]
         try:
           output_params['err_str'] = self.getErrorString(output_params['err']) + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      elif err_api_match:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value)
         try:
           output_params['err_str'] = "API Error: " + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      else:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value
         output_params['err_str'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.name
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value)
         output_params['errcode'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN
      if (output_params['err'] and self.shouldraise):
         raise ScintilError(output_params['errcode'] or scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN, output_params)
      source_match = re.match(r".*\*source=(\S+)", response.text, flags=re.DOTALL)
      if source_match:
         output_params['source'] = scintil_hal_tec_object_source_t(int(source_match.groups()[0]))
      else:
         output_params['source'] = None
    except requests.exceptions.RequestException as e:
      ch_error = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL
      output_params['err'] = ch_error.value
      output_params['err_str'] = ch_error.name
      output_params['errcode'] = ch_error
      if (self.shouldraise):
         raise ScintilError(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL, output_params)
    return output_params

  def scintil_hal_tec_set_object_source_selection( self, module: scintil_hal_module_t, source: scintil_hal_tec_object_source_t):
    # 2 input arguments
    # 0 output arguments
    output_params = {}
    request = f"http://{self.server}:{self.port}/hal{'delegate' if self.delegate else ''}/scintil_hal_tec_set_object_source_selection/{module.value if hasattr(module,'value') else module}/{source.value if hasattr(source,'value') else source}"
    if self.token:
      request += f"?lock-token=" + self.token
    logging.debug("Request : " + request)
    try:
      response = requests.get(request)
      #output_params['response'] = response.text
      logging.debug("Response : " + response.text)
      err_match = re.match(r'.*\nerr=(0x\S+)\n.*', response.text, flags=re.DOTALL)
      err_api_match = re.match(r'(Invalid method.*)', response.text, flags=re.DOTALL)
      output_params['status_code'] = response.status_code
      if err_match:
         output_params['err'] = int(err_match.groups()[0],0)
         output_params['err_hex'] = err_match.groups()[0]
         try:
           output_params['err_str'] = self.getErrorString(output_params['err']) + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      elif err_api_match:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value)
         try:
           output_params['err_str'] = "API Error: " + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      else:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value
         output_params['err_str'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.name
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value)
         output_params['errcode'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN
      if (output_params['err'] and self.shouldraise):
         raise ScintilError(output_params['errcode'] or scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN, output_params)
    except requests.exceptions.RequestException as e:
      ch_error = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL
      output_params['err'] = ch_error.value
      output_params['err_str'] = ch_error.name
      output_params['errcode'] = ch_error
      if (self.shouldraise):
         raise ScintilError(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL, output_params)
    return output_params

  def scintil_hal_temperature_module_get_val( self, module: scintil_hal_module_t):
    # 1 input arguments
    # 1 output arguments
    output_params = {}
    request = f"http://{self.server}:{self.port}/hal{'delegate' if self.delegate else ''}/scintil_hal_temperature_module_get_val/{module.value if hasattr(module,'value') else module}"
    if self.token:
      request += f"?lock-token=" + self.token
    logging.debug("Request : " + request)
    try:
      response = requests.get(request)
      #output_params['response'] = response.text
      logging.debug("Response : " + response.text)
      err_match = re.match(r'.*\nerr=(0x\S+)\n.*', response.text, flags=re.DOTALL)
      err_api_match = re.match(r'(Invalid method.*)', response.text, flags=re.DOTALL)
      output_params['status_code'] = response.status_code
      if err_match:
         output_params['err'] = int(err_match.groups()[0],0)
         output_params['err_hex'] = err_match.groups()[0]
         try:
           output_params['err_str'] = self.getErrorString(output_params['err']) + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      elif err_api_match:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value)
         try:
           output_params['err_str'] = "API Error: " + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      else:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value
         output_params['err_str'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.name
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value)
         output_params['errcode'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN
      if (output_params['err'] and self.shouldraise):
         raise ScintilError(output_params['errcode'] or scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN, output_params)
      temperature_match = re.match(r".*\*temperature=(\S+)", response.text, flags=re.DOTALL)
      if temperature_match:
         output_params['temperature'] = float(temperature_match.groups()[0])
      else:
         output_params['temperature'] = None
    except requests.exceptions.RequestException as e:
      ch_error = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL
      output_params['err'] = ch_error.value
      output_params['err_str'] = ch_error.name
      output_params['errcode'] = ch_error
      if (self.shouldraise):
         raise ScintilError(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL, output_params)
    return output_params

  def scintil_hal_temperature_get_val( self, instance: scintil_hal_temp_t):
    # 1 input arguments
    # 1 output arguments
    output_params = {}
    request = f"http://{self.server}:{self.port}/hal{'delegate' if self.delegate else ''}/scintil_hal_temperature_get_val/{instance.value if hasattr(instance,'value') else instance}"
    if self.token:
      request += f"?lock-token=" + self.token
    logging.debug("Request : " + request)
    try:
      response = requests.get(request)
      #output_params['response'] = response.text
      logging.debug("Response : " + response.text)
      err_match = re.match(r'.*\nerr=(0x\S+)\n.*', response.text, flags=re.DOTALL)
      err_api_match = re.match(r'(Invalid method.*)', response.text, flags=re.DOTALL)
      output_params['status_code'] = response.status_code
      if err_match:
         output_params['err'] = int(err_match.groups()[0],0)
         output_params['err_hex'] = err_match.groups()[0]
         try:
           output_params['err_str'] = self.getErrorString(output_params['err']) + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      elif err_api_match:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value)
         try:
           output_params['err_str'] = "API Error: " + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      else:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value
         output_params['err_str'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.name
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value)
         output_params['errcode'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN
      if (output_params['err'] and self.shouldraise):
         raise ScintilError(output_params['errcode'] or scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN, output_params)
      temperature_match = re.match(r".*\*temperature=(\S+)", response.text, flags=re.DOTALL)
      if temperature_match:
         output_params['temperature'] = float(temperature_match.groups()[0])
      else:
         output_params['temperature'] = None
    except requests.exceptions.RequestException as e:
      ch_error = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL
      output_params['err'] = ch_error.value
      output_params['err_str'] = ch_error.name
      output_params['errcode'] = ch_error
      if (self.shouldraise):
         raise ScintilError(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL, output_params)
    return output_params

  def scintil_hal_temperature_pic_get_val( self, module: scintil_hal_module_t):
    # 1 input arguments
    # 1 output arguments
    output_params = {}
    request = f"http://{self.server}:{self.port}/hal{'delegate' if self.delegate else ''}/scintil_hal_temperature_pic_get_val/{module.value if hasattr(module,'value') else module}"
    if self.token:
      request += f"?lock-token=" + self.token
    logging.debug("Request : " + request)
    try:
      response = requests.get(request)
      #output_params['response'] = response.text
      logging.debug("Response : " + response.text)
      err_match = re.match(r'.*\nerr=(0x\S+)\n.*', response.text, flags=re.DOTALL)
      err_api_match = re.match(r'(Invalid method.*)', response.text, flags=re.DOTALL)
      output_params['status_code'] = response.status_code
      if err_match:
         output_params['err'] = int(err_match.groups()[0],0)
         output_params['err_hex'] = err_match.groups()[0]
         try:
           output_params['err_str'] = self.getErrorString(output_params['err']) + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      elif err_api_match:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value)
         try:
           output_params['err_str'] = "API Error: " + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      else:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value
         output_params['err_str'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.name
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value)
         output_params['errcode'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN
      if (output_params['err'] and self.shouldraise):
         raise ScintilError(output_params['errcode'] or scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN, output_params)
      temperature_match = re.match(r".*\*temperature=(\S+)", response.text, flags=re.DOTALL)
      if temperature_match:
         output_params['temperature'] = float(temperature_match.groups()[0])
      else:
         output_params['temperature'] = None
    except requests.exceptions.RequestException as e:
      ch_error = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL
      output_params['err'] = ch_error.value
      output_params['err_str'] = ch_error.name
      output_params['errcode'] = ch_error
      if (self.shouldraise):
         raise ScintilError(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL, output_params)
    return output_params

  def scintil_hal_ll_temperature_get_status( self, instance: scintil_hal_temp_t):
    # 1 input arguments
    # 1 output arguments
    output_params = {}
    request = f"http://{self.server}:{self.port}/hal{'delegate' if self.delegate else ''}/scintil_hal_ll_temperature_get_status/{instance.value if hasattr(instance,'value') else instance}"
    if self.token:
      request += f"?lock-token=" + self.token
    logging.debug("Request : " + request)
    try:
      response = requests.get(request)
      #output_params['response'] = response.text
      logging.debug("Response : " + response.text)
      err_match = re.match(r'.*\nerr=(0x\S+)\n.*', response.text, flags=re.DOTALL)
      err_api_match = re.match(r'(Invalid method.*)', response.text, flags=re.DOTALL)
      output_params['status_code'] = response.status_code
      if err_match:
         output_params['err'] = int(err_match.groups()[0],0)
         output_params['err_hex'] = err_match.groups()[0]
         try:
           output_params['err_str'] = self.getErrorString(output_params['err']) + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      elif err_api_match:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value)
         try:
           output_params['err_str'] = "API Error: " + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      else:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value
         output_params['err_str'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.name
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value)
         output_params['errcode'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN
      if (output_params['err'] and self.shouldraise):
         raise ScintilError(output_params['errcode'] or scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN, output_params)
      status_match = re.match(r".*\*status=(\S+)", response.text, flags=re.DOTALL)
      if status_match:
         output_params['status'] = int(status_match.groups()[0])
      else:
         output_params['status'] = None
    except requests.exceptions.RequestException as e:
      ch_error = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL
      output_params['err'] = ch_error.value
      output_params['err_str'] = ch_error.name
      output_params['errcode'] = ch_error
      if (self.shouldraise):
         raise ScintilError(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL, output_params)
    return output_params

  def scintil_hal_ll_temperature_get_value( self, instance: scintil_hal_temp_t, type: scintil_hal_temp_type_t):
    # 2 input arguments
    # 1 output arguments
    output_params = {}
    request = f"http://{self.server}:{self.port}/hal{'delegate' if self.delegate else ''}/scintil_hal_ll_temperature_get_value/{instance.value if hasattr(instance,'value') else instance}/{type.value if hasattr(type,'value') else type}"
    if self.token:
      request += f"?lock-token=" + self.token
    logging.debug("Request : " + request)
    try:
      response = requests.get(request)
      #output_params['response'] = response.text
      logging.debug("Response : " + response.text)
      err_match = re.match(r'.*\nerr=(0x\S+)\n.*', response.text, flags=re.DOTALL)
      err_api_match = re.match(r'(Invalid method.*)', response.text, flags=re.DOTALL)
      output_params['status_code'] = response.status_code
      if err_match:
         output_params['err'] = int(err_match.groups()[0],0)
         output_params['err_hex'] = err_match.groups()[0]
         try:
           output_params['err_str'] = self.getErrorString(output_params['err']) + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      elif err_api_match:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value)
         try:
           output_params['err_str'] = "API Error: " + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      else:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value
         output_params['err_str'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.name
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value)
         output_params['errcode'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN
      if (output_params['err'] and self.shouldraise):
         raise ScintilError(output_params['errcode'] or scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN, output_params)
      temperature_match = re.match(r".*\*temperature=(\S+)", response.text, flags=re.DOTALL)
      if temperature_match:
         output_params['temperature'] = float(temperature_match.groups()[0])
      else:
         output_params['temperature'] = None
    except requests.exceptions.RequestException as e:
      ch_error = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL
      output_params['err'] = ch_error.value
      output_params['err_str'] = ch_error.name
      output_params['errcode'] = ch_error
      if (self.shouldraise):
         raise ScintilError(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL, output_params)
    return output_params

  def scintil_hal_config_save(self):
    # 0 input arguments
    # 0 output arguments
    output_params = {}
    request = f"http://{self.server}:{self.port}/hal{'delegate' if self.delegate else ''}/scintil_hal_config_save"
    if self.token:
      request += f"?lock-token=" + self.token
    logging.debug("Request : " + request)
    try:
      response = requests.get(request)
      #output_params['response'] = response.text
      logging.debug("Response : " + response.text)
      err_match = re.match(r'.*\nerr=(0x\S+)\n.*', response.text, flags=re.DOTALL)
      err_api_match = re.match(r'(Invalid method.*)', response.text, flags=re.DOTALL)
      output_params['status_code'] = response.status_code
      if err_match:
         output_params['err'] = int(err_match.groups()[0],0)
         output_params['err_hex'] = err_match.groups()[0]
         try:
           output_params['err_str'] = self.getErrorString(output_params['err']) + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      elif err_api_match:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value)
         try:
           output_params['err_str'] = "API Error: " + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      else:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value
         output_params['err_str'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.name
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value)
         output_params['errcode'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN
      if (output_params['err'] and self.shouldraise):
         raise ScintilError(output_params['errcode'] or scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN, output_params)
    except requests.exceptions.RequestException as e:
      ch_error = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL
      output_params['err'] = ch_error.value
      output_params['err_str'] = ch_error.name
      output_params['errcode'] = ch_error
      if (self.shouldraise):
         raise ScintilError(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL, output_params)
    return output_params

  def scintil_hal_config_load(self):
    # 0 input arguments
    # 0 output arguments
    output_params = {}
    request = f"http://{self.server}:{self.port}/hal{'delegate' if self.delegate else ''}/scintil_hal_config_load"
    if self.token:
      request += f"?lock-token=" + self.token
    logging.debug("Request : " + request)
    try:
      response = requests.get(request)
      #output_params['response'] = response.text
      logging.debug("Response : " + response.text)
      err_match = re.match(r'.*\nerr=(0x\S+)\n.*', response.text, flags=re.DOTALL)
      err_api_match = re.match(r'(Invalid method.*)', response.text, flags=re.DOTALL)
      output_params['status_code'] = response.status_code
      if err_match:
         output_params['err'] = int(err_match.groups()[0],0)
         output_params['err_hex'] = err_match.groups()[0]
         try:
           output_params['err_str'] = self.getErrorString(output_params['err']) + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      elif err_api_match:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value)
         try:
           output_params['err_str'] = "API Error: " + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      else:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value
         output_params['err_str'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.name
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value)
         output_params['errcode'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN
      if (output_params['err'] and self.shouldraise):
         raise ScintilError(output_params['errcode'] or scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN, output_params)
    except requests.exceptions.RequestException as e:
      ch_error = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL
      output_params['err'] = ch_error.value
      output_params['err_str'] = ch_error.name
      output_params['errcode'] = ch_error
      if (self.shouldraise):
         raise ScintilError(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL, output_params)
    return output_params

  def scintil_hal_config_set_serial_number( self, serial_number: int):
    # 1 input arguments
    # 0 output arguments
    output_params = {}
    request = f"http://{self.server}:{self.port}/hal{'delegate' if self.delegate else ''}/scintil_hal_config_set_serial_number/{serial_number}"
    if self.token:
      request += f"?lock-token=" + self.token
    logging.debug("Request : " + request)
    try:
      response = requests.get(request)
      #output_params['response'] = response.text
      logging.debug("Response : " + response.text)
      err_match = re.match(r'.*\nerr=(0x\S+)\n.*', response.text, flags=re.DOTALL)
      err_api_match = re.match(r'(Invalid method.*)', response.text, flags=re.DOTALL)
      output_params['status_code'] = response.status_code
      if err_match:
         output_params['err'] = int(err_match.groups()[0],0)
         output_params['err_hex'] = err_match.groups()[0]
         try:
           output_params['err_str'] = self.getErrorString(output_params['err']) + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      elif err_api_match:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value)
         try:
           output_params['err_str'] = "API Error: " + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      else:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value
         output_params['err_str'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.name
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value)
         output_params['errcode'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN
      if (output_params['err'] and self.shouldraise):
         raise ScintilError(output_params['errcode'] or scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN, output_params)
    except requests.exceptions.RequestException as e:
      ch_error = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL
      output_params['err'] = ch_error.value
      output_params['err_str'] = ch_error.name
      output_params['errcode'] = ch_error
      if (self.shouldraise):
         raise ScintilError(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL, output_params)
    return output_params

  def scintil_hal_config_get_serial_number(self):
    # 0 input arguments
    # 1 output arguments
    output_params = {}
    request = f"http://{self.server}:{self.port}/hal{'delegate' if self.delegate else ''}/scintil_hal_config_get_serial_number"
    if self.token:
      request += f"?lock-token=" + self.token
    logging.debug("Request : " + request)
    try:
      response = requests.get(request)
      #output_params['response'] = response.text
      logging.debug("Response : " + response.text)
      err_match = re.match(r'.*\nerr=(0x\S+)\n.*', response.text, flags=re.DOTALL)
      err_api_match = re.match(r'(Invalid method.*)', response.text, flags=re.DOTALL)
      output_params['status_code'] = response.status_code
      if err_match:
         output_params['err'] = int(err_match.groups()[0],0)
         output_params['err_hex'] = err_match.groups()[0]
         try:
           output_params['err_str'] = self.getErrorString(output_params['err']) + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      elif err_api_match:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value)
         try:
           output_params['err_str'] = "API Error: " + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      else:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value
         output_params['err_str'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.name
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value)
         output_params['errcode'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN
      if (output_params['err'] and self.shouldraise):
         raise ScintilError(output_params['errcode'] or scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN, output_params)
      serial_number_match = re.match(r".*\*serial_number=(\S+)", response.text, flags=re.DOTALL)
      if serial_number_match:
         output_params['serial_number'] = int(serial_number_match.groups()[0])
      else:
         output_params['serial_number'] = None
    except requests.exceptions.RequestException as e:
      ch_error = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL
      output_params['err'] = ch_error.value
      output_params['err_str'] = ch_error.name
      output_params['errcode'] = ch_error
      if (self.shouldraise):
         raise ScintilError(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL, output_params)
    return output_params

  def scintil_hal_config_get_servoloop_laser( self, laser: scintil_hal_laser_t):
    # 1 input arguments
    # 1 output arguments
    output_params = {}
    request = f"http://{self.server}:{self.port}/hal{'delegate' if self.delegate else ''}/scintil_hal_config_get_servoloop_laser/{laser.value if hasattr(laser,'value') else laser}"
    if self.token:
      request += f"?lock-token=" + self.token
    logging.debug("Request : " + request)
    try:
      response = requests.get(request)
      #output_params['response'] = response.text
      logging.debug("Response : " + response.text)
      err_match = re.match(r'.*\nerr=(0x\S+)\n.*', response.text, flags=re.DOTALL)
      err_api_match = re.match(r'(Invalid method.*)', response.text, flags=re.DOTALL)
      output_params['status_code'] = response.status_code
      if err_match:
         output_params['err'] = int(err_match.groups()[0],0)
         output_params['err_hex'] = err_match.groups()[0]
         try:
           output_params['err_str'] = self.getErrorString(output_params['err']) + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      elif err_api_match:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value)
         try:
           output_params['err_str'] = "API Error: " + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      else:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value
         output_params['err_str'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.name
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value)
         output_params['errcode'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN
      if (output_params['err'] and self.shouldraise):
         raise ScintilError(output_params['errcode'] or scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN, output_params)
      conf_match = re.match(r".*\*conf=\s*({\S+})", response.text, flags=re.DOTALL)
      if conf_match:
         output_params['conf'] = scintil_hal_servoloop_laser_t.fromstring(conf_match.groups()[0])
      else:
         output_params['conf'] = None
    except requests.exceptions.RequestException as e:
      ch_error = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL
      output_params['err'] = ch_error.value
      output_params['err_str'] = ch_error.name
      output_params['errcode'] = ch_error
      if (self.shouldraise):
         raise ScintilError(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL, output_params)
    return output_params

  def scintil_hal_config_set_servoloop_laser( self, laser: scintil_hal_laser_t, conf: scintil_hal_servoloop_laser_t):
    # 2 input arguments
    # 0 output arguments
    output_params = {}
    request = f"http://{self.server}:{self.port}/hal{'delegate' if self.delegate else ''}/scintil_hal_config_set_servoloop_laser/{laser.value if hasattr(laser,'value') else laser}/{conf}"
    if self.token:
      request += f"?lock-token=" + self.token
    logging.debug("Request : " + request)
    try:
      response = requests.get(request)
      #output_params['response'] = response.text
      logging.debug("Response : " + response.text)
      err_match = re.match(r'.*\nerr=(0x\S+)\n.*', response.text, flags=re.DOTALL)
      err_api_match = re.match(r'(Invalid method.*)', response.text, flags=re.DOTALL)
      output_params['status_code'] = response.status_code
      if err_match:
         output_params['err'] = int(err_match.groups()[0],0)
         output_params['err_hex'] = err_match.groups()[0]
         try:
           output_params['err_str'] = self.getErrorString(output_params['err']) + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      elif err_api_match:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value)
         try:
           output_params['err_str'] = "API Error: " + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      else:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value
         output_params['err_str'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.name
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value)
         output_params['errcode'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN
      if (output_params['err'] and self.shouldraise):
         raise ScintilError(output_params['errcode'] or scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN, output_params)
    except requests.exceptions.RequestException as e:
      ch_error = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL
      output_params['err'] = ch_error.value
      output_params['err_str'] = ch_error.name
      output_params['errcode'] = ch_error
      if (self.shouldraise):
         raise ScintilError(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL, output_params)
    return output_params

  def scintil_hal_config_get_servoloop_heater( self, heater: scintil_hal_mux_heater_t):
    # 1 input arguments
    # 1 output arguments
    output_params = {}
    request = f"http://{self.server}:{self.port}/hal{'delegate' if self.delegate else ''}/scintil_hal_config_get_servoloop_heater/{heater.value if hasattr(heater,'value') else heater}"
    if self.token:
      request += f"?lock-token=" + self.token
    logging.debug("Request : " + request)
    try:
      response = requests.get(request)
      #output_params['response'] = response.text
      logging.debug("Response : " + response.text)
      err_match = re.match(r'.*\nerr=(0x\S+)\n.*', response.text, flags=re.DOTALL)
      err_api_match = re.match(r'(Invalid method.*)', response.text, flags=re.DOTALL)
      output_params['status_code'] = response.status_code
      if err_match:
         output_params['err'] = int(err_match.groups()[0],0)
         output_params['err_hex'] = err_match.groups()[0]
         try:
           output_params['err_str'] = self.getErrorString(output_params['err']) + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      elif err_api_match:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value)
         try:
           output_params['err_str'] = "API Error: " + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      else:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value
         output_params['err_str'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.name
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value)
         output_params['errcode'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN
      if (output_params['err'] and self.shouldraise):
         raise ScintilError(output_params['errcode'] or scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN, output_params)
      conf_match = re.match(r".*\*conf=\s*({\S+})", response.text, flags=re.DOTALL)
      if conf_match:
         output_params['conf'] = scintil_hal_servoloop_heater_t.fromstring(conf_match.groups()[0])
      else:
         output_params['conf'] = None
    except requests.exceptions.RequestException as e:
      ch_error = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL
      output_params['err'] = ch_error.value
      output_params['err_str'] = ch_error.name
      output_params['errcode'] = ch_error
      if (self.shouldraise):
         raise ScintilError(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL, output_params)
    return output_params

  def scintil_hal_config_set_servoloop_heater( self, heater: scintil_hal_mux_heater_t, conf: scintil_hal_servoloop_heater_t):
    # 2 input arguments
    # 0 output arguments
    output_params = {}
    request = f"http://{self.server}:{self.port}/hal{'delegate' if self.delegate else ''}/scintil_hal_config_set_servoloop_heater/{heater.value if hasattr(heater,'value') else heater}/{conf}"
    if self.token:
      request += f"?lock-token=" + self.token
    logging.debug("Request : " + request)
    try:
      response = requests.get(request)
      #output_params['response'] = response.text
      logging.debug("Response : " + response.text)
      err_match = re.match(r'.*\nerr=(0x\S+)\n.*', response.text, flags=re.DOTALL)
      err_api_match = re.match(r'(Invalid method.*)', response.text, flags=re.DOTALL)
      output_params['status_code'] = response.status_code
      if err_match:
         output_params['err'] = int(err_match.groups()[0],0)
         output_params['err_hex'] = err_match.groups()[0]
         try:
           output_params['err_str'] = self.getErrorString(output_params['err']) + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      elif err_api_match:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value)
         try:
           output_params['err_str'] = "API Error: " + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      else:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value
         output_params['err_str'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.name
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value)
         output_params['errcode'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN
      if (output_params['err'] and self.shouldraise):
         raise ScintilError(output_params['errcode'] or scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN, output_params)
    except requests.exceptions.RequestException as e:
      ch_error = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL
      output_params['err'] = ch_error.value
      output_params['err_str'] = ch_error.name
      output_params['errcode'] = ch_error
      if (self.shouldraise):
         raise ScintilError(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL, output_params)
    return output_params

  def scintil_hal_config_get_servoloop_ring(self):
    # 0 input arguments
    # 1 output arguments
    output_params = {}
    request = f"http://{self.server}:{self.port}/hal{'delegate' if self.delegate else ''}/scintil_hal_config_get_servoloop_ring"
    if self.token:
      request += f"?lock-token=" + self.token
    logging.debug("Request : " + request)
    try:
      response = requests.get(request)
      #output_params['response'] = response.text
      logging.debug("Response : " + response.text)
      err_match = re.match(r'.*\nerr=(0x\S+)\n.*', response.text, flags=re.DOTALL)
      err_api_match = re.match(r'(Invalid method.*)', response.text, flags=re.DOTALL)
      output_params['status_code'] = response.status_code
      if err_match:
         output_params['err'] = int(err_match.groups()[0],0)
         output_params['err_hex'] = err_match.groups()[0]
         try:
           output_params['err_str'] = self.getErrorString(output_params['err']) + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      elif err_api_match:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value)
         try:
           output_params['err_str'] = "API Error: " + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      else:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value
         output_params['err_str'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.name
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value)
         output_params['errcode'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN
      if (output_params['err'] and self.shouldraise):
         raise ScintilError(output_params['errcode'] or scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN, output_params)
      conf_match = re.match(r".*\*conf=\s*({\S+})", response.text, flags=re.DOTALL)
      if conf_match:
         output_params['conf'] = scintil_hal_servoloop_ring_t.fromstring(conf_match.groups()[0])
      else:
         output_params['conf'] = None
    except requests.exceptions.RequestException as e:
      ch_error = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL
      output_params['err'] = ch_error.value
      output_params['err_str'] = ch_error.name
      output_params['errcode'] = ch_error
      if (self.shouldraise):
         raise ScintilError(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL, output_params)
    return output_params

  def scintil_hal_config_set_servoloop_ring( self, conf: scintil_hal_servoloop_ring_t):
    # 1 input arguments
    # 0 output arguments
    output_params = {}
    request = f"http://{self.server}:{self.port}/hal{'delegate' if self.delegate else ''}/scintil_hal_config_set_servoloop_ring/{conf}"
    if self.token:
      request += f"?lock-token=" + self.token
    logging.debug("Request : " + request)
    try:
      response = requests.get(request)
      #output_params['response'] = response.text
      logging.debug("Response : " + response.text)
      err_match = re.match(r'.*\nerr=(0x\S+)\n.*', response.text, flags=re.DOTALL)
      err_api_match = re.match(r'(Invalid method.*)', response.text, flags=re.DOTALL)
      output_params['status_code'] = response.status_code
      if err_match:
         output_params['err'] = int(err_match.groups()[0],0)
         output_params['err_hex'] = err_match.groups()[0]
         try:
           output_params['err_str'] = self.getErrorString(output_params['err']) + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      elif err_api_match:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value)
         try:
           output_params['err_str'] = "API Error: " + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      else:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value
         output_params['err_str'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.name
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value)
         output_params['errcode'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN
      if (output_params['err'] and self.shouldraise):
         raise ScintilError(output_params['errcode'] or scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN, output_params)
    except requests.exceptions.RequestException as e:
      ch_error = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL
      output_params['err'] = ch_error.value
      output_params['err_str'] = ch_error.name
      output_params['errcode'] = ch_error
      if (self.shouldraise):
         raise ScintilError(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL, output_params)
    return output_params

  def scintil_hal_config_get_servoloop_common(self):
    # 0 input arguments
    # 1 output arguments
    output_params = {}
    request = f"http://{self.server}:{self.port}/hal{'delegate' if self.delegate else ''}/scintil_hal_config_get_servoloop_common"
    if self.token:
      request += f"?lock-token=" + self.token
    logging.debug("Request : " + request)
    try:
      response = requests.get(request)
      #output_params['response'] = response.text
      logging.debug("Response : " + response.text)
      err_match = re.match(r'.*\nerr=(0x\S+)\n.*', response.text, flags=re.DOTALL)
      err_api_match = re.match(r'(Invalid method.*)', response.text, flags=re.DOTALL)
      output_params['status_code'] = response.status_code
      if err_match:
         output_params['err'] = int(err_match.groups()[0],0)
         output_params['err_hex'] = err_match.groups()[0]
         try:
           output_params['err_str'] = self.getErrorString(output_params['err']) + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      elif err_api_match:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value)
         try:
           output_params['err_str'] = "API Error: " + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      else:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value
         output_params['err_str'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.name
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value)
         output_params['errcode'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN
      if (output_params['err'] and self.shouldraise):
         raise ScintilError(output_params['errcode'] or scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN, output_params)
      conf_match = re.match(r".*\*conf=\s*({\S+})", response.text, flags=re.DOTALL)
      if conf_match:
         output_params['conf'] = scintil_hal_servoloop_common_t.fromstring(conf_match.groups()[0])
      else:
         output_params['conf'] = None
    except requests.exceptions.RequestException as e:
      ch_error = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL
      output_params['err'] = ch_error.value
      output_params['err_str'] = ch_error.name
      output_params['errcode'] = ch_error
      if (self.shouldraise):
         raise ScintilError(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL, output_params)
    return output_params

  def scintil_hal_config_set_servoloop_common( self, conf: scintil_hal_servoloop_common_t):
    # 1 input arguments
    # 0 output arguments
    output_params = {}
    request = f"http://{self.server}:{self.port}/hal{'delegate' if self.delegate else ''}/scintil_hal_config_set_servoloop_common/{conf}"
    if self.token:
      request += f"?lock-token=" + self.token
    logging.debug("Request : " + request)
    try:
      response = requests.get(request)
      #output_params['response'] = response.text
      logging.debug("Response : " + response.text)
      err_match = re.match(r'.*\nerr=(0x\S+)\n.*', response.text, flags=re.DOTALL)
      err_api_match = re.match(r'(Invalid method.*)', response.text, flags=re.DOTALL)
      output_params['status_code'] = response.status_code
      if err_match:
         output_params['err'] = int(err_match.groups()[0],0)
         output_params['err_hex'] = err_match.groups()[0]
         try:
           output_params['err_str'] = self.getErrorString(output_params['err']) + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      elif err_api_match:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value)
         try:
           output_params['err_str'] = "API Error: " + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      else:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value
         output_params['err_str'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.name
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value)
         output_params['errcode'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN
      if (output_params['err'] and self.shouldraise):
         raise ScintilError(output_params['errcode'] or scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN, output_params)
    except requests.exceptions.RequestException as e:
      ch_error = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL
      output_params['err'] = ch_error.value
      output_params['err_str'] = ch_error.name
      output_params['errcode'] = ch_error
      if (self.shouldraise):
         raise ScintilError(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL, output_params)
    return output_params

  def scintil_hal_config_set_laser_limit( self, limit: float):
    # 1 input arguments
    # 0 output arguments
    output_params = {}
    request = f"http://{self.server}:{self.port}/hal{'delegate' if self.delegate else ''}/scintil_hal_config_set_laser_limit/{limit}"
    if self.token:
      request += f"?lock-token=" + self.token
    logging.debug("Request : " + request)
    try:
      response = requests.get(request)
      #output_params['response'] = response.text
      logging.debug("Response : " + response.text)
      err_match = re.match(r'.*\nerr=(0x\S+)\n.*', response.text, flags=re.DOTALL)
      err_api_match = re.match(r'(Invalid method.*)', response.text, flags=re.DOTALL)
      output_params['status_code'] = response.status_code
      if err_match:
         output_params['err'] = int(err_match.groups()[0],0)
         output_params['err_hex'] = err_match.groups()[0]
         try:
           output_params['err_str'] = self.getErrorString(output_params['err']) + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      elif err_api_match:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value)
         try:
           output_params['err_str'] = "API Error: " + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      else:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value
         output_params['err_str'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.name
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value)
         output_params['errcode'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN
      if (output_params['err'] and self.shouldraise):
         raise ScintilError(output_params['errcode'] or scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN, output_params)
    except requests.exceptions.RequestException as e:
      ch_error = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL
      output_params['err'] = ch_error.value
      output_params['err_str'] = ch_error.name
      output_params['errcode'] = ch_error
      if (self.shouldraise):
         raise ScintilError(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL, output_params)
    return output_params

  def scintil_hal_config_get_laser_limit(self):
    # 0 input arguments
    # 1 output arguments
    output_params = {}
    request = f"http://{self.server}:{self.port}/hal{'delegate' if self.delegate else ''}/scintil_hal_config_get_laser_limit"
    if self.token:
      request += f"?lock-token=" + self.token
    logging.debug("Request : " + request)
    try:
      response = requests.get(request)
      #output_params['response'] = response.text
      logging.debug("Response : " + response.text)
      err_match = re.match(r'.*\nerr=(0x\S+)\n.*', response.text, flags=re.DOTALL)
      err_api_match = re.match(r'(Invalid method.*)', response.text, flags=re.DOTALL)
      output_params['status_code'] = response.status_code
      if err_match:
         output_params['err'] = int(err_match.groups()[0],0)
         output_params['err_hex'] = err_match.groups()[0]
         try:
           output_params['err_str'] = self.getErrorString(output_params['err']) + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      elif err_api_match:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value)
         try:
           output_params['err_str'] = "API Error: " + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      else:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value
         output_params['err_str'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.name
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value)
         output_params['errcode'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN
      if (output_params['err'] and self.shouldraise):
         raise ScintilError(output_params['errcode'] or scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN, output_params)
      limit_match = re.match(r".*\*limit=(\S+)", response.text, flags=re.DOTALL)
      if limit_match:
         output_params['limit'] = float(limit_match.groups()[0])
      else:
         output_params['limit'] = None
    except requests.exceptions.RequestException as e:
      ch_error = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL
      output_params['err'] = ch_error.value
      output_params['err_str'] = ch_error.name
      output_params['errcode'] = ch_error
      if (self.shouldraise):
         raise ScintilError(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL, output_params)
    return output_params

  def scintil_hal_config_set_heater_limit( self, limit: float):
    # 1 input arguments
    # 0 output arguments
    output_params = {}
    request = f"http://{self.server}:{self.port}/hal{'delegate' if self.delegate else ''}/scintil_hal_config_set_heater_limit/{limit}"
    if self.token:
      request += f"?lock-token=" + self.token
    logging.debug("Request : " + request)
    try:
      response = requests.get(request)
      #output_params['response'] = response.text
      logging.debug("Response : " + response.text)
      err_match = re.match(r'.*\nerr=(0x\S+)\n.*', response.text, flags=re.DOTALL)
      err_api_match = re.match(r'(Invalid method.*)', response.text, flags=re.DOTALL)
      output_params['status_code'] = response.status_code
      if err_match:
         output_params['err'] = int(err_match.groups()[0],0)
         output_params['err_hex'] = err_match.groups()[0]
         try:
           output_params['err_str'] = self.getErrorString(output_params['err']) + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      elif err_api_match:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value)
         try:
           output_params['err_str'] = "API Error: " + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      else:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value
         output_params['err_str'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.name
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value)
         output_params['errcode'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN
      if (output_params['err'] and self.shouldraise):
         raise ScintilError(output_params['errcode'] or scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN, output_params)
    except requests.exceptions.RequestException as e:
      ch_error = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL
      output_params['err'] = ch_error.value
      output_params['err_str'] = ch_error.name
      output_params['errcode'] = ch_error
      if (self.shouldraise):
         raise ScintilError(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL, output_params)
    return output_params

  def scintil_hal_config_get_heater_limit(self):
    # 0 input arguments
    # 1 output arguments
    output_params = {}
    request = f"http://{self.server}:{self.port}/hal{'delegate' if self.delegate else ''}/scintil_hal_config_get_heater_limit"
    if self.token:
      request += f"?lock-token=" + self.token
    logging.debug("Request : " + request)
    try:
      response = requests.get(request)
      #output_params['response'] = response.text
      logging.debug("Response : " + response.text)
      err_match = re.match(r'.*\nerr=(0x\S+)\n.*', response.text, flags=re.DOTALL)
      err_api_match = re.match(r'(Invalid method.*)', response.text, flags=re.DOTALL)
      output_params['status_code'] = response.status_code
      if err_match:
         output_params['err'] = int(err_match.groups()[0],0)
         output_params['err_hex'] = err_match.groups()[0]
         try:
           output_params['err_str'] = self.getErrorString(output_params['err']) + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      elif err_api_match:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value)
         try:
           output_params['err_str'] = "API Error: " + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      else:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value
         output_params['err_str'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.name
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value)
         output_params['errcode'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN
      if (output_params['err'] and self.shouldraise):
         raise ScintilError(output_params['errcode'] or scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN, output_params)
      limit_match = re.match(r".*\*limit=(\S+)", response.text, flags=re.DOTALL)
      if limit_match:
         output_params['limit'] = float(limit_match.groups()[0])
      else:
         output_params['limit'] = None
    except requests.exceptions.RequestException as e:
      ch_error = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL
      output_params['err'] = ch_error.value
      output_params['err_str'] = ch_error.name
      output_params['errcode'] = ch_error
      if (self.shouldraise):
         raise ScintilError(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL, output_params)
    return output_params

  def scintil_hal_config_set_temp_threshold_limit( self, type: scintil_hal_threshold_type_t, channel: scintil_hal_threshold_channel_t, temperature: float):
    # 3 input arguments
    # 0 output arguments
    output_params = {}
    request = f"http://{self.server}:{self.port}/hal{'delegate' if self.delegate else ''}/scintil_hal_config_set_temp_threshold_limit/{type.value if hasattr(type,'value') else type}/{channel.value if hasattr(channel,'value') else channel}/{temperature}"
    if self.token:
      request += f"?lock-token=" + self.token
    logging.debug("Request : " + request)
    try:
      response = requests.get(request)
      #output_params['response'] = response.text
      logging.debug("Response : " + response.text)
      err_match = re.match(r'.*\nerr=(0x\S+)\n.*', response.text, flags=re.DOTALL)
      err_api_match = re.match(r'(Invalid method.*)', response.text, flags=re.DOTALL)
      output_params['status_code'] = response.status_code
      if err_match:
         output_params['err'] = int(err_match.groups()[0],0)
         output_params['err_hex'] = err_match.groups()[0]
         try:
           output_params['err_str'] = self.getErrorString(output_params['err']) + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      elif err_api_match:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value)
         try:
           output_params['err_str'] = "API Error: " + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      else:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value
         output_params['err_str'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.name
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value)
         output_params['errcode'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN
      if (output_params['err'] and self.shouldraise):
         raise ScintilError(output_params['errcode'] or scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN, output_params)
    except requests.exceptions.RequestException as e:
      ch_error = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL
      output_params['err'] = ch_error.value
      output_params['err_str'] = ch_error.name
      output_params['errcode'] = ch_error
      if (self.shouldraise):
         raise ScintilError(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL, output_params)
    return output_params

  def scintil_hal_config_get_temp_threshold_limit( self, type: scintil_hal_threshold_type_t, channel: scintil_hal_threshold_channel_t):
    # 2 input arguments
    # 1 output arguments
    output_params = {}
    request = f"http://{self.server}:{self.port}/hal{'delegate' if self.delegate else ''}/scintil_hal_config_get_temp_threshold_limit/{type.value if hasattr(type,'value') else type}/{channel.value if hasattr(channel,'value') else channel}"
    if self.token:
      request += f"?lock-token=" + self.token
    logging.debug("Request : " + request)
    try:
      response = requests.get(request)
      #output_params['response'] = response.text
      logging.debug("Response : " + response.text)
      err_match = re.match(r'.*\nerr=(0x\S+)\n.*', response.text, flags=re.DOTALL)
      err_api_match = re.match(r'(Invalid method.*)', response.text, flags=re.DOTALL)
      output_params['status_code'] = response.status_code
      if err_match:
         output_params['err'] = int(err_match.groups()[0],0)
         output_params['err_hex'] = err_match.groups()[0]
         try:
           output_params['err_str'] = self.getErrorString(output_params['err']) + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      elif err_api_match:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value)
         try:
           output_params['err_str'] = "API Error: " + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      else:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value
         output_params['err_str'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.name
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value)
         output_params['errcode'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN
      if (output_params['err'] and self.shouldraise):
         raise ScintilError(output_params['errcode'] or scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN, output_params)
      temperature_match = re.match(r".*\*temperature=(\S+)", response.text, flags=re.DOTALL)
      if temperature_match:
         output_params['temperature'] = float(temperature_match.groups()[0])
      else:
         output_params['temperature'] = None
    except requests.exceptions.RequestException as e:
      ch_error = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL
      output_params['err'] = ch_error.value
      output_params['err_str'] = ch_error.name
      output_params['errcode'] = ch_error
      if (self.shouldraise):
         raise ScintilError(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL, output_params)
    return output_params

  def scintil_hal_ring_mpd_get_voltage( self, module: scintil_hal_module_t, ring_type: scintil_hal_ring_type_t):
    # 2 input arguments
    # 1 output arguments
    output_params = {}
    request = f"http://{self.server}:{self.port}/hal{'delegate' if self.delegate else ''}/scintil_hal_ring_mpd_get_voltage/{module.value if hasattr(module,'value') else module}/{ring_type.value if hasattr(ring_type,'value') else ring_type}"
    if self.token:
      request += f"?lock-token=" + self.token
    logging.debug("Request : " + request)
    try:
      response = requests.get(request)
      #output_params['response'] = response.text
      logging.debug("Response : " + response.text)
      err_match = re.match(r'.*\nerr=(0x\S+)\n.*', response.text, flags=re.DOTALL)
      err_api_match = re.match(r'(Invalid method.*)', response.text, flags=re.DOTALL)
      output_params['status_code'] = response.status_code
      if err_match:
         output_params['err'] = int(err_match.groups()[0],0)
         output_params['err_hex'] = err_match.groups()[0]
         try:
           output_params['err_str'] = self.getErrorString(output_params['err']) + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      elif err_api_match:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value)
         try:
           output_params['err_str'] = "API Error: " + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      else:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value
         output_params['err_str'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.name
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value)
         output_params['errcode'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN
      if (output_params['err'] and self.shouldraise):
         raise ScintilError(output_params['errcode'] or scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN, output_params)
      val_match = re.match(r".*\*val=(\S+)", response.text, flags=re.DOTALL)
      if val_match:
         output_params['val'] = float(val_match.groups()[0])
      else:
         output_params['val'] = None
    except requests.exceptions.RequestException as e:
      ch_error = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL
      output_params['err'] = ch_error.value
      output_params['err_str'] = ch_error.name
      output_params['errcode'] = ch_error
      if (self.shouldraise):
         raise ScintilError(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL, output_params)
    return output_params

  def scintil_hal_ring_heater_set_voltage( self, module: scintil_hal_module_t, val: float):
    # 2 input arguments
    # 0 output arguments
    output_params = {}
    request = f"http://{self.server}:{self.port}/hal{'delegate' if self.delegate else ''}/scintil_hal_ring_heater_set_voltage/{module.value if hasattr(module,'value') else module}/{val}"
    if self.token:
      request += f"?lock-token=" + self.token
    logging.debug("Request : " + request)
    try:
      response = requests.get(request)
      #output_params['response'] = response.text
      logging.debug("Response : " + response.text)
      err_match = re.match(r'.*\nerr=(0x\S+)\n.*', response.text, flags=re.DOTALL)
      err_api_match = re.match(r'(Invalid method.*)', response.text, flags=re.DOTALL)
      output_params['status_code'] = response.status_code
      if err_match:
         output_params['err'] = int(err_match.groups()[0],0)
         output_params['err_hex'] = err_match.groups()[0]
         try:
           output_params['err_str'] = self.getErrorString(output_params['err']) + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      elif err_api_match:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value)
         try:
           output_params['err_str'] = "API Error: " + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      else:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value
         output_params['err_str'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.name
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value)
         output_params['errcode'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN
      if (output_params['err'] and self.shouldraise):
         raise ScintilError(output_params['errcode'] or scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN, output_params)
    except requests.exceptions.RequestException as e:
      ch_error = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL
      output_params['err'] = ch_error.value
      output_params['err_str'] = ch_error.name
      output_params['errcode'] = ch_error
      if (self.shouldraise):
         raise ScintilError(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL, output_params)
    return output_params

  def scintil_hal_ring_heater_get_voltage( self, module: scintil_hal_module_t):
    # 1 input arguments
    # 1 output arguments
    output_params = {}
    request = f"http://{self.server}:{self.port}/hal{'delegate' if self.delegate else ''}/scintil_hal_ring_heater_get_voltage/{module.value if hasattr(module,'value') else module}"
    if self.token:
      request += f"?lock-token=" + self.token
    logging.debug("Request : " + request)
    try:
      response = requests.get(request)
      #output_params['response'] = response.text
      logging.debug("Response : " + response.text)
      err_match = re.match(r'.*\nerr=(0x\S+)\n.*', response.text, flags=re.DOTALL)
      err_api_match = re.match(r'(Invalid method.*)', response.text, flags=re.DOTALL)
      output_params['status_code'] = response.status_code
      if err_match:
         output_params['err'] = int(err_match.groups()[0],0)
         output_params['err_hex'] = err_match.groups()[0]
         try:
           output_params['err_str'] = self.getErrorString(output_params['err']) + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      elif err_api_match:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value)
         try:
           output_params['err_str'] = "API Error: " + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      else:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value
         output_params['err_str'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.name
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value)
         output_params['errcode'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN
      if (output_params['err'] and self.shouldraise):
         raise ScintilError(output_params['errcode'] or scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN, output_params)
      val_match = re.match(r".*\*val=(\S+)", response.text, flags=re.DOTALL)
      if val_match:
         output_params['val'] = float(val_match.groups()[0])
      else:
         output_params['val'] = None
    except requests.exceptions.RequestException as e:
      ch_error = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL
      output_params['err'] = ch_error.value
      output_params['err_str'] = ch_error.name
      output_params['errcode'] = ch_error
      if (self.shouldraise):
         raise ScintilError(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL, output_params)
    return output_params

  def scintil_hal_toolbox_init_system(self):
    # 0 input arguments
    # 0 output arguments
    output_params = {}
    request = f"http://{self.server}:{self.port}/hal{'delegate' if self.delegate else ''}/scintil_hal_toolbox_init_system"
    if self.token:
      request += f"?lock-token=" + self.token
    logging.debug("Request : " + request)
    try:
      response = requests.get(request)
      #output_params['response'] = response.text
      logging.debug("Response : " + response.text)
      err_match = re.match(r'.*\nerr=(0x\S+)\n.*', response.text, flags=re.DOTALL)
      err_api_match = re.match(r'(Invalid method.*)', response.text, flags=re.DOTALL)
      output_params['status_code'] = response.status_code
      if err_match:
         output_params['err'] = int(err_match.groups()[0],0)
         output_params['err_hex'] = err_match.groups()[0]
         try:
           output_params['err_str'] = self.getErrorString(output_params['err']) + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      elif err_api_match:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value)
         try:
           output_params['err_str'] = "API Error: " + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      else:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value
         output_params['err_str'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.name
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value)
         output_params['errcode'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN
      if (output_params['err'] and self.shouldraise):
         raise ScintilError(output_params['errcode'] or scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN, output_params)
    except requests.exceptions.RequestException as e:
      ch_error = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL
      output_params['err'] = ch_error.value
      output_params['err_str'] = ch_error.name
      output_params['errcode'] = ch_error
      if (self.shouldraise):
         raise ScintilError(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL, output_params)
    return output_params

  def scintil_hal_controller_calibrate_mux_S11_AE(self):
    # 0 input arguments
    # 0 output arguments
    output_params = {}
    request = f"http://{self.server}:{self.port}/hal{'delegate' if self.delegate else ''}/scintil_hal_controller_calibrate_mux_S11_AE"
    if self.token:
      request += f"?lock-token=" + self.token
    logging.debug("Request : " + request)
    try:
      response = requests.get(request)
      #output_params['response'] = response.text
      logging.debug("Response : " + response.text)
      err_match = re.match(r'.*\nerr=(0x\S+)\n.*', response.text, flags=re.DOTALL)
      err_api_match = re.match(r'(Invalid method.*)', response.text, flags=re.DOTALL)
      output_params['status_code'] = response.status_code
      if err_match:
         output_params['err'] = int(err_match.groups()[0],0)
         output_params['err_hex'] = err_match.groups()[0]
         try:
           output_params['err_str'] = self.getErrorString(output_params['err']) + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      elif err_api_match:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_API.value)
         try:
           output_params['err_str'] = "API Error: " + " (" + response.text + ")"
           output_params['errcode'] = scintil_hal_error_bit_t(output_params['err'])
         except:
           pass
      else:
         output_params['err'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value
         output_params['err_str'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.name
         output_params['err_hex'] = hex(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN.value)
         output_params['errcode'] = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN
      if (output_params['err'] and self.shouldraise):
         raise ScintilError(output_params['errcode'] or scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_UNKNOWN, output_params)
    except requests.exceptions.RequestException as e:
      ch_error = scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL
      output_params['err'] = ch_error.value
      output_params['err_str'] = ch_error.name
      output_params['errcode'] = ch_error
      if (self.shouldraise):
         raise ScintilError(scintil_hal_error_bit_t.SCINTIL_HAL_ERROR_CHANNEL, output_params)
    return output_params

## @} End of group pythonapi
