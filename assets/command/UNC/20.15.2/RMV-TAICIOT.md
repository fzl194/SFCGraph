---
id: UNC@20.15.2@MMLCommand@RMV TAICIOT
type: MMLCommand
name: RMV TAICIOT（删除CIoT能力配置）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: TAICIOT
command_category: 配置类
applicable_nf:
- MME
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 业务安全管理
- M2M管理
- CIoT能力配置
status: active
---

# RMV TAICIOT（删除CIoT能力配置）

## 功能

**适用网元：MME**

该命令用于删除TAI范围内所有eNodeB的蜂窝物联网（CIoT）能力。

## 注意事项

- 该命令执行后，在用户新的Attach/TAU流程中系统将不会识别eNodeB的蜂窝物联网（CIoT）能力。
- 删除配置后，MME默认eNodeB支持CP CIoT。
- 如果不输入任何参数，执行该命令会删除所有记录。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| BEGINTAI | 起始TAI | 可选必选说明：可选参数<br>参数含义：该参数用于指定跟踪区标识，标识一个起始跟踪区。<br>数据来源：全网规划<br>取值范围：9～10位的字符串。<br>默认值：无<br>配置原则：输入的起始TAI必须是系统中已存在记录的起始TAI。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/TAICIOT]] · CIoT能力配置（TAICIOT）

## 使用实例

假设用户需要删除起始TAI为308015101的CIoT能力配置：

RMV TAICIOT: BEGINTAI="308015101";

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除CIoT能力配置(RMV-TAICIOT)_72345381.md`
