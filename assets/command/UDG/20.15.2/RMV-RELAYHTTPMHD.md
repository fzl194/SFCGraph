---
id: UDG@20.15.2@MMLCommand@RMV RELAYHTTPMHD
type: MMLCommand
name: RMV RELAYHTTPMHD（删除媒体中继HTTP消息头）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: RELAYHTTPMHD
command_category: 配置类
applicable_nf:
- UPF
- PGW-U
effect_mode: 立即生效
is_dangerous: false
category_path:
- 用户面服务管理
- 业务控制策略
- 媒体中继
- 媒体中继HTTP消息头
status: active
---

# RMV RELAYHTTPMHD（删除媒体中继HTTP消息头）

## 功能

**适用NF：UPF、PGW-U**

该命令用于删除媒体中继HTTP消息头。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| HTTPMSGCTRLNAME | HTTP消息控制名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定HTTP消息控制名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~31。不区分大小写。<br>默认值：无<br>配置原则：<br>- 该参数使用ADD RELAYHTTPMCTL命令配置生成。<br>- 该取值必须和ADD RELAYHTTPMCTL中配置的"HTTPMAGCTRLNAME"参数取值相同。 |
| MSGTYPE | 消息类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定消息类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- UEHTTPRSP：UE HTTP响应。<br>- CDNHTTPREQ：CDN HTTP请求。<br>默认值：无<br>配置原则：无 |
| HEADERNAME | 头域名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定头域名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。区分大小写，不允许仅大小写不同的重复记录。<br>默认值：无<br>配置原则：以下字段为通用必选或条件必选字段，不允许配置 Connection、Content-Length、Content-Range、Content-Type、Date、Location。 |

## 操作的配置对象

- [媒体中继HTTP消息头（RELAYHTTPMHD）](configobject/UDG/20.15.2/RELAYHTTPMHD.md)

## 使用实例

删除媒体中继HTTP消息头：

```
RMV RELAYHTTPMHD: HTTPMSGCTRLNAME="http01";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/删除媒体中继HTTP消息头（RMV-RELAYHTTPMHD）_43992604.md`
