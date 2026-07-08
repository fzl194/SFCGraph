---
id: UNC@20.15.2@MMLCommand@RMV QOSRULEACL
type: MMLCommand
name: RMV QOSRULEACL（流分类下删除ACL规则组）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: QOSRULEACL
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 安全管理
- QoS管理
- ACL规则
status: active
---

# RMV QOSRULEACL（流分类下删除ACL规则组）

## 功能

该命令用来删除流分类下配置的ACL匹配规则。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CLASSIFIERNAME | 分类名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定流分类名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无<br>配置原则：区分大小写，不支持空格。 |
| IPVERSION | IP协议版本 | 可选必选说明：必选参数<br>参数含义：该参数用于指定ACL规则的IP协议版本。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- IPv4：IPv4类型。<br>- IPv6：IPv6类型。<br>默认值：无 |
| ACLTYPE | ACL类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定ACL规则的类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- acl-number：ACL编号。<br>- acl-name：ACL名称。<br>默认值：无 |
| ACLNUM | ACL编号 | 可选必选说明：条件必选参数<br>前提条件：该参数在“ACLTYPE”配置为“acl-number”时为必选参数。<br>参数含义：该参数用于指定基于IPv4或IPv6的ACL编号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为2000～4999。<br>默认值：无 |
| ACLNAME | ACL名称 | 可选必选说明：条件必选参数<br>前提条件：该参数在“ACLTYPE”配置为“acl-name”时为必选参数。<br>参数含义：该参数用于指定基于IPv4或IPv6的ACL名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～32。<br>默认值：无<br>配置原则：区分大小写，不支持空格。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@QOSRULEACL]] · 流分类下删除ACL规则组（QOSRULEACL）

## 使用实例

- 删除在流分类c1上配置基于名称acl1的IPv4 ACL规则：
  ```
  RMV QOSRULEACL: CLASSIFIERNAME="c1",IPVERSION=IPv4,ACLTYPE=acl-name,ACLNAME="acl1";
  ```
- 删除在流分类c1上配置基于编号2001的IPv6 ACL规则：
  ```
  RMV QOSRULEACL: CLASSIFIERNAME="c1",IPVERSION=IPv6,ACLTYPE=acl-number,ACLNUM=2001;
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-QOSRULEACL.md`
