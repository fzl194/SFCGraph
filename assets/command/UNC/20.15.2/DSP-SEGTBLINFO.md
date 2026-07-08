---
id: UNC@20.15.2@MMLCommand@DSP SEGTBLINFO
type: MMLCommand
name: DSP SEGTBLINFO（显示号段表信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: SEGTBLINFO
command_category: 查询类
applicable_nf:
- NRF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- NRF业务及策略管理
- 对端NF管理
- 号段配置管理
- 号段导入管理
status: active
---

# DSP SEGTBLINFO（显示号段表信息）

## 功能

**适用NF：NRF**

该命令用于查询所有A、B表的主备状态及NF的号段支持等信息。

当需要通过号段配置文件方式刷新NF支持的号段信息时，可以通过此命令查看备表的状态信息，进而执行ACT SEGFILE命令进行备表的激活。

若要查询所有的记录，请不要输入参数；若要查询特定号段类型的记录，请输入“号段类型”参数。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SEGTYPE | 号段类型 | 可选必选说明：可选参数<br>参数含义：该参数用于表示号段的号段类型。<br>数据来源：本端规划<br>取值范围：<br>- IMSI（IMSI）<br>- MSISDN（MSISDN）<br>- IMSIRT（IMSIRT）<br>- MSISDNRT（MSISDNRT）<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@SEGTBLINFO]] · 号段表信息（SEGTBLINFO）

## 使用实例

查询号段表的信息：

```
DSP SEGTBLINFO:;
            %%DSP SEGTBLINFO:;%%
            RETCODE = 0  操作成功

            结果如下
            ------------------------
            号段类型  NF类型  号段表类型  号段总数  版本号       操作状态         是否主表  号段文件名称                     进度   加载时间

            IMSI      AUSF    A表         1000      NULL         加载完成未激活   否        segdata-all-9000.zip             100%   2019-10-07 02:29:29
            IMSI      AUSF    B表         4         v1           激活态           是        segdata1569419846013729800.zip   100%   2019-10-07 02:29:29
            IMSI      UDR     A表         0         NULL         初始状态         是        NULL                             0%     NULL
            IMSI      UDR     B表         1000      NULL         加载完成未激活   否        segdata-all-9000.zip             0%     2019-10-07 02:29:29
            IMSI      CHF     A表         1000      NULL         加载完成未激活   否        segdata-all-9000.zip             100%   2019-10-07 02:29:29
            IMSI      CHF     B表         4         v1           激活态           是        segdata1569419846013729800.zip   100%   2019-10-07 02:29:29
            MSISDN    PCF     A表         0         NULL         初始状态         是        NULL                             0%     NULL
            MSISDN    PCF     B表         1000      NULL         加载完成未激活   否        segdata-all-9000.zip             0%     2019-10-07 02:29:29
            (结果个数 = 8)
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-SEGTBLINFO.md`
