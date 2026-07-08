---
id: UDG@20.15.2@MMLCommand@SET GLBIPV6INFID
type: MMLCommand
name: SET GLBIPV6INFID（设置整机IPv6接口ID配置）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: GLBIPV6INFID
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: true
max_records: 1
category_path:
- 用户面服务管理
- 会话管理
- 会话地址管理
- IPv6接口标识管理
- 全局IPv6接口标识管理
status: active
---

# SET GLBIPV6INFID（设置整机IPv6接口ID配置）

## 功能

**适用NF：PGW-U、UPF**

![](设置整机IPv6接口ID配置（SET GLBIPV6INFID）_71074283.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，开启本功能后IPv6地址interface ID将会包含用户标识信息IMSI，请关注个人隐私保护。

该命令用于控制全局为用户分配IPv6地址时，是否开启IMSI作为用户的IPv6地址interface ID(IPv6地址的后64位)功能。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为1。
- 该配置应与SMF保持一致。
- 开启本功能时建议根据实际情况部署安全传输功能如IPsec，提高对个人隐私的保护能力。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | IMSI |
| --- | --- |
| 初始值 | DISABLE |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IMSI | 配置IMSI作为IPv6 interface ID | 可选必选说明：必选参数<br>参数含义：该参数用于控制开启和关闭IMSI作为用户的IPv6地址interface ID功能。<br>数据来源：本端规划<br>取值范围：枚举类型。必须全部为整数。 IMSI由三部分组成： 1、Mobile Country Code (MCC)包含3个数字。MCC唯一标识移动用户的居住国家。 2、Mobile Network Code (MNC)包含2个或3个数字用于GSM/UMTS应用。MNC标识移动用户的归属PLMN。MNC的长度取决于MCC的值。不推荐单个MCC区内两个和三个数字混合编码的MNC，此种情况已经在本书之外。 3、Mobile Subscriber Identification Number (MSIN)标识PLMN内的移动用户。<br>- DISABLE：不使能。<br>- ENABLE：使能。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/GLBIPV6INFID]] · 整机IPv6接口ID配置（GLBIPV6INFID）

## 使用实例

配置IMSI作为用户的IPv6地址interface ID(IPv6地址的后64位)功能使能：

```
SET GLBIPV6INFID: IMSI=ENABLE;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/设置整机IPv6接口ID配置（SET-GLBIPV6INFID）_71074283.md`
