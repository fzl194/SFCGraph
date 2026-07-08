---
id: UDG@20.15.2@MMLCommand@LST APNAPPPARA
type: MMLCommand
name: LST APNAPPPARA（显示基于APN的应用参数）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: APNAPPPARA
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 用户面服务管理
- 业务匹配策略
- 业务匹配公共配置
- 业务公共参数管理
- APN应用参数配置
status: active
---

# LST APNAPPPARA（显示基于APN的应用参数）

## 功能

**适用NF：PGW-U、UPF**

该命令用于显示基于APN的应用参数配置。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APN | APN | 可选必选说明：可选参数<br>参数含义：用于指定APN实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”特殊字符，不区分大小写。<br>默认值：无<br>配置原则：不指定APN时，显示所有APN的参数配置。 |

## 操作的配置对象

- [基于APN的应用参数（APNAPPPARA）](configobject/UDG/20.15.2/APNAPPPARA.md)

## 使用实例

显示基于APN的应用参数：

```
LST APNAPPPARA: APN="apn1";
```

```

RETCODE = 0  操作成功。

APN的应用参数
-------------------------------
APN  =  apn1
APP规则生效条件  =  INHERIT
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/显示基于APN的应用参数（LST-APNAPPPARA）_74982442.md`
