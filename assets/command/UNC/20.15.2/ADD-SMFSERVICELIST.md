---
id: UNC@20.15.2@MMLCommand@ADD SMFSERVICELIST
type: MMLCommand
name: ADD SMFSERVICELIST（增加特定SMF功能实例服务名）
nf: UNC
version: 20.15.2
verb: ADD
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

# ADD SMFSERVICELIST（增加特定SMF功能实例服务名）

## 功能

**适用NF：SMF**

本命令用于添加特定SMF功能实例服务。

## 注意事项

- 该命令执行后立即生效。

- 最多可输入100条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SERVICENAME | 服务名称 | 可选必选说明：必选参数<br>参数含义：特定SMF功能实例服务名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~65。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [特定SMF功能实例服务名（SMFSERVICELIST）](configobject/UNC/20.15.2/SMFSERVICELIST.md)

## 使用实例

添加SMF服务名称：

```
ADD SMFSERVICELIST: SERVICENAME="SMF-SERVICENAME001";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加特定SMF功能实例服务名（ADD-SMFSERVICELIST）_09654442.md`
