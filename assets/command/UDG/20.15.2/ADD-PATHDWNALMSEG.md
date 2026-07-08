---
id: UDG@20.15.2@MMLCommand@ADD PATHDWNALMSEG
type: MMLCommand
name: ADD PATHDWNALMSEG（增加单条路径断告警抑制参数的分段配置）
nf: UDG
version: 20.15.2
verb: ADD
object_keyword: PATHDWNALMSEG
command_category: 配置类
applicable_nf:
- SGW-U
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
max_records: 300
category_path:
- 用户面服务管理
- 业务运维
- 业务告警管理
- 单条路径断告警的分段抑制参数
status: active
---

# ADD PATHDWNALMSEG（增加单条路径断告警抑制参数的分段配置）

## 功能

**适用NF：SGW-U、PGW-U、UPF**

由于现网传输的原因，部分eNodeB/gNodeB可能偶然出现中断，而由于短时间内的单条链路故障，对业务影响可控，客户并不特别关注，但是给客户的维护人员造成困扰。故而对于偶然闪断的链路，进行告警抑制，当中断超过一定的次数时，再上报此链路的故障告警（ALM-81018 GTPU路径断）。该命令用来配置指定eNodeB/gNodeB地址段内的单条路径断告警抑制。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为300。
- 四个可选参数说明： ALMDELAYTMS=2，UPF在给对端发送连续2次路径探测request，并且没有收到response的时候上报告警； ALMRPTDETECTTMS=5, ALMRPTDOWNTMS =3。UPF在给对端连续发送5次路径探测request，并且其中有3次没有收到response的时候上报告警； ALMRESTORETMS=5，UPF在给对端连续发送5次路径探测request，并且5次都回了response的时候告警清除。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ALMDELAYTMS | 告警上报的连续中断次数 | 可选必选说明：可选参数<br>参数含义：指定单条数据路径断告警上报的连续中断次数阈值大小。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～10，单位是次数。<br>默认值：5<br>配置原则：无 |
| ALMRPTDETECTTMS | 告警上报的探测次数 | 可选必选说明：可选参数<br>参数含义：指定单条数据路径断告警上报的探测次数。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～15，单位是次数。<br>默认值：5<br>配置原则：无 |
| ALMRPTDOWNTMS | 告警上报的累计中断次数 | 可选必选说明：可选参数<br>参数含义：指定单条数据路径断告警上报的累计中断次数阈值大小。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～15，单位是次数。<br>默认值：3<br>配置原则：无 |
| ALMRESTORETMS | 告警恢复的连续正常次数 | 可选必选说明：可选参数<br>参数含义：指定单条数据路径断告警恢复的连续正常次数阈值大小。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～10，单位是次数。<br>默认值：5<br>配置原则：该配置需要和网络规划一致。 |
| ENBIPVERSION | IP地址版本 | 可选必选说明：必选参数<br>参数含义：该参数用于设置地址版本类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- IPV4：表示地址类型为IPv4。<br>- IPV6：表示地址类型为IPv6。<br>默认值：无<br>配置原则：无 |
| V4STARTIP | IPv4类型的eNodeB地址段起始地址 | 可选必选说明：条件必选参数<br>前提条件：该参数在“ENBIPVERSION”配置为“IPV4”时为必选参数。<br>参数含义：指定IPv4类型的eNodeB地址段的起始地址。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。<br>默认值：无<br>配置原则：无 |
| V4ENDIP | IPv4类型的eNodeB地址段终止地址 | 可选必选说明：条件必选参数<br>前提条件：该参数在“ENBIPVERSION”配置为“IPV4”时为必选参数。<br>参数含义：指定IPv4类型的eNodeB地址段的终止地址。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。<br>默认值：无<br>配置原则：无 |
| V6STARTIP | IPv6类型的eNodeB地址段起始地址 | 可选必选说明：条件必选参数<br>前提条件：该参数在“ENBIPVERSION”配置为“IPV6”时为必选参数。<br>参数含义：指定IPv6类型的eNodeB地址段的起始地址。<br>数据来源：本端规划<br>取值范围：IPv6地址类型。采用冒号分十六进制X:X:X:X:X:X:X:X格式。<br>默认值：无<br>配置原则：无 |
| V6ENDIP | IPv6类型的eNodeB地址段终止地址 | 可选必选说明：条件必选参数<br>前提条件：该参数在“ENBIPVERSION”配置为“IPV6”时为必选参数。<br>参数含义：指定IPv6类型的eNodeB地址段的终止地址。<br>数据来源：本端规划<br>取值范围：IPv6地址类型。采用冒号分十六进制X:X:X:X:X:X:X:X格式。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/PATHDWNALMSEG]] · 单条路径断告警抑制参数的分段配置（PATHDWNALMSEG）

## 使用实例

为避免eNodeB/gNodeB偶然出现中断，造成路径断告警，新增指定eNodeB/gNodeB地址段的单条路径断告警抑制参数配置 ：

```
ADD PATHDWNALMSEG: ALMDELAYTMS=5, ALMRPTDOWNTMS=3, ALMRESTORETMS=5, ENBIPVERSION=IPV4, V4STARTIP="10.1.1.1", V4ENDIP="10.1.1.10";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/增加单条路径断告警抑制参数的分段配置（ADD-PATHDWNALMSEG）_82837867.md`
