---
id: UNC@20.15.2@MMLCommand@ADD SRVNODEGROUP
type: MMLCommand
name: ADD SRVNODEGROUP（增加服务节点组）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: SRVNODEGROUP
command_category: 配置类
applicable_nf:
- PGW-C
- GGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- 虚拟APN映射管理
- 基于对接IP地址的虚拟APN映射管理
- 虚拟APN映射的服务节点组
status: active
---

# ADD SRVNODEGROUP（增加服务节点组）

## 功能

**适用NF：PGW-C、GGSN**

该命令用来添加一个新的服务节点组。当需要用SGSN IP、SGW IP、PCF IP进行虚拟APN映射时，在不同的场景下需要使用该命令添加SGSN/SGW/PCF新的服务节点组，可以在该服务节点组下绑定服务节点IP地址。

## 注意事项

- 该命令执行后立即生效。

- 最多可输入3000条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| GROUPNAME | 服务节点组名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定服务节点组名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~32。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/SRVNODEGROUP]] · 服务节点组（SRVNODEGROUP）

## 使用实例

在根据SGSN IP进行虚拟APN映射的时候，需要配置一个服务节点组，名称为“huawei”：

```
ADD SRVNODEGROUP:GROUPNAME="huawei";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加服务节点组（ADD-SRVNODEGROUP）_09651376.md`
