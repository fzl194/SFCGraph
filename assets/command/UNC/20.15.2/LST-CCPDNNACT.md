---
id: UNC@20.15.2@MMLCommand@LST CCPDNNACT
type: MMLCommand
name: LST CCPDNNACT（查询融合计费Proxy基于DNN处理动作）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: CCPDNNACT
command_category: 查询类
applicable_nf:
- NCG
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- NCG业务及策略管理
- 融合计费Proxy基于DNN处理动作
status: active
---

# LST CCPDNNACT（查询融合计费Proxy基于DNN处理动作）

## 功能

**适用NF：NCG**

该命令用于查询融合计费Proxy基于DNN处理动作。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DNNTYPE | DNN类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定DNN的类型。<br>数据来源：本端规划<br>取值范围：<br>- DEFAULT（针对未指定的DNN设置处理动作）<br>- VALUE（针对DNN设置处理动作）<br>默认值：无<br>配置原则：无 |
| DNNID | 数据网络名称 | 可选必选说明：该参数在"DNNTYPE"配置为"VALUE"时为条件可选参数。<br>参数含义：该参数用于指定数据网络名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”等特殊字符，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [融合计费Proxy基于DNN处理动作（CCPDNNACT）](configobject/UNC/20.15.2/CCPDNNACT.md)

## 使用实例

查询融合计费Proxy基于DNN处理动作：

```
LST CCPDNNACT:;
RETCODE = 0  操作成功

结果如下
--------
          DNN类型  =  针对DNN设置处理动作
   数据网络名称  =  IMS
   是否转发OCS  =  否
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询融合计费Proxy基于DNN处理动作（LST-CCPDNNACT）_39951745.md`
