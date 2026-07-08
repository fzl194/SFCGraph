---
id: UDG@20.15.2@MMLCommand@SET APNTRAFDFUNC
type: MMLCommand
name: SET APNTRAFDFUNC（设置流量转发APN开关）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: APNTRAFDFUNC
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 用户面服务管理
- DN管理
- 流量转发管理
- APN流量转发功能
status: active
---

# SET APNTRAFDFUNC（设置流量转发APN开关）

## 功能

**适用NF：PGW-U、UPF**

设置流量转发APN开关，当TRAFFICFDSW配置为ENABLE时，UPF支持通过VXLAN隧道转发数据流到MPF，否则不支持。

## 注意事项

- 该命令执行后立即生效。
- 系统最多支持配置10000条。
- 初始值均为DISABLE。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APN | APN | 可选必选说明：必选参数<br>参数含义：该参数用于指定APN实例名。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：<br>- 该参数使用ADD APN命令配置生成。<br>- 该参数必须已经通过ADD APN命令配置。 |
| TRAFFICFDSW | 流量转发开关 | 可选必选说明：必选参数<br>参数含义：该参数用于配置是否开启流量转发功能。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能。<br>- ENABLE：使能。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/APNTRAFDFUNC]] · APN流量转发配置（APNTRAFDFUNC）

## 使用实例

设置APN apn1的流量转发开关为ENABLE：

```
SET APNTRAFDFUNC: APN="apn1", TRAFFICFDSW=ENABLE;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/SET-APNTRAFDFUNC.md`
