---
id: UDG@20.15.2@MMLCommand@MOD PATHDWNALMSEG
type: MMLCommand
name: MOD PATHDWNALMSEG（修改单条路径断告警抑制参数的分段配置）
nf: UDG
version: 20.15.2
verb: MOD
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

# MOD PATHDWNALMSEG（修改单条路径断告警抑制参数的分段配置）

## 功能

**适用NF：SGW-U、PGW-U、UPF**

该命令用于修改指定eNodeB/gNodeB地址段内的单条路径断告警抑制的配置。在该命令中，系统通过以下关键参数的组合来唯一标识一条记录。

a.IP地址版本;b.eNodeB/gNodeB地址段起始地址;c.eNodeB/gNodeB地址段终止地址。

## 注意事项

- 该命令执行后立即生效。
- 四个告警相关参数至少需要输入一个，否则命令执行失败。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ALMDELAYTMS | 告警上报的连续中断次数 | 可选必选说明：可选参数<br>参数含义：指定单条数据路径断告警上报的连续中断次数阈值大小。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～10，单位是次数。<br>默认值：无<br>配置原则：该配置需要和网络规划一致。 |
| ALMRPTDETECTTMS | 告警上报的探测次数 | 可选必选说明：可选参数<br>参数含义：指定单条数据路径断告警上报的探测次数。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～15，单位是次数。<br>默认值：无<br>配置原则：该配置需要和网络规划一致。 |
| ALMRPTDOWNTMS | 告警上报的累计中断次数 | 可选必选说明：可选参数<br>参数含义：指定单条数据路径断告警上报的累计中断次数阈值大小。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～15，单位是次数。<br>默认值：无<br>配置原则：该配置需要和网络规划一致。 |
| ALMRESTORETMS | 告警恢复的连续正常次数 | 可选必选说明：可选参数<br>参数含义：指定单条数据路径断告警恢复的连续正常次数阈值大小。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～10，单位是次数。<br>默认值：无<br>配置原则：该配置需要和网络规划一致。 |
| ENBIPVERSION | IP地址版本 | 可选必选说明：必选参数<br>参数含义：该参数用于设置地址版本类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- IPV4：表示地址类型为IPv4。<br>- IPV6：表示地址类型为IPv6。<br>默认值：无<br>配置原则：无 |
| V4STARTIP | IPv4类型的eNodeB地址段起始地址 | 可选必选说明：条件必选参数<br>前提条件：该参数在“ENBIPVERSION”配置为“IPV4”时为必选参数。<br>参数含义：指定IPv4类型的eNodeB地址段的起始地址。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。<br>默认值：无<br>配置原则：无 |
| V4ENDIP | IPv4类型的eNodeB地址段终止地址 | 可选必选说明：条件必选参数<br>前提条件：该参数在“ENBIPVERSION”配置为“IPV4”时为必选参数。<br>参数含义：指定IPv4类型的eNodeB地址段的终止地址。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。<br>默认值：无<br>配置原则：无 |
| V6STARTIP | IPv6类型的eNodeB地址段起始地址 | 可选必选说明：条件必选参数<br>前提条件：该参数在“ENBIPVERSION”配置为“IPV6”时为必选参数。<br>参数含义：指定IPv6类型的eNodeB地址段的起始地址。<br>数据来源：本端规划<br>取值范围：IPv6地址类型。采用冒号分十六进制X:X:X:X:X:X:X:X格式。<br>默认值：无<br>配置原则：无 |
| V6ENDIP | IPv6类型的eNodeB地址段终止地址 | 可选必选说明：条件必选参数<br>前提条件：该参数在“ENBIPVERSION”配置为“IPV6”时为必选参数。<br>参数含义：指定IPv6类型的eNodeB地址段的终止地址。<br>数据来源：本端规划<br>取值范围：IPv6地址类型。采用冒号分十六进制X:X:X:X:X:X:X:X格式。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [单条路径断告警抑制参数的分段配置（PATHDWNALMSEG）](configobject/UDG/20.15.2/PATHDWNALMSEG.md)

## 使用实例

eNodeB/gNodeB组网变化时，修改指定IP地址段eNodeB/gNodeB的单条路径断告警抑制参数配置：

```
MOD PATHDWNALMSEG: ALMDELAYTMS=5, ALMRPTDETECTTMS=6, ALMRPTDOWNTMS=5, ALMRESTORETMS=5, ENBIPVERSION=IPV4, V4STARTIP="10.1.1.1", V4ENDIP="10.1.1.10";%
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/修改单条路径断告警抑制参数的分段配置（MOD-PATHDWNALMSEG）_82837868.md`
