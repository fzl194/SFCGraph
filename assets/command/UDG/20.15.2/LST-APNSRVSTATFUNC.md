---
id: UDG@20.15.2@MMLCommand@LST APNSRVSTATFUNC
type: MMLCommand
name: LST APNSRVSTATFUNC（查询APN业务统计开关）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: APNSRVSTATFUNC
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 业务运维
- 业务性能统计管理
- APN的业务统计开关设置
status: active
---

# LST APNSRVSTATFUNC（查询APN业务统计开关）

## 功能

**适用NF：PGW-U、UPF**

该命令用于显示指定APN的ServiceStatistic检测功能配置信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APN | APN | 可选必选说明：可选参数<br>参数含义：该参数用于指定APN的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”特殊字符，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [APN业务统计开关（APNSRVSTATFUNC）](configobject/UDG/20.15.2/APNSRVSTATFUNC.md)

## 使用实例

假如运营商需要查询APN为“apntest”的ServiceStatistic检测功能配置，则命令如下：

```
LST APNSRVSTATFUNC:;
```

```

RETCODE = 0  操作成功。

APN 业务统计开关信息
--------------------
     APN  =  apntest
开关标识  =  不使能
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询APN业务统计开关（LST-APNSRVSTATFUNC）_82837849.md`
