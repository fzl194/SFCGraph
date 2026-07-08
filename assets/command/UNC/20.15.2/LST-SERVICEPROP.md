---
id: UNC@20.15.2@MMLCommand@LST SERVICEPROP
type: MMLCommand
name: LST SERVICEPROP（查询业务属性）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: SERVICEPROP
command_category: 查询类
applicable_nf:
- PGW-C
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 计费和策略的业务管理
- 业务策略
- 业务属性
status: active
---

# LST SERVICEPROP（查询业务属性）

## 功能

**适用NF：PGW-C、SMF**

该命令用于查询业务属性。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| OPTYPE | 操作类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定业务属性的操作类型。<br>数据来源：全网规划<br>取值范围：枚举类型。<br>- SRV_PROP_NAME：删除SRVPROPNAME。<br>- SERVICE_ID：删除SERVICEID。<br>默认值：无<br>配置原则：<br>- SRV_PROP_NAME：当OPTYPE值为SRV_PROP_NAME时，表示基于SRVPROPNAME查询记录。<br>- SERVICE_ID：当OPTYPE值为SERVICE_ID时，表示基于SERVICEID查询记录。 |
| SRVPROPNAME | 业务属性名称 | 可选必选说明：条件可选参数<br>前提条件：该参数在“OPTYPE”配置为“SRV_PROP_NAME”时为可选参数。<br>参数含义：该参数用于指定业务属性名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |
| SERVICEID | 业务标识 | 可选必选说明：条件可选参数<br>前提条件：该参数在“OPTYPE”配置为“SERVICE_ID”时为可选参数。<br>参数含义：该参数用于指定业务标识。全局唯一。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围为1～4294967295。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@SERVICEPROP]] · 业务属性（SERVICEPROP）

## 使用实例

查询业务属性配置：OPTYPE为SRV_PROP_NAME，SRVPROPNAME为test：

```
LST SERVICEPROP:OPTYPE=SRV_PROP_NAME,SRVPROPNAME="test";
```

```

RETCODE = 0  操作成功。

业务属性信息
------------
业务属性名称  =  test
    业务标识  =  1
      优先级  =  10
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-SERVICEPROP.md`
