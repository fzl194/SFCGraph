---
id: UDG@20.15.2@MMLCommand@RMV UPDIAMAAABNDG
type: MMLCommand
name: RMV UPDIAMAAABNDG（删除Diameter AAA服务器组里的Diameter AAA服务器）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: UPDIAMAAABNDG
command_category: 配置类
applicable_nf:
- UPF
effect_mode: 立即生效
is_dangerous: true
category_path:
- 用户面服务管理
- Diameter AAA管理
- 服务器配置
- Diameter AAA服务器和Diameter AAA服务器组的绑定关系
status: active
---

# RMV UPDIAMAAABNDG（删除Diameter AAA服务器组里的Diameter AAA服务器）

## 功能

**适用NF：UPF**

![](删除Diameter AAA服务器组里的Diameter AAA服务器（RMV UPDIAMAAABNDG）_45432716.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，该操作会删除Diameter AAA组下的Diameter AAA服务器，可能会导致新激活用户无可用Diameter AAA服务器而激活失败。

此命令用于从Diameter AAA组删除指定的Diameter AAA服务器或者所有的Diameter AAA服务器。当新建立的会话不再需要到某个Diameter AAA鉴权时，操作员可以执行此命令解除该绑定关系。

## 注意事项

- 该命令执行后立即生效。
- 对于同一个服务器组，添加记录时，请先添加主用服务器再添加备用服务器；删除记录时，请先删除备用服务器再删除主用服务器。
- Diameter AAA从组内移除，并不影响已经建立的会话状态，该激活用户的后续鉴权操作仍然经由该Diameter AAA处理，直到会话释放。
- 当Diameter AAA从指定组移除后，如果该组内剩下的Diameter AAA都不可用，将导致后续新建立并且关联到该Diameter AAA组的会话鉴权失败。Diameter AAA组下的绑定配置全部被删除之后的结果与此相同。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| GROUPNAME | Diameter AAA组名 | 可选必选说明：必选参数<br>参数含义：该参数用于指定Diameter AAA组名。<br>数据来源：本端规划<br>取值范围：不区分大小写，不支持空格。<br>默认值：无<br>配置原则：该参数使用ADD UPDIAMAAAGRP命令配置生成。 |
| SERVERTYPE | 服务器类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定服务器类型。<br>数据来源：本端规划<br>取值范围：<br>- PARA_3GPP：表示使用遵循3GPP协议的服务器。<br>默认值：无<br>配置原则：无 |
| HOSTNAME | 主机名 | 可选必选说明：可选参数<br>参数含义：该参数用于指定Diameter AAA。<br>数据来源：全网规划<br>取值范围：只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”等特殊字符，由软参BIT2670控制是否区分大小写。BIT2670值为0时，不区分大小写；值为1时，区分大小写，但不允许配置多个仅大小写不同的host-name或realm-name。<br>默认值：无<br>配置原则：该参数使用ADD UPDIAMETERAAA命令配置生成。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/UPDIAMAAABNDG]] · Diameter AAA服务器组里的Diameter AAA服务器（UPDIAMAAABNDG）

## 使用实例

- 根据网络规划，从名称为“diametergroup”的Diameter AAA组中删除名称为“diameteraaa1”的Diameter AAA服务器：
  ```
  RMV UPDIAMAAABNDG:GROUPNAME="diametergroup",HOSTNAME="diameteraaa1";
  ```
- 根据网络规划，从名称为“diametergroup”的Diameter AAA组中删除所有Diameter AAA服务器：
  ```
  RMV UPDIAMAAABNDG:GROUPNAME="diametergroup";
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/删除Diameter-AAA服务器组里的Diameter-AAA服务器（RMV-UPDIAMAAABNDG）_45432716.md`
