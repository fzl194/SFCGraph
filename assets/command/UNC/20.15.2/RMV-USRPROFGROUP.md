---
id: UNC@20.15.2@MMLCommand@RMV USRPROFGROUP
type: MMLCommand
name: RMV USRPROFGROUP（删除用户模板组）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: USRPROFGROUP
command_category: 配置类
applicable_nf:
- PGW-C
- SMF
effect_mode: 立即生效
is_dangerous: true
category_path:
- 业务服务管理
- 会话管理
- 计费和策略的业务管理
- 业务模板
- 用户模板组
status: active
---

# RMV USRPROFGROUP（删除用户模板组）

## 功能

**适用NF：PGW-C、SMF**

![](删除用户模板组（RMV USRPROFGROUP）_09897221.assets/notice_3.0-zh-cn_2.png)

本命令属于高危命令，如果不输入UsrProfGroup名称，表示删除系统内的所有UsrProfGroup，同时会删除此UsrProfGroup和所有UserProfile的绑定关系。删除后使用该UsrProfGroup的用户可能会因为无法命中UserProfile导致业务受损，请谨慎使用并联系华为支持协助操作。

此命令用于删除UsrProfGroup。如果指定UsrProfGroup名字，只删除该UsrProfGroup，如果没有指定UsrProfGroup名字，则删除系统内的所有UsrProfGroup。

## 注意事项

- 该命令执行后立即生效。
- 删除一个UsrProfGroup的同时会删除此UsrProfGroup下所有的和UserProfile的绑定关系。
- 如果UsrProfGroup已经绑定在APN下，则不允许删除，需要先解除绑定关系后再删除。
- 业务进行中删除UsrProfGroup时，如果有用户在使用此UsrProfGroup下绑定的UserProfile，则不允许删除。
- 业务进行中删除UsrProfGroup时，如果有AAA下发UsrProfGroup的用户使用此UsrProfGroup，则不允许删除。
- 该命令属于高危命令，不允许批量删除操作。如果需要执行此类操作，应将BYTE976的值设置为169。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| USERPROFGNAME | 用户模板组名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定用户模板组的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/USRPROFGROUP]] · 用户模板组（USRPROFGROUP）

## 使用实例

删除指定名称的UsrProfGroup配置：

```
RMV USRPROFGROUP:USERPROFGNAME="userprofg1";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-USRPROFGROUP.md`
