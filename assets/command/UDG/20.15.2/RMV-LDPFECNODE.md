---
id: UDG@20.15.2@MMLCommand@RMV LDPFECNODE
type: MMLCommand
name: RMV LDPFECNODE（删除FEC节点）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: LDPFECNODE
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- MPLS管理
- LDP管理
- LDP FEC节点
status: active
---

# RMV LDPFECNODE（删除FEC节点）

## 功能

该命令用于删除FEC节点。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| FECLISTNAME | FEC列表名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定FEC列表的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无 |
| IPADDRESS | IP地址 | 可选必选说明：必选参数<br>参数含义：该参数用于指定FEC的IP地址。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/LDPFECNODE]] · FEC节点（LDPFECNODE）

## 使用实例

删除FEC节点：

```
RMV LDPFECNODE:FECLISTNAME="name1",IPADDRESS="192.168.1.1";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/删除FEC节点（RMV-LDPFECNODE）_49961710.md`
