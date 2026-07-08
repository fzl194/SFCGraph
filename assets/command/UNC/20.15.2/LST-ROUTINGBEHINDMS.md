---
id: UNC@20.15.2@MMLCommand@LST ROUTINGBEHINDMS
type: MMLCommand
name: LST ROUTINGBEHINDMS（查询手机后路由配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: ROUTINGBEHINDMS
command_category: 查询类
applicable_nf:
- PGW-C
- SMF
- GGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- UE地址管理
- DHCP管理
- 手机后路由
status: active
---

# LST ROUTINGBEHINDMS（查询手机后路由配置）

## 功能

**适用NF：PGW-C、SMF、GGSN**

该命令用于查询本地配置的手机后路由信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IMSI | 用户IMSI号 | 可选必选说明：可选参数<br>参数含义：用户的IMSI信息。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是5~15。<br>默认值：无<br>配置原则：无 |
| APN | APN名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定APN实例名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“ ” ”、“ ` ”特殊字符，不区分大小写。<br>默认值：无<br>配置原则：<br>该参数必须已经通过命令ADD APN配置。 |
| FRAMEDROUTEIP | 后路由IPv4地址 | 可选必选说明：可选参数<br>参数含义：该参数用于指定后路由的网段地址。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。采用点分十进制"X.X.X.X"格式。<br>默认值：无<br>配置原则：<br>IPv4地址不能配置为0.0.0.0、255.255.255.255和环回地址(127.x.y.z)。业务地址必须是A、B或者C类地址。 |
| FRAMEDROUTEMASK | 后路由掩码 | 可选必选说明：可选参数<br>参数含义：该参数用于指定后路由的网段掩码。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。采用点分十进制"X.X.X.X"格式。<br>默认值：无<br>配置原则：<br>输入的掩码要求对应的二进制值1和1之间不允许存在0。例如：“255.255.0.0”是有效掩码；“123.123.123.123”是无效掩码。因为123对应的二进制为“1111011”，1之间存在0。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/ROUTINGBEHINDMS]] · 手机后路由配置（ROUTINGBEHINDMS）

## 使用实例

查询本地配置的手机后路由信息：

```
LST ROUTINGBEHINDMS:;
RETCODE = 0  操作成功。

手机后路由配置
-------------------------------
                     
                      用户IMSI号  =  123456789125001
                         APN名称  =  demo.com
                  后路由IPv4地址  =  192.168.1.0
                      后路由掩码  =  255.255.255.0
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-ROUTINGBEHINDMS.md`
