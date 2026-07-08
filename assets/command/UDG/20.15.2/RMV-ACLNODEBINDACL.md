---
id: UDG@20.15.2@MMLCommand@RMV ACLNODEBINDACL
type: MMLCommand
name: RMV ACLNODEBINDACL（删除Acl节点绑定关系）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: ACLNODEBINDACL
command_category: 配置类
applicable_nf:
- SGW-U
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 用户面服务管理
- 业务安全防护
- 用户ACL管理
- ACL节点绑定ACL
status: active
---

# RMV ACLNODEBINDACL（删除Acl节点绑定关系）

## 功能

**适用NF：SGW-U、PGW-U、UPF**

该命令用于删除acl节点的绑定关系。支持删除指定的acl下的acl节点绑定关系，或者删除指定acl节点对应的绑定关系，或者删除当前所有的acl节点的绑定关系。

## 注意事项

- 该命令执行后立即生效。
- ACL正在被使用时，允许解除ACL与其中某个ACL节点的绑定关系。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ACLNAME | ACL名称 | 可选必选说明：可选参数<br>参数含义：该参数用于配置ACL名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |
| ACLNODENAME | ACL节点名称 | 可选必选说明：可选参数<br>参数含义：该参数用于配置ACL节点名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [Acl节点绑定关系（ACLNODEBINDACL）](configobject/UDG/20.15.2/ACLNODEBINDACL.md)

## 使用实例

- 假如运营商需要删除ACL为“testacl1”下ACL节点为“testaclnode1”的绑定关系：
  ```
  RMV ACLNODEBINDACL: ACLNAME="testacl1",ACLNODENAME="testaclnode1";
  ```
- 假如运营线需要删除ACL为“testacl1”下的所有节点绑定关系：
  ```
  RMV ACLNODEBINDACL: ACLNAME="testacl1";
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/删除Acl节点绑定关系（RMV-ACLNODEBINDACL）_82837736.md`
