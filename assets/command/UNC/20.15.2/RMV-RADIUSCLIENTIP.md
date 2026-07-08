---
id: UNC@20.15.2@MMLCommand@RMV RADIUSCLIENTIP
type: MMLCommand
name: RMV RADIUSCLIENTIP（删除Radius Group Client IP接口）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: RADIUSCLIENTIP
command_category: 配置类
applicable_nf:
- PGW-C
- SMF
effect_mode: 立即生效
is_dangerous: true
category_path:
- 业务服务管理
- 会话管理
- RADIUS管理
- 连接管理
- Radius Client
status: active
---

# RMV RADIUSCLIENTIP（删除Radius Group Client IP接口）

## 功能

**适用NF：PGW-C、SMF**

![](删除Radius Group Client IP接口（RMV RADIUSCLIENTIP）_09896741.assets/notice_3.0-zh-cn_2.png)

本命令属于高危命令，删除Gi接口与RADIUS server group实例的绑定关系，可能会导致发送鉴权或计费请求消息失败。

RMV RADIUSCLIENTIP命令用来删除Radius Group Client IP接口。

## 注意事项

- 该命令执行后立即生效。
- 当未指定接口名称时，禁止执行该命令。若需要执行，需将软参BYTE976的值设置为169。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RDSSVRGRPNAME | Radius Server Group名称 | 可选必选说明：必选参数<br>参数含义：指定Radius Server Group名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无<br>配置原则：无 |
| AUTHORACCT | 鉴权或计费 | 可选必选说明：可选参数<br>参数含义：指定鉴权或计费。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ACCOUNTING：表示指定的Gi接口的IP地址是计费时的radius client ip。<br>- AUTHENTICATION：表示指定的Gi接口的IP地址是鉴权时的radius client ip。<br>- ACCT_AND_AUTH：表示指定的Gi接口的IP地址既是鉴权时的radius client ip，也是计费时的radius client ip。<br>默认值：无<br>配置原则：<br>- ACCOUNTING：表示计费。<br>- AUTHENTICATION：表示鉴权。<br>- ACCT_AND_AUTH：表示计费和鉴权。 |
| INTFNAME | 接口名称 | 可选必选说明：可选参数<br>参数含义：指定接口名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～13。用户输入形式例如：giif1/0/0。其中giif为逻辑接口类型；1/0/0中第一个数字为组号，第二个数字为实例类型；第三个数字为逻辑接口号，各逻辑接口类型有各自的配置范围。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@RADIUSCLIENTIP]] · Radius Group Client IP接口（RADIUSCLIENTIP）

## 使用实例

如果想要删除Radius Group Client IP接口，可以指定RADIUS服务器组名为"aaa"，例如：

```
RMV RADIUSCLIENTIP: RDSSVRGRPNAME="aaa";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-RADIUSCLIENTIP.md`
