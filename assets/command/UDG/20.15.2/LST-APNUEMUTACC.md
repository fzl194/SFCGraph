---
id: UDG@20.15.2@MMLCommand@LST APNUEMUTACC
type: MMLCommand
name: LST APNUEMUTACC（查询APN下用户互访控制配置）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: APNUEMUTACC
command_category: 查询类
applicable_nf:
- UPF
- PGW-U
effect_mode: 立即生效
is_dangerous: false
category_path:
- 用户面服务管理
- 业务安全防护
- 用户攻击防护
- 用户互访控制
- APN用户互访控制
status: active
---

# LST APNUEMUTACC（查询APN下用户互访控制配置）

## 功能

**适用NF：UPF、PGW-U**

该命令用于查询APN下用户互访禁止功能开关是否开启，包括APN间的用户互访及APN内的用户互访。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APN | APN名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定APN实例名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”特殊字符，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@APNUEMUTACC]] · APN下用户互访控制配置（APNUEMUTACC）

## 使用实例

查询APN为apn1.com的用户互访禁止功能开关是否开启：

```
LST APNUEMUTACC: APN="apn1.com";
```

```

RETCODE = 0  操作成功。

APN下用户互访禁止开关
---------------------
不同APN间的控制开关          =  使能
  同APN内的控制开关          =  使能
          APN名称           =  apn1.com
同APN内S5S8P口互访控制开关   = 使能
同APN内N9A口互访控制开关     = 使能
不同APN间S5S8P口互访控制开关 = 使能
不同APN间N9A口互访控制开关   = 使能
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-APNUEMUTACC.md`
