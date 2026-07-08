---
id: UDG@20.15.2@MMLCommand@ADD ACL
type: MMLCommand
name: ADD ACL（增加ACL）
nf: UDG
version: 20.15.2
verb: ADD
object_keyword: ACL
command_category: 配置类
applicable_nf:
- SGW-U
- PGW-U
- UPF
effect_mode: ''
is_dangerous: true
max_records: 5000
category_path:
- 用户面服务管理
- 业务安全防护
- 用户ACL管理
- ACL
status: active
---

# ADD ACL（增加ACL）

## 功能

**适用NF：SGW-U、PGW-U、UPF**

![](增加ACL（ADD ACL）_82837747.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，操作不当会导致性能下降明显，请谨慎使用并联系华为技术支持协助操作。

该命令用于有新的增加ACL需求情况下增加ACL名称及ACL节点的匹配方式。

## 注意事项

- 该命令最大记录数为5000。
- ACL配置增加后，在执行SET REFRESHSRV命令30s后才会生效。SET REFRESHSRV必须在对所有ACL的配置修改完成后执行。
- 操作不当会导致性能下降明显，请谨慎使用并联系华为技术支持协助操作。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ACLNAME | ACL名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定ACL名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |
| MATCHORDER | 匹配方式 | 可选必选说明：必选参数<br>参数含义：该参数用于设置ACL节点的匹配方式。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- AUTO：自动排序，即按照filter深度优先。<br>- CONFIG：按照ACL节点的优先级排序。<br>默认值：无<br>配置原则：<br>- 该参数配置为AUTO时，不能指定ACL下绑定的ACL节点的优先级。<br>- 该参数配置为CONFIG时，必须指定该ACL下绑定的ACL节点的优先级。可以通过ADD AclNodeBindAcl对优先级进行指定。 |
| CFGDOMAINNAME | 配置域名称 | 可选必选说明：可选参数<br>参数含义：该参数表示命令所属公共配置域的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/ACL]] · ACL（ACL）

## 使用实例

- 假如运营商需要增加一条ACL，其匹配方式为AUTO：
  ```
  ADD ACL: ACLNAME="testacl1",MATCHORDER=AUTO;
  ```
- 假如运营商需要增加一条ACL，其匹配方式为CONFIG：
  ```
  ADD ACL: ACLNAME="testacl2",MATCHORDER=CONFIG;
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/ADD-ACL.md`
