---
id: UNC@20.15.2@MMLCommand@LST FHBYPASS
type: MMLCommand
name: LST FHBYPASS（查询失败旁路处理配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: FHBYPASS
command_category: 查询类
applicable_nf:
- SGW-C
- PGW-C
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- 计费和策略接口管理
- 失败旁路处理
status: active
---

# LST FHBYPASS（查询失败旁路处理配置）

## 功能

**适用NF：SGW-C、PGW-C、SMF**

该命令用来查看当前的全局旁路设置。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UNC/20.15.2/FHBYPASS]] · 旁路失败处理的配置参数（FHBYPASS）

## 使用实例

查询当前的全局旁路设置：

```
LST FHBYPASS:;
```

```

RETCODE = 0  操作成功。

失败放通处理配置信息
--------------------
                             在线计费  =  允许
                         Gy异常结果码  =  禁止
话单中记录failureHandlingContinue标识  =  允许
                       策略与计费控制  =  禁止
                         Gx异常结果码  =  禁止
                           Radius鉴权  =  禁止
                           Radius计费  =  禁止
                 用户保持时长（分钟）  =  10
             用户保持调整时长（分钟）  =  30
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询失败旁路处理配置（LST-FHBYPASS）_09896715.md`
