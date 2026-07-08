---
id: UNC@20.15.2@MMLCommand@DSP MULDNNPDUSES
type: MMLCommand
name: DSP MULDNNPDUSES（显示专用DNN会话信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: MULDNNPDUSES
command_category: 查询类
applicable_nf:
- PGW-C
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- 接入管理运维
- 查询专有DNN会话信息
status: active
---

# DSP MULDNNPDUSES（显示专用DNN会话信息）

## 功能

**适用NF：PGW-C、SMF**

该命令用于查询当前普通DNN会话关联的专用DNN会话信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| QUERYTYPE | 查询方式 | 可选必选说明：必选参数<br>参数含义：该参数用于指定查询方式。<br>数据来源：本端规划<br>取值范围：<br>- IMSI（国际移动用户标识）<br>- IMEI（国际移动设备标识）<br>默认值：无<br>配置原则：无 |
| IMSI | 国际移动用户标识 | 可选必选说明：该参数在"QUERYTYPE"配置为"IMSI"时为条件必选参数。<br>参数含义：该参数用于指定用户永久标识或者国际移动用户标识。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是5~15。<br>默认值：无<br>配置原则：<br>该参数为23G/4G的输出参数。5G时对应输出为SUPI。 |
| IMEI | IMEI | 可选必选说明：该参数在"QUERYTYPE"配置为"IMEI"时为条件必选参数。<br>参数含义：该参数用于指定永久设备标识或国际移动设备标识。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~16。<br>默认值：无<br>配置原则：无 |
| PDUSESSIONID | PDU会话标识 | 可选必选说明：该参数在"QUERYTYPE"配置为"IMSI"、"IMEI"时为条件必选参数。<br>参数含义：该参数用于指定PDU会话ID，4G情况下指EPS承载标识。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~15。<br>默认值：无<br>配置原则：<br>可以通过简单查询获取到后作为详细查询的输入参数。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/MULDNNPDUSES]] · 专用DNN会话信息（MULDNNPDUSES）

## 使用实例

查询方式为IMSI，IMSI为123031700100001，PDUSESSIONID为5的专有DNN会话信息：

```
%%DSP MULDNNPDUSES: QUERYTYPE=IMSI, IMSI="123032900100001", PDUSESSIONID=5;%%
RETCODE = 0  操作成功

pdusession info
------------------------
               IMSI  =  123032900100001
               IMEI  =  1234567800000190
           PDU会话ID =  5
  专用DNN PDU会话ID  =  15
                DNN  =  huawei.com
 SNssaiSst/SNssaiSd  =  129/AAAAAA

(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示专用DNN会话信息（DSP-MULDNNPDUSES）_10370646.md`
