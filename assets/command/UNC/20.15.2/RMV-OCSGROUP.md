---
id: UNC@20.15.2@MMLCommand@RMV OCSGROUP
type: MMLCommand
name: RMV OCSGROUP（删除Ocs组）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: OCSGROUP
command_category: 配置类
applicable_nf:
- PGW-C
- SMF
effect_mode: 立即生效
is_dangerous: true
category_path:
- 业务服务管理
- 会话管理
- 计费管理
- 在线计费
- OCS Diameter连接
- OCS Group
status: active
---

# RMV OCSGROUP（删除Ocs组）

## 功能

**适用NF：PGW-C、SMF**

![](删除Ocs组（RMV OCSGROUP）_09896960.assets/notice_3.0-zh-cn_2.png)

该命令属于高危命令，如果不输入OCS组名称，表示删除系统内的所有OCS组，可能会导致用户在激活时因选不到OCS失败，不允许批量删除操作。如果需要执行此类操作，应将BYTE976的值设置为169。

此命令用来删除指定的OCS组。

## 注意事项

- 该命令执行后立即生效。
- 删除指定OCS组，删除时必须要指定OCS组的名字。
- 删除OCS组，输入一个不存在的OCS组的名子时，会提示删除失败。
- 如果OCS组绑在DCC模板下，删除时则提示删除失败。
- 删除后会导致在线计费失败。
- 如果UNC当前选择的ADD OCS命令配置的OCS状态正常，则UNC可以继续和配置的OCS进行交互。
- 如果UNC当前选择的ADD OCS命令配置的OCS状态异常，则UNC无法在删除的OCS组内重新选择ADD OCS命令配置的OCS。
- 如果要使用该OCS组则必须绑定到DCC TEMPLATE模板下。
- 该命令属于高危命令，不允许批量删除操作。如果需要执行此类操作，应将BYTE976的值设置为169。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| OCSGRPNAME | Ocs组名称 | 可选必选说明：必选参数<br>参数含义：ocs组的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@OCSGROUP]] · Ocs组（OCSGROUP）

## 使用实例

删除OCS组ocsgroup1的配置： OcsGrpName为ocsgroup1：

```
RMV OCSGROUP:OCSGRPNAME="OcsGroup1";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-OCSGROUP.md`
