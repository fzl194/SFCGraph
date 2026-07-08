---
id: UDG@20.15.2@MMLCommand@RMV PATHDWNALMSEG
type: MMLCommand
name: RMV PATHDWNALMSEG（删除单条路径断告警抑制参数的分段配置）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: PATHDWNALMSEG
command_category: 配置类
applicable_nf:
- SGW-U
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 用户面服务管理
- 业务运维
- 业务告警管理
- 单条路径断告警的分段抑制参数
status: active
---

# RMV PATHDWNALMSEG（删除单条路径断告警抑制参数的分段配置）

## 功能

**适用NF：SGW-U、PGW-U、UPF**

该命令用于删除指定eNodeB/gNodeB地址段内的单条路径断告警抑制的配置。

## 注意事项

- 该命令执行后立即生效。
- 执行该删除操作，将不会产生指定eNodeB/gNodeB地址段内的单条路径断告警抑制的现象。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| V4STARTIP | IPv4类型的eNodeB地址段起始地址 | 可选必选说明：条件必选参数<br>前提条件：该参数在“ENBIPVERSION”配置为“IPV4”时为必选参数。<br>参数含义：指定IPv4类型的eNodeB地址段的起始地址。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。<br>默认值：无<br>配置原则：无 |
| V4ENDIP | IPv4类型的eNodeB地址段终止地址 | 可选必选说明：条件必选参数<br>前提条件：该参数在“ENBIPVERSION”配置为“IPV4”时为必选参数。<br>参数含义：指定IPv4类型的eNodeB地址段的终止地址。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。<br>默认值：无<br>配置原则：无 |
| V6STARTIP | IPv6类型的eNodeB地址段起始地址 | 可选必选说明：条件必选参数<br>前提条件：该参数在“ENBIPVERSION”配置为“IPV6”时为必选参数。<br>参数含义：指定IPv6类型的eNodeB地址段的起始地址。<br>数据来源：本端规划<br>取值范围：IPv6地址类型。采用冒号分十六进制X:X:X:X:X:X:X:X格式。<br>默认值：无<br>配置原则：无 |
| V6ENDIP | IPv6类型的eNodeB地址段终止地址 | 可选必选说明：条件必选参数<br>前提条件：该参数在“ENBIPVERSION”配置为“IPV6”时为必选参数。<br>参数含义：指定IPv6类型的eNodeB地址段的终止地址。<br>数据来源：本端规划<br>取值范围：IPv6地址类型。采用冒号分十六进制X:X:X:X:X:X:X:X格式。<br>默认值：无<br>配置原则：无 |
| ENBIPVERSION | IP地址版本 | 可选必选说明：必选参数<br>参数含义：该参数用于设置地址版本类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- IPV4：表示地址类型为IPv4。<br>- IPV6：表示地址类型为IPv6。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [单条路径断告警抑制参数的分段配置（PATHDWNALMSEG）](configobject/UDG/20.15.2/PATHDWNALMSEG.md)

## 使用实例

不需要配置单条路径断告警抑制参数的分段配置时,，删除单条路径断指定eNodeB/gNodeB地址段的告警抑制参数配置：

```
RMV PATHDWNALMSEG: ENBIPVERSION=IPV4, V4STARTIP="10.1.1.1", V4ENDIP="10.1.1.1";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/删除单条路径断告警抑制参数的分段配置（RMV-PATHDWNALMSEG）_82837869.md`
