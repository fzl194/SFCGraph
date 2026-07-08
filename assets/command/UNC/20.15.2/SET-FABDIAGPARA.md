---
id: UNC@20.15.2@MMLCommand@SET FABDIAGPARA
type: MMLCommand
name: SET FABDIAGPARA（设置Pod Fabric平面亚健康诊断参数）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: FABDIAGPARA
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- 可靠性管理
- 微服务可靠性管理
status: active
---

# SET FABDIAGPARA（设置Pod Fabric平面亚健康诊断参数）

## 功能

该命令用来设置Pod Fabric平面亚健康诊断参数。

## 注意事项

- 该命令执行后立即生效。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| PODSUBHEALTHD |
| --- |
| 50 |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PODSUBHEALTHD | POD亚健康阈值(%) | 可选必选说明：必选参数<br>参数含义：该参数用于指定Pod级fabric平面亚健康诊断阈值，单位：%。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~100。<br>默认值：无。<br>配置原则：无 |

## 操作的配置对象

- [Pod Fabric平面亚健康诊断参数（FABDIAGPARA）](configobject/UNC/20.15.2/FABDIAGPARA.md)

## 使用实例

设置Pod Fabric平面亚健康诊断参数为50%。

```
SET FABDIAGPARA: PODSUBHEALTHD=50;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/设置Pod-Fabric平面亚健康诊断参数（SET-FABDIAGPARA）_48110865.md`
