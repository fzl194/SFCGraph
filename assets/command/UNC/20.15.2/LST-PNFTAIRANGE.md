---
id: UNC@20.15.2@MMLCommand@LST PNFTAIRANGE
type: MMLCommand
name: LST PNFTAIRANGE（查询对端NF的TAI范围）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: PNFTAIRANGE
command_category: 查询类
applicable_nf:
- AMF
- SMF
- NSSF
- SMSF
- NCG
- PGW-C
- SGW-C
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- 服务化接口管理
- 注册与服务发现
- 本地NRF功能管理
- 对端NF实例TAI范围管理
status: active
---

# LST PNFTAIRANGE（查询对端NF的TAI范围）

## 功能

**适用NF：AMF、SMF、NSSF、SMSF、NCG、PGW-C、SGW-C**

该命令用于查询本地配置的对端NF实例支持的TAI范围信息。

## 注意事项

- 当PRISWITCH为“INHERIT”时，对端UPF实例的优先级以PNFPROFILE中的优先级为准；当PRISWITCH为“SPECIFIC”时，对端UPF实例的优先级以该配置中的优先级为准。
- 当CAPSWITCH为“INHERIT”时，对端UPF实例的容量以PNFPROFILE中的容量为准；当CAPSWITCH为“SPECIFIC”时，对端UPF实例的容量以该配置中的容量为准。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| INDEX | 索引 | 可选必选说明：可选参数<br>参数含义：该参数用于指定TAI范围对应的索引。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~4294967295。<br>默认值：无<br>配置原则：无 |
| NFINSTANCEID | NF实例标识 | 可选必选说明：可选参数<br>参数含义：该参数用于指定NF实例标识。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~50。NFINSTANCEID参数建议满足以下约束规则：1.如果输入为uuid格式（格式例如：a6a61c6f-0d3a-4221-b1da-424eda3ccf67）只能为A-F、a-f、0-9和“-”的字符。2.如果输入不为uuid格式，长度不能超过18且不允许输入只包含0-9和“.”的字符串，例如：1.2.3.4、不允许输入只包含十六进制数（A-F、a-f、0-9）和“:”的字符串，例如：1::2、FBFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF。<br>默认值：无<br>配置原则：<br>本参数取值与ADD PNFPROFILE命令中的“NF实例标识”参数取值保持一致时，关联关系生效。 |
| PNFNSINDEX | 对端NF的切片索引 | 可选必选说明：可选参数<br>参数含义：该参数用于指定对端NF实例支持以TAIRANGE为条件配置优先级与权重时所关联的切片索引。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~4294967295。<br>默认值：无<br>配置原则：<br>当该值配置为空或0时，代表支持所有切片索引。 |
| BINDNWDAFINFOID | 绑定的NWDAFINFO ID | 可选必选说明：可选参数<br>参数含义：该参数用于指定绑定的PNFNWDAFEVENT记录。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~32。该参数大小写不敏感。<br>默认值：无<br>配置原则：<br>BINDNWDAFINFOID需要与ADD PNFNWDAFEVENT中的NWDAFINFOID一致。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@PNFTAIRANGE]] · 对端NF的TAI范围（PNFTAIRANGE）

## 使用实例

查询对端NF的TAI范围信息。

```
%%LST PNFTAIRANGE:;%%
RETCODE = 0  操作成功

结果如下
--------
              索引  =  1
        NF实例标识  =  upf_instance_0
        移动国家码  =  460
          移动网号  =  30
          查询方式  =  START_END
          起始号段  =  123455
          终止号段  =  234567
              模式  =  NULL
  对端NF的切片索引  =  0
    优先级功能开关  =  继承
            优先级  =  0
      容量功能开关  =  继承
              容量  =  0
绑定的NWDAFINFO ID  =  null
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-PNFTAIRANGE.md`
