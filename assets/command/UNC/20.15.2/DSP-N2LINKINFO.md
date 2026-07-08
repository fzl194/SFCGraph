---
id: UNC@20.15.2@MMLCommand@DSP N2LINKINFO
type: MMLCommand
name: DSP N2LINKINFO（显示N2链路信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: N2LINKINFO
command_category: 查询类
applicable_nf:
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- N2接口管理
- 显示N2链路信息
status: active
---

# DSP N2LINKINFO（显示N2链路信息）

## 功能

![](显示N2链路信息（DSP N2LINKINFO）_71516427.assets/notice_3.0-zh-cn_2.png)

若连续多次执行该命令可能导致OMU虚机CPU使用率突增。

**适用NF：AMF**

该命令用于查询N2链路信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/N2LINKINFO]] · N2链路信息（N2LINKINFO）

## 使用实例

查询N2链路信息，执行如下命令：

```
%%DSP N2LINKINFO:;%%
RETCODE = 0  操作成功

结果如下
--------
            POD ID  =  uncpod-0
        SCTP偶联ID  =  65027
    NG-RAN基站类型  =  Global gNB
    NG-RAN基站标识  =  4194641
     本端IPv4地址1  =  192.168.138.2
     本端IPv4地址2  =  0.0.0.0
     本端IPv6地址1  =  ::
     本端IPv6地址2  =  ::
        本端端口号  =  36412
     对端IPv4地址1  =  10.70.240.1
     对端IPv4地址2  =  0.0.0.0
     对端IPv6地址1  =  ::
     对端IPv6地址2  =  ::
        对端端口号  =  2011
      链路状态变更  =  UP->DOWN
链路状态变更时间戳  =  09:30:05 06/04/2021
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示N2链路信息（DSP-N2LINKINFO）_71516427.md`
