---
id: UNC@20.15.2@MMLCommand@RMV LDPFECLIST
type: MMLCommand
name: RMV LDPFECLIST（删除FEC列表）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: LDPFECLIST
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- MPLS管理
- LDP管理
- LDP FEC列表
status: active
---

# RMV LDPFECLIST（删除FEC列表）

## 功能

该命令用于删除FEC列表。

## 注意事项

- 该命令执行后立即生效。
- 删除FEC列表会同时删除该列表中的FEC节点。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| FECLISTNAME | FEC列表名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定FEC列表的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@LDPFECLIST]] · FEC列表（LDPFECLIST）

## 使用实例

删除FEC列表：

```
RMV LDPFECLIST:FECLISTNAME="name1";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-LDPFECLIST.md`
