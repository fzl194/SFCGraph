---
id: UDG@20.15.2@MMLCommand@SET NPFABRICHEALTHY
type: MMLCommand
name: SET NPFABRICHEALTHY（设置全局亚健康相关配置）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: NPFABRICHEALTHY
command_category: 配置类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- FEMF
status: active
---

# SET NPFABRICHEALTHY（设置全局亚健康相关配置）

## 功能

该命令用来设置全局亚健康相关配置：包括亚健康阈值和亚健康检测周期。

> **说明**
> - 该命令执行后立即生效。
>
> - 如果修改阈值，需要注意：阈值过小，链路切换敏感，选路频繁变化，在网络负荷很大的场景下，频繁切换会导致网络传输质量下降。
> - 该命令仅适用于NP卡加速模式场景。
>
> - 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：
>
> | THRESHOLD | INTERVAL |
> | --- | --- |
> | 50 | 100 |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| THRESHOLD | 亚健康阙值 | 可选必选说明：必选参数<br>参数含义：NP Fabric亚健康阈值，阈值 = 丢包率（千分比）+5 * 错包率（千分比）。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~1000。<br>默认值：无。<br>配置原则：无 |
| INTERVAL | 亚健康探测周期 | 可选必选说明：必选参数<br>参数含义：NP Fabric亚健康探测周期，单位为秒。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是100~500，单位是秒。<br>默认值：无。<br>配置原则：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@NPFABRICHEALTHY]] · 全局亚健康相关配置（NPFABRICHEALTHY）

## 使用实例

设置亚健康阈值为50，亚健康探测周期为100：

```
SET NPFABRICHEALTHY: THRESHOLD=50, INTERVAL=100;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/SET-NPFABRICHEALTHY.md`
