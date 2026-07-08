---
id: UDG@20.15.2@MMLCommand@ADD ACLNODEBINDACL
type: MMLCommand
name: ADD ACLNODEBINDACL（增加Acl节点绑定关系）
nf: UDG
version: 20.15.2
verb: ADD
object_keyword: ACLNODEBINDACL
command_category: 配置类
applicable_nf:
- SGW-U
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
max_records: 10000
category_path:
- 用户面服务管理
- 业务安全防护
- 用户ACL管理
- ACL节点绑定ACL
status: active
---

# ADD ACLNODEBINDACL（增加Acl节点绑定关系）

## 功能

**适用NF：SGW-U、PGW-U、UPF**

该命令用于增加ACL节点和ACL的绑定关系。

基于APN做ACL业务控制的场景，需要将ACL节点绑定到ACL下，再将ACL绑定到APN下。这样用户接入在该APN下时，就可以使用ACL节点下配置的策略进行业务控制。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为10000。
- 每条ACL下可以绑定5000条ACL节点。系统整机支持最大的绑定规格是10000。
- 对于ACL为自动排序方式的，在绑定ACL节点时不需要指定优先级，如果指定了优先级，优先级也是无效的。
- ACL正在被使用时，可以继续往ACL上绑定ACL节点。
- ACL节点的动作类型需要与ACL下其他ACL节点的动作类型一致。
- 修改或删除ACL后需要执行SET REFRESHSRV使当前配置生效，建议该操作在对所有ACL的配置修改完成后执行。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ACLNAME | ACL名称 | 可选必选说明：必选参数<br>参数含义：该参数用于配置ACL名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：参数已通过ADD ACL命令配置，无需重新配置。 |
| ACLNODENAME | ACL节点名称 | 可选必选说明：必选参数<br>参数含义：该参数用于配置ACL节点名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：参数已通过ADD ACLNODE命令配置，无需重新配置。 |
| PRIORITY | 优先级 | 可选必选说明：可选参数<br>参数含义：该参数用于配置ACL节点的优先级。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～65535。<br>默认值：无<br>配置原则：<br>- 该参数的值越小优先级越高。<br>- 当ACL的MatchOrder配置方式为CONFIG时必须要配置优先级。 |

## 操作的配置对象

- [Acl节点绑定关系（ACLNODEBINDACL）](configobject/UDG/20.15.2/ACLNODEBINDACL.md)

## 使用实例

- 假如运营商需要在增加一个ACL节点绑定关系到ACL“testacl1”上，ACL为自动排序方式：
  ```
  ADD ACLNODEBINDACL: ACLNAME="testacl1",ACLNODENAME="testaclnode1";
  ```
- 假如运营商需要在增加一个ACL节点绑定关系到ACL“testacl2”上，ACL为优先级排序方式，优先级为25：
  ```
  ADD ACLNODEBINDACL: ACLNAME="testacl2",ACLNODENAME="testaclnode2",PRIORITY=25;
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/增加Acl节点绑定关系（ADD-ACLNODEBINDACL）_82837734.md`
