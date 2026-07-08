---
id: UNC@20.15.2@MMLCommand@RMV SMSCTX
type: MMLCommand
name: RMV SMSCTX（删除用户的SMS上下文）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: SMSCTX
command_category: 配置类
applicable_nf:
- SMSF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- SMSF业务管理
- 用户上下文管理
- SMS上下文
status: active
---

# RMV SMSCTX（删除用户的SMS上下文）

## 功能

![](删除用户的SMS上下文（RMV SMSCTX）_96243010.assets/notice_3.0-zh-cn_2.png)

删除SMS上下文将影响用户正在进行的短消息业务。

**适用NF：SMSF**

该命令用于删除用户的SMS上下文。当功能调测或拨测过程中需要手动删除用户的SMS上下文时，使用该命令。

## 注意事项

- 该命令执行后立即生效。

- 删除SMS上下文将影响用户正在进行的短消息业务，请慎重使用此命令。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SUPI | SUPI | 可选必选说明：必选参数<br>参数含义：该参数用于指定用户的SUPI，在本命令中，可以按指定SUPI删除对应用户的SMS上下文。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是5~15。只允许输入十进制数字(0-9)。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@SMSCTX]] · 用户的SMS上下文（SMSCTX）

## 使用实例

操作员在功能调测过程中手动删除值为460023500100001的SUPI对应的用户的SMS上下文。

```
RMV SMSCTX: SUPI="460023500100001";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-SMSCTX.md`
