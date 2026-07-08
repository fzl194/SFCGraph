---
id: UNC@20.15.2@MMLCommand@MOD GTPPLOCINFO
type: MMLCommand
name: MOD GTPPLOCINFO（修改GTPP本端信息）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: GTPPLOCINFO
command_category: 配置类
applicable_nf:
- SGW-C
- PGW-C
- SMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 计费管理
- 离线计费
- GTPP信令
- GTPP本地信息
status: active
---

# MOD GTPPLOCINFO（修改GTPP本端信息）

## 功能

**适用NF：SGW-C、PGW-C、SMF**

该命令用来修改GTPP本端信息。

## 注意事项

- 该命令执行后立即生效。
- 当前版本不支持此命令。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| HOSTNAME | 本端主机名 | 可选必选说明：必选参数<br>参数含义：该参数用于指定本端主机名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格。<br>默认值：无<br>配置原则：无 |
| REALMNAME | 本端域名 | 可选必选说明：可选参数<br>参数含义：该参数用于指定本端域名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格。<br>默认值：无<br>配置原则：无 |
| SERVICECONTEXT | 业务上下文标识 | 可选必选说明：可选参数<br>参数含义：该参数用于标识业务上下文ID，业务上下文Id是业务定位文档的标识。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格。<br>默认值：无<br>配置原则：无 |
| LOCINTERFACE | 本端接口名 | 可选必选说明：必选参数<br>参数含义：该参数用于指定GTPP本端接口名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：该参数使用ADD LOGICINF命令配置生成。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@GTPPLOCINFO]] · GTPP本端信息（GTPPLOCINFO）

## 使用实例

修改GTPP本端信息，本端主机名为“test”，本端域名为“test”， 业务上下文标识为“abc”， 逻辑接口名称为“gaif1/0/1”：

```
MOD GTPPLOCINFO: HOSTNAME="test", REALMNAME="test", SERVICECONTEXT="abc", LOCINTERFACE="gaif1/0/1";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/MOD-GTPPLOCINFO.md`
