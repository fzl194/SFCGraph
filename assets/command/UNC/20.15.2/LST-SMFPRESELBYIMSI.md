---
id: UNC@20.15.2@MMLCommand@LST SMFPRESELBYIMSI
type: MMLCommand
name: LST SMFPRESELBYIMSI（查询基于IMSI优选指定SMF配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: SMFPRESELBYIMSI
command_category: 查询类
applicable_nf:
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 移动性管理
- NF发现和选择管理
- SMF优选策略管理
status: active
---

# LST SMFPRESELBYIMSI（查询基于IMSI优选指定SMF配置）

## 功能

**适用NF：AMF**

该命令用于查询基于IMSI优选指定SMF配置。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IMSI | IMSI | 可选必选说明：可选参数<br>参数含义：该参数用于指定进行优选指定SMF的用户IMSI。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是14~15。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/SMFPRESELBYIMSI]] · 基于IMSI优选指定SMF配置（SMFPRESELBYIMSI）

## 使用实例

查询IMSI为“123456789012345”的用户优选指定SMF配置，执行如下命令：

```
%%LST SMFPRESELBYIMSI:IMSI="123456789012345";%%
RETCODE = 0  操作成功

结果如下
--------
     IMSI  =  123456789012345
SMF实例ID  =  a6a61c6f-0d3a-4221-b1da-424eda3ccf67
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询基于IMSI优选指定SMF配置（LST-SMFPRESELBYIMSI）_20333897.md`
