---
id: UNC@20.15.2@MMLCommand@LST NGIPAREADNN
type: MMLCommand
name: LST NGIPAREADNN（查询5G IP区域DNN）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NGIPAREADNN
command_category: 查询类
applicable_nf:
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 移动性管理
- IP细分管理
- 5G IP细分区域DNN管理
status: active
---

# LST NGIPAREADNN（查询5G IP区域DNN）

## 功能

**适用NF：AMF**

该命令用于查询5G IP区域DNN记录。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DNN | DNN | 可选必选说明：可选参数<br>参数含义：该参数用于指定支持“基于位置的地址分配”功能的DNN。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~63。可输入的字符有字母、十进制数字、“-”和“.”，并且开头和结尾只能是数字或者字母。不能出现连续两个“.”。字母大小写不敏感。<br>默认值：无<br>配置原则：<br>“*”表示通配符，如果DNN为“*”，表示所有DNN都支持“基于位置的地址分配”功能。 |
| ISNSSAI | 是否匹配S-NSSAI | 可选必选说明：可选参数<br>参数含义：该参数用于表示实现“基于位置的地址分配”功能时是否匹配S-NSSAI。<br>数据来源：本端规划<br>取值范围：<br>- “YES（是）”：是<br>- “NO（否）”：否<br>默认值：无<br>配置原则：<br>设置为“NO”，匹配所有S-NSSAI。 |
| SST | 切片业务类型 | 可选必选说明：该参数在"ISNSSAI"配置为"YES"时为条件可选参数。<br>参数含义：该参数用于表示组成“基于位置的地址分配”功能目标网络切片的业务类型信息。网络切片标识（S-NSSAI）由切片业务类型（SST）和切片细分标识（SD）两部分组成，其中切片细分标识是可选的。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是0~255。<br>默认值：无<br>配置原则：无 |
| SD | 切片细分标识 | 可选必选说明：该参数在"ISNSSAI"配置为"YES"时为条件可选参数。<br>参数含义：该参数用于表示组成“基于位置的地址分配”功能目标网络切片的细分标识。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度是6。采用十六进制表示（无须输入“0x”前缀），只能由数字（0-9），字母（A-F、a-f）组成。<br>默认值：无<br>配置原则：<br>该值若不设置，默认值为FFFFFF。表示“基于位置的地址分配”功能不匹配SD。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/NGIPAREADNN]] · 5G IP区域DNN（NGIPAREADNN）

## 使用实例

查询所有支持“基于位置的地址分配”功能的目标DNN记录，执行如下命令：

```
%%LST NGIPAREADNN:;%%
RETCODE = 0  操作成功

结果如下
------------------------
             DNN  =  HUAWEI.COM
 是否匹配S-NSSAI  =  Yes
    切片业务类型  =  1
    切片细分标识  =  FFFFFF
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询5G-IP区域DNN（LST-NGIPAREADNN）_96242250.md`
