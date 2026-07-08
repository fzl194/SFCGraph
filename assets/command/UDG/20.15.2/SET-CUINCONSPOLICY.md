---
id: UDG@20.15.2@MMLCommand@SET CUINCONSPOLICY
type: MMLCommand
name: SET CUINCONSPOLICY（设置CP和UP关键配置不一致的处理策略）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: CUINCONSPOLICY
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: true
max_records: 1
category_path:
- 用户面服务管理
- 业务控制策略
- 配置校验控制
- CP和UP关键配置不一致策略
status: active
---

# SET CUINCONSPOLICY（设置CP和UP关键配置不一致的处理策略）

## 功能

**适用NF：PGW-U、UPF**

![](设置CP和UP关键配置不一致的处理策略（SET CUINCONSPOLICY）_64015288.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，该命令仅用于紧急情况下的故障恢复，执行该命令可能会导致一定的计费误差，请谨慎使用。执行该命令将改变失败处理的原则，请确认已经进行了必要的预检查，并已获得了执行该命令的权限。

设置SMF/PGW-C和UPF/PGW-U关键配置不一致的处理策略。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为1。
- 修改告警参数为非零时，需要提前使用CIP或FMA工具对UPF的内容计费配置进行配置核查，如果工具检查出现异常，可能会出现计费属性不一致的告警。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | BYPASSSW | CHGATTRRPTTHD | CHGATTRCLRTHD |
| --- | --- | --- | --- |
| 初始值 | DISABLE | 10 | 5 |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| BYPASSSW | 旁路处理开关 | 可选必选说明：可选参数<br>参数含义：该参数用于指定SMF/PGW-C和UPF/PGW-U关键配置不一致时是否进行旁路处理。旁路处理指允许用户激活或更新成功。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能（关闭）。<br>- ENABLE：使能（开启）。<br>默认值：无<br>配置原则：<br>- DISABLE：关闭旁路功能，用户激活或更新失败。<br>- ENABLE：开启旁路功能，用户激活或更新成功。 |
| CHGATTRRPTTHD | 计费属性告警上报门限 | 可选必选说明：可选参数<br>参数含义：该参数用于设置计费属性SMF/PGW-C和UPF/PGW-U不一致告警上报门限。<br>数据来源：本端规划<br>取值范围：1.整数类型，取值范围为0~100000，单位是次数。 2.该参数的值必须大于计费属性告警恢复门限。 3.该参数与计费属性告警恢复门限同时取值为0时，表示告警功能关闭。<br>默认值：无<br>配置原则：无 |
| CHGATTRCLRTHD | 计费属性告警恢复门限 | 可选必选说明：可选参数<br>参数含义：该参数用于设置计费属性SMF/PGW-C和UPF/PGW-U不一致告警恢复门限。<br>数据来源：本端规划<br>取值范围：1. 整数类型，取值范围为0~100000，单位是次数。 2. 该参数的值必须小于计费属性告警上报门限。 3. 该参数与计费属性告警上报门限同时取值为0时，表示告警功能关闭。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/CUINCONSPOLICY]] · CP和UP关键配置不一致的处理策略（CUINCONSPOLICY）

## 使用实例

SMF/PGW-C和UPF/PGW-U关键配置不一致时，配置旁路功能：

```
SET CUINCONSPOLICY: BYPASSSW=ENABLE;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/设置CP和UP关键配置不一致的处理策略（SET-CUINCONSPOLICY）_64015288.md`
