---
id: UNC@20.15.2@MMLCommand@LST NSACTRLPROP
type: MMLCommand
name: LST NSACTRLPROP（查询NSA控制处理配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NSACTRLPROP
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
- 接入控制
- NSA控制管理
status: active
---

# LST NSACTRLPROP（查询NSA控制处理配置）

## 功能

**适用NF：SGW-C、PGW-C**

该命令用于查询NSA相关的控制处理配置。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/NSACTRLPROP]] · NSA控制处理配置（NSACTRLPROP）

## 使用实例

查询NSA相关的设置：

```
%%LST NSACTRLPROP:;%%
RETCODE = 0  操作成功

结果如下
--------
                    NSA用户的判断方法  =  SRUDR
                       支持5G流量上报  =  使能
               SGW-C发送NR标记给PGW-C  =  不使能
          S1 Release中SGW-C累加5G流量  =  不使能
               支持5G小区位置功能开关  =  不使能
SGW-C S5接口发送5G小区位置信息给PGW-C  =  不使能
SGW-C S8接口发送5G小区位置信息给PGW-C  =  不使能
     支持EPS到5GS切换流程中5G流量上报  =  不使能
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-NSACTRLPROP.md`
