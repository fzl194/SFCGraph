---
id: UNC@20.15.2@MMLCommand@LST PNFDNN
type: MMLCommand
name: LST PNFDNN（查询对端NF的DNN信息）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: PNFDNN
command_category: 查询类
applicable_nf:
- AMF
- SMF
- NSSF
- SMSF
- NCG
- SGW-C
- PGW-C
- GGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- 服务化接口管理
- 注册与服务发现
- 本地NRF功能管理
- 对端DNN信息管理
status: active
---

# LST PNFDNN（查询对端NF的DNN信息）

## 功能

**适用NF：AMF、SMF、NSSF、SMSF、NCG、SGW-C、PGW-C、GGSN**

该命令用于查询本地配置的对端NF实例支持的DNN及其归属切片的信息。

## 注意事项

- 当PRISWITCH为“INHERIT”时，对端UPF实例的优先级以PNFPROFILE中的优先级为准；当PRISWITCH为“SPECIFIC”时，对端UPF实例的优先级以该配置中的优先级为准。
- 当CAPSWITCH为“INHERIT”时，对端UPF实例的容量以PNFPROFILE中的容量为准；当CAPSWITCH为“SPECIFIC”时，对端UPF实例的容量以该配置中的容量为准。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| INDEX | 索引 | 可选必选说明：可选参数<br>参数含义：该参数用于指定DNN的索引。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~4294967295。<br>默认值：无<br>配置原则：<br>该参数取值不能重复，建议从0开始顺序取值。 |
| NFINSTANCEID | NF实例标识 | 可选必选说明：可选参数<br>参数含义：该参数用于指定对端NF实例标识。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~38。NFINSTANCEID参数建议满足以下约束规则：1.如果输入为uuid格式（格式例如：a6a61c6f-0d3a-4221-b1da-424eda3ccf67）只能为A-F、a-f、0-9和“-”的字符。2.如果输入不为uuid格式，长度不能超过18且不允许输入只包含0-9和“.”的字符串，例如：1.2.3.4、不允许输入只包含十六进制数（A-F、a-f、0-9）和“:”的字符串，例如：1::2、FBFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF。3.该参数大小写不敏感。<br>默认值：无<br>配置原则：<br>本参数取值与ADD PNFPROFILE命令中的“NF实例标识”参数取值保持一致时，关联关系生效。 |
| DNN | 数据网络名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定对端NF实例支持的数据网络名。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~66。不区分大小写。<br>默认值：无<br>配置原则：无 |
| ISLOCKED | 是否被锁定 | 可选必选说明：可选参数<br>参数含义：该参数用于指定记录是否被锁定。<br>数据来源：本端规划<br>取值范围：<br>- TRUE(TRUE)<br>- FALSE(FALSE)<br>默认值：无<br>配置原则：<br>当设置为"TRUE"时，说明该记录被锁定，不会用于本地服务发现匹配对端NF。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@PNFDNN]] · 对端NF的DNN信息（PNFDNN）

## 使用实例

查询本地配置的对端NF支持的DNN信息。

```
%%LST PNFDNN:;%%
RETCODE = 0 操作成功

结果如下
------------------------
            索引 = 1
      NF实例标识 = smf_instance_0
    数据网络名称 = huawei.com
对端NF的切片索引 = 0
     PDU会话类型 = IPV4&IPV6&IPV4V6&UNSTRUCTURED&ETHERNET
  优先级功能开关 = INHERIT
          优先级 = 0
    容量功能开关 = INHERIT
            容量 = 0
      是否被锁定 = FALSE
（结果个数 = 1）

----    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-PNFDNN.md`
