---
id: UNC@20.15.2@MMLCommand@SET BTRUNCFUNC
type: MMLCommand
name: SET BTRUNCFUNC（设置宽带集群系统扩展功能）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: BTRUNCFUNC
command_category: 配置类
applicable_nf:
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 移动性管理
- 宽带集群系统扩展功能管理
status: active
---

# SET BTRUNCFUNC（设置宽带集群系统扩展功能）

## 功能

**适用NF：MME**

此命令用于设置专网中，宽带集群系统支持的扩展功能。

## 注意事项

- 该命令执行后立即生效。
- 开关“是否支持集群业务”打开，对于TSN双备场景会向eNB同步MME设备能力为0，影响新用户接入。
- 开关“是否支持集群业务”打开时，MME会向TSN同步未同步的基站TA信息，导致TM接口消息突增。

## 权限

manage-ug;system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| BTRUNC | 是否支持集群业务 | 可选必选说明：可选参数<br>参数含义：该参数当前系统是否支持宽带集群业务。在开启的情况下，系统需要与TSN网元交互，完成集群用户相关业务。<br>数据来源：全网规划<br>取值范围：<br>- “YES(是)”<br>- “NO(否)”<br>系统初始设置值：“NO(否)” |

## 操作的配置对象

- [[configobject/UNC/20.15.2/BTRUNCFUNC]] · 宽带集群系统扩展功能（BTRUNCFUNC）

## 使用实例

系统开启宽带集群系统扩展功能，支持集群用户业务：

```
SET BTRUNCFUNC:BTRUNC=YES;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/设置宽带集群系统扩展功能(SET-BTRUNCFUNC)_41660661.md`
