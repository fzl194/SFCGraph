---
id: UDG@20.15.2@MMLCommand@LST APNBINDPATH
type: MMLCommand
name: LST APNBINDPATH（查询APNBindPath配置）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: APNBINDPATH
command_category: 查询类
applicable_nf:
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 路径管理
- N6路径管理
- APN与路径绑定关系
status: active
---

# LST APNBINDPATH（查询APNBindPath配置）

## 功能

**适用NF：UPF**

该命令用来查看与指定APN绑定的探测路径或者已配置的所有APN与探测路径的绑定关系。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APN | APN名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定APN实例名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”等特殊字符，不区分大小写。<br>默认值：无<br>配置原则：该参数使用ADD APN命令配置生成。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/APNBINDPATH]] · APNBindPath配置（APNBINDPATH）

## 使用实例

查询当前所有的apn与探测路径的绑定关系：

```
LST APNBINDPATH:;
```

```

RETCODE = 0  操作成功

APN与探测路径的绑定关系
-----------------------
 APN名称  =  testapn
路径名称  =  testpath3
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-APNBINDPATH.md`
