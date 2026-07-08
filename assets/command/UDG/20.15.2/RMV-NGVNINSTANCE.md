---
id: UDG@20.15.2@MMLCommand@RMV NGVNINSTANCE
type: MMLCommand
name: RMV NGVNINSTANCE（删除5G VNInstance的配置）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: NGVNINSTANCE
command_category: 配置类
applicable_nf:
- UPF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 用户面服务管理
- 5G LAN管理
- 5G LAN基础配置
- 5G LAN实例配置
status: active
---

# RMV NGVNINSTANCE（删除5G VNInstance的配置）

## 功能

**适用NF：UPF**

该命令用于删除一个5G LAN会话实例。

## 注意事项

- 该命令执行后立即生效。
- 当存在5G LAN组会话和UE会话的时候不允许删除该配置；删除该配置后，对应的5G LAN组会话及UE会话无法激活。
- 当存在静态组播组绑定5G LAN组会话实例时，不允许删除该配置。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VNINSTANCE | 5G LAN组名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定5G LAN组名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为18～37。VNINSTANCE以连字号分为4段，形式为GroupServiceID-MCC-MNC-LocalGroupID。其中，GroupServiceID长度为8，只能输入数字或者范围为A到F或a-f的字母；MCC长度为3，只能输入数字；MNC长度为2~3，只能输入数字；LocalGroupID长度为2~20的偶数，只能输入数字或者范围为A到F或a-f的字母。例如，A0000001-460-003-01，A0000001-460-003-A000000001。不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@NGVNINSTANCE]] · 5G VNInstance配置（NGVNINSTANCE）

## 使用实例

删除名为"A0000001-460-003-01"的实例：

```
RMV NGVNINSTANCE: VNINSTANCE="A0000001-460-003-01";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/RMV-NGVNINSTANCE.md`
