---
id: UDG@20.15.2@MMLCommand@LST APNSGLPASS
type: MMLCommand
name: LST APNSGLPASS（查询APN单通检测开关）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: APNSGLPASS
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 会话管理
- 会话连通性检测
- 网络侧连通性检测
- 单通检测
status: active
---

# LST APNSGLPASS（查询APN单通检测开关）

## 功能

**适用NF：PGW-U、UPF**

该命令用于查询用户数据流量单通故障检测功能开关是否开启。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APN | APN名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定APN实例名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”特殊字符，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/APNSGLPASS]] · APN单通检测开关（APNSGLPASS）

## 使用实例

查询APN为apn1.com的单通故障检测功能开关是否开启：

```
LST APNSGLPASS: APN="apn1.com";
```

```

RETCODE = 0  操作成功。

APN单通检测开关
---------------
 APN名称  =  apn1.com
开关标识  =  不使能
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-APNSGLPASS.md`
