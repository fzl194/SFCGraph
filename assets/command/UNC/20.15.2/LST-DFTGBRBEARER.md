---
id: UNC@20.15.2@MMLCommand@LST DFTGBRBEARER
type: MMLCommand
name: LST DFTGBRBEARER（查询缺省GBR承载参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: DFTGBRBEARER
command_category: 查询类
applicable_nf:
- PGW-C
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- PCC管理
- 基本功能
- 缺省GBR承载
status: active
---

# LST DFTGBRBEARER（查询缺省GBR承载参数）

## 功能

**适用NF：PGW-C、SMF**

该命令用于查询SMF是否支持创建default-gbr承载（提供最低带宽保障的any to any GBR专有承载）、本地触发创建default-gbr承载时的承载QoS、以及删除default-gbr承载时SMF是否去活整个PDU会话。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APN | APN名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定APN名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”特殊字符，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@DFTGBRBEARER]] · 缺省GBR承载参数（DFTGBRBEARER）

## 使用实例

假如运营商需要查询指定APN是否支持创建default-gbr承载，则使用该实例：

```
LST DFTGBRBEARER: APN="test1";
```

```

RETCODE = 0  操作成功

缺省GBR承载参数
---------------
                               APN名称  =  test1
                       缺省GBR承载开关  =  使能
                      缺省GBR承载QCI值  =  1
                      缺省GBR承载ARP值  =  2
   缺省GBR承载Pre-emption-Capability值  =  使能
缺省GBR承载Pre-emption-Vulnerability值  =  使能
      缺省GBR承载UL MBR值（千比特/秒）  =  64
        缺省GBR承载DL MBR值(千比特/秒)  =  64
      缺省GBR承载UL GBR值（千比特/秒）  =  60
      缺省GBR承载DL GBR值（千比特/秒）  =  60
          缺省GBR承载去活时去活PDU会话  =  使能
                         用户接入类型  =  非5G接入
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-DFTGBRBEARER.md`
