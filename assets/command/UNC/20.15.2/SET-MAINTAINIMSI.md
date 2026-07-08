---
id: UNC@20.15.2@MMLCommand@SET MAINTAINIMSI
type: MMLCommand
name: SET MAINTAINIMSI（设置在线承载为保留承载）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: MAINTAINIMSI
command_category: 配置类
applicable_nf:
- PGW-C
- SGW-C
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- 网络管理
- 业务快速恢复
- 将指定在线承载变为保留承载
status: active
---

# SET MAINTAINIMSI（设置在线承载为保留承载）

## 功能

**适用NF：PGW-C、SGW-C**

该命令用于将指定的已经激活的并且支持MME Restoration功能或者支持SGW Restoration承载转变为保留承载。当现网调测MME故障恢复功能时在SGW-C上执行或者在调测SGW-C故障恢复功能时在PGW-C上执行。

## 注意事项

- 该命令执行后立即生效。

- 如果执行该命令时系统已经有指定IMSI的承载，则系统会将承载所属的PDN连接转变为保留承载。
- 如果执行该命令时系统没有指定的IMSI的承载，则保留承载操作失败。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IMSI | 用户IMSI号 | 可选必选说明：可选参数<br>参数含义：指定待转变为保留承载的用户的IMSI号。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~15。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST MAINTAINIMSI查询当前参数配置值。<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@MAINTAINIMSI]] · 在线承载为保留承载（MAINTAINIMSI）

## 使用实例

假设用户需要指定IMSI号为460000100000的用户保留承载：

```
SET MAINTAINIMSI:IMSI="460000100000";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/SET-MAINTAINIMSI.md`
