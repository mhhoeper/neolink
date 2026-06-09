# Analysis Video Download

## Argus 2

```
RUST_LOG=replay=debug ./neolink replay --config neolink.toml Hofkamera download --name 0120260608060802 --output 0120260608060802.mp4
Parsed BcMedia replay and muxed to 0120260608060802.mp4
❯ RUST_LOG=debug ./neolink replay --config neolink.toml Hofkamera download --name 0120260608060802 --output 0120260608060802.mp4
[2026-06-09T06:23:49Z INFO  neolink] Neolink 0.7.0-beta (unknown commit) debug
[2026-06-09T06:23:49Z INFO  neolink::utils] Hofkamera: Connecting to camera at UID: xxxxxxxxxxxxxxxx
[2026-06-09T06:23:49Z INFO  neolink::replay] Replay download: name=0120260608060802 stream=subStream (stops on response 300 or --duration)
[2026-06-09T06:23:49Z INFO  neolink::replay] Replay play: name=0120260608060802 stream=subStream speed=1
[2026-06-09T06:23:49Z INFO  neolink_core::bc_protocol] Hofkamera: Trying local discovery
[2026-06-09T06:23:49Z DEBUG neolink_core::bc_protocol::connection::discovery] Broadcasting to: [(255.255.255.255, 2015), (255.255.255.255, 2018), (192.168.2.255, 2015), (192.168.2.255, 2018), (192.168.2.255, 2015), (192.168.2.255, 2018)]
[2026-06-09T06:23:49Z DEBUG neolink_core::bc_protocol::connection::discovery] Also sending to []
[2026-06-09T06:23:49Z DEBUG neolink_core::bc_protocol::connection::discovery] Trying a direct connect to: 255.255.255.255:2015 with tid: 5
[2026-06-09T06:23:49Z DEBUG neolink_core::bc_protocol::connection::discovery] Trying a direct connect to: 255.255.255.255:2018 with tid: 163
[2026-06-09T06:23:49Z DEBUG neolink_core::bc_protocol::connection::discovery] Trying a direct connect to: 192.168.2.255:2015 with tid: 90
[2026-06-09T06:23:49Z DEBUG neolink_core::bc_protocol::connection::discovery] Trying a direct connect to: 192.168.2.255:2018 with tid: 5
[2026-06-09T06:23:49Z DEBUG neolink_core::bc_protocol::connection::discovery] Trying a direct connect to: 192.168.2.255:2015 with tid: 64
[2026-06-09T06:23:49Z DEBUG neolink_core::bc_protocol::connection::discovery] Trying a direct connect to: 192.168.2.255:2018 with tid: 248
[2026-06-09T06:23:49Z DEBUG neolink_core::bc_protocol::connection::discovery] Registering 192.168.2.90:53832 to reolink
[2026-06-09T06:23:50Z DEBUG neolink_core::bc_protocol::connection::discovery] Direct connect success at 255.255.255.255:2015 client: 2057778464, device: 224
[2026-06-09T06:23:50Z DEBUG neolink_core::bc_protocol::connection::discovery] Returning direct connect: ConnectResult { addr: 192.168.2.82:57610, client_id: 2057778464, camera_id: 224, sid: 0 }
[2026-06-09T06:23:50Z INFO  neolink_core::bc_protocol] Hofkamera: Local discovery success xxxxxxxxxxxxxxxx at 192.168.2.82:57610
[2026-06-09T06:23:50Z INFO  neolink::utils] Hofkamera: Logging in
[2026-06-09T06:23:51Z DEBUG neolink_core::bc_protocol::login] Populating abilities
[2026-06-09T06:23:51Z DEBUG neolink_core::bc_protocol::abilityinfo] Abilities: <AbilityInfo><userName>admin</userName><system><subModule><abilityValue>general_rw, norm_rw, version_ro, uid_ro, autoReboot_rw, restore_rw, reboot_rw, shutdown_rw, dst_rw, log_ro, performance_ro, upgrade_rw, export_rw, import_rw, bootPwd_rw</abilityValue></subModule></system><network><subModule><abilityValue>port_rw, dns_rw, email_rw, ipFilter_rw, localLink_rw, pppoe_rw, upnp_rw, wifi_rw, ntp_rw, netStatus_rw</abilityValue></subModule></network><alarm><subModule><abilityValue>rfAlarm_rw</abilityValue></subModule><subModule><channelId>0</channelId><abilityValue>motion_rw</abilityValue></subModule></alarm><image><subModule><channelId>0</channelId><abilityValue>ispBasic_rw, ispAdvance_rw, ledState_rw</abilityValue></subModule></image><video><subModule><channelId>0</channelId><abilityValue>osdName_rw, osdTime_rw, shelter_rw</abilityValue></subModule></video><security><subModule><abilityValue>user_rw, userOnline_rw, bootPwd_rw</abilityValue></subModule></security><replay><subModule><channelId>0</channelId><abilityValue>replay_rw, seek_rw</abilityValue></subModule></replay><PTZ><subModule><abilityValue>control_rw, preset_rw, cruise_rw, track_rw, decoder_rw, ptzInfo_ro</abilityValue></subModule></PTZ><streaming><subModule><channelId>0</channelId><abilityValue>preview_rw, compress_rw, snap_rw, rtsp_rw, streamTable_ro</abilityValue></subModule></streaming></AbilityInfo>
[2026-06-09T06:23:51Z INFO  neolink::utils] Hofkamera: Connected and logged in
[2026-06-09T06:23:53Z INFO  neolink::common::camthread] Hofkamera: Camera time is already set: 2026-06-09 8:23:53.0 -01:00:00
[2026-06-09T06:23:55Z INFO  neolink::common::neocam] Hofkamera: Model Argus 2
[2026-06-09T06:23:55Z INFO  neolink::common::neocam] Hofkamera: Firmware Version 1115_458_346_27
[2026-06-09T06:23:56Z INFO  neolink::replay] Replay: file duration 21 s (from file list), will stop when complete
[2026-06-09T06:23:56Z INFO  neolink::replay] Replay: expected file size 927286 bytes (from file list), will stop when complete
[2026-06-09T06:23:56Z INFO  neolink::replay] Replay: file recordType = md
[2026-06-09T06:23:56Z INFO  neolink_core::bc_protocol::replay] Replay: seek (MSG 123) done
[2026-06-09T06:23:56Z INFO  neolink_core::bc_protocol::replay] Replay: start_time 2026-06-08 06:08:02
[2026-06-09T06:23:56Z INFO  neolink_core::bc_protocol::replay] Replay: sending MSG 5 start_replay name=0120260608060802 channel=0 streamType=subStream
[2026-06-09T06:23:56Z INFO  neolink_core::bc_protocol::replay] Replay: MSG 5 sent, waiting for first response...
[2026-06-09T06:23:58Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=200 body=binary(32 bytes)
[2026-06-09T06:23:58Z INFO  neolink_core::bc_protocol::replay] Replay: camera accepted (200), streaming...
[2026-06-09T06:23:58Z INFO  neolink_core::bc_protocol::replay] Replay: skipping 32 byte replay header (first packet)
[2026-06-09T06:23:58Z DEBUG neolink_core::bc_protocol::replay] Replay: header hex: [31, 30, 30, 32, 20, 00, 00, 00, 80, 02, 00, 00, 60, 01, 00, 00, 01, 96, 7e, 06, 08, 04, 08, 02, 7e, 06, 08, 04, 08, 17, 00, 00]
[2026-06-09T06:23:58Z INFO  neolink_core::bc_protocol::replay] Replay: 1 packets, 0 KB received
[2026-06-09T06:23:58Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(2294 bytes)
[2026-06-09T06:23:58Z DEBUG neolink_core::bc_protocol::replay] Replay: accepting streaming response_code 45436 (added to accepted set)
[2026-06-09T06:23:58Z INFO  neolink_core::bc_protocol::replay] Replay: packet 2 not ftyp (decrypted: [6e, 00, 00, 00, 23, 12, 44, 26]), treating as container/raw
[2026-06-09T06:23:58Z INFO  neolink_core::bc_protocol::replay] Replay: 2 packets, 2 KB received
[2026-06-09T06:23:58Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(374 bytes)
[2026-06-09T06:23:58Z INFO  neolink_core::bc_protocol::replay] Replay: 3 packets, 2 KB received
[2026-06-09T06:23:58Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(11606 bytes)
[2026-06-09T06:23:58Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(374 bytes)
[2026-06-09T06:23:58Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(374 bytes)
[2026-06-09T06:23:58Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(16950 bytes)
[2026-06-09T06:23:58Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(374 bytes)
[2026-06-09T06:23:58Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(374 bytes)
[2026-06-09T06:23:58Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(374 bytes)
[2026-06-09T06:23:58Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(14046 bytes)
[2026-06-09T06:23:58Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(374 bytes)
[2026-06-09T06:23:58Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(374 bytes)
[2026-06-09T06:23:58Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(374 bytes)
[2026-06-09T06:23:58Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(9990 bytes)
[2026-06-09T06:23:58Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(390 bytes)
[2026-06-09T06:23:58Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(374 bytes)
[2026-06-09T06:23:58Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(366 bytes)
[2026-06-09T06:23:58Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(8198 bytes)
[2026-06-09T06:23:58Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(374 bytes)
[2026-06-09T06:23:58Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(478 bytes)
[2026-06-09T06:23:58Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(358 bytes)
[2026-06-09T06:23:58Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(5214 bytes)
[2026-06-09T06:23:58Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(366 bytes)
[2026-06-09T06:23:58Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(350 bytes)
[2026-06-09T06:23:58Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(350 bytes)
[2026-06-09T06:23:58Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(366 bytes)
[2026-06-09T06:23:58Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(2142 bytes)
[2026-06-09T06:23:58Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(374 bytes)
[2026-06-09T06:23:58Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(374 bytes)
[2026-06-09T06:23:58Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(374 bytes)
[2026-06-09T06:23:59Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(3366 bytes)
[2026-06-09T06:23:59Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(374 bytes)
[2026-06-09T06:23:59Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(374 bytes)
[2026-06-09T06:23:59Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(374 bytes)
[2026-06-09T06:23:59Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(1950 bytes)
[2026-06-09T06:23:59Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(374 bytes)
[2026-06-09T06:23:59Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(374 bytes)
[2026-06-09T06:23:59Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(374 bytes)
[2026-06-09T06:23:59Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(3142 bytes)
[2026-06-09T06:23:59Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(374 bytes)
[2026-06-09T06:23:59Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(374 bytes)
[2026-06-09T06:23:59Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(374 bytes)
[2026-06-09T06:23:59Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(4142 bytes)
[2026-06-09T06:23:59Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(374 bytes)
[2026-06-09T06:23:59Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(374 bytes)
[2026-06-09T06:23:59Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(374 bytes)
[2026-06-09T06:23:59Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(1830 bytes)
[2026-06-09T06:23:59Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(374 bytes)
[2026-06-09T06:23:59Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(374 bytes)
[2026-06-09T06:23:59Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(374 bytes)
[2026-06-09T06:23:59Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(2998 bytes)
[2026-06-09T06:23:59Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(398 bytes)
[2026-06-09T06:23:59Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(358 bytes)
[2026-06-09T06:23:59Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(374 bytes)
[2026-06-09T06:23:59Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(3646 bytes)
[2026-06-09T06:23:59Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(374 bytes)
[2026-06-09T06:23:59Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(374 bytes)
[2026-06-09T06:23:59Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(374 bytes)
[2026-06-09T06:23:59Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(374 bytes)
[2026-06-09T06:23:59Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(5254 bytes)
[2026-06-09T06:23:59Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(374 bytes)
[2026-06-09T06:23:59Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(422 bytes)
[2026-06-09T06:23:59Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(342 bytes)
[2026-06-09T06:23:59Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(2846 bytes)
[2026-06-09T06:23:59Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(366 bytes)
[2026-06-09T06:23:59Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(374 bytes)
[2026-06-09T06:23:59Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(374 bytes)
[2026-06-09T06:23:59Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(3110 bytes)
[2026-06-09T06:23:59Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(374 bytes)
[2026-06-09T06:23:59Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(374 bytes)
[2026-06-09T06:23:59Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(374 bytes)
[2026-06-09T06:23:59Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(4238 bytes)
[2026-06-09T06:23:59Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(374 bytes)
[2026-06-09T06:23:59Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(382 bytes)
[2026-06-09T06:23:59Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(374 bytes)
[2026-06-09T06:23:59Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(1670 bytes)
[2026-06-09T06:23:59Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(382 bytes)
[2026-06-09T06:23:59Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(374 bytes)
[2026-06-09T06:23:59Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(374 bytes)
[2026-06-09T06:24:00Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(39598 bytes)
[2026-06-09T06:24:00Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(878 bytes)
[2026-06-09T06:24:00Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(374 bytes)
[2026-06-09T06:24:00Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(374 bytes)
[2026-06-09T06:24:00Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(374 bytes)
[2026-06-09T06:24:00Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(1878 bytes)
[2026-06-09T06:24:00Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(454 bytes)
[2026-06-09T06:24:00Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(454 bytes)
[2026-06-09T06:24:00Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(350 bytes)
[2026-06-09T06:24:00Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(2358 bytes)
[2026-06-09T06:24:00Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(334 bytes)
[2026-06-09T06:24:00Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(374 bytes)
[2026-06-09T06:24:00Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(350 bytes)
[2026-06-09T06:24:00Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(342 bytes)
[2026-06-09T06:24:00Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(4142 bytes)
[2026-06-09T06:24:00Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(366 bytes)
[2026-06-09T06:24:00Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(374 bytes)
[2026-06-09T06:24:00Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(374 bytes)
[2026-06-09T06:24:00Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(1806 bytes)
[2026-06-09T06:24:00Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(406 bytes)
[2026-06-09T06:24:00Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(406 bytes)
[2026-06-09T06:24:00Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(358 bytes)
[2026-06-09T06:24:00Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(3462 bytes)
[2026-06-09T06:24:00Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(350 bytes)
[2026-06-09T06:24:00Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(374 bytes)
[2026-06-09T06:24:00Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(374 bytes)
[2026-06-09T06:24:00Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(5462 bytes)
[2026-06-09T06:24:00Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(374 bytes)
[2026-06-09T06:24:00Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(398 bytes)
[2026-06-09T06:24:00Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(366 bytes)
[2026-06-09T06:24:00Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(3014 bytes)
[2026-06-09T06:24:00Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(382 bytes)
[2026-06-09T06:24:00Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(422 bytes)
[2026-06-09T06:24:00Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(414 bytes)
[2026-06-09T06:24:00Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(5390 bytes)
[2026-06-09T06:24:00Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(454 bytes)
[2026-06-09T06:24:00Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(398 bytes)
[2026-06-09T06:24:00Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(318 bytes)
[2026-06-09T06:24:00Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(5446 bytes)
[2026-06-09T06:24:00Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(366 bytes)
[2026-06-09T06:24:00Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(286 bytes)
[2026-06-09T06:24:00Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(350 bytes)
[2026-06-09T06:24:00Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(3502 bytes)
[2026-06-09T06:24:00Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(374 bytes)
[2026-06-09T06:24:00Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(382 bytes)
[2026-06-09T06:24:00Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(414 bytes)
[2026-06-09T06:24:00Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(366 bytes)
[2026-06-09T06:24:00Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(4790 bytes)
[2026-06-09T06:24:00Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(350 bytes)
[2026-06-09T06:24:00Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(374 bytes)
[2026-06-09T06:24:00Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(374 bytes)
[2026-06-09T06:24:00Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(3430 bytes)
[2026-06-09T06:24:00Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(374 bytes)
[2026-06-09T06:24:00Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(374 bytes)
[2026-06-09T06:24:00Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(374 bytes)
[2026-06-09T06:24:00Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(5174 bytes)
[2026-06-09T06:24:00Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(374 bytes)
[2026-06-09T06:24:00Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(438 bytes)
[2026-06-09T06:24:00Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(390 bytes)
[2026-06-09T06:24:00Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(3846 bytes)
[2026-06-09T06:24:00Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(374 bytes)
[2026-06-09T06:24:00Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(358 bytes)
[2026-06-09T06:24:00Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(374 bytes)
[2026-06-09T06:24:00Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(5182 bytes)
[2026-06-09T06:24:00Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(358 bytes)
[2026-06-09T06:24:00Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(390 bytes)
[2026-06-09T06:24:00Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(366 bytes)
[2026-06-09T06:24:00Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(3558 bytes)
[2026-06-09T06:24:00Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(414 bytes)
[2026-06-09T06:24:00Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(390 bytes)
[2026-06-09T06:24:00Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(382 bytes)
[2026-06-09T06:24:00Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(4670 bytes)
[2026-06-09T06:24:00Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(342 bytes)
[2026-06-09T06:24:00Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(366 bytes)
[2026-06-09T06:24:00Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(358 bytes)
[2026-06-09T06:24:00Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(3526 bytes)
[2026-06-09T06:24:00Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(462 bytes)
[2026-06-09T06:24:00Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(382 bytes)
[2026-06-09T06:24:00Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(398 bytes)
[2026-06-09T06:24:00Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(390 bytes)
[2026-06-09T06:24:00Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(4886 bytes)
[2026-06-09T06:24:00Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(342 bytes)
[2026-06-09T06:24:00Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(350 bytes)
[2026-06-09T06:24:00Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(342 bytes)
[2026-06-09T06:24:00Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(39598 bytes)
[2026-06-09T06:24:00Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(10838 bytes)
[2026-06-09T06:24:00Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(350 bytes)
[2026-06-09T06:24:00Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(382 bytes)
[2026-06-09T06:24:00Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(398 bytes)
[2026-06-09T06:24:00Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(2870 bytes)
[2026-06-09T06:24:00Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(398 bytes)
[2026-06-09T06:24:00Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(350 bytes)
[2026-06-09T06:24:00Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(366 bytes)
[2026-06-09T06:24:00Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(3838 bytes)
[2026-06-09T06:24:00Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(390 bytes)
[2026-06-09T06:24:00Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(366 bytes)
[2026-06-09T06:24:00Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(358 bytes)
[2026-06-09T06:24:00Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(5430 bytes)
[2026-06-09T06:24:00Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(374 bytes)
[2026-06-09T06:24:00Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(374 bytes)
[2026-06-09T06:24:00Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(374 bytes)
[2026-06-09T06:24:00Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(2614 bytes)
[2026-06-09T06:24:00Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(462 bytes)
[2026-06-09T06:24:00Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(374 bytes)
[2026-06-09T06:24:00Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(334 bytes)
[2026-06-09T06:24:00Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(4094 bytes)
[2026-06-09T06:24:00Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(342 bytes)
[2026-06-09T06:24:00Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(374 bytes)
[2026-06-09T06:24:00Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(374 bytes)
[2026-06-09T06:24:00Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(5654 bytes)
[2026-06-09T06:24:00Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(422 bytes)
[2026-06-09T06:24:00Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(422 bytes)
[2026-06-09T06:24:00Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(382 bytes)
[2026-06-09T06:24:00Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(390 bytes)
[2026-06-09T06:24:00Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(3222 bytes)
[2026-06-09T06:24:00Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(342 bytes)
[2026-06-09T06:24:00Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(350 bytes)
[2026-06-09T06:24:00Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(350 bytes)
[2026-06-09T06:24:01Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(5086 bytes)
[2026-06-09T06:24:01Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(358 bytes)
[2026-06-09T06:24:01Z INFO  neolink_core::bc_protocol::replay] Replay: 200 packets, 355 KB received
[2026-06-09T06:24:01Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(374 bytes)
[2026-06-09T06:24:01Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(374 bytes)
[2026-06-09T06:24:01Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(3142 bytes)
[2026-06-09T06:24:01Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(374 bytes)
[2026-06-09T06:24:01Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(374 bytes)
[2026-06-09T06:24:01Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(374 bytes)
[2026-06-09T06:24:01Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(3430 bytes)
[2026-06-09T06:24:01Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(398 bytes)
[2026-06-09T06:24:01Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(406 bytes)
[2026-06-09T06:24:01Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(358 bytes)
[2026-06-09T06:24:01Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(5902 bytes)
[2026-06-09T06:24:01Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(358 bytes)
[2026-06-09T06:24:01Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(374 bytes)
[2026-06-09T06:24:01Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(374 bytes)
[2026-06-09T06:24:01Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(3246 bytes)
[2026-06-09T06:24:01Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(374 bytes)
[2026-06-09T06:24:01Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(374 bytes)
[2026-06-09T06:24:01Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(374 bytes)
[2026-06-09T06:24:01Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(4886 bytes)
[2026-06-09T06:24:01Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(398 bytes)
[2026-06-09T06:24:01Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(406 bytes)
[2026-06-09T06:24:01Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(382 bytes)
[2026-06-09T06:24:01Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(2302 bytes)
[2026-06-09T06:24:01Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(390 bytes)
[2026-06-09T06:24:01Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(414 bytes)
[2026-06-09T06:24:01Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(390 bytes)
[2026-06-09T06:24:01Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(358 bytes)
[2026-06-09T06:24:01Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(3398 bytes)
[2026-06-09T06:24:01Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(350 bytes)
[2026-06-09T06:24:01Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(358 bytes)
[2026-06-09T06:24:01Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(366 bytes)
[2026-06-09T06:24:01Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(5334 bytes)
[2026-06-09T06:24:01Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(382 bytes)
[2026-06-09T06:24:01Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(350 bytes)
[2026-06-09T06:24:01Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(414 bytes)
[2026-06-09T06:24:01Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(3798 bytes)
[2026-06-09T06:24:01Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(366 bytes)
[2026-06-09T06:24:01Z INFO  neolink::replay] Replay: received 409600 bytes total (container/raw)
[2026-06-09T06:24:01Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(358 bytes)
[2026-06-09T06:24:01Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(366 bytes)
[2026-06-09T06:24:01Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(5038 bytes)
[2026-06-09T06:24:01Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(382 bytes)
[2026-06-09T06:24:01Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(390 bytes)
[2026-06-09T06:24:01Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(406 bytes)
[2026-06-09T06:24:01Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(3718 bytes)
[2026-06-09T06:24:01Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(382 bytes)
[2026-06-09T06:24:01Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(398 bytes)
[2026-06-09T06:24:01Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(366 bytes)
[2026-06-09T06:24:01Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(39598 bytes)
[2026-06-09T06:24:01Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(39598 bytes)
[2026-06-09T06:24:01Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(4702 bytes)
[2026-06-09T06:24:01Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(342 bytes)
[2026-06-09T06:24:01Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(398 bytes)
[2026-06-09T06:24:01Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(342 bytes)
[2026-06-09T06:24:01Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(2190 bytes)
[2026-06-09T06:24:01Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(374 bytes)
[2026-06-09T06:24:01Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(374 bytes)
[2026-06-09T06:24:01Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(422 bytes)
[2026-06-09T06:24:01Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(1742 bytes)
[2026-06-09T06:24:01Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(334 bytes)
[2026-06-09T06:24:01Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(374 bytes)
[2026-06-09T06:24:01Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(406 bytes)
[2026-06-09T06:24:01Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(350 bytes)
[2026-06-09T06:24:01Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(1662 bytes)
[2026-06-09T06:24:01Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(374 bytes)
[2026-06-09T06:24:01Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(374 bytes)
[2026-06-09T06:24:01Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(374 bytes)
[2026-06-09T06:24:01Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(2006 bytes)
[2026-06-09T06:24:01Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(374 bytes)
[2026-06-09T06:24:01Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(374 bytes)
[2026-06-09T06:24:01Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(406 bytes)
[2026-06-09T06:24:01Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(1878 bytes)
[2026-06-09T06:24:01Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(350 bytes)
[2026-06-09T06:24:01Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(374 bytes)
[2026-06-09T06:24:01Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(374 bytes)
[2026-06-09T06:24:01Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(1766 bytes)
[2026-06-09T06:24:01Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(374 bytes)
[2026-06-09T06:24:01Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(382 bytes)
[2026-06-09T06:24:01Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(382 bytes)
[2026-06-09T06:24:01Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(1686 bytes)
[2026-06-09T06:24:01Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(366 bytes)
[2026-06-09T06:24:01Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(374 bytes)
[2026-06-09T06:24:01Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(374 bytes)
[2026-06-09T06:24:01Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(1614 bytes)
[2026-06-09T06:24:01Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(374 bytes)
[2026-06-09T06:24:01Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(374 bytes)
[2026-06-09T06:24:01Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(374 bytes)
[2026-06-09T06:24:01Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(1574 bytes)
[2026-06-09T06:24:01Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(398 bytes)
[2026-06-09T06:24:01Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(422 bytes)
[2026-06-09T06:24:01Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(358 bytes)
[2026-06-09T06:24:01Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(1518 bytes)
[2026-06-09T06:24:01Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(390 bytes)
[2026-06-09T06:24:01Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(398 bytes)
[2026-06-09T06:24:01Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(342 bytes)
[2026-06-09T06:24:01Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(374 bytes)
[2026-06-09T06:24:01Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(1550 bytes)
[2026-06-09T06:24:01Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(342 bytes)
[2026-06-09T06:24:01Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(374 bytes)
[2026-06-09T06:24:01Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(374 bytes)
[2026-06-09T06:24:01Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(1486 bytes)
[2026-06-09T06:24:01Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(374 bytes)
[2026-06-09T06:24:01Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(374 bytes)
[2026-06-09T06:24:01Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(374 bytes)
[2026-06-09T06:24:01Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(2158 bytes)
[2026-06-09T06:24:01Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(374 bytes)
[2026-06-09T06:24:01Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(374 bytes)
[2026-06-09T06:24:01Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(374 bytes)
[2026-06-09T06:24:01Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(2702 bytes)
[2026-06-09T06:24:01Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(374 bytes)
[2026-06-09T06:24:01Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(374 bytes)
[2026-06-09T06:24:01Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(374 bytes)
[2026-06-09T06:24:01Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(3422 bytes)
[2026-06-09T06:24:01Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(390 bytes)
[2026-06-09T06:24:01Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(398 bytes)
[2026-06-09T06:24:01Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(406 bytes)
[2026-06-09T06:24:01Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(4030 bytes)
[2026-06-09T06:24:01Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(366 bytes)
[2026-06-09T06:24:01Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(382 bytes)
[2026-06-09T06:24:01Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(374 bytes)
[2026-06-09T06:24:02Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(4694 bytes)
[2026-06-09T06:24:02Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(342 bytes)
[2026-06-09T06:24:02Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(374 bytes)
[2026-06-09T06:24:02Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(374 bytes)
[2026-06-09T06:24:02Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(3990 bytes)
[2026-06-09T06:24:02Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(366 bytes)
[2026-06-09T06:24:02Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(406 bytes)
[2026-06-09T06:24:02Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(350 bytes)
[2026-06-09T06:24:02Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(374 bytes)
[2026-06-09T06:24:02Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(4118 bytes)
[2026-06-09T06:24:02Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(374 bytes)
[2026-06-09T06:24:02Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(374 bytes)
[2026-06-09T06:24:02Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(382 bytes)
[2026-06-09T06:24:02Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(39598 bytes)
[2026-06-09T06:24:03Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(33182 bytes)
[2026-06-09T06:24:03Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(398 bytes)
[2026-06-09T06:24:03Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(398 bytes)
[2026-06-09T06:24:03Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(390 bytes)
[2026-06-09T06:24:03Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(4526 bytes)
[2026-06-09T06:24:03Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(366 bytes)
[2026-06-09T06:24:03Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(374 bytes)
[2026-06-09T06:24:03Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(350 bytes)
[2026-06-09T06:24:03Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(4214 bytes)
[2026-06-09T06:24:03Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(374 bytes)
[2026-06-09T06:24:03Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(406 bytes)
[2026-06-09T06:24:03Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(342 bytes)
[2026-06-09T06:24:03Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(2902 bytes)
[2026-06-09T06:24:03Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(406 bytes)
[2026-06-09T06:24:03Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(358 bytes)
[2026-06-09T06:24:03Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(358 bytes)
[2026-06-09T06:24:03Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(3254 bytes)
[2026-06-09T06:24:03Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(382 bytes)
[2026-06-09T06:24:03Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(374 bytes)
[2026-06-09T06:24:03Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(374 bytes)
[2026-06-09T06:24:03Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(3510 bytes)
[2026-06-09T06:24:03Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(374 bytes)
[2026-06-09T06:24:03Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(374 bytes)
[2026-06-09T06:24:03Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(374 bytes)
[2026-06-09T06:24:03Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(3286 bytes)
[2026-06-09T06:24:03Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(374 bytes)
[2026-06-09T06:24:03Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(382 bytes)
[2026-06-09T06:24:03Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(382 bytes)
[2026-06-09T06:24:03Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(374 bytes)
[2026-06-09T06:24:03Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(3558 bytes)
[2026-06-09T06:24:03Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(470 bytes)
[2026-06-09T06:24:03Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(350 bytes)
[2026-06-09T06:24:03Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(382 bytes)
[2026-06-09T06:24:03Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(3110 bytes)
[2026-06-09T06:24:03Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(366 bytes)
[2026-06-09T06:24:03Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(398 bytes)
[2026-06-09T06:24:03Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(350 bytes)
[2026-06-09T06:24:03Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(3454 bytes)
[2026-06-09T06:24:03Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(326 bytes)
[2026-06-09T06:24:03Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(374 bytes)
[2026-06-09T06:24:03Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(382 bytes)
[2026-06-09T06:24:03Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(3902 bytes)
[2026-06-09T06:24:03Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(374 bytes)
[2026-06-09T06:24:03Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(374 bytes)
[2026-06-09T06:24:03Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(374 bytes)
[2026-06-09T06:24:03Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(3822 bytes)
[2026-06-09T06:24:03Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(390 bytes)
[2026-06-09T06:24:03Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(366 bytes)
[2026-06-09T06:24:03Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(390 bytes)
[2026-06-09T06:24:03Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(4126 bytes)
[2026-06-09T06:24:03Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(374 bytes)
[2026-06-09T06:24:03Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(374 bytes)
[2026-06-09T06:24:03Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(374 bytes)
[2026-06-09T06:24:03Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(4830 bytes)
[2026-06-09T06:24:03Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(374 bytes)
[2026-06-09T06:24:03Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(374 bytes)
[2026-06-09T06:24:03Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(382 bytes)
[2026-06-09T06:24:03Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(4030 bytes)
[2026-06-09T06:24:03Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(374 bytes)
[2026-06-09T06:24:03Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(374 bytes)
[2026-06-09T06:24:03Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(390 bytes)
[2026-06-09T06:24:03Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(374 bytes)
[2026-06-09T06:24:03Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(3734 bytes)
[2026-06-09T06:24:03Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(382 bytes)
[2026-06-09T06:24:03Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(374 bytes)
[2026-06-09T06:24:03Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(374 bytes)
[2026-06-09T06:24:03Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(3334 bytes)
[2026-06-09T06:24:03Z INFO  neolink_core::bc_protocol::replay] Replay: 400 packets, 708 KB received
[2026-06-09T06:24:03Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(406 bytes)
[2026-06-09T06:24:03Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(382 bytes)
[2026-06-09T06:24:03Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(398 bytes)
[2026-06-09T06:24:03Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(2710 bytes)
[2026-06-09T06:24:03Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(358 bytes)
[2026-06-09T06:24:03Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(350 bytes)
[2026-06-09T06:24:03Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(374 bytes)
[2026-06-09T06:24:03Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(2510 bytes)
[2026-06-09T06:24:03Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(374 bytes)
[2026-06-09T06:24:03Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(374 bytes)
[2026-06-09T06:24:03Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(398 bytes)
[2026-06-09T06:24:03Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(2198 bytes)
[2026-06-09T06:24:03Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(374 bytes)
[2026-06-09T06:24:03Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(374 bytes)
[2026-06-09T06:24:03Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(358 bytes)
[2026-06-09T06:24:06Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(39598 bytes)
[2026-06-09T06:24:07Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(14374 bytes)
[2026-06-09T06:24:07Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(382 bytes)
[2026-06-09T06:24:07Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(374 bytes)
[2026-06-09T06:24:07Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(374 bytes)
[2026-06-09T06:24:07Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(1982 bytes)
[2026-06-09T06:24:07Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(374 bytes)
[2026-06-09T06:24:07Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(374 bytes)
[2026-06-09T06:24:07Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(374 bytes)
[2026-06-09T06:24:07Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(1502 bytes)
[2026-06-09T06:24:07Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(374 bytes)
[2026-06-09T06:24:07Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(374 bytes)
[2026-06-09T06:24:07Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(374 bytes)
[2026-06-09T06:24:07Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(374 bytes)
[2026-06-09T06:24:07Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(1502 bytes)
[2026-06-09T06:24:07Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(374 bytes)
[2026-06-09T06:24:07Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(382 bytes)
[2026-06-09T06:24:07Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(374 bytes)
[2026-06-09T06:24:07Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(1478 bytes)
[2026-06-09T06:24:07Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(374 bytes)
[2026-06-09T06:24:07Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(382 bytes)
[2026-06-09T06:24:07Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(462 bytes)
[2026-06-09T06:24:07Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(2174 bytes)
[2026-06-09T06:24:07Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(430 bytes)
[2026-06-09T06:24:07Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(374 bytes)
[2026-06-09T06:24:07Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(374 bytes)
[2026-06-09T06:24:07Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(1654 bytes)
[2026-06-09T06:24:07Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(366 bytes)
[2026-06-09T06:24:07Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(350 bytes)
[2026-06-09T06:24:07Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(366 bytes)
[2026-06-09T06:24:07Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(1462 bytes)
[2026-06-09T06:24:07Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(334 bytes)
[2026-06-09T06:24:07Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(342 bytes)
[2026-06-09T06:24:07Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(382 bytes)
[2026-06-09T06:24:07Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(1198 bytes)
[2026-06-09T06:24:07Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(382 bytes)
[2026-06-09T06:24:07Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(398 bytes)
[2026-06-09T06:24:07Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(374 bytes)
[2026-06-09T06:24:07Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(902 bytes)
[2026-06-09T06:24:07Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(406 bytes)
[2026-06-09T06:24:07Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(406 bytes)
[2026-06-09T06:24:07Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(350 bytes)
[2026-06-09T06:24:07Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(926 bytes)
[2026-06-09T06:24:07Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(366 bytes)
[2026-06-09T06:24:07Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(374 bytes)
[2026-06-09T06:24:07Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(358 bytes)
[2026-06-09T06:24:07Z DEBUG neolink_core::bc_protocol::replay] Replay: recv msg_id=5 msg_num=15 response_code=45436 body=binary(350 bytes)
[2026-06-09T06:24:18Z INFO  neolink::replay] Replay: 21s duration reached, sending replay stop (MSG 7) and closing file.
[2026-06-09T06:24:18Z INFO  neolink::replay] Replay: sending MSG 7 (stop) with 5s timeout
[2026-06-09T06:24:18Z INFO  neolink::replay] Replay: MSG 7 (stop) completed successfully in 143.103456ms
[2026-06-09T06:24:18Z DEBUG neolink::replay] Replay: no ftyp in buffer (first 32 bytes): [6e, 00, 00, 00, 23, 12, 44, 26, 36, 49, 0e, 9a, 6d, 5e, 55, 24, 34, 54, 5a, ce, 31, 1d, 1e, 6b, 3f, 07, 1b, 90, 7b, 44, 52, 2c]
[2026-06-09T06:24:18Z WARN  neolink::replay] Replay: could not assemble MP4: Replay buffer does not start with ftyp; trying BcMedia decode
[2026-06-09T06:24:18Z INFO  neolink::replay] Replay: BcMedia stream (819660 bytes) saved to 0120260608060802.replay.bin
[2026-06-09T06:24:22Z INFO  neolink_core::bc_protocol::replay] Replay: no data for 15s (camera may have stopped without 300), finishing (462 packets, 819806 bytes)
[2026-06-09T06:24:22Z INFO  neolink_core::bc_protocol::replay] Replay stream ended: 462 packets, 819806 bytes binary
[2026-06-09T06:24:22Z INFO  neolink::replay] Replay: collected 21764 bytes of AAC audio from BcMedia stream
[2026-06-09T06:24:22Z INFO  neolink::replay] Replay: actual avg fps from timestamps = 5.00 (declared fps = 25)
[2026-06-09T06:24:22Z INFO  neolink::replay::gst] Replay GStreamer: set metadata tags on mp4mux TagSetter
[2026-06-09T06:24:22Z INFO  neolink::replay::gst] Replay GStreamer: pushed 5504 ms of AAC audio
[2026-06-09T06:24:22Z INFO  neolink::replay::gst] Replay GStreamer: muxed 25 video frames + audio to 0120260608060802.mp4
Parsed BcMedia replay and muxed to 0120260608060802.mp4
[2026-06-09T06:24:22Z INFO  neolink_core::bc_protocol::stream] StreamData::drop: starting
[2026-06-09T06:24:22Z INFO  neolink_core::bc_protocol::stream] StreamData::drop: abort_handle cancelled
[2026-06-09T06:24:22Z INFO  neolink_core::bc_protocol::stream] StreamData::drop: handle is finished, dropping
[2026-06-09T06:24:22Z INFO  neolink_core::bc_protocol::stream] StreamData::drop: complete
```



```
ffprobe -i 0120260608060802.replay.bin -show_format -show_streams
```
ffprobe version n8.1.1 Copyright (c) 2007-2026 the FFmpeg developers
  built with gcc 16.1.1 (GCC) 20260430
  configuration: --prefix=/usr --disable-debug --disable-static --disable-stripping --enable-amf --enable-avisynth --enable-cuda-llvm --enable-lto --enable-fontconfig --enable-frei0r --enable-gmp --enable-gnutls --enable-gpl --enable-ladspa --enable-lcms2 --enable-libaom --enable-libass --enable-libbluray --enable-libbs2b --enable-libdav1d --enable-libdrm --enable-libdvdnav --enable-libdvdread --enable-libfreetype --enable-libfribidi --enable-libglslang --enable-libgsm --enable-libharfbuzz --enable-libiec61883 --enable-libjack --enable-libjxl --enable-libmodplug --enable-libmp3lame --enable-libopencore_amrnb --enable-libopencore_amrwb --enable-libopenjpeg --enable-libopenmpt --enable-libopus --enable-libplacebo --enable-libpulse --enable-librav1e --enable-librsvg --enable-librubberband --enable-libsnappy --enable-libsoxr --enable-libspeex --enable-libsrt --enable-libssh --enable-libsvtav1 --enable-libtheora --enable-libv4l2 --enable-libvidstab --enable-libvmaf --enable-libvorbis --enable-libvpl --enable-libvpx --enable-libwebp --enable-libx264 --enable-libx265 --enable-libxcb --enable-libxml2 --enable-libxvid --enable-libzimg --enable-libzmq --enable-nvdec --enable-nvenc --enable-opencl --enable-opengl --enable-shared --enable-vapoursynth --enable-version3 --enable-vulkan
  libavutil      60. 26.101 / 60. 26.101
  libavcodec     62. 28.101 / 62. 28.101
  libavformat    62. 12.101 / 62. 12.101
  libavdevice    62.  3.101 / 62.  3.101
  libavfilter    11. 14.101 / 11. 14.101
  libswscale      9.  5.101 /  9.  5.101
  libswresample   6.  3.101 /  6.  3.101
Input #0, h264, from '0120260608060802.replay.bin':
  Duration: N/A, bitrate: N/A
  Stream #0:0: Video: h264 (High), yuv420p(progressive), 640x352, 25 fps, 1200k tbr, 1200k tbn
[STREAM]
index=0
codec_name=h264
codec_long_name=H.264 / AVC / MPEG-4 AVC / MPEG-4 part 10
profile=High
codec_type=video
codec_tag_string=[0][0][0][0]
codec_tag=0x0000
mime_codec_string=avc1.64001e
width=640
height=352
coded_width=640
coded_height=352
has_b_frames=0
sample_aspect_ratio=N/A
display_aspect_ratio=N/A
pix_fmt=yuv420p
level=30
color_range=unknown
color_space=unknown
color_transfer=unknown
color_primaries=unknown
chroma_location=unspecified
field_order=progressive
is_avc=false
nal_length_size=0
id=N/A
r_frame_rate=1200000/1
avg_frame_rate=25/1
time_base=1/1200000
start_pts=N/A
start_time=N/A
duration_ts=N/A
duration=N/A
bit_rate=N/A
max_bit_rate=N/A
bits_per_raw_sample=8
nb_frames=N/A
nb_read_frames=N/A
nb_read_packets=N/A
extradata_size=21
DISPOSITION:default=0
DISPOSITION:dub=0
DISPOSITION:original=0
DISPOSITION:comment=0
DISPOSITION:lyrics=0
DISPOSITION:karaoke=0
DISPOSITION:forced=0
DISPOSITION:hearing_impaired=0
DISPOSITION:visual_impaired=0
DISPOSITION:clean_effects=0
DISPOSITION:attached_pic=0
DISPOSITION:timed_thumbnails=0
DISPOSITION:non_diegetic=0
DISPOSITION:captions=0
DISPOSITION:descriptions=0
DISPOSITION:metadata=0
DISPOSITION:dependent=0
DISPOSITION:still_image=0
DISPOSITION:multilayer=0
[/STREAM]
[FORMAT]
filename=0120260608060802.replay.bin
nb_streams=1
nb_programs=0
nb_stream_groups=0
format_name=h264
format_long_name=raw H.264 video
start_time=N/A
duration=N/A
size=819660
bit_rate=N/A
probe_score=51
[/FORMAT]
```

Additionally exported AAC stream

```
ffprobe -i 0120260608060802.replay.aac.bin -show_format -show_streams
ffprobe version n8.1.1 Copyright (c) 2007-2026 the FFmpeg developers
  built with gcc 16.1.1 (GCC) 20260430
  configuration: --prefix=/usr --disable-debug --disable-static --disable-stripping --enable-amf --enable-avisynth --enable-cuda-llvm --enable-lto --enable-fontconfig --enable-frei0r --enable-gmp --enable-gnutls --enable-gpl --enable-ladspa --enable-lcms2 --enable-libaom --enable-libass --enable-libbluray --enable-libbs2b --enable-libdav1d --enable-libdrm --enable-libdvdnav --enable-libdvdread --enable-libfreetype --enable-libfribidi --enable-libglslang --enable-libgsm --enable-libharfbuzz --enable-libiec61883 --enable-libjack --enable-libjxl --enable-libmodplug --enable-libmp3lame --enable-libopencore_amrnb --enable-libopencore_amrwb --enable-libopenjpeg --enable-libopenmpt --enable-libopus --enable-libplacebo --enable-libpulse --enable-librav1e --enable-librsvg --enable-librubberband --enable-libsnappy --enable-libsoxr --enable-libspeex --enable-libsrt --enable-libssh --enable-libsvtav1 --enable-libtheora --enable-libv4l2 --enable-libvidstab --enable-libvmaf --enable-libvorbis --enable-libvpl --enable-libvpx --enable-libwebp --enable-libx264 --enable-libx265 --enable-libxcb --enable-libxml2 --enable-libxvid --enable-libzimg --enable-libzmq --enable-nvdec --enable-nvenc --enable-opencl --enable-opengl --enable-shared --enable-vapoursynth --enable-version3 --enable-vulkan
  libavutil      60. 26.101 / 60. 26.101
  libavcodec     62. 28.101 / 62. 28.101
  libavformat    62. 12.101 / 62. 12.101
  libavdevice    62.  3.101 / 62.  3.101
  libavfilter    11. 14.101 / 11. 14.101
  libswscale      9.  5.101 /  9.  5.101
  libswresample   6.  3.101 /  6.  3.101
[aac @ 0x561d57b87480] channel element 0.0 is not allocated
    Last message repeated 2 times
[aac @ 0x561d57b87480] TYPE_FIL: Input buffer exhausted before END element found
[aac @ 0x561d57b87480] channel element 0.0 is not allocated
[aac @ 0x561d57b86840] Estimating duration from bitrate, this may be inaccurate
Input #0, aac, from '0120260608060802.replay.aac.bin':
  Duration: 00:00:05.54, bitrate: 31 kb/s
  Stream #0:0: Audio: aac (LC), 16000 Hz, mono, fltp, 31 kb/s
[STREAM]
index=0
codec_name=aac
codec_long_name=AAC (Advanced Audio Coding)
profile=LC
codec_type=audio
codec_tag_string=[0][0][0][0]
codec_tag=0x0000
mime_codec_string=mp4a.40.2
sample_fmt=fltp
sample_rate=16000
channels=1
channel_layout=mono
bits_per_sample=0
initial_padding=0
id=N/A
r_frame_rate=0/0
avg_frame_rate=0/0
time_base=1/28224000
start_pts=N/A
start_time=N/A
duration_ts=156371701
duration=5.540381
bit_rate=31426
max_bit_rate=N/A
bits_per_raw_sample=N/A
nb_frames=N/A
nb_read_frames=N/A
nb_read_packets=N/A
DISPOSITION:default=0
DISPOSITION:dub=0
DISPOSITION:original=0
DISPOSITION:comment=0
DISPOSITION:lyrics=0
DISPOSITION:karaoke=0
DISPOSITION:forced=0
DISPOSITION:hearing_impaired=0
DISPOSITION:visual_impaired=0
DISPOSITION:clean_effects=0
DISPOSITION:attached_pic=0
DISPOSITION:timed_thumbnails=0
DISPOSITION:non_diegetic=0
DISPOSITION:captions=0
DISPOSITION:descriptions=0
DISPOSITION:metadata=0
DISPOSITION:dependent=0
DISPOSITION:still_image=0
DISPOSITION:multilayer=0
[/STREAM]
[FORMAT]
filename=0120260608060802.replay.aac.bin
nb_streams=1
nb_programs=0
nb_stream_groups=0
format_name=aac
format_long_name=raw ADTS AAC (Advanced Audio Coding)
start_time=N/A
duration=5.540381
size=21764
bit_rate=31425
probe_score=51
[/FORMAT]
```