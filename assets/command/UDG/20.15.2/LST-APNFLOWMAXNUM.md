---
id: UDG@20.15.2@MMLCommand@LST APNFLOWMAXNUM
type: MMLCommand
name: LST APNFLOWMAXNUM（查询APN最大流数）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: APNFLOWMAXNUM
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- DN管理
- APN管理
- APN最大五元组数
status: active
---

# LST APNFLOWMAXNUM（查询APN最大流数）

## 功能

**适用NF：PGW-U、UPF**

该命令用于查询指定APN下的最大流数。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APN | APN | 可选必选说明：必选参数<br>参数含义：该参数用于指定APN实例名。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”特殊字符，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/APNFLOWMAXNUM]] · APN最大流数（APNFLOWMAXNUM）

## 使用实例

查询APN最大流数：

```
LST APNFLOWMAXNUM:APN="aa";
```

```

RETCODE = 0  操作成功。

APN最大流数信息
---------------
                APN  =  aa
APN最大五元组节点数  =  500
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-APNFLOWMAXNUM.md`
