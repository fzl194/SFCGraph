---
id: UNC@20.15.2@MMLCommand@LST TACGROUPINNSSF
type: MMLCommand
name: LST TACGROUPINNSSF（查询跟踪区域码分组记录）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: TACGROUPINNSSF
command_category: 查询类
applicable_nf:
- NSSF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- NSSF业务及策略管理
- TAC分组配置管理
status: active
---

# LST TACGROUPINNSSF（查询跟踪区域码分组记录）

## 功能

**适用NF：NSSF**

该命令用于查询跟踪区域码分组记录。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| INDEX | 索引 | 可选必选说明：可选参数<br>参数含义：该参数用于描述命令的索引值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~4294967295。<br>默认值：无<br>配置原则：无 |
| TACGROUPNAME | 跟踪区域码分组名称 | 可选必选说明：可选参数<br>参数含义：该参数用于描述跟踪区代码分组的名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~255。<br>默认值：无<br>配置原则：无 |
| TACSTART | TAC起始字符 | 可选必选说明：可选参数<br>参数含义：该参数用于表示TAI路由的TAC起始字符。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是4~6。该参数只能由字母（A-F或者a-f）、数字（0-9）组成。<br>默认值：无<br>配置原则：无 |
| TACEND | TAC结束字符 | 可选必选说明：可选参数<br>参数含义：该参数用于表示TAI路由的TAC结束字符。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是4~6。该参数只能由字母（A-F或者a-f）、数字（0-9）组成。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/TACGROUPINNSSF]] · 跟踪区域码分组记录（TACGROUPINNSSF）

## 使用实例

若运营商希望查询所有的TACGROUP数据，执行下列命令。

```
LST TACGROUPINNSSF:;
%%LST TACGROUPINNSSF:;%%
RETCODE = 0  操作成功

结果如下
------------------------
              索引  =  1
跟踪区域码分组名称  =  TACGROUP01
       TAC起始字符  =  010101
       TAC结束字符  =  010105
(结果个数 = 1)
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-TACGROUPINNSSF.md`
