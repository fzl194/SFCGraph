---
id: UNC@20.15.2@MMLCommand@MOD TACGROUPINNSSF
type: MMLCommand
name: MOD TACGROUPINNSSF（修改跟踪区域码分组记录）
nf: UNC
version: 20.15.2
verb: MOD
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

# MOD TACGROUPINNSSF（修改跟踪区域码分组记录）

## 功能

**适用NF：NSSF**

该命令用于修改跟踪区域码分组记录。

## 注意事项

- 该命令执行后立即生效。

- 主备或双活组网的场景下，如果需要配置此命令，则两个NSSF上均需执行此命令，且配置参数一致。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| INDEX | 索引 | 可选必选说明：必选参数<br>参数含义：该参数用于描述命令的索引值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~4294967295。<br>默认值：无<br>配置原则：无 |
| TACGROUPNAME | 跟踪区域码分组名称 | 可选必选说明：可选参数<br>参数含义：该参数用于描述跟踪区代码分组的名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~255。<br>默认值：无<br>配置原则：无 |
| TACSTART | TAC起始字符 | 可选必选说明：可选参数<br>参数含义：该参数用于表示TAI路由的TAC起始字符。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是4~6。该参数只能由字母（A-F或者a-f）、数字（0-9）组成。<br>默认值：无<br>配置原则：无 |
| TACEND | TAC结束字符 | 可选必选说明：可选参数<br>参数含义：该参数用于表示TAI路由的TAC结束字符。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是4~6。该参数只能由字母（A-F或者a-f）、数字（0-9）组成。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@TACGROUPINNSSF]] · 跟踪区域码分组记录（TACGROUPINNSSF）

## 使用实例

假如运营商希望将已有索引为1记录修改为跟踪区域码分组名称为"TACGROUP01"、TAC起始字符为"010101"、TAC结束字符为"010105"，执行下列命令。

```
MOD TACGROUPINNSSF: INDEX=1, TACGROUPNAME="TACGROUP01", TACSTART="010101", TACEND="010105";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/MOD-TACGROUPINNSSF.md`
