---
id: UNC@20.15.2@MMLCommand@RMV AMFSERVICELIST
type: MMLCommand
name: RMV AMFSERVICELIST（删除AMF服务列表）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: AMFSERVICELIST
command_category: 配置类
applicable_nf:
- AMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- 性能统计管理
- AMF性能对象管理
status: active
---

# RMV AMFSERVICELIST（删除AMF服务列表）

## 功能

**适用NF：AMF**

本命令删除特定AMF功能实体服务名。本命令执行影响北向网管对接功能。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SERVICENAME | AMF服务名称 | 可选必选说明：必选参数<br>参数含义：特定AMF功能实例的服务名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~64。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [AMF服务列表（AMFSERVICELIST）](configobject/UNC/20.15.2/AMFSERVICELIST.md)

## 使用实例

删除指定的AMF实例服务名称：

```
RMV AMFSERVICELIST: SERVICENAME="namfComm";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除AMF服务列表（RMV-AMFSERVICELIST）_09652985.md`
