---
id: UNC@20.15.2@MMLCommand@DSP MULDNNSESSNUM
type: MMLCommand
name: DSP MULDNNSESSNUM（显示专用DNN会话数）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: MULDNNSESSNUM
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
- 查询专有DNN会话上下文数
status: active
---

# DSP MULDNNSESSNUM（显示专用DNN会话数）

## 功能

**适用NF：PGW-C、SMF**

该命令用于查询N11SMF、N16aSMF、PGW-C和SPGW-C上通用DNN会话关联的专用DNN会话数。

## 注意事项

“查询分类”参数不输入时，表示查询汇总的信息。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| QRY_SCOPE | 查询范围 | 可选必选说明：可选参数<br>参数含义：该参数用于指定查询会话上下文的范围。<br>数据来源：本端规划<br>取值范围：<br>- “SUMMARY（汇总信息）”：查询汇总信息。以汇总方式呈现。<br>- “ALL_POD_INFO（所有POD信息）”：查询所有POD信息。以POD粒度呈现。<br>- “SPECIFIED_POD_INFO（指定POD信息）”：查询指定POD信息。<br>默认值：SUMMARY<br>配置原则：无 |
| APN | APN名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定2B2C漫游双DNN特性的通用DNN会话的APN实例名。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~63。<br>默认值：无<br>配置原则：无 |
| POD_ID | POD名称 | 可选必选说明：该参数在"QRY_SCOPE"配置为"SPECIFIED_POD_INFO"时为条件必选参数。<br>参数含义：该参数用于指定需要查询会话上下文数的POD名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~255。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@MULDNNSESSNUM]] · 专用DNN会话数（MULDNNSESSNUM）

## 使用实例

当希望查询UNC设备上各形态创建的专用DNN会话数量时，使用如下命令：

```
%%DSP MULDNNSESSNUM: QRY_SCOPE=SUMMARY, APN="huawei.com";%%
RETCODE = 0  操作成功

结果如下
------------------------
                            查询范围  =  汇总信息
                                 APN  =  huawei.com
      PGW-C上激活的专用DNN PDU会话数  =  0
    S/PGW-C上激活的专用DNN PDU会话数  =  0
N16a接口SMF上激活的专用DNN PDU会话数  =  0
 N11接口SMF上激活的专用DNN PDU会话数  =  0
                 专用DNN PDU会话总数  =  0
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-MULDNNSESSNUM.md`
