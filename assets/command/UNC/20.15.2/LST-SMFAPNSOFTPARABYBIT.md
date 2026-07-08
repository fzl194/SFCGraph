---
id: UNC@20.15.2@MMLCommand@LST SMFAPNSOFTPARABYBIT
type: MMLCommand
name: LST SMFAPNSOFTPARABYBIT（查询SMF APN软件参数比特位）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: SMFAPNSOFTPARABYBIT
command_category: 查询类
applicable_nf:
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- 软件参数管理
status: active
---

# LST SMFAPNSOFTPARABYBIT（查询SMF APN软件参数比特位）

## 功能

**适用NF：SMF**

该命令用于查询SMF APN软件参数，查询结果以二进制形式输出。同时，该命令也支持查询指定软件参数中某个比特位的值。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APN | APN | 可选必选说明：必选参数<br>参数含义：该参数用于指定APN实例名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。字符串类型，输入长度范围为1～63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”特殊字符，不区分大小写。<br>默认值：无<br>配置原则：无 |
| DT | 数据类型 | 可选必选说明：必选参数<br>参数含义：该参数表示软件参数的数据类型。<br>数据来源：本端规划<br>取值范围：<br>- Dw（双字）<br>- Byte（字节）<br>默认值：无<br>配置原则：无 |
| DWORDNUM | Dword索引 | 可选必选说明：该参数在"DT"配置为"Dw"时为条件可选参数。<br>参数含义：该参数表示Dword类型软件参数的索引。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~16。<br>默认值：无<br>配置原则：无 |
| BYTENUM | Byte索引 | 可选必选说明：该参数在"DT"配置为"Byte"时为条件可选参数。<br>参数含义：该参数表示Byte类型软件参数的索引。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~8。<br>默认值：无<br>配置原则：无 |
| POSITION | 比特位 | 可选必选说明：可选参数<br>参数含义：该参数表示软件参数比特位的位置。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~64。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@SMFAPNSOFTPARABYBIT]] · SMF APN软件参数比特位（SMFAPNSOFTPARABYBIT）

## 使用实例

查询APN为huawei.com数据类型为双字的软参值：

```
%%LST SMFAPNSOFTPARABYBIT: APN="huawei.com", DT=Dw;%%
RETCODE = 0  Operation succeeded

The result is as follows
------------------------
APN         Data Type  Soft para number  Bit position  Soft para value                          

huawei.com  Dword      1                 NULL          0000 0000 0000 0000 0000 0000 0000 0000  
huawei.com  Dword      2                 NULL          0000 0000 0000 0000 0000 0000 1111 1101  
(Number of results = 2)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-SMFAPNSOFTPARABYBIT.md`
