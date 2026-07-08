---
id: UNC@20.15.2@MMLCommand@SET IFMTUFRAGMODE
type: MMLCommand
name: SET IFMTUFRAGMODE（设置分片方式）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: IFMTUFRAGMODE
command_category: 配置类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- IP性能配置
- 分片方式配置
status: active
---

# SET IFMTUFRAGMODE（设置分片方式）

## 功能

该命令用来配置Label+IP分片方式。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| FRAGMODE | 分片方式 | 可选必选说明：必选参数<br>参数含义：该参数用于表示分片方式信息。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- FRACHECKMODE_IP：IP分片方式。<br>- FRACHECKMODE_LABELANDIP：标签加IP分片方式。<br>默认值：无 |

## 操作的配置对象

- [分片方式（IFMTUFRAGMODE）](configobject/UNC/20.15.2/IFMTUFRAGMODE.md)

## 使用实例

配置接口Label+IP分片方式：

```
SET IFMTUFRAGMODE:FRAGMODE=FRACHECKMODE_LABELANDIP;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/设置分片方式（SET-IFMTUFRAGMODE）_00866285.md`
