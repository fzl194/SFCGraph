---
id: UNC@20.15.2@MMLCommand@SET SMSFMAPVERSION
type: MMLCommand
name: SET SMSFMAPVERSION（设置SMSF使用的MAP接口版本）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: SMSFMAPVERSION
command_category: 配置类
applicable_nf:
- SMSF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- SMSF业务管理
- 版本号管理
- MAP版本号管理
status: active
---

# SET SMSFMAPVERSION（设置SMSF使用的MAP接口版本）

## 功能

**适用NF：SMSF**

该命令用于设置SMSF/VLR在MO流程中使用的MAP接口版本号。

## 注意事项

- 该命令执行后立即生效。

- 双活组网的场景下，如果需要配置此命令，则两个SMSF上均需执行此命令，且配置参数一致。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| MAPVERSION |
| --- |
| V2Plus |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MAPVERSION | MAP 版本号 | 可选必选说明：必选参数<br>参数含义：该参数用于表示指定MO流程中MAP接口使用的版本号。<br>数据来源：全网规划<br>取值范围：<br>- “V2（V2）”：MAP接口使用的版本号为v2<br>- “V2Plus（V2+）”：MAP接口使用的版本号为v2+。<br>默认值：无。<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/SMSFMAPVERSION]] · SMSF使用的MAP接口版本（SMSFMAPVERSION）

## 使用实例

运营商希望设置MAP接口使用的版本号为V2，执行如下命令：

```
SET SMSFMAPVERSION: MAPVERSION=V2;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/设置SMSF使用的MAP接口版本（SET-SMSFMAPVERSION）_44008048.md`
