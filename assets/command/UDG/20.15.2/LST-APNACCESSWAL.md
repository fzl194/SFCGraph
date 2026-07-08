---
id: UDG@20.15.2@MMLCommand@LST APNACCESSWAL
type: MMLCommand
name: LST APNACCESSWAL（查询Apn接入速率配置）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: APNACCESSWAL
command_category: 查询类
applicable_nf:
- SGW-U
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 会话管理
- 会话信息管理
- APN的接入速率属性配置
status: active
---

# LST APNACCESSWAL（查询Apn接入速率配置）

## 功能

**适用NF：SGW-U、PGW-U、UPF**

该命令用来查询APN的接入速率。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APN | APN名称 | 可选必选说明：必选参数<br>参数含义：指定APN实例名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“ ” ”、“ ` ”特殊字符，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/APNACCESSWAL]] · Apn接入速率配置（APNACCESSWAL）

## 使用实例

查询名称为“apn1.com”的APN的接入速率：

```
LST APNACCESSWAL: APN="huawei.com";
```

```

RETCODE = 0  操作成功。

结果如下
--------
       APN名称  =  huawei.com
       ISU组号  =  1
用户的接入速率  =  300
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询Apn接入速率配置（LST-APNACCESSWAL）_06054798.md`
