---
id: UNC@20.15.2@MMLCommand@LST APNIDLETIME
type: MMLCommand
name: LST APNIDLETIME（查询APN空闲上下文定时器配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: APNIDLETIME
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

# LST APNIDLETIME（查询APN空闲上下文定时器配置）

## 功能

**适用NF：SGW-C、PGW-C、SMF、GGSN**

该命令用于查询指定APN的空闲上下文定时器的配置信息，包括空闲上下文核查开关、空闲上下文去激活时长等。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APN | APN名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定APN名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“ ” ”、“ ` ”特殊字符，不区分大小写。<br>默认值：无<br>配置原则：<br>该参数使用ADD APN命令配置生成。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@APNIDLETIME]] · APN空闲上下文定时器配置（APNIDLETIME）

## 使用实例

查询“APN名称”为“HUAWEI.COM”的空闲上下文定时器配置信息：

```
%%LST APNIDLETIME:;%%
RETCODE = 0  操作成功

结果如下
------------------------
                             APN名称  =  huawei.com
                        继承默认开关  =  是
             SGW-C空闲上下文核查开关  =  使能
PGW-C和SGW-C/PGW-C空闲上下文检查开关  =  使能
              GGSN空闲上下文检查开关  =  使能
             H-SMF空闲上下文核查开关  =  使能
           H-SMF不活动上下文核查开关  =  使能
       I-SMF/V-SMF空闲上下文核查开关  =  使能
     I-SMF/V-SMF不活动上下文核查开关  =  使能
                     GUL承载级别参数  =  会话级
           缺省承载和默认GBR的定时器  =  一天
                     承载定时器(min)  =  1440
                 会话定时器时长(min)  =  1440
          SMF会话空闲定时器时长(min)  =  1440
        SMF会话不活动定时器时长(min)  =  40
                空闲超时发送更新消息  =  去使能
             H-SMF空闲上下文核查级别  =  会话级
     专有QoS Flow空闲定时器时长(min)  =  1440
     缺省QoS Flow空闲定时器时长(min)  =  1440
            GGSN一次激活上下文定时器  =  一天
       Proxy-SMF S8空闲上下文核查开关 = 使能
          Proxy-SMF 空闲上下文核查开关 = 使能
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-APNIDLETIME.md`
