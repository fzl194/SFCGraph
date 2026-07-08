---
id: UNC@20.15.2@MMLCommand@RMV SMFSERVICELIST
type: MMLCommand
name: RMV SMFSERVICELIST（删除特定SMF功能实例服务名）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: SMFSERVICELIST
command_category: 配置类
applicable_nf:
- SMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- 性能统计管理
- SMF性能对象管理
status: active
---

# RMV SMFSERVICELIST（删除特定SMF功能实例服务名）

## 功能

![](删除特定SMF功能实例服务名（RMV SMFSERVICELIST）_09654435.assets/notice_3.0-zh-cn_2.png)

本命令执行会影响北向网管对接功能。

**适用NF：SMF**

本命令删除特定SMF功能实体服务名。本命令执行影响北向网管对接功能。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SERVICENAME | 服务名称 | 可选必选说明：必选参数<br>参数含义：特定SMF功能实例服务名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~65。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [特定SMF功能实例服务名（SMFSERVICELIST）](configobject/UNC/20.15.2/SMFSERVICELIST.md)

## 使用实例

删除SMF实例服务名称：

```
RMV SMFSERVICELIST: SERVICENAME="SMF-SERVICENAME001";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除特定SMF功能实例服务名（RMV-SMFSERVICELIST）_09654435.md`
