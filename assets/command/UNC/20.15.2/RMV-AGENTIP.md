---
id: UNC@20.15.2@MMLCommand@RMV AGENTIP
type: MMLCommand
name: RMV AGENTIP（删除远端地址池代理IP信息）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: AGENTIP
command_category: 配置类
applicable_nf:
- PGW-C
- SMF
- GGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- UE地址管理
- UE地址池管理
- 代理IP管理
status: active
---

# RMV AGENTIP（删除远端地址池代理IP信息）

## 功能

![](删除远端地址池代理IP信息（RMV AGENTIP）_87143004.assets/notice_3.0-zh-cn_2.png)

如果Agent IP关联了地址段，则先回收地址段(ACT RECYCLE)再执行该命令，否则可能导致租约到期时续租失败，已在线用户被去激活。

**适用NF：PGW-C、SMF、GGSN**

该命令用于删除远端地址池的代理IP地址。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| POOLNAME | 地址池名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定配置代理IP地址的地址池名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~79。不支持空格及特殊字符“_”、“#”、“$”和“&”等，由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”，不区分大小写。<br>默认值：无<br>配置原则：<br>该参数使用ADD ADDRPOOL命令配置生成。 |
| SECTIONNUM | 地址段号 | 可选必选说明：可选参数<br>参数含义：该参数用于指定配置代理IP地址的地址段号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~63，65535。<br>默认值：65535<br>配置原则：<br>当没有配置地址段时，此DHCP服务器分配的地址采用主机路由方式发布。当该参数的取值为65535时，表示该参数无效。 |

## 操作的配置对象

- [远端地址池代理IP信息（AGENTIP）](configobject/UNC/20.15.2/AGENTIP.md)

## 使用实例

假设运营商不再使用远端地址池testpool的代理地址时，如果指定网段中地址都已被收回，则可以使用该命令删除：

```
RMV AGENTIP:POOLNAME="testpool",SECTIONNUM=0;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除远端地址池代理IP信息（RMV-AGENTIP）_87143004.md`
