---
id: UDG@20.15.2@MMLCommand@LST APNREPORTATTR
type: MMLCommand
name: LST APNREPORTATTR（查询ApnReportAttr配置）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: APNREPORTATTR
command_category: 查询类
applicable_nf:
- SGW-U
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- DN管理
- APN管理
- APN上报属性
status: active
---

# LST APNREPORTATTR（查询ApnReportAttr配置）

## 功能

**适用NF：SGW-U、PGW-U、UPF**

该命令用于查询性能统计，头增强，给CloudUDN上报记录时，与其他网元交互和支持拥塞控制使用的APN类型。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APN | APN名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定配置上报属性的APN。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”特殊字符，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/APNREPORTATTR]] · ApnReportAttr配置（APNREPORTATTR）

## 使用实例

查询APN apn1.com下性能统计，头增强，给CloudUDN上报记录时，与其他网元交互时和支持拥塞控制使用的APN类型：

```
LST APNREPORTATTR:APN="apn1.com";
```

```

RETCODE = 0  操作成功。

APN的上报配置信息
-----------------
                      APN名称  =  apn1.com
          上报给头增强的APN名  =  请求的
            上报给话统的APN名  =  请求的
      上报给报表服务器的APN名  =  请求的
                     拥塞控制  =  使能
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询ApnReportAttr配置（LST-APNREPORTATTR）_16615230.md`
