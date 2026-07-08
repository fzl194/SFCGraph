---
id: UNC@20.15.2@MMLCommand@DSP TMGI
type: MMLCommand
name: DSP TMGI（显示TMGI）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: TMGI
command_category: 查询类
applicable_nf:
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 5G组播广播管理
- MB-SMF组播广播管理
- 显示MB-SMF TMGI
status: active
---

# DSP TMGI（显示TMGI）

## 功能

**适用NF：SMF**

该参数用于查询TMGI信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| QRY_SCOPE | 查询范围 | 可选必选说明：必选参数<br>参数含义：该参数用于指定查询范围。<br>数据来源：本端规划<br>取值范围：<br>- SUMMARY（汇总信息）<br>- SPECIFIED_TMGI_INFO（指定TMGI信息）<br>默认值：无<br>配置原则：无 |
| MCC | 移动国家代码 | 可选必选说明：该参数在"QRY_SCOPE"配置为"SPECIFIED_TMGI_INFO"时为条件必选参数。<br>参数含义：该参数用于指定移动国家代码。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度是3。仅支持0-9的数字。<br>默认值：无<br>配置原则：无 |
| MNC | 移动网号 | 可选必选说明：该参数在"QRY_SCOPE"配置为"SPECIFIED_TMGI_INFO"时为条件必选参数。<br>参数含义：该参数用于指定移动网号。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是2~3。仅支持0-9的数字。<br>默认值：无<br>配置原则：无 |
| MBSSERVICEID | 组播广播服务标识 | 可选必选说明：该参数在"QRY_SCOPE"配置为"SPECIFIED_TMGI_INFO"时为条件必选参数。<br>参数含义：该参数用于指定组播广播服务标识。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度是6。组播广播服务标识编码为16进制数，按照字符串格式输入，字符串长度为6，只能由数字（0-9），字母（A-F、a-f）组成。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/TMGI]] · TMGI（TMGI）

## 使用实例

当需要显示查询类型为SPECIFIED_TMGI_INFO，MCC为460，MNC为03，MBSSERVICEID为000001的TMGI信息时，执行如下命令：

```
%%DSP TMGI: QRY_SCOPE=SPECIFIED_TMGI_INFO, MCC="460", MNC="03", MBSSERVICEID="000001";%%
RETCODE = 0  操作成功

结果如下
--------
        TMGI  =  460-03-000001
TMGI过期时间  =  2022-11-25 14:34:28
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示TMGI（DSP-TMGI）_47342117.md`
