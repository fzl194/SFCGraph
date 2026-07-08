---
id: UNC@20.15.2@MMLCommand@LST NGIPV4DNSH
type: MMLCommand
name: LST NGIPV4DNSH（查询IPv4 DNS Hostfile记录）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NGIPV4DNSH
command_category: 查询类
applicable_nf:
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- NRF业务及策略管理
- NRF业务参数
- DNS客户端管理
status: active
---

# LST NGIPV4DNSH（查询IPv4 DNS Hostfile记录）

## 功能

**适用NF：AMF**

该命令用于查询网元接口所对应的IPv4地址信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| HSINDEX | 主机名索引 | 可选必选说明：可选参数<br>参数含义：该参数用于指定主机名的索引。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是1~1024。<br>默认值：无<br>配置原则：无 |
| HOSTNAME | 主机名 | 可选必选说明：可选参数<br>参数含义：该参数用于配置主机名。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~255。该参数只能由字母（A-Z或者a-z）、数字（0-9）、连字符（-）和点（.）组成，大小写不敏感，主机名不能以“.”开始，也不能以“.”结束。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/NGIPV4DNSH]] · IPv4 DNS Hostfile记录（NGIPV4DNSH）

## 使用实例

查询主机名为“RAC0002.LAC2301.MNC123.MCC456.3GPPNETWORK.ORG”所对应的配置记录：

```
%%LST NGIPV4DNSH: HOSTNAME="RAC0002.LAC2301.MNC123.MCC456.3GPPNETWORK.ORG";%%
RETCODE = 0  操作成功

结果如下
--------
  主机名索引  =  511
      主机名  =  RAC0002.LAC2301.MNC123.MCC456.3GPPNETWORK.ORG
  地址区间号  =  SECTION1
   IPv4地址1  =  192.168.74.97
     优先级1  =  127
       权重1  =  127
   IPv4地址2  =  0.0.0.0
     优先级2  =  127
       权重2  =  127
   IPv4地址3  =  0.0.0.0
     优先级3  =  127
       权重3  =  127
   IPv4地址4  =  0.0.0.0
     优先级4  =  127
       权重4  =  127
   IPv4地址5  =  0.0.0.0
     优先级5  =  127
       权重5  =  127
   IPv4地址6  =  0.0.0.0
     优先级6  =  127
       权重6  =  127
   IPv4地址7  =  0.0.0.0
     优先级7  =  127
       权重7  =  127
   IPv4地址8  =  0.0.0.0
     优先级8  =  127
       权重8  =  127
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-NGIPV4DNSH.md`
