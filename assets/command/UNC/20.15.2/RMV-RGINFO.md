---
id: UNC@20.15.2@MMLCommand@RMV RGINFO
type: MMLCommand
name: RMV RGINFO（删除费率组信息）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: RGINFO
command_category: 配置类
applicable_nf:
- NCG
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- NCG业务及策略管理
- 计费管理
- 业务系统管理
- 流量统计
status: active
---

# RMV RGINFO（删除费率组信息）

## 功能

**适用NF：NCG**

该命令用于删除已添加的话单费率组。

执行任务之前，可执行 [**LST RGINFO**](显示费率组信息（LST RGINFO）_51174324.md) 命令查询当前系统中的费率组信息，找到对应的费率组ID。

## 注意事项

删除费率组信息，可能会导致以费率组ID为对象的流量统计信息不全。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RGID | 费率组ID | 可选必选说明：必选参数<br>参数含义：该参数用于表示用户话单所属的费率组。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～4294967295。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@RGINFO]] · 费率组信息（RGINFO）

## 使用实例

删除ID为“33”的费率组：

```
RMV RGINFO: RGID=33;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-RGINFO.md`
