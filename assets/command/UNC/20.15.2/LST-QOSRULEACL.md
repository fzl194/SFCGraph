---
id: UNC@20.15.2@MMLCommand@LST QOSRULEACL
type: MMLCommand
name: LST QOSRULEACL（流分类下查询ACL规则组）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: QOSRULEACL
command_category: 查询类
effect_mode: ''
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

# LST QOSRULEACL（流分类下查询ACL规则组）

## 功能

该命令用来查询流分类下配置的所有ACL匹配规则。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CLASSIFIERNAME | 分类名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定流分类名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无<br>配置原则：区分大小写，不支持空格。 |
| IPVERSION | IP协议版本 | 可选必选说明：可选参数<br>参数含义：该参数用于指定ACL规则的IP协议版本。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- IPv4：IPv4类型。<br>- IPv6：IPv6类型。<br>默认值：无 |
| ACLNAME | ACL名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定基于IPv4或IPv6的ACL名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～32。<br>默认值：无<br>配置原则：区分大小写，不支持空格。 |
| ACLNUM | ACL编号 | 可选必选说明：可选参数<br>参数含义：该参数用于指定基于IPv4或IPv6的ACL编号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为2000～4999。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/QOSRULEACL]] · 流分类下删除ACL规则组（QOSRULEACL）

## 使用实例

查询当前所有在流分类下配置的ACL规则：

```
LST QOSRULEACL:;
```

```

RETCODE = 0  操作成功

结果如下
-------------------------
分类名称    IP协议版本     ACL名称     ACL编号   
c1          IPv4           acl1        0          
c1          IPv6           NULL        2001       
(结果个数 = 2)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-QOSRULEACL.md`
