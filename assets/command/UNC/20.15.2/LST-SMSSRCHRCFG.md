---
id: UNC@20.15.2@MMLCommand@LST SMSSRCHRCFG
type: MMLCommand
name: LST SMSSRCHRCFG（查询SMS小范围CHR上报规则配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: SMSSRCHRCFG
command_category: 查询类
applicable_nf:
- SMSF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- SMSF业务管理
- CHR管理
status: active
---

# LST SMSSRCHRCFG（查询SMS小范围CHR上报规则配置）

## 功能

**适用NF：SMSF**

该命令用于查询SMS小范围CHR上报规则配置。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SUBRANGE | 用户范围 | 可选必选说明：可选参数<br>参数含义：该参数用于指定配置小范围CHR的用户范围。<br>数据来源：本端规划<br>取值范围：<br>- “SPECIFIC_IMSI（指定用户IMSI）”：表示指定用户IMSI。<br>默认值：无<br>配置原则：无 |
| IMSIPRE | IMSI前缀 | 可选必选说明：该参数在"SUBRANGE"配置为"SPECIFIC_IMSI"时为条件可选参数。<br>参数含义：该参数用于指定IMSI前缀。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是5~15。只允许输入十进制数字（0-9）。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@SMSSRCHRCFG]] · SMS小范围CHR上报规则配置（SMSSRCHRCFG）

## 使用实例

运营商希望查询SMS小范围CHR上报规则配置，执行如下命令 ：

```
LST SMSSRCHRCFG:;
%%LST SMSSRCHRCFG:;%%
RETCODE = 0  操作成功

结果如下：
------------------------
用户范围 =  指定用户IMSI
IMSI前缀  =  12303120010
流程控制模板索引 = 2
       
(结果个数 = 1)
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-SMSSRCHRCFG.md`
