---
id: UNC@20.15.2@MMLCommand@ADD GMLCCLIENT
type: MMLCommand
name: ADD GMLCCLIENT（增加GMLC和LCS Client对照关系）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: GMLCCLIENT
command_category: 配置类
applicable_nf:
- SGSN
effect_mode: 立即生效
is_dangerous: false
max_records: 8192
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 业务安全管理
- LCS
- GMLC和LCS Client对照表
status: active
---

# ADD GMLCCLIENT（增加GMLC和LCS Client对照关系）

## 功能

**适用网元：SGSN**

此命令用于增加GMLC和LCS CLIENT的对照关系。在移动始发的位置业务中，SGSN根据手机发送信息中携带的LCS CLIENT信息，查询此表，获得对应的GMLC。

## 注意事项

- 此命令执行后立即生效。
- 此命令最大记录数是8192。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CLIENTNUM | LCS客户端号码 | 可选必选说明：必选参数<br>参数含义：该参数用于指定LCS Client Number，是LCS客户端的E.164地址。<br>数据来源：整网规划<br>取值范围：1～16位十进制数字<br>默认值：无<br>配置原则：一个LCS CLIENT号码只能对应一个GMLC号码，但一个GMLC号码可以与多个LCS CLIENT号码对应。 |
| GMLCNUM | GMLC号码 | 可选必选说明：必选参数<br>参数含义：该参数用于指定GMLC号码。<br>数据来源：整网规划<br>取值范围：1～16位十进制数<br>默认值：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@GMLCCLIENT]] · GMLC和LCS Client对照关系（GMLCCLIENT）

## 使用实例

增加GMLC和LCS CLIENT的对照关系，LCS CLIENT的号码为861380123456789，GMLC的号码为861390123456789：

ADD GMLCCLIENT: CLIENTNUM="861380123456789", GMLCNUM="861390123456789";

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-GMLCCLIENT.md`
