---
id: UDG@20.15.2@MMLCommand@ADD MCASTGRPMEM
type: MMLCommand
name: ADD MCASTGRPMEM（增加组播组成员配置）
nf: UDG
version: 20.15.2
verb: ADD
object_keyword: MCASTGRPMEM
command_category: 配置类
applicable_nf:
- UPF
effect_mode: 立即生效
is_dangerous: false
max_records: 16384
category_path:
- 用户面服务管理
- 5G LAN管理
- 5G LAN静态组播配置
- 组播组成员配置
status: active
---

# ADD MCASTGRPMEM（增加组播组成员配置）

## 功能

**适用NF：UPF**

该命令用于增加静态组播组内成员。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为16384。
- 该静态组播组必须在MulticastGrp记录里存在。
- 单个静态组播组最多添加64个IMSI、32个双发选收结对、8个VTEP或者1个以太PDN。
- IMSI绑定到静态组播组时，如果该IMSI和静态组播组绑定的双发选收结对中的IMSI重复，则绑定失败。
- 双发选收结对绑定到静态组播组时，如果双发选收结对中的IMSI和静态组播组中绑定的IMSI重复，绑定失败。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MCASTGRPNAME | 组播组名称 | 可选必选说明：必选参数<br>参数含义：该参数用于配置组播组的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63，区分大小写。<br>默认值：无<br>配置原则：无 |
| MEMTYPE | 成员类型 | 可选必选说明：可选参数<br>参数含义：该参数用于配置成员类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- IMSI：IMSI。<br>- VTEP：VTEP。<br>- DFSRPAIR：双发选收结对。<br>- ETHERNETPDN：以太PDN。<br>默认值：IMSI<br>配置原则：无 |
| IMSI | IMSI | 可选必选说明：条件必选参数<br>前提条件：该参数在“MEMTYPE”配置为“IMSI”时为必选参数。<br>参数含义：组播组成员IMSI。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～15，每个字符必须为0~9的数字。<br>默认值：无<br>配置原则：无 |
| VTEPNAME | VXLAN隧道端点名称 | 可选必选说明：条件必选参数<br>前提条件：该参数在“MEMTYPE”配置为“VTEP”时为必选参数。<br>参数含义：该参数用于配置VXLAN隧道端点名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不区分大小写，不支持空格。<br>默认值：无<br>配置原则：无 |
| DFSRPAIRID | 双发选收结对ID | 可选必选说明：条件必选参数<br>前提条件：该参数在“MEMTYPE”配置为“DFSRPAIR”时为必选参数。<br>参数含义：该参数用于配置双发选收结对ID。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～2048。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [组播组成员配置（MCASTGRPMEM）](configobject/UDG/20.15.2/MCASTGRPMEM.md)

## 使用实例

增加静态组播组成员配置：

```
ADD MCASTGRPMEM: MCASTGRPNAME="group1", MEMTYPE=IMSI, IMSI="217456789012353";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/增加组播组成员配置（ADD-MCASTGRPMEM）_15950656.md`
