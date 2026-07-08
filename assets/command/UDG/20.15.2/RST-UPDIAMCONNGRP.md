---
id: UDG@20.15.2@MMLCommand@RST UPDIAMCONNGRP
type: MMLCommand
name: RST UPDIAMCONNGRP（重建Diameter链路组）
nf: UDG
version: 20.15.2
verb: RST
object_keyword: UPDIAMCONNGRP
command_category: 动作类
applicable_nf:
- UPF
effect_mode: 立即生效
is_dangerous: true
category_path:
- 用户面服务管理
- Diameter管理
- Diameter连接
- 重建Diameter链路组
status: active
---

# RST UPDIAMCONNGRP（重建Diameter链路组）

## 功能

**适用NF：UPF**

![](重建Diameter链路组（RST UPDIAMCONNGRP）_97314565.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，重建Diameter链路会导致Diameter链路中断，进而影响用户使用业务，比如用户被去活等。

该命令用于重建Diamter链路，即该命令执行以后，当前指定的Diameter链路组下的所有Normal状态的链路会重建链。

## 注意事项

- 该命令执行后立即生效。
- 本命令属于高危命令，操作不当，会影响用户业务使用，请谨慎使用并联系华为技术支持协助操作。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PEERHOSTNAME | 对端主机名 | 可选必选说明：必选参数<br>参数含义：该参数用于指定Diameter链路组的对端主机名。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～127。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：该参数使用ADD UPDIAMETERAAA或ADD UPDRA命令配置生成。 |
| LOCALHOSTNAME | 本端主机名 | 可选必选说明：可选参数<br>参数含义：该参数用于指定Diameter链路组的本端主机名。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～127。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：该参数使用ADD UPDIAMLOCINFO命令配置生成。 |
| APPLICATION | Diameter应用 | 可选必选说明：可选参数<br>参数含义：该参数用于指定Diameter链路组的应用类型。<br>数据来源：全网规划<br>取值范围：位域类型。<br>- SWM：SWM接口应用。<br>默认值：无<br>配置原则：该参数所指定的应用必须与PEERHOSTNAME参数对应服务器的应用类型相同。 |

## 操作的配置对象

- [Diameter链路组（UPDIAMCONNGRP）](configobject/UDG/20.15.2/UPDIAMCONNGRP.md)

## 使用实例

重建对端主机名为test的所有链路：

```
RST UPDIAMCONNGRP: PEERHOSTNAME="test";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/重建Diameter链路组（RST-UPDIAMCONNGRP）_97314565.md`
