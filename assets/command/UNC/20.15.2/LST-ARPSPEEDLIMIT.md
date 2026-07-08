---
id: UNC@20.15.2@MMLCommand@LST ARPSPEEDLIMIT
type: MMLCommand
name: LST ARPSPEEDLIMIT（查询速率限制）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: ARPSPEEDLIMIT
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- ARP管理
- ARP系统配置
status: active
---

# LST ARPSPEEDLIMIT（查询速率限制）

## 功能

该命令用于查询ARP报文或者ARP Miss消息的速率抑制值。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SUPPTYPE | 抑制类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定需要配置ARP的报文限速还是ARP Miss的消息限速。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ARP：针对ARP报文上送速率进行抑制。<br>- ARP-miss：针对上送的ARP Miss消息上送速率进行抑制。<br>默认值：无 |
| SUPPBASETYPE | 抑制基础类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定限速方式。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- Dest_Ip：基于目的IP地址进行时间戳抑制。<br>- Src_Ip：基于源IP地址进行时间戳抑制。<br>默认值：无 |
| RUNAME | RU名称 | 可选必选说明：可选参数<br>参数含义：需要配置限速功能的资源单元名称。通过DSP RU命令可以查询资源单元信息。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/ARPSPEEDLIMIT]] · 速率限制（ARPSPEEDLIMIT）

## 使用实例

查询ARP报文的速率抑制值：

```
LST ARPSPEEDLIMIT:SUPPTYPE=ARP;
```

```

RETCODE = 0  操作成功

结果如下
-------------------------
抑制类型    抑制基础类型   RU名称                        抑制值（pps）
ARP类型     目的IP         VNODE_VNRS_VNFC_OMU_0001      500
ARP类型     目的IP         VNODE_VNRS_VNFC_OMU_0002      500
(结果个数 = 2)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询速率限制（LST-ARPSPEEDLIMIT）_00441141.md`
