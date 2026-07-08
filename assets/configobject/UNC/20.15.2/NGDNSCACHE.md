---
id: UNC@20.15.2@ConfigObject@NGDNSCACHE
type: ConfigObject
name: NGDNSCACHE（DNS缓存）
nf: UNC
version: 20.15.2
object_name: NGDNSCACHE
object_kind: global_setting
applicable_nf:
- AMF
- SGW-C
status: active
---

# NGDNSCACHE（DNS缓存）

## 说明

![](设置DNS缓存参数（SET NGDNSCACHE）_10765250.assets/notice_3.0-zh-cn_2.png)

修改DNS缓存参数可能导致系统CPU负荷增大，系统的内存使用增长，或系统向DNS服务器的查询次数增加。

**适用NF：SGW-C、AMF**

该命令用于设置DNS缓存参数。

## 操作本对象的命令

- [CLR NGDNSCACHE](command/UNC/20.15.2/CLR-NGDNSCACHE.md)
- [DSP NGDNSCACHE](command/UNC/20.15.2/DSP-NGDNSCACHE.md)
- [LST NGDNSCACHE](command/UNC/20.15.2/LST-NGDNSCACHE.md)
- [SET NGDNSCACHE](command/UNC/20.15.2/SET-NGDNSCACHE.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示DNS缓存（DSP-NGDNSCACHE）_10765244.md`
- 原始手册：`evidence/UNC/20.15.2/查询DNS缓存参数（LST-NGDNSCACHE）_55725191.md`
- 原始手册：`evidence/UNC/20.15.2/清除DNS缓存（CLR-NGDNSCACHE）_55845121.md`
- 原始手册：`evidence/UNC/20.15.2/设置DNS缓存参数（SET-NGDNSCACHE）_10765250.md`
