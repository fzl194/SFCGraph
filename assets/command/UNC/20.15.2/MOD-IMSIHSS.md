---
id: UNC@20.15.2@MMLCommand@MOD IMSIHSS
type: MMLCommand
name: MOD IMSIHSS（修改IMSI-HSS对应关系）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: IMSIHSS
command_category: 配置类
applicable_nf:
- SGSN
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- Diameter应用协议
- IMSI-HSS转换信息
status: active
---

# MOD IMSIHSS（修改IMSI-HSS对应关系）

## 功能

**适用网元：SGSN、MME**

此命令用于修改IMSI与HSS的映射关系表记录， UNC 根据IMSI与HSS的映射关系表记录选择IMSI归属的HSS。

当需要修改 “HSS域名” ， “Diameter路由组索引” ， “移动网络名称” 时，用该命令进行修改。

## 注意事项

- 此命令执行后立即生效。
- 此命令不能修改“IMSI前缀”。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IMSIPRE | IMSI前缀 | 可选必选说明：必选参数<br>参数含义：待修改的IMSI前缀。<br>数据来源：全网规划<br>取值范围：1～15位数字<br>默认值：无<br>配置原则：无 |
| HSSRLM | HSS域名 | 可选必选说明：可选参数<br>参数含义：该待修改的HSS域名。在不配置HSS主机名的情况下，<br>UNC<br>根据HSS域名选择HSS。<br>数据来源：全网规划<br>取值范围：1～127位字符串<br>默认值：无<br>配置原则:<br>- 不能为非法字符，只允许输入字母，数字，“.”和“-”，不区分大小写。例如：epc.mnc123.mcc123.3gppnetwork.org。<br>- 不允许配置以“null”开头的字符串。<br>- 与对端HSS配置的HSS域名保持一致。 |
| GRPIDX | Diameter路由组索引 | 可选必选说明：可选参数<br>参数含义：该参数用于在系统范围内标识一条Diameter路由组。<br>数据来源：本端规划<br>取值范围：0~1023<br>默认值：无<br>配置原则：无<br>说明：- 当用户使用主机路由（**ADD DMHOSTRT**）并且“应用名称”为“S6A/S6D(S6a/S6d)”，或域路由（[**ADD DMRT**](../../信令传输管理/Diameter管理/Diameter路由/增加Diameter域路由配置(ADD DMRT)_26306100.md)）的“SELMODE_IMSI_PRIORITY(IMSI指定优选)”模式选路时，才需要填写此参数。<br>- 在“MML命令行-UNC”窗口上执行命令[**ADD DMRTGRP**](../../信令传输管理/Diameter管理/Diameter路由组/增加Diameter路由组(ADD DMRTGRP)_26146292.md)设置此参数。 |
| MNNAME | 移动网络名称 | 可选必选说明：可选参数<br>参数含义：待修改的用户所属的移动网络名称。<br>数据来源：本端规划<br>取值范围：1～32位字符串<br>默认值：无<br>配置原则：建议取有实际意义的名称，以方便识别。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/IMSIHSS]] · IMSI-HSS对应关系（IMSIHSS）

## 使用实例

修改IMSI前缀为3080107000的记录，将HSS域名改为epc.mnc123.mcc123.3gppnetwork.org，Diameter路由组索引改为1，移动网络名称为"mobile-network1"：

```
MOD IMSIHSS: IMSIPRE="3080107000", HSSRLM="epc.mnc015.mcc234.3gppnetwork.org", GRPIDX=1, MNNAME="mobile-network1";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改IMSI-HSS对应关系(MOD-IMSIHSS)_26305266.md`
