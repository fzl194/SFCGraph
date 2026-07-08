---
id: UNC@20.15.2@MMLCommand@DSP NETINSTRU
type: MMLCommand
name: DSP NETINSTRU（查询网络实例对应RU信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: NETINSTRU
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 单体服务编排功能管理
- 系统管理
- 资源管理
- 网络实例管理
status: active
---

# DSP NETINSTRU（查询网络实例对应RU信息）

## 功能

该命令用于查询网络实例对应RU信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NETINSTNAME | 网络实例名称 | 可选必选说明：可选参数。<br>参数含义：要查询的网络实例的名称。<br>数据来源：本端规划。<br>默认值：无。<br>取值范围：长度为1～63的字符串。<br>配置原则：不支持空格和符号'?'，区分大小写。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@NETINSTRU]] · 网络实例对应RU信息（NETINSTRU）

## 使用实例

查询网络实例NetInstanceDefault对应的RU信息。

```
DSP NETINSTRU: NETINSTNAME="NetInstanceDefault";
```

```
%%DSP NETINSTRU: NETINSTNAME="NetInstanceDefault";%%
RETCODE = 0  操作成功。

结果如下
-------------------------
网络实例名称       网络实例ID     ScaleGroup名称     ScaleGroup ID      RU ID     VNFC类型
NetInstanceDefault 0              SG0_CSLB_IPFWD     0                  64        CSLB_VNFC
NetInstanceDefault 0              SG0_CSLB_IPFWD     0                  65        CSLB_VNFC
NetInstanceDefault 0              SG0_CSLB_IPFWD     0                  65        VNRS_VNFC
NetInstanceDefault 0              SG0_CSLB_IPFWD     0                  64        VNRS_VNFC  
(结果个数 = 4)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-NETINSTRU.md`
