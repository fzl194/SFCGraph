---
id: UNC@20.15.2@MMLCommand@LST APNREPORTATTR
type: MMLCommand
name: LST APNREPORTATTR（查询APN的上报属性）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: APNREPORTATTR
command_category: 查询类
applicable_nf:
- SMF
- SGW-C
- PGW-C
- GGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- APN管理
- 周边接口呈现APN策略管理
- 基于APN的上报APN策略控制
status: active
---

# LST APNREPORTATTR（查询APN的上报属性）

## 功能

**适用NF：SMF、SGW-C、PGW-C、GGSN**

该命令用于查询性能统计，头增强，给报表服务器上报记录时或与其他网元交互时使用的APN类型。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APN | APN名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定配置上报属性的APN。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。字符串类型，输入长度范围为1～63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”特殊字符，不区分大小写。<br>默认值：无<br>配置原则：<br>该参数使用ADD APN命令配置生成。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/APNREPORTATTR]] · APN的上报属性（APNREPORTATTR）

## 使用实例

查询APN huawei.com下性能统计，头增强，给报表服务器上报记录时或与其他网元交互时使用的APN类型。

```
%%LST APNREPORTATTR: APN="huawei.com";%%
RETCODE = 0  操作成功。

结果如下
-----------------
                            APN名称  =  huawei.com
                           拥塞控制  =  不使能
                       智能网关选择  =  不使能
                           实时位置  =  不使能
通过本地配置获取VLR ID/Global Title  =  不使能
               上报给AAA计费的APN名  =  真实的
               上报给AAA鉴权的APN名  =  真实的
                    上报给CG的APN名  =  真实的
          上报给Diameter AAA的APN名  =  请求的
                   上报给OCS的APN名  =  真实的
                   上报给CHF的APN名  =  请求的
                  上报给PCRF的APN名  =  真实的
                   上报给PCF的APN名  =  请求的
                  上报给话统的APN名  =  真实的
                上报给用户面的APN名  =  真实的
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询APN的上报属性（LST-APNREPORTATTR）_09653252.md`
