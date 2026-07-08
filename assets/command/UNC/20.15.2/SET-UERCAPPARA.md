---
id: UNC@20.15.2@MMLCommand@SET UERCAPPARA
type: MMLCommand
name: SET UERCAPPARA（设置UE Radio Capability信元参数）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: UERCAPPARA
command_category: 配置类
applicable_nf:
- SGSN
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 移动性管理
- UE无线能力参数
status: active
---

# SET UERCAPPARA（设置UE Radio Capability信元参数）

## 功能

**适用网元：SGSN、MME**

该命令用于配置根据UE无线能力的参数，设置告警阈值。

## 注意事项

该命令执行后立即生效。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| REPORTALM | 上报告警百分比 | 可选必选说明：可选参数。<br>参数含义：该参数表示上报<br>[ALM-80717 4G UE无线能力处理超出上限](../../../../../../../../网络运维/故障处理/UNC告警处理/业务告警/SGSN&MME/ALM-80717 4G UE无线能力处理超出上限_24366550.md)<br>告警的百分比。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是1~100。<br>默认值：95。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过相关查询命令获取当前参数配置值。<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/UERCAPPARA]] · UE Radio Capability信元参数（UERCAPPARA）

## 使用实例

设置UE Radio Capability信元参数， “上报告警百分比” 设置为20；

```
SET UERCAPPARA: REPORTALM=20;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/设置UE-Radio-Capability信元参数（SET-UERCAPPARA）_72749349.md`
