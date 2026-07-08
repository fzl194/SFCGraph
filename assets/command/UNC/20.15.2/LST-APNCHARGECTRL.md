---
id: UNC@20.15.2@MMLCommand@LST APNCHARGECTRL
type: MMLCommand
name: LST APNCHARGECTRL（查询APN的计费配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: APNCHARGECTRL
command_category: 查询类
applicable_nf:
- SGW-C
- PGW-C
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 计费管理
- 计费控制
- APN计费配置
status: active
---

# LST APNCHARGECTRL（查询APN的计费配置）

## 功能

**适用NF：SGW-C、PGW-C、SMF**

该命令用来查询APN实例下绑定的离线计费模板名称、话单字段模板名称、在线计费模板名称，以及费率切换组名称、计费属性名称和计费模式的配置情况。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APN | APN名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定APN实例名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”特殊字符，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@APNCHARGECTRL]] · APN的计费配置（APNCHARGECTRL）

## 使用实例

显示所有APNChargeCtrl实例的信息：

```
LST APNCHARGECTRL: APN="apn-test";
```

```

RETCODE = 0  操作成功

APN计费配置
-----------
                        APN名称  =  apn-test
                   在线计费开关  =  继承
                   离线计费开关  =  继承
              PGW离线计费模板名  =  NULL
              SGW离线计费模板名  =  NULL
             GGSN离线计费模板名  =  NULL
          PGW-CDR话单字段模板名  =  NULL
          SGW-CDR话单字段模板名  =  NULL
            G-CDR话单字段模板名  =  NULL
                    DCC模板名称  =  NULL
                   费率切换组名  =  NULL
                   计费属性名称  =  NULL
                   融合计费开关  =  继承
                   融合计费模板  =  NULL
              SMF离线计费模板名  =  NULL
               业务申请上报模式  =  融合业务申请上报模式
                N40消息属性模板  =  NULL
                    QBC计费开关  =  使能
I-SMF/SGW使用的融合计费模板名称  =  NULL
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-APNCHARGECTRL.md`
