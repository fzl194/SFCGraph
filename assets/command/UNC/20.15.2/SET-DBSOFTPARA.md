---
id: UNC@20.15.2@MMLCommand@SET DBSOFTPARA
type: MMLCommand
name: SET DBSOFTPARA（设置CSDB软件调试参数表）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: DBSOFTPARA
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- CSDB功能管理
- CSDB管理
- 软件参数管理
status: active
---

# SET DBSOFTPARA（设置CSDB软件调试参数表）

## 功能

该命令用于设置CSDB功能开关。

## 注意事项

- 系统初次上电运行时，会执行系统初始设置值。
- 该命令执行后立即生效。
- 该命令参数的具体说明请参见产品文档中“CSDB软件参数”。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PARAID | 参数标识 | 可选必选说明：必选参数。<br>参数含义：该参数用于指定唯一一个参数标识号。<br>数据来源：本端规划<br>取值范围：0～1023。<br>默认值：无。 |
| PARAVALUE | 参数值 | 可选必选说明：必选参数。<br>参数含义：该参数用于指定参数的取值。<br>数据来源：本端规划<br>取值范围：0～4294967295。<br>默认值：无。 |

## 操作的配置对象

- [CSDB软件调试参数表（DBSOFTPARA）](configobject/UNC/20.15.2/DBSOFTPARA.md)

## 使用实例

设置 “参数标识” 为 “1” 、 “参数值” 为 “1” 的软调参数：

```
SET DBSOFTPARA: PARAID=1, PARAVALUE=1;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/设置CSDB软件调试参数表(SET-DBSOFTPARA)_80429704.md`
