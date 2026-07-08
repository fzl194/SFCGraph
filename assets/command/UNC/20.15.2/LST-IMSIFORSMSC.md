---
id: UNC@20.15.2@MMLCommand@LST IMSIFORSMSC
type: MMLCommand
name: LST IMSIFORSMSC（查询融合短消息功能共部署SMSC支持的IMSI号段配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: IMSIFORSMSC
command_category: 查询类
applicable_nf:
- SMSF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- SMSF业务管理
- SMSC选择管理
status: active
---

# LST IMSIFORSMSC（查询融合短消息功能共部署SMSC支持的IMSI号段配置）

## 功能

**适用NF：SMSF**

该命令用于查询融合短消息功能共部署SMSC支持的IMSI号段或MSISDN号段（通过DWORD16 BIT9软参配置）配置。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SEGSTART | IMSI号段起始号码 | 可选必选说明：可选参数<br>参数含义：该参数用于表示IMSI或MSISDN号段起始号码。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是5~15。号段起始字符串长度为15位，不足15位时系统自动在末尾补0。十进制数字，号段的起始号码数值必须小于或等于号段结束号码的数值，且号段的起始号码不能以0开始，全0除外。<br>默认值：无<br>配置原则：<br>当COMMONSOFTPARA DWORD16 BIT9软参设置为0时，表示配置MSISDN号段，当软参设置为1时，表示配置IMSI号段。 |
| SEGEND | IMSI号段结束号码 | 可选必选说明：可选参数<br>参数含义：该参数用以表示IMSI或MSISDN号段结束号码。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是5~15。号段结束字符串长度为15位，不足15位时系统自动在末尾补9。十进制数字，号段的结束号码数值必须大于或等于起始号码的数值，且号段的结束号码不能为以0开始。<br>默认值：无<br>配置原则：<br>当COMMONSOFTPARA DWORD16 BIT9软参设置为0时，表示配置MSISDN号段，当软参设置为1时，表示配置IMSI号段。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/IMSIFORSMSC]] · 融合短消息功能共部署SMSC支持的IMSI号段配置（IMSIFORSMSC）

## 使用实例

运营商希望查询融合短消息功能共部署SMSC支持的IMSI号段配置，执行如下命令：

```
LST IMSIFORSMSC:;
%%LST IMSIFORSMSC:;%%
RETCODE = 0  操作成功

结果如下：
------------------------
        IMSI号段起始号码 =  460023500100001
        IMSI号段结束号码 =  460023500100009
(结果个数 = 1)
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-IMSIFORSMSC.md`
