---
id: UDG@20.15.2@MMLCommand@LST APNTETHERFUNC
type: MMLCommand
name: LST APNTETHERFUNC（查询APN Tethering检测开关）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: APNTETHERFUNC
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 业务匹配策略
- 业务过滤器管理
- Tethering检测
- APN Tethering检测功能
status: active
---

# LST APNTETHERFUNC（查询APN Tethering检测开关）

## 功能

**适用NF：PGW-U、UPF**

该命令用于在APN下显示该APN是否启用Tethering检测功能。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APN | APN | 可选必选说明：可选参数<br>参数含义：该参数用于指定APN实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”特殊字符，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/APNTETHERFUNC]] · APN Tethering检测开关（APNTETHERFUNC）

## 使用实例

如果在apn01下显示该APN是启用Tethering检测功能：

```
LST APNTETHERFUNC:;
```

```

RETCODE = 0  操作成功。

APN Tethering检测开关信息
-------------------------
     APN  =  apn01
开关标识  =  不使能
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询APN-Tethering检测开关（LST-APNTETHERFUNC）_82837442.md`
