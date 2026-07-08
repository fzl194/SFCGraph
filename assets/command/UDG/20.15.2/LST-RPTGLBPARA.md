---
id: UDG@20.15.2@MMLCommand@LST RPTGLBPARA
type: MMLCommand
name: LST RPTGLBPARA（查询业务报表全局参数）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: RPTGLBPARA
command_category: 查询类
applicable_nf:
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 业务报表管理
- 报表功能管理
- 报表全局参数
status: active
---

# LST RPTGLBPARA（查询业务报表全局参数）

## 功能

**适用NF：UPF**

此命令用于查询业务报表全局参数。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [业务报表全局参数（RPTGLBPARA）](configobject/UDG/20.15.2/RPTGLBPARA.md)

## 使用实例

假如运营商需要查询业务报表全局参数：

```
LST RPTGLBPARA:;
```

```

RETCODE = 0 操作成功

业务报表全局参数配置信息
------------------------
TCP业务分析上报功能流抽样率  =  1000
             流的识别抽样率  =  100
                   网元标识  =  1
            控制URL上报功能  =  全量上报
 根据负载选择服务器控制开关  =  使能（开启）
    Tls名字信息上报控制开关  =  不使能（关闭）
                URL上报长度  =  默认长度
   控制上报的信令面地址来源  =  N4接口地址
    上行TCP业务时延异常阈值  =  0
    下行TCP业务时延异常阈值  =  0
 控制上报的网关设备地址来源  =  N4接口地址
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询业务报表全局参数（LST-RPTGLBPARA）_05977162.md`
