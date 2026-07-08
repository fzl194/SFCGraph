---
id: UNC@20.15.2@MMLCommand@SET LBTNIPINIPSWITCH
type: MMLCommand
name: SET LBTNIPINIPSWITCH（设置CSLB隧道IP-in-IP开关）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: LBTNIPINIPSWITCH
command_category: 配置类
effect_mode: 立即生效
is_dangerous: true
category_path:
- 平台服务管理
- CSLB功能管理
- 业务管理
- 隧道管理
- CSLB隧道探测参数
status: active
---

# SET LBTNIPINIPSWITCH（设置CSLB隧道IP-in-IP开关）

## 功能

![](设置CSLB隧道IP-in-IP开关（SET LBTNIPINIPSWITCH）_21584628.assets/notice_3.0-zh-cn_2.png)

本命令属于高危命令，操作不当会导致容灾业务受损，请谨慎使用并联系华为技术支持协助操作。

该命令用于设置CSLB隧道IP-in-IP功能开关配置。

该命令使用场景：网络防火墙存在对分片报文的带宽限制，会导致容灾业务受损。此时，配置容灾关系的网元，可开启CSLB隧道IP-in-IP功能开关，隧道中的IPV6分片报文会被重新进行UDP封装，避免网络防火墙对带宽的限制，防止容灾业务受损。

## 注意事项

- 该命令执行后立即生效。
- 该命令只对地址类型为IPV6的隧道生效。
- 该命令参数配置需要和对端保持一致，否则会导致容灾业务受损。
- 该命令存在系统初始记录，参数的初始设置值如下表：
  | SWFLAG |
  | --- |
  | SW_DISABLE |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SWFLAG | CSLB隧道IP-in-IP配置开关 | 可选必选说明：必选参数<br>参数含义：<br>该参数表示使能或去使能<br>CSLB隧道IP-in-IP功能配置。<br>数据来源：全网规划<br>取值范围：枚举类型:<br>- SW_ENABLE(CSLB隧道IP-in-IP开启)：使能CSLB隧道IP-in-IP功能开关。<br>- SW_DISABLE(CSLB隧道IP-in-IP关闭)：去使能CSLB隧道IP-in-IP功能开关。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [CSLB隧道IP-in-IP开关（LBTNIPINIPSWITCH）](configobject/UNC/20.15.2/LBTNIPINIPSWITCH.md)

## 使用实例

设置CSLB隧道开启IP-in-IP功能，命令如下：

```
SET LBTNIPINIPSWITCH: SWFLAG=SW_ENABLE;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/设置CSLB隧道IP-in-IP开关（SET-LBTNIPINIPSWITCH）_21584628.md`
