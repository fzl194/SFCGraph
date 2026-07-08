---
id: UNC@20.15.2@MMLCommand@LST RESTRICTSNSSAI
type: MMLCommand
name: LST RESTRICTSNSSAI（查询受限的S-NSSAI）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: RESTRICTSNSSAI
command_category: 查询类
applicable_nf:
- NSSF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- NSSF业务及策略管理
- 受限的S-NSSAI配置管理
status: active
---

# LST RESTRICTSNSSAI（查询受限的S-NSSAI）

## 功能

**适用NF：NSSF**

该命令用于查询受限的S-NSSAI列表。

## 注意事项

查询条件都不填时，即查询所有。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| INDEX | 索引 | 可选必选说明：可选参数<br>参数含义：该参数用于描述命令的索引值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~4294967295。<br>默认值：无<br>配置原则：无 |
| MCC | 移动国家码 | 可选必选说明：可选参数<br>参数含义：该参数用于描述移动国家码。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度是3。3位十进制数。<br>默认值：无<br>配置原则：无 |
| MNC | 移动网号 | 可选必选说明：可选参数<br>参数含义：该参数用于描述移动网号。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是2~3。2位或者3位十进制数。<br>默认值：无<br>配置原则：无 |
| TAC | 跟踪区域码 | 可选必选说明：可选参数<br>参数含义：该参数用于描述跟踪区域码。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是4~6。该参数只能由字母（A-F或者a-f）、数字（0-9）组成。<br>默认值：无<br>配置原则：无 |
| SST | 切片服务类型 | 可选必选说明：可选参数<br>参数含义：该参数用于描述切片服务类型。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是0~255。<br>默认值：无<br>配置原则：无 |
| SD | 切片细分标识 | 可选必选说明：可选参数<br>参数含义：该参数用于表示切片细分标识。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度是6。该参数只能由字母（A-F或者a-f）、数字（0-9）组成。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/RESTRICTSNSSAI]] · 受限的S-NSSAI（RESTRICTSNSSAI）

## 使用实例

若运营商希望查询所有的数据，执行下列命令。

```
LST RESTRICTSNSSAI:;
%%LST RESTRICTSNSSAI:;%%
RETCODE = 0  操作成功

操作结果如下
------------
        索引  =  1
  移动国家码  =  460
    移动网号  =  03
  跟踪区域码  =  0101
切片服务类型  =  1
切片细分标识  =  010101
        描述  =  NULL
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-RESTRICTSNSSAI.md`
