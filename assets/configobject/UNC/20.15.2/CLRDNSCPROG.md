---
id: UNC@20.15.2@ConfigObject@CLRDNSCPROG
type: ConfigObject
name: CLRDNSCPROG（离散清缓存进度）
nf: UNC
version: 20.15.2
object_name: CLRDNSCPROG
object_kind: query_target
applicable_nf:
- SGSN
- MME
status: active
---

# CLRDNSCPROG（离散清缓存进度）

## 说明

**适用网元：SGSN、MME**

该命令用于查询一级Cache离散清除进度。

DNS Cache是使用DNS服务器解析时查找到的域名和IP地址信息在系统中的缓存，用于快速解析域名。

DNS Cache分为一级Cache和二级Cache。一级Cache保存在SPP进程上，保存了每个SPP进程各自常用的域名记录；二级Cache保存在1号SGP进程上，保存的域名记录为每个SPP进程中域名记录的集合。当SPP进程需要获取域名记录时，首先在HOSTFILE中查询。如果HOSTFILE中查询不到需要的域名记录，则在一级Cache中进行查询。如果一级Cache中查询不到需要的域名记录，则在二级Cache上查询。如果二级Cache仍查询不到需要的域名记录，则向DNS服务器进行查询。

每条Cache的记录具有一定的生命周期，生命周期结束后，该记录失效。

DNS服务器上的数据修改后，可以使用CLR DNSC命令清除MME网元整系统DNS Cache，即使用命令清除二级Cache和一级Cache。

当软参BYTE_EX_B25 BIT1、BYTE_EX_B25 BIT3~BIT4、BYTE_EX_B322 BIT1~BIT2或者BYTE_EX_B332 BIT6不为0时，打开离散清缓存功能，即执行CLR DNSC并不会立即清除一级Cache，按照软参说明离散清除一级Cache。DSP CLRDNSCPROG命令用于在BYTE_EX_B25 BIT1、BYTE_EX_B25 BIT3~BIT4、BYTE_EX_B322 BIT1~BIT2或者BYTE_EX_B332 BIT6不为0时，查询一级Cache离散清除进度。

## 操作本对象的命令

- [[command/UNC/20.15.2/DSP-CLRDNSCPROG]] · DSP CLRDNSCPROG

## 证据

- 原始手册：`evidence/UNC/20.15.2/CLRDNSCPROG.md`
