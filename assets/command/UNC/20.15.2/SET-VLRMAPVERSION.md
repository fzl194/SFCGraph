---
id: UNC@20.15.2@MMLCommand@SET VLRMAPVERSION
type: MMLCommand
name: SET VLRMAPVERSION（设置VLR使用的MAP接口版本）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: VLRMAPVERSION
command_category: 配置类
applicable_nf:
- SMSF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- VLR业务管理
- MAP版本号管理
status: active
---

# SET VLRMAPVERSION（设置VLR使用的MAP接口版本）

## 功能

**适用NF：SMSF**

该命令用于设置VLR对接HLR业务中使用的MAP接口版本号。

## 注意事项

- 该命令执行后立即生效。

- 双活组网的场景下，如果需要配置此命令，则两个VLR上均需执行此命令，且配置参数一致。当前不支持V1、V2。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| MAPVERSION |
| --- |
| V3 |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MAPVERSION | MAP版本号 | 可选必选说明：必选参数<br>参数含义：该参数用于表示VLR对接HLR业务中使用的MAP接口版本号。<br>数据来源：本端规划<br>取值范围：<br>- “V1（V1）”：MAP接口使用的版本号为V1。<br>- “V2（V2）”：MAP接口使用的版本号为V2。<br>- “V3（V3）”：MAP接口使用的版本号为V3。<br>默认值：无。<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/VLRMAPVERSION]] · VLR使用的MAP接口版本（VLRMAPVERSION）

## 使用实例

运营商希望设置VLR对接HLR业务中使用的“MAP接口版本号”为“V3”，执行如下命令：

```
SET VLRMAPVERSION: MAPVERSION=V3;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/SET-VLRMAPVERSION.md`
