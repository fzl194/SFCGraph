---
id: UNC@20.15.2@MMLCommand@LST EPSQOS4DEFBER
type: MMLCommand
name: LST EPSQOS4DEFBER（查询Qos Profile缺省承载QoS属性）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: EPSQOS4DEFBER
command_category: 查询类
applicable_nf:
- SGW-C
- PGW-C
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- QoS
- EPS QoS配置
- 缺省承载的EPS QoS
status: active
---

# LST EPSQOS4DEFBER（查询Qos Profile缺省承载QoS属性）

## 功能

**适用NF：SGW-C、PGW-C**

该命令用来查询Qos Profile缺省承载QoS属性。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| QOSPROFILENAME | Qos Profile名 | 可选必选说明：必选参数<br>参数含义：该参数用来指定Qos Profile名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：<br>该参数使用ADD QOSPROFILE命令配置生成。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@EPSQOS4DEFBER]] · Qos Profile缺省承载QoS属性（EPSQOS4DEFBER）

## 使用实例

查询QosProfileName为“test”的缺省承载Qos属性：

```
%%LST EPSQOS4DEFBER:QOSPROFILENAME="test";%%
RETCODE = 0  操作成功。

缺省承载的QoS配置信息
---------------------
            Qos Profile名  =  test
                    QCI值  =  5
            ARP的优先级别  =  11
下行APN AMBR（千比特/秒）  =  500
上行APN AMBR（千比特/秒）  =  500
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-EPSQOS4DEFBER.md`
