---
id: UNC@20.15.2@MMLCommand@SET CEAORIGHOSTCHK
type: MMLCommand
name: SET CEAORIGHOSTCHK（设置对Gy接口的cea消息中的Origin-Host检查开关）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: CEAORIGHOSTCHK
command_category: 配置类
applicable_nf:
- PGW-C
- SMF
effect_mode: 立即生效
is_dangerous: false
max_records: 1
category_path:
- 业务服务管理
- 接口管理
- 计费和策略接口管理
- Diameter管理
- 公共参数
- Diameter公共参数
status: active
---

# SET CEAORIGHOSTCHK（设置对Gy接口的cea消息中的Origin-Host检查开关）

## 功能

**适用NF：PGW-C、SMF**

为了实现某运营商的特定需求。该命令用于配置Diameter对Gy接口的cea消息中的Origin-Host检查开关。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为1。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | CEAORIGHOSTCHK |
| --- | --- |
| 初始值 | ENABLE |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CEAORIGHOSTCHK | 检查Gy的CEA消息中的Origin-Host | 可选必选说明：可选参数<br>参数含义：该参数用于配置UNC是否检查Gy接口CEA消息中的Origin-Host。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ENABLE：是。<br>- DISABLE：否。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [对Gy接口的cea消息中的Origin-Host检查开关（CEAORIGHOSTCHK）](configobject/UNC/20.15.2/CEAORIGHOSTCHK.md)

## 使用实例

配置Diameter对Gy接口的cea消息中的Origin-Host检查开关，则可按如下配置：

```
SET CEAORIGHOSTCHK:CEAORIGHOSTCHK=DISABLE;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/设置对Gy接口的cea消息中的Origin-Host检查开关（SET-CEAORIGHOSTCHK）_09897240.md`
