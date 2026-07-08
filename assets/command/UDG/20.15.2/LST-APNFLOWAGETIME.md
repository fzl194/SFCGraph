---
id: UDG@20.15.2@MMLCommand@LST APNFLOWAGETIME
type: MMLCommand
name: LST APNFLOWAGETIME（查询APN五元组老化时间）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: APNFLOWAGETIME
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 业务匹配策略
- 业务匹配公共配置
- 业务五元组管理
- APN五元组节点老化时间
status: active
---

# LST APNFLOWAGETIME（查询APN五元组老化时间）

## 功能

**适用NF：PGW-U、UPF**

该命令用于查询指定APN下的五元组老化时间。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APN | APN名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定APN实例名。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”等特殊字符，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@APNFLOWAGETIME]] · APN五元组老化时间（APNFLOWAGETIME）

## 使用实例

查询APN五元组老化时间：

```
LST APNFLOWAGETIME: APN="aa";
```

```

RETCODE = 0  操作成功。

APN五元组老化时间信息
---------------------
                APN名称  =  aa
APN五元组老化时间（秒）  =  100
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-APNFLOWAGETIME.md`
