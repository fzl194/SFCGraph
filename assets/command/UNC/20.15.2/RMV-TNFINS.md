---
id: UNC@20.15.2@MMLCommand@RMV TNFINS
type: MMLCommand
name: RMV TNFINS（删除目标NF实例）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: TNFINS
command_category: 配置类
applicable_nf:
- AMF
- SMF
- NSSF
- SMSF
- NCG
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- 服务化接口管理
- 注册与服务发现
- 本地NRF功能管理
- 目标NF实例管理
status: active
---

# RMV TNFINS（删除目标NF实例）

## 功能

**适用NF：AMF、SMF、NSSF、SMSF、NCG**

该命令用于删除目标NF实例的配置。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TNFINSINDEX | 目标NF实例索引 | 可选必选说明：必选参数<br>参数含义：本参数用于指定目标NF实例索引。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~2047。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [目标NF实例（TNFINS）](configobject/UNC/20.15.2/TNFINS.md)

## 使用实例

运营商A需要删除索引为1的目标NF实例。

```
RMV TNFINS: TNFINSINDEX=1;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除目标NF实例（RMV-TNFINS）_09651333.md`
