---
id: UNC@20.15.2@MMLCommand@RMV TACGROUPINNSSF
type: MMLCommand
name: RMV TACGROUPINNSSF（删除跟踪区域码分组记录）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: TACGROUPINNSSF
command_category: 配置类
applicable_nf:
- NSSF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- NSSF业务及策略管理
- TAC分组配置管理
status: active
---

# RMV TACGROUPINNSSF（删除跟踪区域码分组记录）

## 功能

**适用NF：NSSF**

该命令用于删除一个跟踪区域码分组记录。

## 注意事项

- 该命令执行后立即生效。

- 主备或双活组网的场景下，如果需要配置此命令，则两个NSSF上均需执行此命令，且配置参数一致。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| INDEX | 索引 | 可选必选说明：必选参数<br>参数含义：该参数用于描述命令的索引值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~4294967295。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/TACGROUPINNSSF]] · 跟踪区域码分组记录（TACGROUPINNSSF）

## 使用实例

假如运营商希望删除INDEX为1的记录，执行下列命令。

```
RMV TACGROUPINNSSF: INDEX=1;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除跟踪区域码分组记录（RMV-TACGROUPINNSSF）_18715638.md`
