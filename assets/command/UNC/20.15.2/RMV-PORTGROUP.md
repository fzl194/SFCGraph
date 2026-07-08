---
id: UNC@20.15.2@MMLCommand@RMV PORTGROUP
type: MMLCommand
name: RMV PORTGROUP（删除端口组）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: PORTGROUP
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 接口管理
- 端口组
status: active
---

# RMV PORTGROUP（删除端口组）

## 功能

该命令用于删除已创建的端口组。

## 注意事项

- 该命令执行后立即生效。
- 删除该端口组时，所有成员口都会被移除出端口组。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PORTGROUPNAME | 端口组名称 | 可选必选说明：必选参数<br>参数含义：该参数用于表示端口组的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～32；字符串由数字、字母、“.”、“-”或“_”组成。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/PORTGROUP]] · 端口组（PORTGROUP）

## 使用实例

删除端口组ifm：

```
RMV PORTGROUP:PORTGROUPNAME="ifm";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除端口组（RMV-PORTGROUP）_00441253.md`
