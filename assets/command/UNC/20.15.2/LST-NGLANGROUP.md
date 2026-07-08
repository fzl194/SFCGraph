---
id: UNC@20.15.2@MMLCommand@LST NGLANGROUP
type: MMLCommand
name: LST NGLANGROUP（查询5G LAN群组）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NGLANGROUP
command_category: 查询类
applicable_nf:
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 5G LAN管理
- 5G LAN组管理
status: active
---

# LST NGLANGROUP（查询5G LAN群组）

## 功能

**适用NF：SMF**

该命令用于查询5G LAN群组。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DNN | DNN | 可选必选说明：可选参数<br>参数含义：该参数用于指定5G LAN群组支持的DNN，即用户请求的DNN。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”等特殊字符，不区分大小写。<br>默认值：无<br>配置原则：无 |
| SST | 切片业务类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定5G LAN群组支持的网络切片业务类型。网络切片标识（S-NSSAI）由切片业务类型（SST）和切片细分标识（SD）两部分组成。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是0~255。<br>默认值：无<br>配置原则：无 |
| SD | 切片细分标识 | 可选必选说明：可选参数<br>参数含义：该参数用于指定5G LAN群组支持的网络切片细分标识。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度是6。只能由数字（0-9），字母（A-F、a-f）组成。字母大小写不敏感。<br>默认值：无<br>配置原则：无 |
| PDUSESSIONTYPE | PDU会话类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定5G LAN群组支持的PDU会话类型。<br>数据来源：全网规划<br>取值范围：<br>- Ethernet（以太类型会话）<br>- IPv4（IPv4类型会话）<br>- IPv6（IPv6类型会话）<br>- IPv4v6（IPv4v6类型会话）<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@NGLANGROUP]] · 5G LAN群组（NGLANGROUP）

## 使用实例

查询DNN为“huawei.com”，SST为1，SD为“010101”，PDU会话类型为Ethernet的5G LAN群组，运行以下命令：

```
%%LST NGLANGROUP: DNN="huawei.com", SST=1, SD="010101", PDUSESSIONTYPE=Ethernet;%%
            RETCODE = 0  操作成功

            结果如下
            --------
            5G LAN组ID  =  a0000001-460-003-01
            DNN  =  huawei.com
            切片业务类型  =  1
            切片细分标识  =  010101
            PDU会话类型  =  以太类型会话
            (结果个数 = 1)

            ---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-NGLANGROUP.md`
