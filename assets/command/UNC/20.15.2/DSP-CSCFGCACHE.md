---
id: UNC@20.15.2@MMLCommand@DSP CSCFGCACHE
type: MMLCommand
name: DSP CSCFGCACHE（显示本地缓存中配置的记录数）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: CSCFGCACHE
command_category: 查询类
applicable_nf:
- AMF
- SMF
- PGW-C
- GGSN
- SGW-C
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- 扩展调测
- OM调测
status: active
---

# DSP CSCFGCACHE（显示本地缓存中配置的记录数）

## 功能

**适用NF：AMF、SMF、PGW-C、GGSN、SGW-C**

该命令用于查看本地缓存中配置的记录数和内容。

## 注意事项

- 当本地缓存中的配置只有一条记录时，会显示该配置的记录数和该记录的详细信息。
- 当本地缓存中的配置有多条记录时，仅显示该配置的记录数。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MMLNAME | 配置命令名称 | 可选必选说明：必选参数<br>参数含义：该参数表示配置命令的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~64。<br>默认值：无<br>配置原则：<br>该参数表示配置命令的名称，比如PLMNNS，不要输入ADD/RMV/MOD/LST等操作字符，优先LST命令名称。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@CSCFGCACHE]] · 本地缓存中配置的记录数（CSCFGCACHE）

## 使用实例

查询PFCPPVTEXT配置在本地缓存的信息：

```
%%DSP CSCFGCACHE: MMLNAME="PFCPPVTEXT";%%
RETCODE = 0  Operation succeeded

The result is as follows
------------------------
配置命令名称                控制业务读取配置数据的策略                 配置的记录数                                                         配置信息      

PFCPPVTEXT                  OMCM                                       [uncpod-0__1012__0][ContainerCtrl] cache num is [30]                 Check cfgCache records in log  
PFCPPVTEXT                  OMCM                                       [uncpod-0__1005__0][ContainerSm]	cache num is [30]                   Check cfgCache records in log  
(结果个数 = 2)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-CSCFGCACHE.md`
