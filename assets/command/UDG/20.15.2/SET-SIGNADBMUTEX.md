---
id: UDG@20.15.2@MMLCommand@SET SIGNADBMUTEX
type: MMLCommand
name: SET SIGNADBMUTEX（配置特征库规则的加载条件）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: SIGNADBMUTEX
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 延迟生效
is_dangerous: true
max_records: 1
category_path:
- 用户面服务管理
- 协议识别
- 特征库管理
- SA特征库规则加载条件
- 特征库规则加载条件相关配置
status: active
---

# SET SIGNADBMUTEX（配置特征库规则的加载条件）

## 功能

**适用NF：PGW-U、UPF**

![](配置特征库规则的加载条件（SET SIGNADBMUTEX）_40174858.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，影响SA业务识别结果。

配置特征库规则的加载条件。

## 注意事项

- 该命令执行后30秒生效。
- 该命令最大记录数为1。
- 启用之前需要先和华为工程师联系，确认当前特征库，以及需要配置的area-id和mutex-id是否支持。
- 避免LOD SIGNATUREDB、ADD SIGNADBRULE、SET SIGNADBMUTEX在5分钟内连续配置操作。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | MUTEXID | AREAID |
| --- | --- | --- |
| 初始值 | 1 | 0 |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MUTEXID | 特征库规则加载分类ID | 可选必选说明：必选参数<br>参数含义：当需要设置特征库的加载规则分类ID时，使用该字段。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～4294967295。<br>默认值：无<br>配置原则：该功能属于定制需求，启用之前需要先和华为工程师联系，确认当前特征库是否支持，以及需要配置的area-id和mutex-id。如果需要配置多个mutex-id，需要确保多个id间无冲突关系。 |
| AREAID | 特征库加载规则区域ID | 可选必选说明：必选参数<br>参数含义：当需要设置特征库的加载规则区域ID时，使用该字段。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～32。<br>默认值：无<br>配置原则：该功能属于定制需求，启用之前需要先和华为工程师联系，确认当前特征库是否支持，以及需要配置的area-id和mutex-id。 |

## 操作的配置对象

- [特征库规则加载区域ID（SIGNADBMUTEX）](configobject/UDG/20.15.2/SIGNADBMUTEX.md)

## 使用实例

配置特征库规则的加载规则分类ID为2，规则区域ID为0如下：

```
SET SIGNADBMUTEX: MUTEXID=2, AREAID=0;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/配置特征库规则的加载条件（SET-SIGNADBMUTEX）_40174858.md`
