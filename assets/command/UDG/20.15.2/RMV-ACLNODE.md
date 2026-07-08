---
id: UDG@20.15.2@MMLCommand@RMV ACLNODE
type: MMLCommand
name: RMV ACLNODE（删除ACL节点）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: ACLNODE
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
- ACL节点
status: active
---

# RMV ACLNODE（删除ACL节点）

## 功能

**适用NF：SGW-U、PGW-U、UPF**

![](删除ACL节点（RMV ACLNODE）_82837731.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，操作不当会导致性能下降明显，请谨慎使用并联系华为技术支持协助操作。

该命令用于删除所有ACL节点配置，或者根据ACL节点名称删除指定的ACL节点配置。

## 注意事项

- ACL节点配置删除后，在执行SET REFRESHSRV命令30s后生效。建议该操作在对所有ACL节点的配置完成后执行。
- 在现网中配置ACL节点后，如果用户正在使用，则不允许被删除。
- 操作不当会导致性能下降明显，请谨慎使用并联系华为技术支持协助操作。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ACLNODENAME | ACL节点名称 | 可选必选说明：可选参数<br>参数含义：该参数用于配置ACL节点名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@ACLNODE]] · ACL节点（ACLNODE）

## 使用实例

- 假如运营商需要删除ACL节点名称为“testaclnode1”的配置：
  ```
  RMV ACLNODE: ACLNODENAME="testaclnode1";
  ```
- 假如运营商需要删除所有ACL节点配置：
  ```
  RMV ACLNODE: ;
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/RMV-ACLNODE.md`
