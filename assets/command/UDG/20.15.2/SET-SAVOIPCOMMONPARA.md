---
id: UDG@20.15.2@MMLCommand@SET SAVOIPCOMMONPARA
type: MMLCommand
name: SET SAVOIPCOMMONPARA（设置SA VOIP业务公共参数）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: SAVOIPCOMMONPARA
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: true
max_records: 1
category_path:
- 用户面服务管理
- 业务匹配策略
- 业务匹配公共配置
- 业务公共参数管理
- 业务公共参数
status: active
---

# SET SAVOIPCOMMONPARA（设置SA VOIP业务公共参数）

## 功能

**适用NF：PGW-U、UPF**

![](设置SA VOIP业务公共参数（SET SAVOIPCOMMONPARA）_82837311.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，此命令的生效范围为整机，开启后可能导致性能下降明显。

该命令用来配置SA VOIP业务相关控制参数，用于开启或关闭VOIP大类识别功能。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为1。
- 此命令的生效范围为整机，开启后可能导致性能下降明显。执行命令前请评估对性能的影响，如果无法评估请联系华为技术支持。
- 该命令设定后的数据，需要通过LST SRVCOMMONPARA命令进行查看。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | VOIPGRSINSPECT |
| --- | --- |
| 初始值 | DISABLE |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VOIPGRSINSPECT | VOIP大类识别功能开关 | 可选必选说明：可选参数<br>参数含义：该参数用于设置SA业务公共参数开启或关闭VOIP大类识别功能。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能（关闭）。<br>- ENABLE：使能（开启）。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/SAVOIPCOMMONPARA]] · SA VOIP业务公共参数（SAVOIPCOMMONPARA）

## 使用实例

设置SA业务公共参数开启VOIP大类识别功能：

```
SET SAVOIPCOMMONPARA:VOIPGRSINSPECT=ENABLE;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/设置SA-VOIP业务公共参数（SET-SAVOIPCOMMONPARA）_82837311.md`
