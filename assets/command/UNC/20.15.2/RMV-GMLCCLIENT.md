---
id: UNC@20.15.2@MMLCommand@RMV GMLCCLIENT
type: MMLCommand
name: RMV GMLCCLIENT（删除GMLC和LCS Client对照关系）
nf: UNC
version: 20.15.2
verb: RMV
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

# RMV GMLCCLIENT（删除GMLC和LCS Client对照关系）

## 功能

**适用网元：SGSN**

此命令用于删除GMLC和LCS CLIENT对照表中的GMLC和LCS CLIENT的对照关系。

## 注意事项

- 此命令执行后立即生效。
- 待删除的LCS CLIENT的号码必须在GMLC和LCS CLIENT对照表中存在。
- 移动始发的位置业务中，SGSN无法根据手机发送信息中携带的LCS CLIENT信息，对应的GMLC，导致定位流程失败。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CLIENTNUM | LCS客户端号码 | 可选必选说明：必选参数<br>参数含义：待删除的LCS客户端的E.164地址。<br>取值范围：1～16位十进制数字<br>默认值：无 |

## 操作的配置对象

- [GMLC和LCS Client对照关系（GMLCCLIENT）](configobject/UNC/20.15.2/GMLCCLIENT.md)

## 使用实例

将GMLC和LCS CLIENT对照表中LCS CLIENT的号码是861380123456789的对照关系删除：

RMV GMLCCLIENT: CLIENTNUM="861380123456789";

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除GMLC和LCS-Client对照关系(RMV-GMLCCLIENT)_26305612.md`
