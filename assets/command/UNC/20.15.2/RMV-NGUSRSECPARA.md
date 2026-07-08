---
id: UNC@20.15.2@MMLCommand@RMV NGUSRSECPARA
type: MMLCommand
name: RMV NGUSRSECPARA（删除5G用户安全配置）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: NGUSRSECPARA
command_category: 配置类
applicable_nf:
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 业务安全管理
- 用户安全参数管理
status: active
---

# RMV NGUSRSECPARA（删除5G用户安全配置）

## 功能

![](删除5G用户安全配置（RMV NGUSRSECPARA）_09653270.assets/notice_3.0-zh-cn_2.png)

如果执行该命令可能导致加密算法或者完整性算法生效范围变化，导致终端接入异常。

**适用NF：AMF**

此命令用于删除指定用户的鉴权、加密、完整性保护等安全配置。

## 注意事项

- 命令执行后在用户发起下一次涉及安全管理流程时生效。

- 此命令只能删除指定号段用户的安全配置，不能删除默认的安全配置。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SUBRANGE | 用户范围 | 可选必选说明：必选参数<br>参数含义：该参数用于指定配置安全参数的用户范围。<br>数据来源：本端规划<br>取值范围：<br>- “ALL_USER（所有用户）”：所有用户<br>- “IMSI_PREFIX（指定IMSI前缀）”：指定IMSI前缀<br>默认值：无<br>配置原则：无 |
| IMSIPRE | IMSI前缀 | 可选必选说明：该参数在"SUBRANGE"配置为"IMSI_PREFIX"时为条件必选参数。<br>参数含义：该参数用于系统根据指定用户的IMSI前缀进行匹配，从而区分不同的用户群。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是5~15。只允许输入十进制数字（0-9）。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/NGUSRSECPARA]] · 5G用户安全配置（NGUSRSECPARA）

## 使用实例

删除IMSI前缀为“123031200100001”的用户的安全配置，执行如下命令：

```
RMV NGUSRSECPARA: SUBRANGE=IMSI_PREFIX, IMSIPRE="123031200100001";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除5G用户安全配置（RMV-NGUSRSECPARA）_09653270.md`
