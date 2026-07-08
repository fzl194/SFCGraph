---
id: UNC@20.15.2@MMLCommand@LST SMCOMMFUNC
type: MMLCommand
name: LST SMCOMMFUNC（查询通用会话拓展功能）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: SMCOMMFUNC
command_category: 查询类
applicable_nf:
- SGW-C
- PGW-C
- SMF
- GGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- 会话协议参数管理
- 会话管理拓展功能
- 通用会话管理拓展功能
status: active
---

# LST SMCOMMFUNC（查询通用会话拓展功能）

## 功能

**适用NF：SGW-C、PGW-C、SMF、GGSN**

该命令用于查询通用会话管理扩展功能。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/SMCOMMFUNC]] · 通用会话拓展功能（SMCOMMFUNC）

## 使用实例

查询通用会话管理扩展功能，执行如下命令：

```
%%LST SMCOMMFUNC:;%%
RETCODE = 0  操作成功

结果如下
--------
           是否支持实时位置订阅  =  不支持
             手机后路由功能开关  =  不使能
          2B2C漫游双DNN特性开关  =  不支持
      携带实例ID向UDM发起去注册  =  不使能
              PGW重定向功能开关  =  不使能
                QoS质差分析开关  =  不支持
               GaGy计费功能开关  =  使能
Restful接口查询PCF/PCRF地址开关  =  不支持
       体验感知信息采集订阅开关  =  不支持
               位置变更订阅开关  =  不支持
               能力开放位置上报  =  不支持
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-SMCOMMFUNC.md`
