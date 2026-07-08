---
id: UDG@20.15.2@MMLCommand@SET IPSQMADJUST
type: MMLCommand
name: SET IPSQMADJUST（设置IPSQM调整参数）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: IPSQMADJUST
command_category: 配置类
applicable_nf:
- SGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
max_records: 1
category_path:
- 用户面服务管理
- 业务控制策略
- IPSQM控制
- IPSQM参数调整配置
status: active
---

# SET IPSQMADJUST（设置IPSQM调整参数）

## 功能

**适用NF：SGW-U、UPF**

该命令用于配置整形资源调整的业务处理节点（POD）的最低保护带宽及突发尺寸。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为1。
- 该命令用于配置低传输能力下的最低保证带宽，配置过小会导致用户丢包过多。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | THRESHOLD | LOWBANDWIDTH | LOWCBS | HIGHBANDWIDTH | HIGHCBS |
| --- | --- | --- | --- | --- | --- |
| 初始值 | 30 | 300 | 2000 | 1000 | 10000 |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| THRESHOLD | 阈值（兆比特/秒） | 可选必选说明：必选参数<br>参数含义：整形带宽调整阈值，用于区分不同传输能力分别设置调整参数，以便能根据不同的传输能力调整带宽控制效果。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～50，单位是兆比特每秒。<br>默认值：无<br>配置原则：无 |
| LOWBANDWIDTH | 低带宽域的最低保护值（千比特/秒） | 可选必选说明：可选参数<br>参数含义：对于低带宽域设置系统根据整机带宽计算出的各业务处理单元带宽的最低保护值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为100～100000，单位是千比特每秒。<br>默认值：无<br>配置原则：无 |
| LOWCBS | 低带宽域的突发尺寸（字节） | 可选必选说明：可选参数<br>参数含义：对于低带宽域设置系统根据整机带宽计算出的各业务处理单元带宽的突发尺寸。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为500～100000000，单位是字节。<br>默认值：无<br>配置原则：无 |
| HIGHBANDWIDTH | 高带宽域的最低保护值（千比特/秒） | 可选必选说明：可选参数<br>参数含义：对于高带宽域设置系统根据整机带宽计算出的各业务处理单元带宽的最低保护值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为100～100000，单位是千比特每秒。<br>默认值：无<br>配置原则：无 |
| HIGHCBS | 高带宽域的突发尺寸（字节） | 可选必选说明：可选参数<br>参数含义：对于高带宽域设置系统根据整机带宽计算出的各业务处理单元带宽的突发尺寸。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为500～100000000，单位是字节。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [IPSQM调整参数（IPSQMADJUST）](configobject/UDG/20.15.2/IPSQMADJUST.md)

## 关联任务

- [[UDG@20.15.2@Task@0-00233]]

## 使用实例

配置整形资源调整的业务处理节点（POD）的最低保护带宽及突发尺寸：

```
SET IPSQMADJUST: THRESHOLD=30, LOWBANDWIDTH=1000, LOWCBS=2000, HIGHBANDWIDTH=5000, HIGHCBS=10000;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/设置IPSQM调整参数（SET-IPSQMADJUST）_08873215.md`
