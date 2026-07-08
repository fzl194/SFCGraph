---
id: UNC@20.15.2@MMLCommand@RMV TALST
type: MMLCommand
name: RMV TALST（删除跟踪区列表）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: TALST
command_category: 配置类
applicable_nf:
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 移动性管理
- TA List管理
status: active
---

# RMV TALST（删除跟踪区列表）

## 功能

**适用网元：MME**

该命令用于删除跟踪区列表或删除跟踪区列表中的一个跟踪区。

## 注意事项

- 该命令执行后立即生效。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TALISTID | TA List 标号 | 可选必选说明：必选参数<br>参数含义：该参数用来指定一个要删除记录的跟踪区列表标识。<br>取值范围：0~65534<br>默认值：无<br>说明：如果只填入跟踪区列表标识，则系统将删除所有跟踪区列表标识匹配的记录。 |
| TAI | TAI | 可选必选说明：可选参数<br>参数含义：该参数用于指定一个待删除的跟踪区。<br>取值范围：9~10位字符串<br>默认值：无<br>说明：同时填入跟踪区列表标识和跟踪区标识只能删除唯一匹配的一条记录。 |

## 操作的配置对象

- [跟踪区列表（TALST）](configobject/UNC/20.15.2/TALST.md)

## 使用实例

1. 删除ID号为0的跟踪区列表：
  RMV TALST: TALISTID=0;
2. 删除ID号为0的跟踪区列表下的ID号为308015101的跟踪区：
  RMV TALST: TALISTID=0, TAI="308015101";

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除跟踪区列表(RMV-TALST)_72345175.md`
