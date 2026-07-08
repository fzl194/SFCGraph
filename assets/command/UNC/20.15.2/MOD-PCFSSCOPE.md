---
id: UNC@20.15.2@MMLCommand@MOD PCFSSCOPE
type: MMLCommand
name: MOD PCFSSCOPE（修改PCF的业务服务区）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: PCFSSCOPE
command_category: 配置类
applicable_nf:
- SMF
- PGW-C
- GGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- PCC管理
- PCF发现和选择管理
- PCF业务服务区
status: active
---

# MOD PCFSSCOPE（修改PCF的业务服务区）

## 功能

**适用NF：SMF、PGW-C、GGSN**

该命令用于修改PCF的业务服务区。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SSCOPEID | 服务区标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定服务区标识。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~32。不区分大小写，转为小写存储。<br>默认值：无<br>配置原则：无 |
| SSCOPENAME | 服务区名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定服务区名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~50。 区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@PCFSSCOPE]] · PCF的业务服务区（PCFSSCOPE）

## 使用实例

修改服务区标识为citya的PCF业务服务区，把服务区名称修改为CityA。

```
MOD PCFSSCOPE: SSCOPEID="citya", SSCOPENAME="CityA";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/MOD-PCFSSCOPE.md`
