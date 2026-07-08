---
id: UDG@20.15.2@MMLCommand@RMV IFL2FLOWMODE
type: MMLCommand
name: RMV IFL2FLOWMODE（删除主接口二层透传模式）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: IFL2FLOWMODE
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 接口管理
- 流模式配置
status: active
---

# RMV IFL2FLOWMODE（删除主接口二层透传模式）

## 功能

该命令用来删除接口的二层透传模式。

## 注意事项

- 该命令执行后立即生效。
- 该命令会将接口的转发模式从二层透传修改三层转发，同时接口下其他配置会开始生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IFNAME | 接口名称 | 可选必选说明：必选参数<br>参数含义：接口名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～47。<br>默认值：无<br>配置原则：请使用LST INTERFACE命令查看可用接口。 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@IFL2FLOWMODE]] · 主接口二层透传模式（IFL2FLOWMODE）

## 使用实例

删除指定主接口的二层透传模式：

```
RMV IFL2FLOWMODE:IFNAME="Ethernet66/0/5";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/RMV-IFL2FLOWMODE.md`
