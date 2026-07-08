---
id: UDG@20.15.2@MMLCommand@LST APNCFFUNC
type: MMLCommand
name: LST APNCFFUNC（查询APN内容过滤开关）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: APNCFFUNC
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 业务控制策略
- 内容过滤
- APN内容过滤开关配置
status: active
---

# LST APNCFFUNC（查询APN内容过滤开关）

## 功能

**适用NF：PGW-U、UPF**

该命令用于查询APN内容过滤开关。如果不输入APN名称，则查询所有APN内容过滤开关。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APNNAME | APN名称 | 可选必选说明：可选参数<br>参数含义：该参数用于设置APN名称。<br>数据来源：本端规划<br>取值范围：只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”特殊字符，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@APNCFFUNC]] · APN内容过滤开关（APNCFFUNC）

## 使用实例

查询名为huawei.com的APN上的内容过滤开关：

```
LST APNCFFUNC: APNNAME="huawei.com";
```

```

RETCODE = 0  操作成功
 
内容过滤功能开关
----------------
         APN名称  =  huawei.com
内容过滤功能开关  =  使能
(结果个数 = 1)
 
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-APNCFFUNC.md`
