---
id: UDG@20.15.2@MMLCommand@RMV WELLKNOWNPORT
type: MMLCommand
name: RMV WELLKNOWNPORT（删除知名端口）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: WELLKNOWNPORT
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: true
category_path:
- 用户面服务管理
- 业务匹配策略
- 业务过滤器管理
- 三四层规则管理
- 知名端口
status: active
---

# RMV WELLKNOWNPORT（删除知名端口）

## 功能

**适用NF：PGW-U、UPF**

![](删除知名端口（RMV WELLKNOWNPORT）_82837334.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，不输入IdenProtName，会批量删除全部知名端口。

RMV WELLKNOWNPORT此命令用来删除指定知名端口或所有知名端口。

## 注意事项

- 该命令执行后立即生效。
- 删除知名端口的配置后，知名端口匹配失败，将使用特征字对报文进行协议识别。
- 输入IdenProtName删除指定知名端口，不输入IdenProtName删除全部知名端口。
- 该命令可以删除所有的IdenProtName，且协议识别可能会产生变化，导致计费、策略等发生改变，请确认删除影响客户可接受后，再进行操作。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IDENPROTNAME | 知名端口名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定指知名端口名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [知名端口（WELLKNOWNPORT）](configobject/UDG/20.15.2/WELLKNOWNPORT.md)

## 使用实例

删除WellKnownPort知名端口，“IDENPROTNAME”为“10086”：

```
RMV WELLKNOWNPORT:IDENPROTNAME="10086";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/删除知名端口（RMV-WELLKNOWNPORT）_82837334.md`
