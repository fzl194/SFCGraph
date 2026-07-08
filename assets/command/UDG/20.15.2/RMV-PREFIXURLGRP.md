---
id: UDG@20.15.2@MMLCommand@RMV PREFIXURLGRP
type: MMLCommand
name: RMV PREFIXURLGRP（删除前缀URL组）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: PREFIXURLGRP
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
- 七层规则管理
- 前缀URL组
status: active
---

# RMV PREFIXURLGRP（删除前缀URL组）

## 功能

**适用NF：PGW-U、UPF**

![](删除前缀URL组（RMV PREFIXURLGRP）_82837403.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，可能会删除前缀URL组下所有绑定关系。

该命令删除所有的前缀URL组，或者删除指定名称的前缀URL组，或者删除前缀URL组中的指定前缀URL。

## 注意事项

- 如果只指定了前缀URL组名字，该命令执行后立即生效；如果指定了前缀URL，该命令执行后60s或配置恢复后60s生效。
- 如果前缀URL组被UserProfile绑定，删除时，需要将绑定关系解除。
- 删除操作要求：
    - 不允许只输入前缀URL参数。
    - 如果不输入任何参数，表示要删除所有的前缀URL组，删除前缀URL组下的前缀URL。
    - 如果只输入前缀URL组名称，表示要删除该前缀URL组，删除该前缀URL组下的前缀URL。
    - 如果同时输入前缀URL组名称和前缀URL，表示要删除前缀URL组下指定的前缀URL。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PREURLGRPNAME | 前缀URL组名字 | 可选必选说明：可选参数<br>参数含义：该参数用于指定前缀URL组名字。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不区分大小写。<br>默认值：无<br>配置原则：无 |
| PREFIXURL | 前缀URL | 可选必选说明：可选参数<br>参数含义：该参数用于指定前缀URL。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@PREFIXURLGRP]] · 前缀URL组（PREFIXURLGRP）

## 使用实例

- 删除前缀URL组，指定前缀URL组名称：PREURLGRPNAME为“testurlgroup”：
  ```
  RMV PREFIXURLGRP:PREURLGRPNAME="testurlgroup";
  ```
- 删除前缀URL组中指定前缀URL：PREURLGRPNAME为“testurlgroup”,PREFIXURL为“www.huawei.com”：
  ```
  RMV PREFIXURLGRP:PREURLGRPNAME="testurlgroup",PREFIXURL="www.huawei.com";
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/RMV-PREFIXURLGRP.md`
