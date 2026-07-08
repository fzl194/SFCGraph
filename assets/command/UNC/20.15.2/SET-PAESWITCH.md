---
id: UNC@20.15.2@MMLCommand@SET PAESWITCH
type: MMLCommand
name: SET PAESWITCH（设置PAE隔离核统计状态）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: PAESWITCH
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- 系统管理
- 资源管理
status: active
---

# SET PAESWITCH（设置PAE隔离核统计状态）

## 功能

该命令用于设置PAE隔离核查询开关，若打开，则计算VM/容器CPU利用率包括PAE隔离核；若关闭，则计算VM/容器CPU利用率不包括PAE隔离核。

## 注意事项

- 该命令执行后立即生效。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| SWITCH |
| --- |
| DISABLE |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SWITCH | PAE隔离核统计开关 | 可选必选说明：必选参数<br>参数含义：该参数表示计算节点CPU利用率是否包含PAE隔离核。<br>数据来源：本端规划<br>取值范围：<br>- “ENABLE（包括PAE隔离核）”：包括PAE隔离核<br>- “DISABLE（去除PAE隔离核）”：去除PAE隔离核<br>默认值：无。<br>配置原则：无 |

## 操作的配置对象

- [PAE开关信息（PAESWITCH）](configobject/UNC/20.15.2/PAESWITCH.md)

## 使用实例

开启PAE隔离核查询。

```
SET PAESWITCH: SWITCH=ENABLE;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/设置PAE隔离核统计状态（SET-PAESWITCH）_31564778.md`
