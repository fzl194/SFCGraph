---
id: UNC@20.15.2@MMLCommand@LST APNTOHCTRL
type: MMLCommand
name: LST APNTOHCTRL（查询APN粒度的智家随行功能控制）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: APNTOHCTRL
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 智家随行会话管理
status: active
---

# LST APNTOHCTRL（查询APN粒度的智家随行功能控制）

## 功能

该命令用于查询APN粒度的智家随行功能控制。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APN | APN | 可选必选说明：可选参数<br>参数含义：该参数用于指定智家随行会话的APN实例名。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”等特殊字符，不区分大小写。<br>默认值：无<br>配置原则：<br>该参数使用ADD APN命令配置生成。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/APNTOHCTRL]] · APN粒度的智家随行会话控制（APNTOHCTRL）

## 使用实例

查询APN粒度的智家随行功能控制。

```
%%LST APNTOHCTRL:;%%
RETCODE = 0  操作成功

结果如下
------------
APN                  智家随行会话开关              FWA开关

toh.apn1             不使能                        不使能
toh.apn2             使能                          使能
(结果个数 = 2)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-APNTOHCTRL.md`
