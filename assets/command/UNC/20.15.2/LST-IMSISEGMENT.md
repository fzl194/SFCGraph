---
id: UNC@20.15.2@MMLCommand@LST IMSISEGMENT
type: MMLCommand
name: LST IMSISEGMENT（查询IMSI号码段）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: IMSISEGMENT
command_category: 查询类
applicable_nf:
- SGW-C
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- UPF选择管理
- UPF绑定用户漫游属性
status: active
---

# LST IMSISEGMENT（查询IMSI号码段）

## 功能

**适用NF：SGW-C**

该命令用于查询IMSI号段。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SEGMENTNAME | IMSI号段名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定IMSI号段名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~31。只允许输入字母、数字、“.”、“_”和“-”。字母会被转换为小写字母进行存储和处理。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/IMSISEGMENT]] · IMSI号码段（IMSISEGMENT）

## 使用实例

查询IMSI号段，执行命令如下：

```
%%LST IMSISEGMENT:;%%
            RETCODE = 0  操作成功

            结果如下
            ------------------------
            IMSI号段名称  =  imsipre1
            IMSI号段类型  =  IMSI_PREFIX
            IMSI前缀  =  28602851
            (结果个数 = 1)

            ---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询IMSI号码段（LST-IMSISEGMENT）_54980970.md`
