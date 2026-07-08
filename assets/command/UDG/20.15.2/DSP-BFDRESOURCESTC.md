---
id: UDG@20.15.2@MMLCommand@DSP BFDRESOURCESTC
type: MMLCommand
name: DSP BFDRESOURCESTC（查询BFD资源统计信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: BFDRESOURCESTC
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- BFD管理
- BFD资源
- BFD资源统计信息
status: active
---

# DSP BFDRESOURCESTC（查询BFD资源统计信息）

## 功能

该命令用于查询RU上BFD会话资源的统计信息。

## 注意事项

BFD将不会联动接口状态。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@BFDRESOURCESTC]] · BFD资源统计信息（BFDRESOURCESTC）

## 使用实例

查询RU上BFD会话资源统计信息：

```
DSP BFDRESOURCESTC:;
```

```

RETCODE = 0  操作成功

结果如下
----------------
             RU名称  =  VNODE_VNRS_VNFC_IPU_0064
    BFD会话总资源数  =  300
  剩余BFD会话资源数  =  300
(结果个数 = 1)
--- END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/DSP-BFDRESOURCESTC.md`
