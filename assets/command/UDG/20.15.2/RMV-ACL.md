---
id: UDG@20.15.2@MMLCommand@RMV ACL
type: MMLCommand
name: RMV ACL（删除ACL）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: ACL
command_category: 配置类
applicable_nf:
- SGW-U
- PGW-U
- UPF
effect_mode: ''
is_dangerous: true
category_path:
- 用户面服务管理
- 业务安全防护
- 用户ACL管理
- ACL
status: active
---

# RMV ACL（删除ACL）

## 功能

**适用NF：SGW-U、PGW-U、UPF**

![](删除ACL（RMV ACL）_82837749.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，操作不当会导致性能下降明显，请谨慎使用并联系华为技术支持协助操作。

该命令用于删除系统当前所有的ACL名称或删除一条指定的ACL名称。

## 注意事项

- 指定删除的ACL名称必须是已配置的。
- 当ACL被绑定在APN或者被指定为缺省的ACL时则不允许删除，需先解除绑定关系。
- Acl配置修改后，在执行SET REFRESHSRV命令30s后生效。建议该操作在对所有ACL的配置修改完成后执行。
- 操作不当会导致性能下降明显，请谨慎使用并联系华为技术支持协助操作。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ACLNAME | ACL名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定ACL名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@ACL]] · ACL（ACL）

## 使用实例

- 假如运营商需要删除ACL名称为“testacl1”的配置，且该ACL未和APN绑定或被指定为缺省的ACL：
  ```
  RMV ACL: ACLNAME="testacl1";
  ```
- 假如运营商要删除当前系统的所有ACL名称配置：
  ```
  RMV ACL: ;
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/RMV-ACL.md`
