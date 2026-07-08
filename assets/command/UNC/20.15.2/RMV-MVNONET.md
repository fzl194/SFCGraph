---
id: UNC@20.15.2@MMLCommand@RMV MVNONET
type: MMLCommand
name: RMV MVNONET（删除MVNO网络配置信息）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: MVNONET
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
- 网络管理
- 归属网络运营商管理
- MVNO管理
- MVNO网络标识配置表
status: active
---

# RMV MVNONET（删除MVNO网络配置信息）

## 功能

**适用网元：SGSN、MME**

该命令用于从MVNO网络信息表中删除一条记录。

## 注意事项

此命令执行后立即生效。

如果不输入任何参数，则提示：请输入"MVNO Mobile Country Code"参数或"MVNO Mobile Network Code"参数或"Matched IMSI"或"MVNO Identity"参数。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MVNOMCC | MVNO移动国家码 | 可选必选说明：可选参数<br>参数含义：该参数用于指定MVNO用户的IMSI的移动国家代码。<br>取值范围：3位十进制数字<br>默认值：无 |
| MVNOMNC | MVNO移动网号 | 可选必选说明：可选参数<br>参数含义：该参数用于指定MVNO用户的IMSI的移动网号。<br>取值范围：位数为2或3的十进制数字<br>默认值：无 |
| MATCHIMSI | 匹配IMSI | 可选必选说明：可选参数<br>参数含义：该参数用于指定MVNO用户除了MCC和MNC外的IMSI的字段。<br>取值范围：长度不超过10的十进制数字<br>默认值：无 |
| MVNOID | MVNO标识 | 可选必选说明：可选参数<br>参数含义：该参数用于指定可以根据MVNO标识删除这个MVNO的网络配置。<br>取值范围：1～64<br>默认值：无 |

## 操作的配置对象

- [MVNO网络配置信息（MVNONET）](configobject/UNC/20.15.2/MVNONET.md)

## 使用实例

删除MVNO标识为1的MVNO的网络资源配置：

RMV MVNONET: MVNOID=1;

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除MVNO网络配置信息(RMV-MVNONET)_26146064.md`
