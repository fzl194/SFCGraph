---
id: UNC@20.15.2@MMLCommand@MOD GMLCCLIENT
type: MMLCommand
name: MOD GMLCCLIENT（修改GMLC和LCS Client对照关系）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: GMLCCLIENT
command_category: 配置类
applicable_nf:
- SGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 业务安全管理
- LCS
- GMLC和LCS Client对照表
status: active
---

# MOD GMLCCLIENT（修改GMLC和LCS Client对照关系）

## 功能

**适用网元：SGSN**

该命令用于修改GMLC和LCS CLIENT的对照关系。可选参数没有输入时该参数保持原有值不变。

## 注意事项

- 此命令执行后立即生效。
- 待修改的LCS CLIENT的号码必须已经在GMLC和LCS CLIENT对照表中存在。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CLIENTNUM | LCS客户端号码 | 可选必选说明：必选参数<br>参数含义：该参数用于指定LCS Client Number，是LCS客户端的E.164地址。<br>数据来源：整网规划<br>取值范围：1～16位十进制数字<br>默认值：无 |
| GMLCNUM | GMLC号码 | 可选必选说明：可选参数<br>参数含义：该参数用于指定GMLC号码。<br>数据来源：整网规划<br>取值范围：1～16位十进制数<br>默认值：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@GMLCCLIENT]] · GMLC和LCS Client对照关系（GMLCCLIENT）

## 使用实例

修改号码为861380123456789的LCS CLIENT对应的GMLC的号码为"861391123456789"：

MOD GMLCCLIENT: CLIENTNUM="861380123456789", GMLCNUM="861391123456789";

## 证据

- 原始手册：`evidence/UNC/20.15.2/MOD-GMLCCLIENT.md`
