---
id: UNC@20.15.2@MMLCommand@LST SMFINFOEXT
type: MMLCommand
name: LST SMFINFOEXT（查询SMF扩展信息）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: SMFINFOEXT
command_category: 查询类
applicable_nf:
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 本局信息管理
- SMF
- SMF信息管理
status: active
---

# LST SMFINFOEXT（查询SMF扩展信息）

## 功能

**适用NF：SMF**

该命令用以查询SMF实例的扩展信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SMFINSTANCENAME | SMF实例名称 | 可选必选说明：可选参数<br>参数含义：该参数用于在服务组（Service Group，简称SG）中唯一指定某个SMF实例。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~50。本参数的构成字符只能是字母A~Z或a~z、数字0~9、下划线“_”和中划线“-”，例如，SMF_Instance_0。<br>默认值：无<br>配置原则：<br>该参数可以参考LST SMFINFO中的SMFINSTANCENAME。 |
| ID | SMFINFOID | 可选必选说明：可选参数<br>参数含义：该参数用于唯一标识SMF实例中的某个SmfInfo。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~32。本参数的构成字符只能是字母A~Z或a~z、数字0~9、下划线“_”和中划线“-”。该参数大小写不敏感。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/SMFINFOEXT]] · SMF扩展信息（SMFINFOEXT）

## 使用实例

查询SMF实例的扩展信息：

```
%%LST SMFINFOEXT:;%%
RETCODE = 0  操作成功

结果如下
--------
      SMF实例名称  =  SMF_Instance_0
        SMFINFOID  =  central
           优先级  =  111
          PGW名称  =  NULL
         接入类型  =  3GPP接入类型
是否支持作为I-SMF  =  无效值
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-SMFINFOEXT.md`
