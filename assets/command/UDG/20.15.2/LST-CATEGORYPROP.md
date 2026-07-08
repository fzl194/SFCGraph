---
id: UDG@20.15.2@MMLCommand@LST CATEGORYPROP
type: MMLCommand
name: LST CATEGORYPROP（查询分类属性）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: CATEGORYPROP
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 业务控制策略
- 带宽控制
- 分类属性
status: active
---

# LST CATEGORYPROP（查询分类属性）

## 功能

**适用NF：PGW-U、UPF**

该命令用来显示所有配置的CATEGORYPROP信息，或者根据名称配置的信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CATEPROPNAME | 分类属性名称 | 可选必选说明：可选参数<br>参数含义：该参数用于设置分类属性名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/CATEGORYPROP]] · 分类属性（CATEGORYPROP）

## 使用实例

显示名称为“test”的分类属性配置信息：

```
LST CATEGORYPROP: CATEPROPNAME="test";
```

```

RETCODE = 0  操作成功。

分类属性信息
------------
分类属性名称  =  test
  配置域名称  =  NULL
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-CATEGORYPROP.md`
