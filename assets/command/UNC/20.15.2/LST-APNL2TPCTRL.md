---
id: UNC@20.15.2@MMLCommand@LST APNL2TPCTRL
type: MMLCommand
name: LST APNL2TPCTRL（查询APN L2TP CTRL配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: APNL2TPCTRL
command_category: 查询类
applicable_nf:
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
- 基于APN的L2TP接入控制
status: active
---

# LST APNL2TPCTRL（查询APN L2TP CTRL配置）

## 功能

**适用NF：PGW-C、SMF、GGSN**

该命令用于查询APN L2TP CTRL记录。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APN | APN名称 | 可选必选说明：可选参数<br>参数含义：APN名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~63。字符串类型，输入长度范围为1～63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“ ” ”、“ ` ”特殊字符，不区分大小写。<br>默认值：无<br>配置原则：<br>该参数使用ADD APN命令配置生成。 |

## 操作的配置对象

- [APN L2TP CTRL配置（APNL2TPCTRL）](configobject/UNC/20.15.2/APNL2TPCTRL.md)

## 使用实例

查询APN为HUAWEI.COM的APN L2TP CTRL记录：

```
%%LST APNL2TPCTRL:;%%
RETCODE = 0  操作成功

结果如下
--------
                                  APN名称  =  huawei.com
                             支持L2TP功能  =  不使能
             MSISDN作为ICCN代理认证用户名  =  不使能
与LNS进行用户鉴权的用户名密码使用公用配置  =  不使能
                 L2TP支持专有承载功能开关  =  不使能
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询APN-L2TP-CTRL配置（LST-APNL2TPCTRL）_25120884.md`
