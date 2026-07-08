---
id: UNC@20.15.2@ConfigObject@LOWPRIDSCP
type: ConfigObject
name: LOWPRIDSCP（低优先级业务DSCP）
nf: UNC
version: 20.15.2
object_name: LOWPRIDSCP
object_kind: entity
applicable_nf:
- SGSN
status: active
---

# LOWPRIDSCP（低优先级业务DSCP）

## 说明

**适用网元：SGSN**

此命令用于增加低优先级业务对应的DSCP的配置。SGSN收到下行数据包时，如果用户处于“STANDBY”状态（3G用户则为“PMM_IDLE”状态），则需要寻呼用户。当SMART PAGING的License功能打开，且对应的GGSN支持SMART PAGING功能时，则在SPP进程出现拥塞时需要对低优先级业务触发的寻呼进行流量控制。系统根据下行数据包中携带的DSCP来判断是否属于低优先级业务。

## 操作本对象的命令

- [ADD LOWPRIDSCP](command/UNC/20.15.2/ADD-LOWPRIDSCP.md)
- [LST LOWPRIDSCP](command/UNC/20.15.2/LST-LOWPRIDSCP.md)
- [RMV LOWPRIDSCP](command/UNC/20.15.2/RMV-LOWPRIDSCP.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除低优先级业务DSCP(RMV-LOWPRIDSCP)_72225191.md`
- 原始手册：`evidence/UNC/20.15.2/增加低优先级业务DSCP(ADD-LOWPRIDSCP)_26145510.md`
- 原始手册：`evidence/UNC/20.15.2/查询低优先级业务DSCP(LST-LOWPRIDSCP)_26305322.md`
