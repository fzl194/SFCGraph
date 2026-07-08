---
id: UDG@20.15.2@MMLCommand@SET ACSELECTSERVICE
type: MMLCommand
name: SET ACSELECTSERVICE（设置仲裁服务配置）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: ACSELECTSERVICE
command_category: 配置类
effect_mode: 立即生效
is_dangerous: true
category_path:
- 平台服务管理
- 单体服务公共功能管理
- 系统管理
- 系统维护
- 仲裁服务配置
status: active
---

# SET ACSELECTSERVICE（设置仲裁服务配置）

## 功能

![](设置仲裁服务配置（SET ACSELECTSERVICE）_44102825.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，操作不当会导致系统有发生脑裂的风险，请谨慎使用并联系华为技术支持协助操作。

该命令用于设置ETCD仲裁服务的客户端相关配置，包括ETCD仲裁的开关和ETCD灯塔特性的开关。

本命令只适用于ACS服务，其他微服务请使用SET ELECTSERVICE命令。

## 注意事项

- 该命令执行后立即生效。
- 该操作可能使得仲裁服务承载的业务受影响。
- 该命令可以关闭仲裁服务，当仲裁服务关闭时，系统有发生脑裂的风险。
- ETCD灯塔开关使能之后，也需要ETCD服务仲裁开关使能才能实现灯塔功能。
- 开启ETCD灯塔功能，会导致ETCD服务的CPU使用率升高。
- 该命令存在系统初始记录，参数的初始设置值如下表：
  | SERVICESWITCH | LIGHTHOUSESWITCH |
  | --- | --- |
  | ENABLE | DISABLE |

## 权限

G_1，管理员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SERVICESWITCH | 仲裁服务开关配置 | 可选必选说明：可选参数<br>参数含义：该参数用于表示仲裁服务的开关配置。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：仲裁服务去使能。<br>- ENABLE：仲裁服务使能。<br>默认值：无 |
| LIGHTHOUSESWITCH | ETCD灯塔开关配置 | 可选必选说明：可选参数<br>参数含义：该参数用于表示ETCD灯塔的开关配置。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：服务去使能。<br>- ENABLE：服务使能。<br>默认值：无<br>配置原则：该参数和可选参数SERVICESWITCH需要至少选择一个。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/ACSELECTSERVICE]] · 仲裁服务状态（ACSELECTSERVICE）

## 使用实例

打开仲裁服务开关：

```
SET ACSELECTSERVICE:SERVICESWITCH=ENABLE,LIGHTHOUSESWITCH=ENABLE;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/设置仲裁服务配置（SET-ACSELECTSERVICE）_44102825.md`
