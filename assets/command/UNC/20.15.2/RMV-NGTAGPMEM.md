---
id: UNC@20.15.2@MMLCommand@RMV NGTAGPMEM
type: MMLCommand
name: RMV NGTAGPMEM（删除5G TA群组成员）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: NGTAGPMEM
command_category: 配置类
applicable_nf:
- AMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- N2接口管理
- NGRAN跟踪区管理
- NGRAN跟踪区群组成员管理
status: active
---

# RMV NGTAGPMEM（删除5G TA群组成员）

## 功能

**适用NF：AMF**

该命令用于删除跟踪区群组成员记录。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NGTAGPID | 跟踪区群组标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定跟踪区群组标识。该参数已经通过ADD NGTAGP命令中的NGTAGPID参数配置。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~256。“跟踪区群组标识”已经通过ADD NGTAGP配置。<br>默认值：无<br>配置原则：无 |
| BGNTAC | 跟踪区编码起始值 | 可选必选说明：必选参数<br>参数含义：该参数用于表示跟踪区编码的起始值。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度是6。TAC编码为16进制数，按照字符串格式输入，字符串长度为6，只能由数字（0-9），字母（A-F、a-f）组成。字母大小写不敏感。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [5G TA群组成员（NGTAGPMEM）](configobject/UNC/20.15.2/NGTAGPMEM.md)

## 使用实例

删除一个TA群组成员，TA群组标识为1，群组成员的跟踪区域码为123456。

```
RMV NGTAGPMEM: NGTAGPID=1, BGNTAC="123456";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除5G-TA群组成员（RMV-NGTAGPMEM）_09572746.md`
