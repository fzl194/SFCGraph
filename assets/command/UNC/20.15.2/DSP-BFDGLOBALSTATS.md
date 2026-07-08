---
id: UNC@20.15.2@MMLCommand@DSP BFDGLOBALSTATS
type: MMLCommand
name: DSP BFDGLOBALSTATS（查询BFD的全局会话统计信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: BFDGLOBALSTATS
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- BFD管理
- BFD资源
- BFD全局统计信息
status: active
---

# DSP BFDGLOBALSTATS（查询BFD的全局会话统计信息）

## 功能

该命令用于查询BFD全局会话的统计信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@BFDGLOBALSTATS]] · BFD的全局会话统计信息（BFDGLOBALSTATS）

## 使用实例

查询BFD全局的统计信息：

```
DSP BFDGLOBALSTATS:;
```

```

RETCODE = 0  操作成功。

结果如下
-------------------------
       BFD组件HA状态  =  正常工作
            IP会话数  =  1
         BFD会话总数  =  1
            Up会话数  =  0
          Down会话数  =  1
          静态会话数  =  1
          动态会话数  =  0
    静态自协商会话数  =  0
    已用会话标识符数  =  1
    (结果个数 = 1)
    ---  END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-BFDGLOBALSTATS.md`
