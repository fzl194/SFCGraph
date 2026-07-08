---
id: UNC@20.15.2@MMLCommand@LST NGPAGINGDNNPRI
type: MMLCommand
name: LST NGPAGINGDNNPRI（查询基于DNN的Paging消息在流控期间放通的优先级）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NGPAGINGDNNPRI
command_category: 查询类
applicable_nf:
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- N2接口管理
- N2接口消息流控优先级管理
- 基于DNN的Paging消息流控优先级管理
status: active
---

# LST NGPAGINGDNNPRI（查询基于DNN的Paging消息在流控期间放通的优先级）

## 功能

**适用NF：AMF**

该命令用于查询基于DNN的Paging消息在流控期间放通的优先级。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DNN | DNN | 可选必选说明：可选参数<br>参数含义：该参数用于指定DNN。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”特殊字符，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@NGPAGINGDNNPRI]] · 基于DNN的Paging消息在流控期间放通的优先级（NGPAGINGDNNPRI）

## 使用实例

查询基于DNN的Paging消息在流控期间放通的优先级，执行如下命令：

```
%%LST NGPAGINGDNNPRI:;%%
RETCODE = 0  操作成功

结果如下
--------
DNN          优先级                 

HUAWEI.COM   低  
IMS          高  
(结果个数 = 2)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-NGPAGINGDNNPRI.md`
