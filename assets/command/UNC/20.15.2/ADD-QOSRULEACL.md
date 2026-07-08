---
id: UNC@20.15.2@MMLCommand@ADD QOSRULEACL
type: MMLCommand
name: ADD QOSRULEACL（流分类下增加ACL规则组）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: QOSRULEACL
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
max_records: 65536
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 安全管理
- QoS管理
- ACL规则
status: active
---

# ADD QOSRULEACL（流分类下增加ACL规则组）

## 功能

该命令用来配置基于IPv4或IPv6的ACL规则进行复杂流分类的匹配规则；当某个接口需要根据接收报文的源IP、目的IP、源端口、目的端口和协议类型对报文进行分类时，可以对该接口通过引用定义的ACL来满足。即先定义ACL以及配置规则，然后在流分类下配置该命令实现复杂流分类。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为65536。
- 该命令虽然引用了ACL规则，但在ACL规则匹配计数中不统计。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CLASSIFIERNAME | 分类名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定流分类名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无<br>配置原则：<br>- 区分大小写，不支持空格。<br>- 需要先使用ADD MQCCLASSIFIER命令配置流分类。 |
| IPVERSION | IP协议版本 | 可选必选说明：必选参数<br>参数含义：该参数用于指定ACL规则的IP协议版本。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- IPv4：IPv4类型。<br>- IPv6：IPv6类型。<br>默认值：无 |
| ACLTYPE | ACL类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定ACL规则的类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- acl-number：ACL编号。<br>- acl-name：ACL名称。<br>默认值：无 |
| ACLNUM | ACL编号 | 可选必选说明：条件必选参数<br>前提条件：该参数在“ACLTYPE”配置为“acl-number”时为必选参数。<br>参数含义：该参数用于指定基于IPv4或IPv6的ACL编号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为2000～4999。<br>默认值：无<br>配置原则：需要先使用ADD ACLGROUP命令配置ACL规则组，如果ADD ACLGROUP命令的ACLNAME参数是整数形式，则基于编号增加ACL规则组。 |
| ACLNAME | ACL名称 | 可选必选说明：条件必选参数<br>前提条件：该参数在“ACLTYPE”配置为“acl-name”时为必选参数。<br>参数含义：该参数用于指定基于IPv4或IPv6的ACL名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～32。<br>默认值：无<br>配置原则：<br>- 区分大小写，不支持空格。<br>- 需要先使用ADD ACLGROUP命令配置ACL规则组，如果ADD ACLGROUP命令的ACLNAME参数是字符串形式，则基于名称增加ACL规则组。 |

## 操作的配置对象

- [流分类下删除ACL规则组（QOSRULEACL）](configobject/UNC/20.15.2/QOSRULEACL.md)

## 使用实例

- 在流分类c1上配置基于名称acl1的IPv4 ACL规则：
  ```
  ADD QOSRULEACL: CLASSIFIERNAME="c1",IPVERSION=IPv4,ACLTYPE=acl-name,ACLNAME="acl1";
  ```
- 在流分类c1上配置基于编号2001的IPv6 ACL规则：
  ```
  ADD QOSRULEACL: CLASSIFIERNAME="c1",IPVERSION=IPv6,ACLTYPE=acl-number,ACLNUM=2001;
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/流分类下增加ACL规则组（ADD-QOSRULEACL）_00600841.md`
