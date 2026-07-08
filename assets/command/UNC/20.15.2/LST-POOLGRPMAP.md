---
id: UNC@20.15.2@MMLCommand@LST POOLGRPMAP
type: MMLCommand
name: LST POOLGRPMAP（查询地址池组映射关系）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: POOLGRPMAP
command_category: 查询类
applicable_nf:
- PGW-C
- SMF
- GGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- UE地址管理
- UE地址池管理
- 地址池组映射配置
status: active
---

# LST POOLGRPMAP（查询地址池组映射关系）

## 功能

**适用NF：PGW-C、SMF、GGSN**

该命令用于查询地址池组和UPF组的映射关系。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MAPPINGNAME | 映射名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定地址池组映射规则名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~79。不支持空格及特殊字符“#”、“$”和“&”等，由“-”、“_”、数字、字母和“.”组成，不能以“.”开头，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [地址池组映射关系（POOLGRPMAP）](configobject/UNC/20.15.2/POOLGRPMAP.md)

## 使用实例

查询地址池组和UPF组的映射关系：

```
LST POOLGRPMAP:;
RETCODE = 0  操作成功。

结果如下
------------------------
     映射名称  =  one
 地址池组名称  =  spoolgrp1
    UPF组名称  =  upfgrp1
 位置区组类型  =  无
 位置区组名称  =  NULL
      APN名称  =  NULL
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询地址池组映射关系（LST-POOLGRPMAP）_32232820.md`
