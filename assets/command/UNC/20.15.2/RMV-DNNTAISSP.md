---
id: UNC@20.15.2@MMLCommand@RMV DNNTAISSP
type: MMLCommand
name: RMV DNNTAISSP（删除DNN的TAI和ServingScope映射）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: DNNTAISSP
command_category: 配置类
applicable_nf:
- AMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 移动性管理
- NF发现和选择管理
- 配置DNN的TAI和ServingScope映射
status: active
---

# RMV DNNTAISSP（删除DNN的TAI和ServingScope映射）

## 功能

**适用NF：AMF**

该命令用于删除DNN的TAI和ServingScope映射。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DNNNI | DNN网络标识 | 可选必选说明：必选参数<br>参数含义：该参数用于表示DNN网络标识。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~63。输入指定的DNN NI，可输入的字符有字母、十进制数字、“-”和“.”，并且开头和结尾只能是数字或者字母，不能出现连续两个“.”。字母大小写不敏感。<br>默认值：无<br>配置原则：无 |
| MCC | MCC | 可选必选说明：必选参数<br>参数含义：该参数用于表示组成商城区域的位置区成员的移动国家码，与无线接入网的MCC一致。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度是3。只允许输入十进制数字（0-9）。<br>默认值：无<br>配置原则：无 |
| MNC | MNC | 可选必选说明：必选参数<br>参数含义：该参数用于表示组成商城区域的位置区成员的移动网号，与无线接入网的MNC一致。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是2~3。只允许输入十进制数字（0-9）。<br>默认值：无<br>配置原则：无 |
| BGNTAC | 跟踪区起始编码 | 可选必选说明：必选参数<br>参数含义：该参数用于表示跟踪区编码起始值。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度是6。TAC编码为16进制数，只能由数字（0-9），字母（A-F、a-f）组成。字母大小写不敏感。<br>默认值：无<br>配置原则：<br>如果组成商城的跟踪区编码是连续的，则可通过本参数以及“跟踪区结束编码”联合表示；如果跟踪区编码是离散的，那么仅使用本参数表示该跟踪区。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/DNNTAISSP]] · DNN的TAI和ServingScope映射（DNNTAISSP）

## 使用实例

删除一条DNN的TAI和ServingScope映射关系，“DNN网络标识”为“huawei.com”，“移动网号”为“03”，“跟踪区编码起始值”为“000112”，执行如下命令：

```
RMV DNNTAISSP: DNNNI="huawei.com", MCC="460", MNC="03", BGNTAC="000112";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-DNNTAISSP.md`
