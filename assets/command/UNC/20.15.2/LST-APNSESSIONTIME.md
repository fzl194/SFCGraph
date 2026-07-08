---
id: UNC@20.15.2@MMLCommand@LST APNSESSIONTIME
type: MMLCommand
name: LST APNSESSIONTIME（查询APN会话上下文定时器配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: APNSESSIONTIME
command_category: 查询类
applicable_nf:
- SGW-C
- PGW-C
- SMF
- GGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- APN管理
- APN定时器属性
status: active
---

# LST APNSESSIONTIME（查询APN会话上下文定时器配置）

## 功能

**适用NF：SGW-C、PGW-C、SMF、GGSN**

该命令用于查询APN最大会话时长。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APN | APN名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指示APN名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。字符串类型，输入长度范围为1～63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“ ” ”、“ ` ”特殊字符，不区分大小写。<br>默认值：无<br>配置原则：<br>该参数使用ADD APN命令配置生成。 |

## 操作的配置对象

- [APN会话上下文定时器配置（APNSESSIONTIME）](configobject/UNC/20.15.2/APNSESSIONTIME.md)

## 使用实例

查询APN为huawei.com的会话时长

```
%%LST APNSESSIONTIME: APN="huawei.com";%%
RETCODE = 0  操作成功

结果如下
--------
     APN名称  =  huawei.com
会话时长开关  =  使能
    会话时长  =  120
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询APN会话上下文定时器配置（LST-APNSESSIONTIME）_96242083.md`
