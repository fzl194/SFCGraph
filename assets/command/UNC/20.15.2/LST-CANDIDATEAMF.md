---
id: UNC@20.15.2@MMLCommand@LST CANDIDATEAMF
type: MMLCommand
name: LST CANDIDATEAMF（查询候选AMF）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: CANDIDATEAMF
command_category: 查询类
applicable_nf:
- NSSF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- NSSF业务及策略管理
- 候选AMF配置管理
status: active
---

# LST CANDIDATEAMF（查询候选AMF）

## 功能

**适用NF：NSSF**

该命令用于查询候选AMF记录。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| INDEX | 索引 | 可选必选说明：可选参数<br>参数含义：该参数用于描述命令的索引值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~4294967295。<br>默认值：无<br>配置原则：无 |
| AMFINSTANCEID | AMF实例标识 | 可选必选说明：可选参数<br>参数含义：该参数用于描述全局唯一的AMF标识。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~255。该参数只能由字母（A-Z或者a-z）、数字（0-9）、中划线（-）组成，不区分大小写。<br>默认值：无<br>配置原则：无 |
| MCC | 移动国家码 | 可选必选说明：可选参数<br>参数含义：该参数用于描述移动国家码。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度是3。3位十进制数。<br>默认值：无<br>配置原则：<br>该参数需要与ADD AMFSETID命令中MCC参数配置保持一致。 |
| MNC | 移动网号 | 可选必选说明：可选参数<br>参数含义：该参数用于描述移动网号。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是2~3。2位或者3位十进制数。<br>默认值：无<br>配置原则：<br>该参数需要与ADD AMFSETID命令中MNC参数配置保持一致。 |
| REGIONID | 区域ID | 可选必选说明：可选参数<br>参数含义：该参数用于描述AMF区域ID。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度是2。按照十六进制输入，输入时不带0x，不足两位时需手动从左边补0，取值范围00~ff。<br>默认值：无<br>配置原则：无 |
| AMFSETID | AMF集合标识 | 可选必选说明：可选参数<br>参数含义：该参数用于描述AMF集合的标识。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度是3。按照十六进制输入，输入时不带0x，不足三位时需手动从左边补0，取值范围000~3ff。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/CANDIDATEAMF]] · 候选AMF（CANDIDATEAMF）

## 使用实例

若运营商希望查询所有的候选AMF数据，执行下列命令。

```
LST CANDIDATEAMF:;
%%LST CANDIDATEAMF:;%%
RETCODE = 0  操作成功

The result is as follows
------------------------
       索引  =  1
AMF实例标识  =  AMF01
 移动国家码  =  460
   移动网号  =  03
     区域ID  =  01
AMF集合标识  =  001
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-CANDIDATEAMF.md`
