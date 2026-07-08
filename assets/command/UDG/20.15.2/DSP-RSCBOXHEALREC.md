---
id: UDG@20.15.2@MMLCommand@DSP RSCBOXHEALREC
type: MMLCommand
name: DSP RSCBOXHEALREC（显示ResourceBox重建历史记录）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: RSCBOXHEALREC
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 可靠性管理
- 微服务可靠性管理
status: active
---

# DSP RSCBOXHEALREC（显示ResourceBox重建历史记录）

## 功能

该命令用于查询ResourceBox重建历史记录。

> **说明**
> 该命令只适用于裸机容器云场景。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RSCBOXNAME | ResourceBox名称 | 可选必选说明：可选参数<br>参数含义：该参数用于显示重建的ResourceBox名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~128。如果不输入该输出，则查询系统内所有ResourceBox的重建记录。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/RSCBOXHEALREC]] · ResourceBox重建历史记录（RSCBOXHEALREC）

## 使用实例

查询ResourceBox重建历史记录:

```
DSP RSCBOXHEALREC:;
RETCODE = 0  操作成功

结果如下
--------
ResourceBox名称                堆栈ID                               重建时间            序号  ResourceBoxID
vsm-super-pod-54ddc977b9-4g42g 524c409a-bc3b-11ea-a186-025565660064 2020-07-09 09:08:03 1     c2208db2-bc3b-11ea-9d1b-fa163eb94edd 
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/显示ResourceBox重建历史记录（DSP-RSCBOXHEALREC）_00601670.md`
