---
id: UDG@20.15.2@MMLCommand@LST UPAPNCHARGE
type: MMLCommand
name: LST UPAPNCHARGE（显示APN计费配置）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: UPAPNCHARGE
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 用户面服务管理
- 业务控制策略
- 计费控制
- APN计费控制
status: active
---

# LST UPAPNCHARGE（显示APN计费配置）

## 功能

**适用NF：PGW-U、UPF**

该命令用于查询APN在线计费默认配额使能开关。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APN | APN | 可选必选说明：可选参数<br>参数含义：该参数用于指定APN实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”特殊字符，不区分大小写。<br>默认值：无<br>配置原则：该参数使用ADD APN命令配置生成。 |

## 操作的配置对象

- [APN计费配置（UPAPNCHARGE）](configobject/UDG/20.15.2/UPAPNCHARGE.md)

## 使用实例

查询APN默认配额使能开关：

```
LST UPAPNCHARGE: APN="apn1";
```

```

RETCODE = 0 操作成功。

显示APN默认使能开关
------------------------
                                       APN = apn1
                   默认配额使能开关 = 开启
          新业务默认配额使能开关 = 继承
 非新业务场景默认配额使能开关 = 关闭
(结果个数 = 1)
--- END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/显示APN计费配置（LST-UPAPNCHARGE）_30179324.md`
