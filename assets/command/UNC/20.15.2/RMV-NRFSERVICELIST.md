---
id: UNC@20.15.2@MMLCommand@RMV NRFSERVICELIST
type: MMLCommand
name: RMV NRFSERVICELIST（删除NRF实例服务名称）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: NRFSERVICELIST
command_category: 配置类
applicable_nf:
- NRF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- 性能统计管理
- NRF性能对象管理
status: active
---

# RMV NRFSERVICELIST（删除NRF实例服务名称）

## 功能

**适用NF：NRF**

该命令用于删除特定NRF功能实例的服务名称，用于与北向网管对接的功能。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SERVICENAME | NRF服务名称 | 可选必选说明：必选参数<br>参数含义：该参数用于表示特定NRF功能实例的服务名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~65。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/NRFSERVICELIST]] · NRF实例服务名称（NRFSERVICELIST）

## 使用实例

运营商想删除一条NRF实例服务名称为nrf-servcename001的记录，执行此命令：

```
RMV NRFSERVICELIST:SERVICENAME="nrf-servcename001";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除NRF实例服务名称（RMV-NRFSERVICELIST）_09651500.md`
