---
id: UDG@20.15.2@MMLCommand@LST UPGLBPMPARA
type: MMLCommand
name: LST UPGLBPMPARA（查询全局策略管理参数）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: UPGLBPMPARA
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 业务控制策略
- 计费控制
- 全局的PM策略控制
status: active
---

# LST UPGLBPMPARA（查询全局策略管理参数）

## 功能

**适用NF：PGW-U、UPF**

该命令用于查询计费策略相关控制参数，参数包括QOSURRAGETIME，显示当内部异常导致承载资源无法回收时，运营商可以通过此命令查看回收删除承载的时间。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UDG/20.15.2/UPGLBPMPARA]] · 全局策略管理参数（UPGLBPMPARA）

## 使用实例

查询计费策略控制参数：

```
LST UPGLBPMPARA:;
```

```

RETCODE = 0  操作成功

全局计费策略配置信息
--------------------
        Qos Urr老化时间(秒)  =  120
                PDR匹配优化  =  使能
       重定向迟滞时间（秒）  =  600
      删除未被引用的URR开关  =  不使能
删除未被引用URR的时延（秒）  =  2
     流描述中Any IP地址格式  =  any格式
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询全局策略管理参数（LST-UPGLBPMPARA）_86527156.md`
