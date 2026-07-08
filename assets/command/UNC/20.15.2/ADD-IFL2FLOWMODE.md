---
id: UNC@20.15.2@MMLCommand@ADD IFL2FLOWMODE
type: MMLCommand
name: ADD IFL2FLOWMODE（配置主接口二层透传模式）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: IFL2FLOWMODE
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
max_records: 7
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 接口管理
- 流模式配置
status: active
---

# ADD IFL2FLOWMODE（配置主接口二层透传模式）

## 功能

该命令用来配置接口的二层透传模式。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为7。
- 该命令目前只支持主接口配置，不支持子接口。
- 配置该命令后，接口下配置的其它命令将不生效，转发不再走3层转发流程，而走2层透传。
- 入接口和出接口均需要配置该命令，这样才能实现报文透传。
- 同一个VPN不能同时绑定多个配置了该命令的接口。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IFNAME | 接口名称 | 可选必选说明：必选参数<br>参数含义：接口名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～47。<br>默认值：无<br>配置原则：请使用LST INTERFACE命令查看可用接口。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/IFL2FLOWMODE]] · 主接口二层透传模式（IFL2FLOWMODE）

## 使用实例

配置指定主接口的二层透传模式：

```
ADD IFL2FLOWMODE:IFNAME="Ethernet66/0/5";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/配置主接口二层透传模式（ADD-IFL2FLOWMODE）_50121690.md`
