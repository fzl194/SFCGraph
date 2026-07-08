---
id: UNC@20.15.2@MMLCommand@LST APNWIFILTEHO
type: MMLCommand
name: LST APNWIFILTEHO（查询基于APN的E-UTRAN和WLAN互操作控制属性）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: APNWIFILTEHO
command_category: 查询类
applicable_nf:
- PGW-C
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- 接入控制
- E-UTRAN和WLAN互操作控制
- 基于APN的E-UTRAN和WLAN互操作控制
status: active
---

# LST APNWIFILTEHO（查询基于APN的E-UTRAN和WLAN互操作控制属性）

## 功能

**适用NF：PGW-C**

该命令用于查询基于APN的E-UTRAN和WLAN互操作控制属性。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APN | APN名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定用户请求的APN。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”等特殊字符，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/APNWIFILTEHO]] · 基于APN的E-UTRAN和WLAN互操作控制属性（APNWIFILTEHO）

## 使用实例

查询APN为"huawei.com"的E-UTRAN和WLAN互操作属性：

```
%%LST APNWIFILTEHO:;%%
RETCODE = 0  操作成功

结果如下
--------
        APN名称  =  huawei.com
S2b接口切换开关  =  使能
S2a接口切换开关  =  使能
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-APNWIFILTEHO.md`
