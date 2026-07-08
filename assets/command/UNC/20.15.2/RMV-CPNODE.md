---
id: UNC@20.15.2@MMLCommand@RMV CPNODE
type: MMLCommand
name: RMV CPNODE（删除CP节点信息）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: CPNODE
command_category: 配置类
applicable_nf:
- SMF
- PGW-C
- SGW-C
- GGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- PFCP接口管理
- CP管理
- CP节点管理
status: active
---

# RMV CPNODE（删除CP节点信息）

## 功能

![](删除CP节点信息（RMV CPNODE）_09654398.assets/notice_3.0-zh-cn_2.png)

在执行此命令前必须先使用RMV CPPOINT命令删除所有相关CPPOINT。

删除CP节点会造成在此CP节点上建立的连接断开，造成会话中断。

**适用NF：SMF、PGW-C、SGW-C、GGSN**

该命令用于删除指定索引编号的CP节点。

## 注意事项

- 该命令执行后立即生效。

- 在执行此命令前必须先使用RMV CPPOINT命令删除所有相关CPPOINT。
- 删除CP节点会造成在此CP节点上建立的连接断开，造成会话中断。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CPNODEINDEX | CP节点索引 | 可选必选说明：必选参数<br>参数含义：该参数用于指定CP节点索引。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围为0。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [CP节点信息（CPNODE）](configobject/UNC/20.15.2/CPNODE.md)

## 使用实例

删除索引为0的CP节点：

```
RMV CPNODE:CPNODEINDEX=0;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除CP节点信息（RMV-CPNODE）_09654398.md`
