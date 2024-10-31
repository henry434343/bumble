# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: netsim/model.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from bumble.transport.grpc_protobuf.netsim import common_pb2 as netsim_dot_common__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from bumble.transport.grpc_protobuf.rootcanal import configuration_pb2 as rootcanal_dot_configuration__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x12netsim/model.proto\x12\x0cnetsim.model\x1a\x13netsim/common.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1drootcanal/configuration.proto\"+\n\x08Position\x12\t\n\x01x\x18\x01 \x01(\x02\x12\t\n\x01y\x18\x02 \x01(\x02\x12\t\n\x01z\x18\x03 \x01(\x02\"7\n\x0bOrientation\x12\x0b\n\x03yaw\x18\x01 \x01(\x02\x12\r\n\x05pitch\x18\x02 \x01(\x02\x12\x0c\n\x04roll\x18\x03 \x01(\x02\"\x84\x0c\n\x04\x43hip\x12%\n\x04kind\x18\x01 \x01(\x0e\x32\x17.netsim.common.ChipKind\x12\n\n\x02id\x18\x02 \x01(\r\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x14\n\x0cmanufacturer\x18\x04 \x01(\t\x12\x14\n\x0cproduct_name\x18\x05 \x01(\t\x12*\n\x02\x62t\x18\x06 \x01(\x0b\x32\x1c.netsim.model.Chip.BluetoothH\x00\x12\x32\n\nble_beacon\x18\t \x01(\x0b\x32\x1c.netsim.model.Chip.BleBeaconH\x00\x12\'\n\x03uwb\x18\x07 \x01(\x0b\x32\x18.netsim.model.Chip.RadioH\x00\x12(\n\x04wifi\x18\x08 \x01(\x0b\x32\x18.netsim.model.Chip.RadioH\x00\x12+\n\x06offset\x18\x0f \x01(\x0b\x32\x16.netsim.model.PositionH\x01\x88\x01\x01\x1aX\n\x05Radio\x12\x12\n\x05state\x18\x01 \x01(\x08H\x00\x88\x01\x01\x12\r\n\x05range\x18\x02 \x01(\x02\x12\x10\n\x08tx_count\x18\x03 \x01(\x05\x12\x10\n\x08rx_count\x18\x04 \x01(\x05\x42\x08\n\x06_state\x1a\xb1\x01\n\tBluetooth\x12,\n\nlow_energy\x18\x01 \x01(\x0b\x32\x18.netsim.model.Chip.Radio\x12)\n\x07\x63lassic\x18\x02 \x01(\x0b\x32\x18.netsim.model.Chip.Radio\x12\x0f\n\x07\x61\x64\x64ress\x18\x03 \x01(\t\x12:\n\rbt_properties\x18\x04 \x01(\x0b\x32#.rootcanal.configuration.Controller\x1a\x8d\x07\n\tBleBeacon\x12(\n\x02\x62t\x18\x01 \x01(\x0b\x32\x1c.netsim.model.Chip.Bluetooth\x12\x0f\n\x07\x61\x64\x64ress\x18\x02 \x01(\t\x12@\n\x08settings\x18\x03 \x01(\x0b\x32..netsim.model.Chip.BleBeacon.AdvertiseSettings\x12<\n\x08\x61\x64v_data\x18\x04 \x01(\x0b\x32*.netsim.model.Chip.BleBeacon.AdvertiseData\x12\x41\n\rscan_response\x18\x05 \x01(\x0b\x32*.netsim.model.Chip.BleBeacon.AdvertiseData\x1a\xaa\x03\n\x11\x41\x64vertiseSettings\x12V\n\x0e\x61\x64vertise_mode\x18\x01 \x01(\x0e\x32<.netsim.model.Chip.BleBeacon.AdvertiseSettings.AdvertiseModeH\x00\x12\x16\n\x0cmilliseconds\x18\x02 \x01(\x04H\x00\x12Y\n\x0etx_power_level\x18\x03 \x01(\x0e\x32?.netsim.model.Chip.BleBeacon.AdvertiseSettings.AdvertiseTxPowerH\x01\x12\r\n\x03\x64\x62m\x18\x04 \x01(\x05H\x01\x12\x11\n\tscannable\x18\x05 \x01(\x08\x12\x0f\n\x07timeout\x18\x06 \x01(\x04\"=\n\rAdvertiseMode\x12\r\n\tLOW_POWER\x10\x00\x12\x0c\n\x08\x42\x41LANCED\x10\x01\x12\x0f\n\x0bLOW_LATENCY\x10\x02\"@\n\x10\x41\x64vertiseTxPower\x12\r\n\tULTRA_LOW\x10\x00\x12\x07\n\x03LOW\x10\x01\x12\n\n\x06MEDIUM\x10\x02\x12\x08\n\x04HIGH\x10\x03\x42\n\n\x08intervalB\n\n\x08tx_power\x1a\xd4\x01\n\rAdvertiseData\x12\x1b\n\x13include_device_name\x18\x01 \x01(\x08\x12\x1e\n\x16include_tx_power_level\x18\x02 \x01(\x08\x12\x19\n\x11manufacturer_data\x18\x03 \x01(\x0c\x12\x44\n\x08services\x18\x04 \x03(\x0b\x32\x32.netsim.model.Chip.BleBeacon.AdvertiseData.Service\x1a%\n\x07Service\x12\x0c\n\x04uuid\x18\x01 \x01(\t\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\x0c\x42\x06\n\x04\x63hipB\t\n\x07_offset\"\xea\x03\n\nChipCreate\x12%\n\x04kind\x18\x01 \x01(\x0e\x32\x17.netsim.common.ChipKind\x12\x0f\n\x07\x61\x64\x64ress\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x14\n\x0cmanufacturer\x18\x04 \x01(\t\x12\x14\n\x0cproduct_name\x18\x05 \x01(\t\x12>\n\nble_beacon\x18\x06 \x01(\x0b\x32(.netsim.model.ChipCreate.BleBeaconCreateH\x00\x12:\n\rbt_properties\x18\x07 \x01(\x0b\x32#.rootcanal.configuration.Controller\x1a\xe5\x01\n\x0f\x42leBeaconCreate\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\t\x12@\n\x08settings\x18\x03 \x01(\x0b\x32..netsim.model.Chip.BleBeacon.AdvertiseSettings\x12<\n\x08\x61\x64v_data\x18\x04 \x01(\x0b\x32*.netsim.model.Chip.BleBeacon.AdvertiseData\x12\x41\n\rscan_response\x18\x05 \x01(\x0b\x32*.netsim.model.Chip.BleBeacon.AdvertiseDataB\x06\n\x04\x63hip\"\xc1\x01\n\x06\x44\x65vice\x12\n\n\x02id\x18\x01 \x01(\r\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x14\n\x07visible\x18\x03 \x01(\x08H\x00\x88\x01\x01\x12(\n\x08position\x18\x04 \x01(\x0b\x32\x16.netsim.model.Position\x12.\n\x0borientation\x18\x05 \x01(\x0b\x32\x19.netsim.model.Orientation\x12!\n\x05\x63hips\x18\x06 \x03(\x0b\x32\x12.netsim.model.ChipB\n\n\x08_visible\"\x9f\x01\n\x0c\x44\x65viceCreate\x12\x0c\n\x04name\x18\x01 \x01(\t\x12(\n\x08position\x18\x02 \x01(\x0b\x32\x16.netsim.model.Position\x12.\n\x0borientation\x18\x03 \x01(\x0b\x32\x19.netsim.model.Orientation\x12\'\n\x05\x63hips\x18\x04 \x03(\x0b\x32\x18.netsim.model.ChipCreate\".\n\x05Scene\x12%\n\x07\x64\x65vices\x18\x01 \x03(\x0b\x32\x14.netsim.model.Device\"\xd1\x01\n\x07\x43\x61pture\x12\n\n\x02id\x18\x01 \x01(\r\x12*\n\tchip_kind\x18\x02 \x01(\x0e\x32\x17.netsim.common.ChipKind\x12\x13\n\x0b\x64\x65vice_name\x18\x03 \x01(\t\x12\x12\n\x05state\x18\x04 \x01(\x08H\x00\x88\x01\x01\x12\x0c\n\x04size\x18\x05 \x01(\x05\x12\x0f\n\x07records\x18\x06 \x01(\x05\x12-\n\ttimestamp\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\r\n\x05valid\x18\x08 \x01(\x08\x42\x08\n\x06_state*e\n\x07PhyKind\x12\x08\n\x04NONE\x10\x00\x12\x15\n\x11\x42LUETOOTH_CLASSIC\x10\x01\x12\x18\n\x14\x42LUETOOTH_LOW_ENERGY\x10\x02\x12\x08\n\x04WIFI\x10\x03\x12\x07\n\x03UWB\x10\x04\x12\x0c\n\x08WIFI_RTT\x10\x05\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'netsim.model_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_PHYKIND']._serialized_start=2877
  _globals['_PHYKIND']._serialized_end=2978
  _globals['_POSITION']._serialized_start=121
  _globals['_POSITION']._serialized_end=164
  _globals['_ORIENTATION']._serialized_start=166
  _globals['_ORIENTATION']._serialized_end=221
  _globals['_CHIP']._serialized_start=224
  _globals['_CHIP']._serialized_end=1764
  _globals['_CHIP_RADIO']._serialized_start=565
  _globals['_CHIP_RADIO']._serialized_end=653
  _globals['_CHIP_BLUETOOTH']._serialized_start=656
  _globals['_CHIP_BLUETOOTH']._serialized_end=833
  _globals['_CHIP_BLEBEACON']._serialized_start=836
  _globals['_CHIP_BLEBEACON']._serialized_end=1745
  _globals['_CHIP_BLEBEACON_ADVERTISESETTINGS']._serialized_start=1104
  _globals['_CHIP_BLEBEACON_ADVERTISESETTINGS']._serialized_end=1530
  _globals['_CHIP_BLEBEACON_ADVERTISESETTINGS_ADVERTISEMODE']._serialized_start=1379
  _globals['_CHIP_BLEBEACON_ADVERTISESETTINGS_ADVERTISEMODE']._serialized_end=1440
  _globals['_CHIP_BLEBEACON_ADVERTISESETTINGS_ADVERTISETXPOWER']._serialized_start=1442
  _globals['_CHIP_BLEBEACON_ADVERTISESETTINGS_ADVERTISETXPOWER']._serialized_end=1506
  _globals['_CHIP_BLEBEACON_ADVERTISEDATA']._serialized_start=1533
  _globals['_CHIP_BLEBEACON_ADVERTISEDATA']._serialized_end=1745
  _globals['_CHIP_BLEBEACON_ADVERTISEDATA_SERVICE']._serialized_start=1708
  _globals['_CHIP_BLEBEACON_ADVERTISEDATA_SERVICE']._serialized_end=1745
  _globals['_CHIPCREATE']._serialized_start=1767
  _globals['_CHIPCREATE']._serialized_end=2257
  _globals['_CHIPCREATE_BLEBEACONCREATE']._serialized_start=2020
  _globals['_CHIPCREATE_BLEBEACONCREATE']._serialized_end=2249
  _globals['_DEVICE']._serialized_start=2260
  _globals['_DEVICE']._serialized_end=2453
  _globals['_DEVICECREATE']._serialized_start=2456
  _globals['_DEVICECREATE']._serialized_end=2615
  _globals['_SCENE']._serialized_start=2617
  _globals['_SCENE']._serialized_end=2663
  _globals['_CAPTURE']._serialized_start=2666
  _globals['_CAPTURE']._serialized_end=2875
# @@protoc_insertion_point(module_scope)