---
id: UNC@20.15.2@MMLCommand@LST APNLOCREPORT
type: MMLCommand
name: LST APNLOCREPORT（查询用户位置上报配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: APNLOCREPORT
command_category: 查询类
applicable_nf:
- PGW-C
- SMF
- GGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- 位置上报管理
- APN用户位置信息上报开关
status: active
---

# LST APNLOCREPORT（查询用户位置上报配置）

## 功能

**适用NF：PGW-C、SMF、GGSN**

该命令用于查询基于APN的用户位置上报信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APN | APN名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定APN实例名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”等特殊字符，不区分大小写。<br>默认值：无<br>配置原则：<br>该参数必须已经通过命令ADD APN配置。 |

## 操作的配置对象

- [基于APN的位置上报配置（APNLOCREPORT）](configobject/UNC/20.15.2/APNLOCREPORT.md)

## 使用实例

显示APN为“HUAWEI.COM”的位置上报配置：

```
%%LST APNLOCREPORT: APN="HUAWEI.COM";%%
            RETCODE = 0  操作成功。

            结果如下
            --------
            APN  =  huawei.com
            配置用户位置信息的trigger  =  使能
            配置路由区域的trigger  =  不使能
            配置跟踪区域的trigger  =  使能
            配置演进的全球小区的trigger  =  使能
            配置5G NR全球小区的trigger =  使能
            基于用户漫游属性控制ULI信息上报  =  NULL
            基于用户漫游属性控制RAI信息上报  =  NULL
            基于用户漫游属性控制TAI信息上报  =  NULL
            基于用户漫游属性控制ECGI信息上报  =  NULL
            基于用户漫游属性控制NCGI信息上报  =  NULL
            基于用户RAT类型控制ULI信息上报  =  NULL
            基于用户RAT类型控制RAI信息上报  =  NULL
            基于用户RAT类型控制TAI信息上报  =  NULL
            基于用户RAT类型控制ECGI信息上报  =  NULL
            位置更新消息上报的迟滞控制时长(秒) =  0
            (结果个数 = 1)
            ---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询用户位置上报配置（LST-APNLOCREPORT）_86372758.md`
