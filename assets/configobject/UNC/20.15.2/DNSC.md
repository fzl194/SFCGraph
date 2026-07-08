---
id: UNC@20.15.2@ConfigObject@DNSC
type: ConfigObject
name: DNSC（DNS缓存）
nf: UNC
version: 20.15.2
object_name: DNSC
object_kind: action
applicable_nf:
- SGSN
- MME
- AMF
status: active
---

# DNSC（DNS缓存）

## 说明

![](清除DNS缓存(CLR DNSC)_72345945.assets/notice_3.0-zh-cn_2.png)

在话务高峰时执行此命令可能导致DNS查询记录不全、话务呼损等问题，建议在凌晨话务低谷时执行。

**适用网元：SGSN、MME、AMF**

该命令用于清除DNS Cache。

DNS Cache是使用DNS服务器解析时查找到的域名和IP地址信息在系统中的缓存，用于快速解析域名。

DNS Cache分为一级Cache和二级Cache。一级Cache保存在SPP进程上，保存了每个SPP进程各自常用的域名记录；二级Cache保存在1号SGP进程上，保存的域名记录为每个SPP进程中域名记录的集合。当SPP进程需要获取域名记录时，首先在HOSTFILE中查询。如果HOSTFILE中查询不到需要的域名记录，则在一级Cache中进行查询。如果一级Cache中查询不到需要的域名记录，则在二级Cache上查询。如果二级Cache仍查询不到需要的域名记录，则向DNS服务器进行查询。

每条Cache的记录具有一定的生命周期，生命周期结束后，该记录失效。

DNS服务器上的数据修改后，可以使用该命令清除 UNC 整系统DNS Cache，即使用该命令依次清除二级Cache和一级Cache。

## 操作本对象的命令

- [[command/UNC/20.15.2/CLR-DNSC]] · CLR DNSC

## 证据

- 原始手册：`evidence/UNC/20.15.2/DNSC.md`
