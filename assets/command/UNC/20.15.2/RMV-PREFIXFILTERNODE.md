---
id: UNC@20.15.2@MMLCommand@RMV PREFIXFILTERNODE
type: MMLCommand
name: RMV PREFIXFILTERNODE（删除IPv4地址前缀列表过滤器节点）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: PREFIXFILTERNODE
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- 路由策略管理
- IP前缀列表
status: active
---

# RMV PREFIXFILTERNODE（删除IPv4地址前缀列表过滤器节点）

## 功能

该命令用于删除前缀过滤器相关属性。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NAME | IP前缀列表名字 | 可选必选说明：必选参数<br>参数含义：该参数用于指定IP前缀列表名字。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～169。<br>默认值：无 |
| NODESEQUENCE | IP前缀列表节点号 | 可选必选说明：可选参数<br>参数含义：该参数用于指定IP前缀列表节点号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～4294967295。<br>默认值：无<br>配置原则：当不输入此参数时，删除所有节点。 |

## 操作的配置对象

- [IPv4地址前缀列表过滤器节点（PREFIXFILTERNODE）](configobject/UNC/20.15.2/PREFIXFILTERNODE.md)

## 使用实例

删除前缀过滤器节点，前缀过滤器名字是a，节点号为1：

```
RMV PREFIXFILTERNODE:NAME="a",NODESEQUENCE=1;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除IPv4地址前缀列表过滤器节点（RMV-PREFIXFILTERNODE）_00600889.md`
