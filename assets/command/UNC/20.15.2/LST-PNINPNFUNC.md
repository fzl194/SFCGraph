---
id: UNC@20.15.2@MMLCommand@LST PNINPNFUNC
type: MMLCommand
name: LST PNINPNFUNC（查询公网集成非公网络管理功能）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: PNINPNFUNC
command_category: 查询类
applicable_nf:
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 移动性管理
- 非公网络接入管理
status: active
---

# LST PNINPNFUNC（查询公网集成非公网络管理功能）

## 功能

**适用NF：AMF**

此命令用于查询公网集成非公网络（PNI-NPN）管理功能。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [公网集成非公网络管理功能（PNINPNFUNC）](configobject/UNC/20.15.2/PNINPNFUNC.md)

## 使用实例

查询公网集成非公网络管理，执行如下命令：

```
%%LST PNINPNFUNC:;%%
RETCODE = 0  操作成功

结果如下
--------
           是否支持PNI-NPN功能  =  开启
     CAG变更业务连续性增强开关  =  开启
  CAG用户紧急注册非CAG小区开关  =  开启
                      流程类型  =  Intra-AMF初始注册
         互操作CAG限制检查增强  =  开启
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询公网集成非公网络管理功能（LST-PNINPNFUNC）_22836791.md`
