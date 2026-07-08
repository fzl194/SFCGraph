---
id: UNC@20.15.2@MMLCommand@RMV SRVNODEIP
type: MMLCommand
name: RMV SRVNODEIP（删除服务节点IP）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: SRVNODEIP
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
- 服务节点组的服务节点IP段
status: active
---

# RMV SRVNODEIP（删除服务节点IP）

## 功能

**适用NF：PGW-C、GGSN**

该命令用来删除服务节点组内绑定的服务节点IP地址段。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| GROUPNAME | 服务节点组名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定服务节点组名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~32。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：<br>本参数通过ADD SRVNODEGROUP命令进行配置。 |
| IPSECTIONID | 服务节点IP地址段编号 | 可选必选说明：必选参数<br>参数含义：该参数用于指定服务节点IP地址段的编号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~2999。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/SRVNODEIP]] · 服务节点IP（SRVNODEIP）

## 使用实例

当需要删除服务节点组内绑定的服务节点IP地址段时，使用如下命令：

```
RMV SRVNODEIP:GROUPNAME="huawei",IPSECTIONID=1;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-SRVNODEIP.md`
