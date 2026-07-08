---
id: UNC@20.15.2@MMLCommand@SET DRTLSMODE
type: MMLCommand
name: SET DRTLSMODE（设置容灾控制通道TLS模式）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: DRTLSMODE
command_category: 配置类
effect_mode: 立即生效
is_dangerous: true
category_path:
- 平台服务管理
- 可靠性管理
- 微服务可靠性管理
status: active
---

# SET DRTLSMODE（设置容灾控制通道TLS模式）

## 功能

![](设置容灾控制通道TLS模式（SET DRTLSMODE）_55919521.assets/notice_3.0-zh-cn_2.png)

本命令属于高危命令，主备网元配置不同可能会导致容灾控制通道通信故障，影响现网业务，请谨慎使用并联系华为技术支持协助操作。

该命令用于设置容灾控制通道TLS模式。

## 注意事项

- 该命令执行后立即生效。

- 该命令要求主备网元配置相同的TLS模式，否则会导致容灾控制通道通信故障。
- 当执行本命令变更网元TLS模式时，必须在容灾心跳控制时间内对其主备网元完成同样的TLS模式变更。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| TLSMODE |
| --- |
| OFF |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TLSMODE | TLS模式 | 可选必选说明：必选参数<br>参数含义：该参数用于指定容灾控制通道TLS模式。<br>数据来源：本端规划<br>取值范围：<br>- “OFF（关闭）”：关闭TLS通信<br>- “ON（开启）”：开启TLS通信<br>默认值：无。<br>配置原则：<br>主备网元要求配置相同的TLS模式。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@DRTLSMODE]] · 容灾控制通道TLS模式（DRTLSMODE）

## 使用实例

设置网元容灾控制通道TLS模式为开启。

```
%%SET DRTLSMODE: TLSMODE=ON;%%
RETCODE = 0  操作成功

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/SET-DRTLSMODE.md`
