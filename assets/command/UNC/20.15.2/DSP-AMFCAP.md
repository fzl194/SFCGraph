---
id: UNC@20.15.2@MMLCommand@DSP AMFCAP
type: MMLCommand
name: DSP AMFCAP（显示AMF相对容量信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: AMFCAP
command_category: 查询类
applicable_nf:
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 可靠性管理
- AMF存储BYPASS处理策略
status: active
---

# DSP AMFCAP（显示AMF相对容量信息）

## 功能

**适用NF：AMF**

该命令用于查询AMF相对容量信息。

## 注意事项

如果使用DSP AMFCAP查询的AMF相对容量信息有效（无效值为0xFFFF），则系统实际生效的AMF相对容量以该命令输出结果为准。否则以LST AMFINFO输出的相对容量信息为准。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@AMFCAP]] · 操作AMF相对容量（AMFCAP）

## 使用实例

查询AMF相对容量信息，执行如下命令：

```
%%DSP AMFCAP:;%%
RETCODE = 0  操作成功

结果如下
--------
 AMF名称  =  AMF1.CLUSTER1.NET2.AMF.5GC.MNC003.MCC460.3GPPNETWORK.ORG
相对容量  =  0
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-AMFCAP.md`
