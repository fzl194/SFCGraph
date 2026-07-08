---
id: UNC@20.15.2@MMLCommand@ADD HSSBPOFC
type: MMLCommand
name: ADD HSSBPOFC（增加故障状态HSS）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: HSSBPOFC
command_category: 配置类
applicable_nf:
- MME
effect_mode: 立即生效
is_dangerous: false
max_records: 10
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 业务安全管理
- 可靠性管理
- HSS故障BYPASS功能
status: active
---

# ADD HSSBPOFC（增加故障状态HSS）

## 功能

**适用网元：MME**

本命令用于添加故障状态HSS配置。当HSS处于全故障状态时，因特殊原因用户无法自动进入HSS BYPASS状态，可以通过该命令紧急触发用户进入HSS BYPASS状态。

## 注意事项

- 该命令执行后立即生效。
- 此命令最大记录数为10。
- 增加局向HSS Bypass配置时，可能导致用户不再与HSS交互获取签约以及鉴权集等，可能对业务产生影响，请确保对接的主备HSS均故障后再使用本命令。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| HOSTNAME | 对端主机名 | 可选必选说明：必选参数<br>参数含义：该参数用于指定进入故障状态的HSS主机名。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~127<br>默认值：无<br>配置原则：该参数只能由字母（A-Z或者a-z）、数字（0-9）、连字符（-）和点（.）组成或者配置为通配符（*）。该参数不区分大小写。配置为“*”时，表示所有HSS均处于故障状态。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@HSSBPOFC]] · 故障状态HSS（HSSBPOFC）

## 使用实例

增加一个故障状态HSS，对端主机名为"huawei"。

```
ADD HSSBPOFC: HOSTNAME="huawei";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-HSSBPOFC.md`
