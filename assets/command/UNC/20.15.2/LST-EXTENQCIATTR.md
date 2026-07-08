---
id: UNC@20.15.2@MMLCommand@LST EXTENQCIATTR
type: MMLCommand
name: LST EXTENQCIATTR（查询应用扩展QCI参数属性）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: EXTENQCIATTR
command_category: 查询类
applicable_nf:
- SGW-C
- PGW-C
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- QoS
- 扩展QCI功能
- 扩展QCI应用属性
status: active
---

# LST EXTENQCIATTR（查询应用扩展QCI参数属性）

## 功能

**适用NF：SGW-C、PGW-C、SMF**

该查询应用扩展QCI参数属性配置。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/EXTENQCIATTR]] · 应用扩展QCI参数属性（EXTENQCIATTR）

## 使用实例

显示应用扩展QCI参数属性配置。

```
%%LST EXTENQCIATTR:;%%
RETCODE = 0  操作成功

结果如下
--------
       用户接入的扩展QCI控制开关  =  不使能
     Ga接口话单的扩展QCI控制开关  =  不使能
  Gy接口CCR消息的扩展QCI控制开关  =  不使能
 Radius请求信令的扩展QCI控制开关  =  不使能
N40接口请求消息的扩展QCI控制开关  =  不使能
                 扩展QCI取值范围  =  扩展QCI的范围为128到254
    扩展QCI映射为标准QCI的缺省值  =  9
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-EXTENQCIATTR.md`
