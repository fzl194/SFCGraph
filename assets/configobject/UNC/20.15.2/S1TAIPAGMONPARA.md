---
id: UNC@20.15.2@ConfigObject@S1TAIPAGMONPARA
type: ConfigObject
name: S1TAIPAGMONPARA（S1 TAI组寻呼异常监控功能参数）
nf: UNC
version: 20.15.2
object_name: S1TAIPAGMONPARA
object_kind: global_setting
applicable_nf:
- MME
status: active
---

# S1TAIPAGMONPARA（S1 TAI组寻呼异常监控功能参数）

## 说明

![](设置S1 TAI组寻呼异常监控功能参数(SET S1TAIPAGMONPARA)_92192794.assets/notice_3.0-zh-cn_2.png)

检测参数设置不当，可能导致寻呼消息误流控或影响寻呼风暴场景下的流控效果。

**适用网元：MME**

该命令用于设置S1 TAI组对象寻呼异常监控功能的参数。针对局部区域（某个或某些TAI）下行寻呼风暴或因基站侧故障不回寻呼响应触发大量寻呼消息重发，导致寻呼成功率下降场景，MME业务侧进行寻呼流控，减少寻呼风暴持续时长，快速恢复寻呼成功率。

## 操作本对象的命令

- [LST S1TAIPAGMONPARA](command/UNC/20.15.2/LST-S1TAIPAGMONPARA.md)
- [SET S1TAIPAGMONPARA](command/UNC/20.15.2/SET-S1TAIPAGMONPARA.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询S1-TAI组寻呼异常监控功能参数(LST-S1TAIPAGMONPARA)_27678301.md`
- 原始手册：`evidence/UNC/20.15.2/设置S1-TAI组寻呼异常监控功能参数(SET-S1TAIPAGMONPARA)_92192794.md`
